import os, platform
from PySide2.QtCore import Signal, QThread
from PySide2.QtGui import Qt,QPixmap

from PySide2 import QtGui

import gi
gi.require_version('Gst', '1.0')
gi.require_version('GstVideo', '1.0')
from gi.repository import Gst,GstVideo, GObject

import faulthandler

faulthandler.enable()

import numpy

import gst_helper

gray_color_table = [QtGui.qRgb(i, i, i) for i in range(256)]
GET_STATE_TIMEOUT = 99999999

if platform.system() == "Windows":
  EVA_ROOT = os.getenv('EVA_ROOT', "") or "C:/ADLINK/eva"  
elif platform.system() == "Linux":
  EVA_ROOT = os.getenv('EVA_ROOT', "") or "/opt/adlink/eva"
  
p = os.path.split(EVA_ROOT)
while p[1] == "":
  p = os.path.split(p[0])

if p[1] == 'scripts':
  EVA_ROOT = p[0]

Element_Plugins_Dir = os.path.join(EVA_ROOT, "plugins")

if platform.system() == "Windows":  
  os.environ['GST_PLUGIN_PATH']=Element_Plugins_Dir+';C:/ADLINK/gstreamer/lib/gstreamer-1.0'
elif platform.system() == "Linux":  
  os.environ['PYTHONPATH'] = os.path.join(EVA_ROOT, "python")
  if platform.processor() == 'aarch64':
    os.environ['GST_PLUGIN_PATH']=Element_Plugins_Dir+':/usr/lib/aarch64-linux-gnu/gstreamer-1.0'
    import PySide2

    dirname = os.path.dirname(PySide2.__file__) 
    if PySide2.__version_info__[1] > 14:    ## aarch 20.04 use PySide2:5.15.2.1
      plugin_path = os.path.join(dirname,'Qt','plugins','platforms')
    else:                                   ## aarch 18.04 use PySide2: 5.14.2.3
      plugin_path = os.path.join(dirname,'plugins','platforms')
    os.environ['QT_QPA_PLATFORM_PLUGIN_PATH']=plugin_path
  else:
    os.environ['GST_PLUGIN_PATH']=Element_Plugins_Dir+':/usr/lib/x86_64-linux-gnu/gstreamer-1.0'


def toQImage(im, fmt=None, copy=False):
    if im is None:
      return QtGui.QImage()

    if isinstance(fmt, str):
      fmt = fmt.upper()

    qt_fmt, need_rgb_swap = None, False
    if len(im.shape) == 2:
      qt_fmt = QtGui.QImage.Format_Indexed8
    elif len(im.shape) == 3:
      if im.shape[2] == 1:
        if fmt is None:
          qt_fmt = QtGui.QImage.Format_Indexed8
        elif fmt == "GRAY8":
          qt_fmt = QtGui.QImage.Format_Indexed8
      elif im.shape[2] == 3:
        if fmt is None:
          qt_fmt = QtGui.QImage.Format_RGB888
        elif fmt == "RGB":
          qt_fmt = QtGui.QImage.Format_RGB888
        elif fmt == "BGR":
          qt_fmt = QtGui.QImage.Format_BGR888
      elif im.shape[2] == 4:
        if fmt is None:
          #qt_fmt = QtGui.QImage.Format_ARGB32
          pass
        elif fmt == "RGBA":
          qt_fmt = QtGui.QImage.Format_RGBA8888
        elif fmt == "RGBX":
          qt_fmt = QtGui.QImage.Format_RGBX8888
        elif fmt == "ARGB":
          #qt_fmt = QtGui.QImage.Format_ARGB32
          pass
        elif fmt == "XRGB":
          pass
        elif fmt == "BGRA":
          qt_fmt = QtGui.QImage.Format_RGBA8888
          need_rgb_swap = True
        elif fmt == "BGRX":
          qt_fmt = QtGui.QImage.Format_RGBX8888
          need_rgb_swap = True
        elif fmt == "ABGR":
          #qt_fmt = QtGui.QImage.Format_ARGB32
          #need_rgb_swap = True
          pass
        elif fmt == "XBGR":
          pass

    if qt_fmt is None:
      return QtGui.QImage()

    qim = QtGui.QImage(im.data, im.shape[1], im.shape[0], im.strides[0], qt_fmt)
    qim.setColorTable(gray_color_table)
    if need_rgb_swap:
      qim = qim.rgbSwapped()
    return qim.copy() if copy else qim 

