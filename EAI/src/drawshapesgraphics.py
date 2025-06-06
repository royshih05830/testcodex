from PySide2.QtWidgets import QGraphicsView,QGraphicsScene,QGraphicsTextItem,QGraphicsRectItem, QGraphicsPixmapItem, QGraphicsItem, QGraphicsLineItem
from PySide2.QtCore import  Signal, QPoint, QPointF,QRectF
from PySide2.QtGui import Qt,QPen,QFont, QPixmap
import re

class DraggableRectItem(QGraphicsRectItem):
    def __init__(self, rect, parent_rect):
        super().__init__(rect)                
        self.setFlag(QGraphicsItem.ItemSendsGeometryChanges, True)
        self.parent_rect = parent_rect

    def itemChange(self, change, value):
        if change == QGraphicsItem.ItemPositionChange:
            new_pos = value + self.rect().topLeft()
         
            parent_rect = self.parent_rect

            if new_pos.x() < parent_rect.left():
                new_pos.setX(parent_rect.left())
            elif new_pos.x() + self.rect().width() > parent_rect.right():
                new_pos.setX(parent_rect.right() - self.rect().width())
                
            if new_pos.y() < parent_rect.top():
                new_pos.setY(parent_rect.top())
            elif new_pos.y() + self.rect().height() > parent_rect.bottom():
                new_pos.setY(parent_rect.bottom() - self.rect().height())
            return new_pos - self.rect().topLeft()
        
        return super().itemChange(change, value)


