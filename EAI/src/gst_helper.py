import contextlib
import ctypes
import os

import numpy as np

import gi
gi.require_version('GObject', '2.0')
gi.require_version('Gst', '1.0')
gi.require_version('GstBase', '1.0')
gi.require_version('GstVideo', '1.0')
from gi.repository import GObject, Gst, GstBase, GstVideo

# Gst.Buffer.map(Gst.MapFlags.WRITE) is broken, this is a workaround. See
# http://lifestyletransfer.com/how-to-make-gstreamer-buffer-writable-in-python/
# https://gitlab.gnome.org/GNOME/gobject-introspection/issues/69
class GstMapInfo(ctypes.Structure):
  _fields_ = [('memory', ctypes.c_void_p),                # GstMemory *memory
              ('flags', ctypes.c_int),                    # GstMapFlags flags
              ('data', ctypes.POINTER(ctypes.c_byte)),    # guint8 *data
              ('size', ctypes.c_size_t),                  # gsize size
              ('maxsize', ctypes.c_size_t),               # gsize maxsize
              ('user_data', ctypes.c_void_p * 4),         # gpointer user_data[4]
              ('_gst_reserved', ctypes.c_void_p * 4)]     # GST_PADDING

# ctypes imports for missing or broken introspection APIs.
libgst = ctypes.CDLL('gstreamer-1.0-0.dll') if os.name == 'nt' else ctypes.CDLL('libgstreamer-1.0.so.0')
libgst.gst_context_writable_structure.restype = ctypes.c_void_p
libgst.gst_context_writable_structure.argtypes = [ctypes.c_void_p]
libgst.gst_structure_set.restype = ctypes.c_void_p
libgst.gst_structure_set.argtypes = [ctypes.c_void_p, ctypes.c_char_p,
                                     ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p]
GST_MAP_INFO_POINTER = ctypes.POINTER(GstMapInfo)
libgst.gst_buffer_map.argtypes = [ctypes.c_void_p, GST_MAP_INFO_POINTER, ctypes.c_int]
libgst.gst_buffer_map.restype = ctypes.c_int
libgst.gst_buffer_unmap.argtypes = [ctypes.c_void_p, GST_MAP_INFO_POINTER]
libgst.gst_buffer_unmap.restype = None
libgst.gst_mini_object_is_writable.argtypes = [ctypes.c_void_p]
libgst.gst_mini_object_is_writable.restype = ctypes.c_int
libgst.gst_buffer_list_get_writable.argtypes = [ctypes.c_void_p, ctypes.c_int]
libgst.gst_buffer_list_get_writable.restype = ctypes.c_void_p

@contextlib.contextmanager
def _gst_buffer_map(buffer, flags):
  ptr = hash(buffer)
  if flags & Gst.MapFlags.WRITE and libgst.gst_mini_object_is_writable(ptr) == 0:
    raise ValueError('Buffer not writable')

  mapping = GstMapInfo()
  success = libgst.gst_buffer_map(ptr, mapping, flags)
  if not success:
    raise RuntimeError('gst_buffer_map failed')
  try:
    yield ctypes.cast(mapping.data, ctypes.POINTER(ctypes.c_byte * mapping.size)).contents
  finally:
    libgst.gst_buffer_unmap(ptr, mapping)

@contextlib.contextmanager
def _gst_get_buffer_list_writable_map(b_list, idx, ret_type=ctypes.c_byte):
  ptr = hash(b_list)
  unref_ptr = False

  if libgst.gst_mini_object_is_writable(ptr) == 0:
    raise ValueError('Buffer list is not writable')# even after try to make writable')

  buf_ptr = libgst.gst_buffer_list_get_writable(ptr, idx)

  if libgst.gst_mini_object_is_writable(buf_ptr) == 0:
    raise ValueError('Buffer in Buffer List is not writable')

  mapping = GstMapInfo()
  success = libgst.gst_buffer_map(buf_ptr, mapping, Gst.MapFlags.WRITE)
  if not success:
    raise RuntimeError('gst_buffer_map failed')
  try:
    elem_size = ctypes.sizeof(ret_type)
    yield ctypes.cast(mapping.data, ctypes.POINTER(ret_type * (mapping.size // elem_size))).contents
  finally:
    libgst.gst_buffer_unmap(buf_ptr, mapping)

def _gst_get_buffer_list_writable_buffer(b_list, idx):
  return libgst.gst_buffer_list_get_writable(hash(b_list), idx)

@contextlib.contextmanager
def get_inference_data_to_numpy(item, shape):
  mapped = None
  if item.__class__ == Gst.Buffer:
    ctx = _gst_buffer_map(item, Gst.MapFlags.READ)
  elif item.__class__ == Gst.BufferList:
    if item.length() == 0:
      raise ValueError("Gst Buffer List should not be empty")
    ctx = _gst_buffer_map(item.get(item.length()-1), Gst.MapFlags.READ)

  with ctx as mapped:
    try:
      yield np.ndarray(shape=shape, dtype=np.float32, buffer=mapped)
    finally:
      pass
