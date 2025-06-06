from PySide2.QtWidgets import QLabel
from PySide2.QtCore import QRect, Signal, QPoint
from PySide2.QtGui import Qt,QPainter,QPen,QFont, QColor
import re

class DrawShapes(QLabel):
    
    labelTriggered = Signal()

    def __init__(self, parent=None, enable_draw=False, statusBar=None ,  *args, **kwargs):
        super().__init__(*args, **kwargs)        
        self.enable_draw = enable_draw               
        self.setAlignment(Qt.AlignCenter)
        self.setScaledContents(True)
        self.start_point = None
        self.end_point = None
        self.completed_rect = None
        self.drawing = False        
        self.setCursor(Qt.CrossCursor)    
        self.labelstring = None
        self.order = "ignore"   
        self.duration = "ignore"
        self.clean = False      
        self.labelsInfo = []
        self.updated = False      
        self.selectlabelInfo = -1     
        self.statusbar = statusBar       
        
        self.isPosition = False
        
        self.pen_anchor1 = QPen(Qt.magenta)
        self.pen_anchor1.setWidth(4)
        
        self.pen_anchor2 = QPen(Qt.green)        
        self.pen_anchor2.setWidth(4)
        
        self.pen_anchor3 = QPen(Qt.cyan)
        self.pen_anchor3.setWidth(4)
        
    def getPixmapRect(self):
        labelsize = self.size()    
        imagesize = self.pixmap().size()
        imagerect = QRect((labelsize.width() - imagesize.width())/2,(labelsize.height() - imagesize.height())/2, imagesize.width(), imagesize.height())
        return imagerect

    def mousePressEvent(self, event):           
        if self.enable_draw:
            if event.button() == Qt.LeftButton:
                self.drawing = True
                self.start_point = event.pos()
                self.end_point = event.pos()
        else:            
            if not self.isPosition:                            
                if self.labelstring:                
                    self.statusbar.showMessage('Please select an image or capture an image.')
                else:
                    self.statusbar.showMessage('please select a label class in Label List.')
        
    def mouseMoveEvent(self, event):            
        if self.start_point:
            self.end_point = event.pos()
            self.update()            
        
    def mouseReleaseEvent(self, event):        
        if event.button() == Qt.LeftButton:
            if self.drawing and (self.start_point != self.end_point):
                self.drawing = False                            
                imagerect = self.getPixmapRect()
                self.completed_rect = imagerect.intersected(QRect(self.start_point, self.end_point).normalized())
                self.labelTriggered.emit()
                self.update()                

    
    def paintEvent(self, event):        
        super().paintEvent(event)
        
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        pen = QPen(Qt.red)
        pen.setWidth(4)
        painter.setPen(pen) 
            
        
        font = QFont()
        font.setFamily('Times')
        font.setBold(True)
        font.setPointSize(15)
        painter.setFont(font)
                                               
        
        if self.drawing: 
            self.drawallRect(painter)                                                           
            rect = QRect(self.start_point, self.end_point).normalized()
            painter.setPen(pen)           
            painter.drawRect(rect)
            self.drawallRect(painter)            
            painter.end()
        elif self.completed_rect:
            self.drawallRect(painter)
            if self.labelstring == 'point1':
                painter.setPen(self.pen_anchor1)        
            elif self.labelstring  == 'point2':
                painter.setPen(self.pen_anchor2)
            elif self.labelstring == 'point3':
                painter.setPen(self.pen_anchor3)
            else:
                painter.setPen(pen)
            painter.drawRect(self.completed_rect)   
            painter.setPen(Qt.yellow)
            painter.drawText(self.completed_rect.left(),self.completed_rect.top()-5,f'{self.labelstring}')
            if self.order.lower() != 'ignore':
                painter.drawText(self.completed_rect.left(),self.completed_rect.bottom()+20,f'order:{self.order}')            
            if self.duration.lower() != 'ignore':
                painter.drawText(self.completed_rect.left(),self.completed_rect.bottom()+35,f'duration:{self.duration}')
            painter.end()
        
        elif self.clean:                                                        
            self.clean = False            
            painter.end()
        
        elif self.updated:                                
            self.updated = False    
            self.selectlabelInfo = -1         
            self.drawallRect(painter)
            self.drawSelectRect(painter)
            painter.end()
                       
        else:            
            if self.labelsInfo:
               self.drawallRect(painter)
               self.drawSelectRect(painter) 
            painter.end()
            
        
    def getLabelRectFromPixmap(self, rectOnPixmapPosition):
        pixmaprect = self.getPixmapRect()
        #move rect on the pixmap
        rectOnPixmapPosition.translate(pixmaprect.left(),pixmaprect.top())
        return rectOnPixmapPosition

    def getROIRectOnPixmap(self):
        rect = self.getPixmapRect()
        #I don't know why "realrect = self.completed_rect" is not a copy action...
        realrect = QRect(self.completed_rect)
        realrect.translate(-rect.x(),-rect.y())
        return realrect
    
    def drawallRect(self,painter):
        pen_green = QPen(Qt.green)
        pen_green.setWidth(4)
                
        if self.labelsInfo:
            for info in self.labelsInfo:
                item = info.split(';')                                
                start_x, start_y = [int(match) for match in re.findall(r'\d+', item[1])]
                end_x, end_y = [int(match) for match in re.findall(r'\d+', item[2])]
                
                start_point = QPoint(start_x,start_y)
                end_point = QPoint(end_x,end_y)        
                if item[0] == 'point1':
                    painter.setPen(self.pen_anchor1)        
                elif item[0] == 'point2':
                    painter.setPen(self.pen_anchor2)
                elif item[0] == 'point3':
                    painter.setPen(self.pen_anchor3)
                else:
                    painter.setPen(pen_green)     
                
                labelrect = self.getLabelRectFromPixmap(QRect(start_point,end_point))
                painter.drawRect(labelrect)                                
                painter.setPen(Qt.yellow)        
                painter.drawText(labelrect.left(),labelrect.top()-5,f'{item[0]}')
                if item[3].lower() != 'ignore':
                    painter.drawText(labelrect.left(),labelrect.bottom()+20,f'order:{item[3]}')
                if item[4].lower() != 'ignore':
                    painter.drawText(labelrect.left(),labelrect.bottom()+35,f'duration:{item[4]}')
                            
    def drawSelectRect(self,painter):        
        if self.selectlabelInfo > -1:
            item = self.labelsInfo[self.selectlabelInfo].split(';')            
            
            pen = QPen(Qt.cyan)
            pen.setWidth(4)
            start_x, start_y = [int(match) for match in re.findall(r'\d+', item[1])]
            end_x, end_y = [int(match) for match in re.findall(r'\d+', item[2])]
            start_point = QPoint(start_x,start_y)
            end_point = QPoint(end_x,end_y)  
            labelrect = self.getLabelRectFromPixmap(QRect(start_point,end_point))          
            painter.setPen(pen)        
            painter.drawRect(labelrect)                
            painter.setPen(Qt.yellow)
            painter.drawText(labelrect.left(),labelrect.top()-5,f'{item[0]}')
            if item[3].lower() != 'ignore':
                painter.drawText(labelrect.left(),labelrect.bottom()+20,f'order:{item[3]}')            
                    
    def clearall(self):
        self.clean = True
        self.completed_rect = None
        self.drawing = None
        self.start_point = None
        self.end_point = None
        self.labelstring = None
        self.order = "ignore"  
        self.duration = "ignore"
        self.selectlabelInfo = -1
        self.labelsInfo = []
        self.update()
        
    def drawselect(self):        
        self.updated = False
        self.drawing = None
        self.completed_rect = None
        self.clean = False
        self.update()