def get_sample_format(sample):
    cap = sample.get_caps()    
    return 'empty' if cap is None else cap.get_structure(0).get_string("format")

def sample_to_numpy(sample):
    buff = sample.get_buffer()
    caps = sample.get_caps()    
    
    s = caps.get_structure(0)
    w, h = s.get_int("width").value, s.get_int("height").value
    f = GstVideo.VideoFormat.from_string(s.get_string("format"))            
    
    channels = None
    if f is GstVideo.VideoFormat.GRAY8:
        channels = 1
    elif f is GstVideo.VideoFormat.RGB or f is GstVideo.VideoFormat.BGR:
        channels = 3
    elif f is GstVideo.VideoFormat.RGBA or f is GstVideo.VideoFormat.ARGB or f is GstVideo.VideoFormat.RGBX or f is GstVideo.VideoFormat.XRGB or f is GstVideo.VideoFormat.BGRA or f is GstVideo.VideoFormat.ABGR or f is GstVideo.VideoFormat.BGRX or f is GstVideo.VideoFormat.XBGR:
        channels = 4
    elif f is GstVideo.VideoFormat.NV12 or f is GstVideo.VideoFormat.I420:
        return buffer_to_numpy(buff, w, h * 3//2, 1)
    else:
        return None
    
    return buffer_to_numpy(buff, w, h, channels)

def buffer_to_numpy(buff, width, height, channels, dtype=numpy.int8, ro=True):
  with gst_helper._gst_buffer_map(buff, Gst.MapFlags.READ if ro else Gst.MapFlags.WRITE) as mapped:
    return numpy.ndarray(shape = (height, width, channels), dtype=dtype, buffer=mapped)

def state_to_str(state):
  if state == Gst.State.PLAYING:
    return 'Play'
  elif state == Gst.State.PAUSED:
    return 'Pause'
  elif state == Gst.State.READY:
    return 'Ready'
  elif state == Gst.State.NULL:
    return 'Stop'
  return ''


class LiveStream(QThread):
    new_frame = Signal(QtGui.QImage)
    newSample = Signal(Gst.Sample)
    def __init__(self, labelsize=None, gstcmd='', *args, **kwargs):
        super().__init__(*args, **kwargs)     
        self.gstcmd = gstcmd 
        self.label = None   
        self.graphics = None 
        self.labelsize = labelsize
        self.oriImage= None                            
      
    def on_message(self, bus: Gst.Bus, message: Gst.Message, none):
        mtype = message.type
        if mtype == Gst.MessageType.EOS:
            print("Media already play end of stream")      
            #self.onlyEnableStop()                    
        elif mtype == Gst.MessageType.WARNING:
            err, debug = message.parse_warning()
            print("WARNING: from element %s: %s\nAdditinal debug info:\n%s\n" % (message.src.get_path_string(),
                                                                               err.message, debug))            

    def message_error(self, bus: Gst.Bus, message: Gst.Message, none):
        src = message.src
        err, debug = message.parse_error()    
        #self.onlyEnableStop()
        print("ERROR: from element %s: %s" % (src.name, err.message))
        print("Additional debug info:\n", debug)        

    def message_warning(self, bus: Gst.Bus, message: Gst.Message, none):
        src = message.src
        err, debug = message.parse_warning()
        print("WARNING: from element %s: %s" % (src.name, err.message))
        print("Additional debug info:\n", debug)        
        print('Pipeline WARNING occurred')
        
    def changestate(self,target_state):
        ret, state, pending_state = self.pipeline.get_state(GET_STATE_TIMEOUT)
        if ret == Gst.StateChangeReturn.ASYNC:
            if target_state != Gst.State.NULL:
                print('[Info] pipeline state still pending to change state from %s to %s' % (state_to_str(state), state_to_str(pending_state)))                
                #self.setButton(pending_state)
                return False
            
        elif ret == Gst.StateChangeReturn.FAILURE and target_state != Gst.State.NULL:
            print('[Warning] Previous change state from %s to %s is failure, please click Stop button and then fix issue' % (state_to_str(state), state_to_str(pending_state)))
            #self.onlyEnableStop()
            return False
        
        if state == target_state:
            print("[Info] Pipeline is in %s state" % state_to_str(state))            
            #self.setButton(state)
            return True
                
        print('[Info] Ready to change state from %s to %s' %(state_to_str(state), state_to_str(target_state)))        
        #self.setButton(target_state)
              
        ret = self.pipeline.set_state(target_state)
        
        if ret == Gst.StateChangeReturn.FAILURE:
            print('[ERROR] Change state from %s to %s failed' % (state_to_str(state), state_to_str(target_state)))
            #self.setButton(state)              
            return False
    
        return True
                                        
    def checkchangestate(self,target_state):
        g_ret=None
        
        while (g_ret != Gst.StateChangeReturn.SUCCESS and g_ret != Gst.StateChangeReturn.NO_PREROLL):                
            g_ret,state,_ = self.pipeline.get_state(GET_STATE_TIMEOUT)
            if state==target_state:
                print('[Info] Change state to %s done.' % (state_to_str(target_state)))    
                return True
        
        
    def parseLaunch(self):
        try:
            self.pipeline = Gst.parse_launch(self.gstcmd)
        except:
            print('[Error] parse Failed')
            return False
                
        self.bus = self.pipeline.get_bus()
        self.bus.add_signal_watch()
        self.bus.connect("message", self.on_message, None)
        self.bus.connect("message::error", self.message_error, None)
        self.bus.connect("message::warning", self.message_warning, None)
        
        self.sink = self.pipeline.get_by_name('sink')
        if self.sink:
          self.sink.connect('new-sample', self.new_sample, None)
        else:
           print('[Error] cannot find sink object')
           return False
        return True
                
    def play(self):         
        target_state = Gst.State.PLAYING      
        if self.changestate(target_state):                      
            if self.checkchangestate(target_state):                
                #print('Playing')
                return True        
        
        return False

    def pause(self):
        target_state = Gst.State.PAUSED
        if self.changestate(target_state):        
            if self.checkchangestate(target_state):                
                #print('Pause')
                return True        
        return False
      
    def isPause(self):
        _, state, _ = self.pipeline.get_state(GET_STATE_TIMEOUT)
        if state == Gst.State.PAUSED:
          return True
        else:
          return False

    def stop(self):
        target_state = Gst.State.NULL
        if self.changestate(target_state):        
            if self.checkchangestate(target_state):
                if self.label:
                  self.label.clear()
                elif self.graphics:                 
                  self.graphics.scene().clear()
                del self.pipeline, self.sink,self.bus
                return True                        
        return False          
	

    def new_sample(self,sink, data) -> Gst.FlowReturn:
        
        sample = sink.emit('pull-sample')
        
        buffer_data = sample_to_numpy(sample)
        fmt = get_sample_format(sample)
        self.setImage(buffer_data, fmt)
        self.newSample.emit(sample)    
             
        return Gst.FlowReturn.OK
    
    def setImage(self, buffer_data, fmt):
      image = toQImage(buffer_data, fmt)

      if self.label:
        if image is None or image.isNull():
            s = 'Unsupport format '+ fmt
            self.label.setText(s)        
        else:       
            self.oriImage= image       
            size = self.labelsize if self.labelsize else self.label.size()                    
            pixmap = QPixmap.fromImage(image).scaled(size,aspectMode=Qt.KeepAspectRatio)
            self.label.setPixmap(pixmap) 
      elif self.graphics:
        if image is None or image.isNull():
            s = 'Unsupport format '+ fmt
            self.graphics.setText(s)
        else:
          self.oriImage = image
          
          self.new_frame.emit(image)          