class DrawShapesGraphics(QGraphicsView):
    
    labelTriggered = Signal()
    movelabelTriggered = Signal()
    drawTriggered = Signal()    
    drawSelectTriggered = Signal(int)    
    drawOverallTrigger = Signal(QPixmap,int,int,int,int)  

    def __init__(self, parent=None, enable_draw=False, statusBar=None ,  *args, **kwargs):
        super().__init__(*args, **kwargs)        
        self.enable_draw = enable_draw       
        self.enable_wheel = True                
        self.m_scene = QGraphicsScene()
        self.setScene(self.m_scene)
        self.setMouseTracking(True)
        self.rect_item_dict = {}
        self.m_pt = QPointF(0,0) 
        self.pixmapItem = None
        self.current_rectitem = None
        self.labelstring_item = None
        self.orderstring_item = None
        self.durationstring_item = None        
        self.start_point = None
        self.end_point = None
        self.drawing = False        
        self.labelstring = None
        self.order = "ignore"   
        self.duration = "ignore"
        self.rect_count = 0
        
        self.enable_move = False
        self.moved_rect = None
        self.focus_rect_item = None
        
        self.drawTriggered.connect(self.drawallRect)  
        self.drawSelectTriggered.connect(self.drawSelectRect)   
        self.drawOverallTrigger.connect(self.drawOverall)    
                         
        self.setTransformationAnchor(QGraphicsView.AnchorViewCenter)
        self.setResizeAnchor(QGraphicsView.AnchorViewCenter)        
                   
        self.labelsInfo = []             
        self.selectlabelInfo = -1     
        self.statusbar = statusBar       
        
        self.isPosition = False
        
        self.pen_red = QPen(Qt.red)
        self.pen_red.setWidth(4)  
        
        self.pen_green = QPen(Qt.green)
        self.pen_green.setWidth(4)   
        
        self.pen_anchor1 = QPen(Qt.magenta)
        self.pen_anchor1.setWidth(4)
        
        self.pen_anchor2 = QPen(Qt.green)        
        self.pen_anchor2.setWidth(4)
        
        self.pen_anchor3 = QPen(Qt.cyan)
        self.pen_anchor3.setWidth(4)   
        
        self.setCursor(Qt.CrossCursor) 
              
        
    def set_image(self, pixmap_image):
        self.addImage(pixmap_image)
        self.scaleImage(pixmap_image)
        
    def addImage(self,pixmap_image):
        # Clear the scene
        self.m_scene.clear()                      
        # Add new image to the scene        
        self.pixmapItem = QGraphicsPixmapItem(pixmap_image)                      
        self.m_scene.addItem(self.pixmapItem)        
    
    def scaleImage(self,pixmap_image):
        ## Issue,  當切換不同像素的圖片或影像時, 圖片會跑到左上方, Scroll bar會出現                        
        
        self.resetTransform()        
        self.resizeAnchor()                  
        
        #scale_factor_1 = self.viewport().height() / pixmap_image.height()
        #scale_factor_2 = self.viewport().width()/pixmap_image.width()  
        #scale_factor = scale_factor_1 if scale_factor_1 < scale_factor_2 else scale_factor_2              
        
        view_rect = self.viewport().rect()
        pixmap_rect = QRectF(QPoint(0,0),pixmap_image.size())                
        
        scale_x = view_rect.width()/pixmap_rect.width()
        scale_y = view_rect.height() / pixmap_rect.height()
        scale_factor = min(scale_x,scale_y)
                        
        self.scale(scale_factor, scale_factor)        
            
        
    def setText(self, string):
        self.m_scene.clear()  # 清空場景中的所有項目
        text_item = QGraphicsTextItem(string)
        text_item.setDefaultTextColor(Qt.black)
        text_item.setFont(self.font())  # 使用預設字體
        self.m_scene.addItem(text_item)
        text_item.setPos(self.m_scene.sceneRect().center() - text_item.boundingRect().center())  # 將文字置於場景中心

        
    def wheelEvent(self, event):
        if self.enable_wheel and event.angleDelta().y() != 0:
            
            # Save the position in scene coordinates before scaling
            scene_pt = self.mapToScene(event.pos())
            
            view_center = self.mapToScene(self.viewport().rect().center())
                        
            midpoint = QPointF((scene_pt.x()+view_center.x())/2, (scene_pt.y()+ view_center.y())/2)
                        
            # Re-center the view on the scene point
            self.centerOn(midpoint)            
            
            # Get the delta angle
            angle = event.angleDelta().y()

            # Calculate the scale factor
            factor = pow(1.0015, angle)

            # Apply the scale transformation
            self.scale(factor, factor)            

        
    def checkPosition(self,pos):
        # check mouse press and move position in Pixmap rect
        if self.pixmapItem:
            pixmapRect = QRectF(QPoint(0,0),self.pixmapItem.pixmap().size())
            return pixmapRect.contains(pos)
        return False
            
    def setPenColor(self,labelstring,default_pen):
        if labelstring == 'point1':
            pen = self.pen_anchor1
        elif labelstring  == 'point2':
            pen = self.pen_anchor2
        elif labelstring == 'point3':
            pen = self.pen_anchor3
        else:
            pen = default_pen
        
        return pen
            
    def mousePressEvent(self, event):                
        self.m_pt = event.pos()                  
        if event.button() == Qt.LeftButton:
            if self.enable_move:
                self.moved_rect = None  
                self.drawing = False
                self.update()
            elif self.enable_draw and (not self.enable_move):                
                self.start_point = self.mapToScene(event.pos())
                
                if self.checkPosition(self.start_point):
                    self.drawing = True                                
                    
                    #if self.labelstring in ['point1','point2','point3']:              
                    if self.isPosition:                
                        if self.labelstring in self.rect_item_dict.keys():  # point1,point2,point3                        
                            self.removeROI(self.rect_item_dict[self.labelstring])                   
                    
                    pixmapRect = QRectF(QPoint(0,0),self.pixmapItem.pixmap().size())                                
                    self.current_rectitem = None
                    self.current_rectitem = DraggableRectItem(QRectF(self.start_point,self.start_point).normalized(),pixmapRect)
                    pen = self.setPenColor(self.labelstring, self.pen_red)
                    self.current_rectitem.setPen(pen)
                    self.m_scene.addItem(self.current_rectitem)                
                    self.update()
            else:                                    
                if not self.isPosition and not self.enable_move:                            
                    if self.statusbar:
                        if self.labelstring:                
                            self.statusbar.showMessage('Please select an image or capture an image.')
                        else:
                            self.statusbar.showMessage('please select a label class in Label List.')
    
                
        
        
        super().mousePressEvent(event)                  
        
    def mouseMoveEvent(self, event): 
        self.m_pt = event.pos()
        if self.drawing:                                     
            self.end_point = self.mapToScene(event.pos())            
            if self.checkPosition(self.end_point):   
                left = self.start_point.x() if self.start_point.x() < self.end_point.x() else self.end_point.x()
                right = self.start_point.x() if self.start_point.x() > self.end_point.x() else self.end_point.x()
                top = self.start_point.y() if self.start_point.y() < self.end_point.y() else self.end_point.y()
                bottom = self.start_point.y() if self.start_point.y() > self.end_point.y() else self.end_point.y()
                
                if self.isPosition:
                    if (bottom - top) > 50 or (right - left) > 50:                              
                        return 
                rect = QRectF(QPointF(left,top),QPointF(right,bottom))            
                self.current_rectitem.setRect(rect)
                self.update()                                                           
            
        super().mouseMoveEvent(event)
        
    def mouseReleaseEvent(self, event):                  
        if event.button() == Qt.LeftButton:
            self.end_point = self.mapToScene(event.pos())
            if self.drawing and (self.start_point != self.end_point):
                self.drawing = False                            
                
                if self.labelstring not in ['point1','point2','point3']:
                    self.current_rectitem.setPen(self.pen_green)
                                
                self.labelstring_item = self.create_text_item(self.labelstring)         
                self.update_text_position(self.current_rectitem,self.labelstring_item,'label')
                if self.order.lower() != 'ignore':
                    self.orderstring_item = self.create_text_item(f'order:{self.order}')
                    self.update_text_position(self.current_rectitem,self.orderstring_item,'order')
                if self.duration.lower() != 'ignore':
                    self.durationstring_item = self.create_text_item(f'duration:{self.duration}')
                    self.update_text_position(self.current_rectitem,self.durationstring_item,'duration')
                
                #if self.labelstring in ['point1','point2','point3']:
                self.addValueToRectDict(self.rect_item_dict,
                                        self.labelstring,
                                        self.labelstring_item,
                                        self.current_rectitem,                                        
                                        self.orderstring_item,
                                        self.durationstring_item
                                        )                                                       
                                  
                self.labelTriggered.emit()
                self.update() 
            elif (not self.drawing):
                if self.selectlabelInfo in self.rect_item_dict.keys():                                                                
                                             
                    new_topleft = self.rect_item_dict[self.selectlabelInfo][1].rect().topLeft()+self.rect_item_dict[self.selectlabelInfo][1].pos()
                    new_bottomright = self.rect_item_dict[self.selectlabelInfo][1].rect().bottomRight()+self.rect_item_dict[self.selectlabelInfo][1].pos()
                    self.moved_rect = QRectF(new_topleft,new_bottomright)                                        
                    
                    temp_item = QGraphicsRectItem(self.moved_rect)                    
                                                    
                    # update textitem postion
                    if isinstance(self.rect_item_dict[self.selectlabelInfo][0],QGraphicsTextItem):                        
                        self.update_text_position(temp_item,self.rect_item_dict[self.selectlabelInfo][0],'label')
                    if isinstance(self.rect_item_dict[self.selectlabelInfo][2],QGraphicsTextItem):                        
                        self.update_text_position(temp_item,self.rect_item_dict[self.selectlabelInfo][2],'order')
                    if isinstance(self.rect_item_dict[self.selectlabelInfo][3],QGraphicsTextItem):                        
                        self.update_text_position(temp_item,self.rect_item_dict[self.selectlabelInfo][3],'duration')
                    
                    del temp_item
                    
                    self.movelabelTriggered.emit()                                       

                    self.update()     
        
            
        super().mouseReleaseEvent(event)
                           
    def addValueToRectDict(self,rect_item_dict,labelstring,labelstring_item,rect_item,orderstring_item=None,durationstring_item=None):
        if self.isPosition:
            rect_item_dict[labelstring] = [labelstring_item,
                                            rect_item,
                                            orderstring_item,
                                            durationstring_item]
        else:
            rect_item_dict[self.rect_count] = [labelstring_item,
                                               rect_item,
                                               orderstring_item,
                                               durationstring_item]
            self.rect_count += 1
            
    
    def update_text_position(self, rect_item, text_item, text_type):
        if rect_item and text_item:
            rect = rect_item.rect().normalized()
            if text_type == 'label':
                text_item.setPos(rect.topLeft() - QPointF(0, 60))
            elif text_type == 'order':
                text_item.setPos(rect.bottomLeft() + QPointF(0, 0))
            elif text_type == 'duration':
                text_item.setPos(rect.bottomLeft() + QPointF(0, 40))
    
            
    def create_text_item(self,text):        
        item = QGraphicsTextItem(text)
        item.setDefaultTextColor(Qt.yellow)
        item.setFont(QFont("Arial", 30 ,QFont.Bold))
        self.m_scene.addItem(item)
        return item        
        
    def removeROI(self,value):  # value from rect_item_dict
        if isinstance(value[0],QGraphicsTextItem):  # Label String
            if value[0] in self.m_scene.items():            
                self.m_scene.removeItem(value[0])
        
        if isinstance(value[1],DraggableRectItem):  # Rect
            if value[1] in  self.m_scene.items():
                self.m_scene.removeItem(value[1])
                
        if isinstance(value[2],QGraphicsTextItem):  # order
            if value[2] in  self.m_scene.items():
                self.m_scene.removeItem(value[2])
                
        if isinstance(value[3],QGraphicsTextItem):  # duration
            if value[3] in  self.m_scene.items():
                self.m_scene.removeItem(value[3])      
    
    def drawallRect(self):        
        '''
            labelInfo format
            Labelstring;(left(),top());(right(),bottom());Order;Duration;[OK/NG]          
            
            rect_item_dict format:
            1. lablestring = ['point1','point2','point3']  / self.isPosition = True
            rect_item_dict = {
                lablestring : [labelstring_item, rect_item, orderstring_item, durationstring_item]
            }
            
            [OK/NG]:
            only support inspection result in operation mode.
            OK will draw green rect.
            NG will draw red rect.
        '''
        self.rect_item_dict = {}
        self.rect_count = 0
        
        
        if self.labelsInfo:
            pixmapRect = QRectF(QPoint(0,0),self.pixmapItem.pixmap().size())
            for info in self.labelsInfo:
                item = info.split(';')     
            
                if len(item)>5:
                    if item[5] == 'NG':
                        pen = self.pen_red
                    elif item[5] == 'OK':
                        pen = self.pen_green
                else:
                    pen = self.pen_green
                
                # rect_item
                start_x, start_y = [int(match) for match in re.findall(r'\d+', item[1])]
                end_x, end_y = [int(match) for match in re.findall(r'\d+', item[2])]                  
                start_point = QPoint(start_x,start_y)
                end_point = QPoint(end_x,end_y)                                
                rect_item = DraggableRectItem(QRectF(start_point,end_point),pixmapRect)
                pen = self.setPenColor(item[0], pen)
                rect_item.setPen(pen)
                self.m_scene.addItem(rect_item)         
                
                #labelstring_item
                labelstring = item[0]       
                labelstring_item = self.create_text_item(labelstring)                                                 
                self.update_text_position(rect_item,labelstring_item,'label')
                
                orderstring_item = None
                durationstring_item = None
                
                #if not self.isPosition:                    
                order = item[3]
                duration = item[4]                    
                if order.lower() != 'ignore':
                    orderstring_item = self.create_text_item(f'order:{order}')
                    self.update_text_position(rect_item,orderstring_item,'order')
                if duration.lower() != 'ignore':
                    durationstring_item = self.create_text_item(f'duration:{duration}')
                    self.update_text_position(rect_item,durationstring_item,'duration')
                    
                    
                self.addValueToRectDict(self.rect_item_dict,
                                        labelstring,
                                        labelstring_item,
                                        rect_item,                                        
                                        orderstring_item,
                                        durationstring_item
                                        )
                        
    def center_and_fit_rect(self,rect_item:QGraphicsRectItem, reduction_factor:float):
        self.centerOn(rect_item)
        
        view_rect = self.viewport().rect()
        scene_rect = self.mapFromScene(rect_item.boundingRect()).boundingRect()
        
        scale_x = view_rect.width()/scene_rect.width()
        scale_y = view_rect.height() / scene_rect.height()
        scale_factor = min(scale_x,scale_y)/reduction_factor
        
        self.resetTransform()
        self.scale(scale_factor,scale_factor)
        
    def drawSelect(self,pen=None,moved=False):                
        if self.selectlabelInfo > -1:            
            
            # show all
            self.showAllItem()            
            #reset all pen to green            
            #for key in self.rect_item_dict.keys():                
            #    self.rect_item_dict[key][1].setPen(self.pen_green)            
            #    self.rect_item_dict[key][1].setFlag(QGraphicsItem.ItemIsMovable, False)                            
            
            for index in self.rect_item_dict.keys():
                labelstring_item = self.rect_item_dict[index][0]
                rect_item = self.rect_item_dict[index][1]
                order_item = self.rect_item_dict[index][2]
                duration_item = self.rect_item_dict[index][3]
                        
                # if self.selectlabelInfo in self.rect_item_dict.keys():                
                    # if pen:
                    #     self.rect_item_dict[self.selectlabelInfo][1].setPen(pen)               
                    # else: 
                    #     self.rect_item_dict[self.selectlabelInfo][1].setPen(self.pen_anchor3)
                        
                        
                    # if moved:
                    #     self.rect_item_dict[self.selectlabelInfo][1].setFlag(QGraphicsItem.ItemIsMovable, True)
                    
                    # self.resetTransform()  
                    # #self.centerOn(self.rect_item_dict[self.selectlabelInfo][1])
                    # self.center_and_fit_rect(self.rect_item_dict[self.selectlabelInfo][1],1.5)                
                    
                    
                if index == self.selectlabelInfo:
                    if isinstance(rect_item,DraggableRectItem):
                        if pen:
                            rect_item.setPen(pen)               
                        else: 
                            rect_item.setPen(self.pen_anchor3)                                                
                        if moved:
                            rect_item.setFlag(QGraphicsItem.ItemIsMovable, True)
                        self.resetTransform()                          
                        self.center_and_fit_rect(rect_item,3)
                    
                    if isinstance(labelstring_item,QGraphicsTextItem):
                        labelstring_item.show()
                                        
                    if isinstance(order_item,QGraphicsTextItem):
                        order_item.show()
                                        
                    if isinstance(duration_item,QGraphicsTextItem):
                        duration_item.show() 
                else:
                    if isinstance(rect_item,DraggableRectItem):
                        rect_item.hide()      
                                            
                    if isinstance(labelstring_item,QGraphicsTextItem):
                        labelstring_item.hide()
                                        
                    if isinstance(order_item,QGraphicsTextItem):
                        order_item.hide()
                                        
                    if isinstance(duration_item,QGraphicsTextItem):
                        duration_item.hide()
                    
    def showSelect(self):
                
        if self.selectlabelInfo > -1:
            for item in self.rect_item_dict.keys():
               labelString_item = self.rect_item_dict[item][0]
               labelString_item.setDefaultTextColor(Qt.yellow)
               
            if self.selectlabelInfo in self.rect_item_dict.keys():                
                rect_item = self.rect_item_dict[self.selectlabelInfo][1]
                self.resetTransform()                 
                self.centerOn(rect_item)     
                                        
                ## Inlcude labelString
                labelString_item = self.rect_item_dict[self.selectlabelInfo][0]  
                labelString_item.setDefaultTextColor(self.pen_anchor3.color())                                
                # TopLeft = labelString_item.pos() - QPointF(30, 0)                                
                # bottom = rect_item.rect().bottom() + 30                
                # labelString_right = labelString_item.boundingRect().width() + labelString_item.pos().x()                                
                # right = labelString_right + 30 if labelString_right > rect_item.rect().right() else rect_item.rect().right() +30                
                # BottomRight = QPointF(right,bottom) 
                
                TopLeft = rect_item.rect().topLeft() - QPointF(15, 15)
                BottomRight = rect_item.rect().bottomRight() + QPointF(15, 15)
                if self.focus_rect_item:
                    if isinstance(self.focus_rect_item, QGraphicsRectItem):
                        if self.focus_rect_item in  self.m_scene.items():
                            self.m_scene.removeItem(self.focus_rect_item)
                    else:
                        self.focus_rect_item = None
                        
                self.focus_rect_item = QGraphicsRectItem(QRectF(TopLeft,BottomRight))
                self.focus_rect_item.setPen(self.pen_anchor3) 
                self.m_scene.addItem(self.focus_rect_item)
    
    def showAllItem(self):
        for index in self.rect_item_dict.keys():             
            labelstring_item = self.rect_item_dict[index][0]
            rect_item = self.rect_item_dict[index][1]
            order_item = self.rect_item_dict[index][2]
            duration_item = self.rect_item_dict[index][3]
            
            if isinstance(rect_item,DraggableRectItem):                
                rect_item.setVisible(True)
                rect_item.show()
                
            if isinstance(labelstring_item,QGraphicsTextItem):                
                labelstring_item.setVisible(True)
                labelstring_item.show()                
                
            if isinstance(order_item,QGraphicsTextItem):    
                order_item.show()
                
            if isinstance(duration_item,QGraphicsTextItem):
                duration_item.show()
                        
        self.scaleImage(self.pixmapItem.pixmap())          
           
                
    def onlyShowSelect(self,select_index):           
        if select_index > -1:                        
            for index in self.rect_item_dict.keys():
                labelstring_item = self.rect_item_dict[index][0]
                rect_item = self.rect_item_dict[index][1]
                order_item = self.rect_item_dict[index][2]
                duration_item = self.rect_item_dict[index][3]
                if index == select_index:
                    if isinstance(rect_item,DraggableRectItem):
                        rect_item.show() 
                        self.resetTransform()                 
                        #self.centerOn(rect_item) 
                        self.center_and_fit_rect(rect_item,3)
                        
                    if isinstance(labelstring_item,QGraphicsTextItem):
                        labelstring_item.show()
                                        
                    if isinstance(order_item,QGraphicsTextItem):
                        order_item.show()
                                        
                    if isinstance(duration_item,QGraphicsTextItem):
                        duration_item.show()
                        
                else:
                    if isinstance(rect_item,DraggableRectItem):
                        rect_item.hide()      
                                            
                    if isinstance(labelstring_item,QGraphicsTextItem):
                        labelstring_item.hide()
                                        
                    if isinstance(order_item,QGraphicsTextItem):
                        order_item.hide()
                                        
                    if isinstance(duration_item,QGraphicsTextItem):
                        duration_item.hide()
                
    def drawSelectRect(self,select_index):             
        self.drawallRect()        
        self.onlyShowSelect(select_index)
        
    def drawOverall(self,pixmap,x1,y1,x2,y2):        
        self.set_image(pixmap)        
        start_point = QPoint(x1,y1)
        end_point = QPoint(x2,y2)
        pixmapRect = QRectF(QPoint(0,0),pixmap.size())
        rect_item = DraggableRectItem(QRectF(start_point,end_point),pixmapRect)        
        self.pen_red.setWidth(20)
        rect_item.setPen(self.pen_red)
        self.m_scene.addItem(rect_item)  
        
        center_x = (x1+x2)/2
        center_y = (y1+y2)/2        
        
        horizontal_line = QGraphicsLineItem(pixmapRect.left(),center_y,pixmapRect.right(),center_y)
        horizontal_line.setPen(self.pen_red)
        self.m_scene.addItem(horizontal_line)
        
        vertical_line = QGraphicsLineItem(center_x,pixmapRect.top(),center_x,pixmapRect.bottom())
        vertical_line.setPen(self.pen_red)
        self.m_scene.addItem(vertical_line)
                
    def updateROI (self, ng_og_state, selectItem, labelstring):
        if ng_og_state == 'NG':
            pen = self.pen_red
        elif ng_og_state == 'OK':
            pen = self.pen_green
            
        if selectItem in self.rect_item_dict.keys(): 
            self.rect_item_dict[self.selectlabelInfo][0].setPlainText(labelstring)
            self.rect_item_dict[self.selectlabelInfo][1].setPen(pen)
            
            
        
                    
    def resetUnMoved(self):
        self.enable_move = False
        self.moved_rect = None
        self.selectlabelInfo = -1
        for key in self.rect_item_dict.keys():
            self.rect_item_dict[key][1].setPen(self.pen_green)            
            self.rect_item_dict[key][1].setFlag(QGraphicsItem.ItemIsMovable, False)             
        self.scaleImage(self.pixmapItem.pixmap())
                    
    
    def resetImage(self,pixmap):
        self.m_scene.clear()  
        self.addImage(pixmap)
                
    def clearall(self):                              
                
        self.rect_item_dict = {}                
        self.current_rectitem = None
        self.labelstring_item = None
        self.orderstring_item = None
        self.durationstring_item = None        
        self.start_point = None
        self.end_point = None
        self.drawing = False        
        self.labelstring = None
        self.order = "ignore"   
        self.duration = "ignore"
        self.rect_count = 0
        
        
        self.selectlabelInfo = -1
        self.labelsInfo = []     
        
        self.enable_move = False
        self.moved_rect =  None