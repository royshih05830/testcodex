from PySide2.QtWidgets import QGraphicsView, QGraphicsView, QGraphicsScene, QGraphicsPixmapItem,QGraphicsRectItem, QGraphicsTextItem
from PySide2.QtCore import QRect, Signal, QPoint, QPointF,QRectF
from PySide2.QtGui import Qt,QPainter,QPen,QFont, QColor, QPixmap, QWheelEvent, QImage
from pivotMatcher import Matcher
import cv2
import numpy as np

class myview(QGraphicsView):
    areaSelected = Signal(str)
    patternSelected = Signal(str)
    readyTriggered = Signal()
    finishTriggered = Signal()
    def __init__(self, parent=None):
        #super(myview, self).__init__(parent)
        super(myview, self).__init__()  # for self.scaleImage
        self.m_scene = QGraphicsScene()
        self.setScene(self.m_scene)
        self.m_pt = QPointF(0, 0)
        self.current_pixmap = QPixmap()
        self.setMouseTracking(True)
        self.areaFlag = False
        self.patternFlag = False
        self.drawing = False
        # Positions storage
        self.area_positions = None
        self.pattern_positions = None
        self.area_text = None
        self.pattern_text = None
        self.objs_positions = []
        # Drawing items
        self.area_item = None
        self.pattern_item = None
        self.threshold = 0.9
        self.overlap =0

    def set_image(self, pixmap):
        # Clear the scene
        self.m_scene.clear()

        # Add new image to the scene
        self.current_pixmap = pixmap
        self.m_scene.addPixmap(self.current_pixmap)
        
        self.scaleImage(pixmap)
        
    def scaleImage(self,pixmap_image):
        scale_factor_1 = self.viewport().height() / pixmap_image.height()
        scale_factor_2 = self.viewport().width()/pixmap_image.width()        
        #self.resetTransform()
        scale_factor = scale_factor_1 if scale_factor_1 < scale_factor_2 else scale_factor_2
        self.scale(scale_factor, scale_factor)

    def enable_draw(self, flag):
        if(flag=="area"):
            self.areaFlag=True
            self.patternFlag = False
        elif(flag=="pattern"):
            self.areaFlag = False
            self.patternFlag = True



    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton and (self.areaFlag or self.patternFlag):
            self.drawing = True
            self.m_pt = event.pos()
            scene_pt = self.mapToScene(self.m_pt)
            pen=QPen(Qt.blue)
            pen.setWidth(4)
            if self.areaFlag:
                self.m_scene.removeItem(self.area_item)
                self.area_item = None
                self.area_item = QGraphicsRectItem(QRectF(scene_pt, scene_pt))
                self.area_item.setPen(pen)
                self.m_scene.addItem(self.area_item)

                self.m_scene.removeItem(self.area_text)
                self.area_text = QGraphicsTextItem("Area")
                self.area_text.setDefaultTextColor(Qt.blue)
                self.area_text.setFont(QFont("Arial", 20))
                self.m_scene.addItem(self.area_text)
                self.update_text_position(self.area_item, self.area_text)

            if self.patternFlag:
                self.m_scene.removeItem(self.pattern_item)
                self.pattern_item = None
                self.pattern_item = QGraphicsRectItem(QRectF(scene_pt, scene_pt))
                pen.setColor(Qt.red)
                self.pattern_item.setPen(pen)
                self.m_scene.addItem(self.pattern_item)

                self.m_scene.removeItem(self.pattern_text)
                self.pattern_text = QGraphicsTextItem("Pattern")
                self.pattern_text.setDefaultTextColor(Qt.red)
                self.pattern_text.setFont(QFont("Arial", 20))
                self.m_scene.addItem(self.pattern_text)
                self.update_text_position(self.pattern_item, self.pattern_text)
            print(f"Initial position: x={scene_pt.x()}, y={scene_pt.y()}")

    def update_text_position(self, rect_item, text_item):
        if rect_item and text_item:
            rect = rect_item.rect()
            text_item.setPos(rect.topLeft() - QPointF(0, 40))

    def mouseMoveEvent(self, event):
        self.m_pt = event.pos()
        #print("ori:",event.pos())
        #print("Map:",self.mapToScene(event.pos()))
        if self.drawing and (self.area_item or self.pattern_item):
            scene_pt = self.mapToScene(self.m_pt)
            if self.areaFlag:
                rect = QRectF(self.area_item.rect().topLeft(), scene_pt).normalized()
                self.area_item.setRect(rect)
                self.update_text_position(self.area_item, self.area_text)
            elif self.patternFlag:
                rect = QRectF(self.pattern_item.rect().topLeft(), scene_pt).normalized()
                self.pattern_item.setRect(rect)

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton and self.drawing:
            self.drawing = False
            if self.areaFlag and self.area_item:
                rect = self.area_item.rect()
                self.area_positions = [rect.x(),rect.y(),rect.width(),rect.height()]
                pos=[int(rect.x()),int(rect.y()),int(rect.width()),int(rect.height())]
                self.areaSelected.emit(str(pos))
                self.enable_autoLabel()
                print(f"Final area rect: x={rect.x()}, y={rect.y()}, width={rect.width()}, height={rect.height()}")
            elif self.patternFlag and self.pattern_item:
                rect = self.pattern_item.rect()
                self.pattern_positions = [rect.x(),rect.y(),rect.width(),rect.height()]
                pos = [int(rect.x()), int(rect.y()), int(rect.width()), int(rect.height())]
                self.patternSelected.emit(str(pos))
                self.enable_autoLabel()

                print(f"Final pattern rect: x={rect.x()}, y={rect.y()}, width={rect.width()}, height={rect.height()}")

    def enable_autoLabel(self):
        if self.area_positions and self.pattern_positions:
            self.readyTriggered.emit()

    def clear_auto_labels(self):
        # Remove only the items added by the auto label process
        items_to_remove = []
        for item in self.m_scene.items():
            if isinstance(item, QGraphicsRectItem) and item.pen().color() == QColor(0, 255, 0):
                items_to_remove.append(item)

        for item in items_to_remove:
            self.m_scene.removeItem(item)

    def qpixmap_to_mat(self,qpixmap):
        qimage = qpixmap.toImage()
        qimage = qimage.convertToFormat(QImage.Format.Format_RGB32)

        width = qimage.width()
        height = qimage.height()

        ptr = qimage.constBits()
        arr = np.array(ptr).reshape(height, width, 4)  # 4 channels for RGBA

        return cv2.cvtColor(arr, cv2.COLOR_RGBA2BGR)
    def auto_label(self):
        # Convert image path to OpenCV image
        self.clear_auto_labels()

        if self.pattern_positions and self.area_positions:
            orin_image = self.qpixmap_to_mat(self.current_pixmap)


            x, y, w, h = map(int, self.pattern_positions)
            pattern_image = orin_image[y:y + h, x:x + w]

            # Save the cropped image
            output_path = "pattern_image.png"  # Change this to your desired path
            #cv2.imwrite(output_path, pattern_image)
            #print(f"Cropped pattern image saved to {output_path}")
            matcher = Matcher()
            matcher.set_pattern_image(pattern_image)
            search_window = (int(self.area_positions[0]), int(self.area_positions[1]), int(self.area_positions[2]), int(self.area_positions[3]))
            rectangle_list, value_list = matcher.match(orin_image, self.threshold, search_window,overlap_threshold=self.overlap)
            self.objs_positions.clear()

            if len(rectangle_list) > 0 :
                for (dx, dy) in rectangle_list:
                    adjusted_x = search_window[0] + dx
                    adjusted_y = search_window[1] + dy

                    self.objs_positions.append([[adjusted_x, adjusted_y],[adjusted_x + w, adjusted_y + h]])
                    #cv2.rectangle(orin_image, (adjusted_x, adjusted_y), (adjusted_x + w, adjusted_y + h), (0, 255, 0), 2)
                    print(adjusted_x, adjusted_y,adjusted_x + w, adjusted_y + h)
                    rect_item = QGraphicsRectItem(
                        QRectF(QPointF(adjusted_x, adjusted_y), QPointF(adjusted_x + w, adjusted_y + h)))
                    rect_item.setPen(QPen(QColor(0, 255, 0), 2))
                    self.m_scene.addItem(rect_item)
                self.finishTriggered.emit()
            #result_path = "result_image.png"
            #cv2.imwrite(result_path, orin_image)
            #print(f"Result image with rectangles saved to {result_path}")

    def get_positions(self):
        return self.objs_positions

    def show_pattern_image(self):
        # Convert QPixmap to OpenCV image
        pattern_image = self.get_opencv_image_from_path(self.current_pixmap)

        # Draw rectangles based on self.pattern_positions
        for rect in [self.pattern_positions]:  # Wrap in a list to iterate
            x, y, w, h = rect
            cv2.rectangle(pattern_image, (int(x), int(y)), (int(x + w), int(y + h)), (0, 255, 0), 2)  # Draw rectangles

        # Display pattern image using OpenCV
        cv2.imshow('Pattern Image', pattern_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def wheelEvent(self, event):
        if event.angleDelta().y() != 0:
            # Save the position in scene coordinates before scaling
            scene_pt = self.mapToScene(event.pos())

            # Get the delta angle
            angle = event.angleDelta().y()

            # Calculate the scale factor
            factor = pow(1.0015, angle)

            # Apply the scale transformation
            self.scale(factor, factor)
            
            view_center = self.mapToScene(self.viewport().rect().center())
                        
            midpoint = QPointF((scene_pt.x()+view_center.x())/2, (scene_pt.y()+ view_center.y())/2)

            # Re-center the view on the scene point
            self.centerOn(midpoint)
