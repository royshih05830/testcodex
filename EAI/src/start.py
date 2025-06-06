import sys,argparse
from PySide2.QtWidgets import QApplication, QMainWindow,QFileDialog,QLabel \
                              ,QTableWidgetItem,QDialog,QMessageBox, QTableWidget \
                              ,QActionGroup,QAction, QComboBox, QHeaderView, QDialogButtonBox \
                              ,QTextBrowser, QStyledItemDelegate, QFrame, QLineEdit,QMenu
from PySide2 import QtCore
from PySide2.QtGui import Qt,QPixmap,QIntValidator, QFont,QImage, QIcon, QDoubleValidator
from ui.login import Ui_login_Dialog
from ui.main_new import Ui_MainWindow
from ui.selectproduct import Ui_SelectProduct
from ui.editlabel import Ui_EditLabel_Dialog
from ui.fileconflict import Ui_FileConflict
from ui.registrationanchor import Ui_RegistrationDialog
from ui.autolabel import Ui_AutoLabel_Widget
from ui.editROInote import Ui_EditROINote_Dialog
from ui.overtimeStep import Ui_OvertimeStep_Dialog
from ui.errorStep import Ui_ErrorStep_Dialog

import os, shutil, platform, pathlib
from natsort import natsorted
import math
import time
from datetime import datetime
import mimetypes
# Required to import to get ADLINK inference metadata
import adroi
from Train import train

import json
import numpy as np

from time import sleep

from liveStream_GraphicsView import LiveStream
from liveStream_GraphicsView import sample_to_numpy, get_sample_format
import re
from enum import Enum
import gi
gi.require_version('Gst', '1.0')
from gi.repository import Gst, GObject

from thresholdRecommander import ThresholdRecommander
from sound.soundControl import SoundThread

TRANSLATOR = QtCore.QTranslator()

isDEMO = False

os.chdir(pathlib.Path(__file__).parent)

def getErrorCodeTable():
    errorcodePath = os.path.join('config','errorCode.json')
    if os.path.exists(errorcodePath):
        with open(errorcodePath,'r') as json_file:
            errorCodeTable = json.load(json_file)
            
    return errorCodeTable

def getErrorStepCodeTable():
    failStepPath = os.path.join('config','failStepCode.json')
    if os.path.exists(failStepPath):
        with open(failStepPath,'r') as json_file:
            failStepcode = json.load(json_file)
            
    return failStepcode


def getMESWebServiceURL():
    serviceConfig = os.path.join('config','MESWebService.json')
    if os.path.exists(serviceConfig):
        with open(serviceConfig,'r') as json_file:
            service = json.load(json_file)
        MESWebService_url = service['MESWebService']['url']
    else:
        MESWebService_url = 'http://itetp.adlinktech.com/Modules/SmartFactory/AutomationTP.asmx/GetADLINKSNInfoJson'
    return MESWebService_url

def getAdmin():
    accountConfig = os.path.join('config','account.json')
    if os.path.exists(accountConfig):
        with open(accountConfig,'r') as json_file:
            account = json.load(json_file)
        adminuser = account['users']['admin']['username']
        adminpw = account['users']['admin']['password']
    else:
        adminuser = "admin"
        adminpw = "admin"
    return adminuser, adminpw

adminuser, adminpw = getAdmin()

class tabNameList():
    systemSetting = 'tab_setting'
    training = 'tab_training'
    inspection = 'tab_inspection'
    reconfirm = 'tab_reconfirm'
    advancedOperation = 'tab_online'    
    sop = 'tab_sop'

class userType(Enum):
    Admin = 0
    Corrector = 1 
    Trainer = 1    
    Operator = 2    

removeTab = {userType.Admin: [], userType.Trainer: [tabNameList.systemSetting,tabNameList.inspection,tabNameList.sop], userType.Operator:[tabNameList.systemSetting,tabNameList.training,tabNameList.reconfirm,tabNameList.advancedOperation]}

trainingModeTab = {'DIP':{'hide':[],
                          'show':[tabNameList.training,tabNameList.reconfirm,tabNameList.advancedOperation]},
                   'SOP':{'hide':[tabNameList.reconfirm,tabNameList.advancedOperation],
                          'show':[tabNameList.training]}}

inferenceModeTab = {'DIP':{'hide':[tabNameList.sop],
                           'show':[tabNameList.inspection]},
                    'SOP':{'hide':[tabNameList.inspection],
                           'show':[tabNameList.sop]}}


class cameraType():    
    usb3 = "USB3 Camera"
    web = "Web Camera"
    basler = "Basler Camera"
    

if platform.system() == "Linux":  
    projectRoot = os.path.join(os.path.expanduser("~"), "AAI")   # ~/AAI
    logRoot = os.path.join(os.path.expanduser("~"), "SOPLog")   # ~/SOPLog, mount to \\{IP}\FT_Report\AVI_log\{專案資料夾}
    
support_image_list = [".png",".jpg",".bmp"]
labled_flag = ['Unlabeled','Labeled']

golden_filename = 'golden.png'
golden_labelinfo = 'golden.txt'

default_threshold = str(0.9)
default_ok_threshold = 1
default_ng_threshold = 0.1
default_pass_frame = 2

maxIndex = 10

comboxItemList1 = [ #'Ignore',
                  '1','2','3','4','5','6','7','8','9','10',
                  '11','12','13','14','15','16','17','18','19','20',
]

comboxItemList2 = ['Ignore',
                  '1','2','3','4','5','6','7','8','9','10',
                  '11','12','13','14','15','16','17','18','19','20',
                  '21','22','23','24','25','26','27','28','29','30',
                  '31','32','33','34','35','36','37','38','39','40',
                  '41','42','43','44','45','46','47','48','49','50',
                  '51','52','53','54','55','56','57','58','59','60']

g_SHIFT_MAP = {'!':'1', '@':'2', '#':'3', '$':'4', '%':'5', '^':'6', '&':'7', '*':'8', '(':'9', ')':'0'}
    
def findProductNum(sn):
        
    url = getMESWebServiceURL()
    from MESWebService.service import getProductNumber2
    PN,_ = getProductNumber2(url,sn)        
        
    if PN:        
        return PN
## for DEMO
    else:  
        if isDEMO:
            print('[Use fake find PN service]')                
            
            #demo, sn mapping pn table. how to generate?
            pnconfig = os.path.join('config','pnlist.json')
            with open(pnconfig,'r') as json_file:
                pnList = json.load(json_file)
                
            for pn in pnList.keys():
                if sn in pnList[pn]['serial']:
                    return pn
        return ""
    
def parsePN(PN):
    pattern = rf'^([A-Za-z0-9]+)-([A-Za-z0-9]+)-([A-Za-z0-9]+)$'
    match = re.match(pattern, PN)
    
    if match:
        # 拆解為 Level, ProductCode, Version
        level, product_code, version = match.groups()
        return True, level, product_code, version
    else:
        return False, None, None, None


def rename_file_with_pathlib(file_path, new_name):
    file = pathlib.Path(file_path)
    
    
    # 構建新的檔案路徑
    new_file_path = file.with_name(f"{new_name}{file.suffix}")
    
    if os.path.exists(file_path):
        # 更改檔案名稱
        file.rename(new_file_path)
    
    print(f"The file has been renamed to : {new_file_path}")
    return new_file_path
    
class SaveImageThread(QtCore.QThread):
    finished = QtCore.Signal()
    
    def __init__(self, pixmap: QPixmap, save_path: str):
        super().__init__()
        self.pixmap = pixmap
        self.save_path = save_path

    def run(self):        
        self.pixmap.save(self.save_path,format='PNG')
        self.finished.emit()
    
class ComBoxDelegate(QStyledItemDelegate):
    def __init__(self, parent= None,comboxList=[] ):
        self.comboxList = comboxList
        super().__init__(parent)
            
    def createEditor(self, parent, option, index):                
        # 创建 QComboBox 作为编辑控件
        
        combo = QComboBox(parent)
        # 添加选项到 QComboBox        
        combo.addItems(self.comboxList)
        return combo

    def setEditorData(self, editor, index):
        # 获取单元格的当前文本
        current_text = index.data()
        # 设置 QComboBox 的当前索引为单元格的值
        idx = editor.findText(current_text)
        if idx >= 0:
            editor.setCurrentIndex(idx)

    def setModelData(self, editor, model, index):
        # 将 QComboBox 的当前选择值写入单元格
        model.setData(index, editor.currentText())

class LoginDialog(QDialog):
    def __init__(self):
        super().__init__()
        
        self.login = Ui_login_Dialog()
        self.login.setupUi(self)
        self.usertype = None
        self.username = ""
        self.password = ""
        self.projectName = ""
        self.newProject = False
        
        self.login.create_checkBox.setEnabled(False)        
        self.login.radioButton_operator.clicked.connect(self.changeType)
        self.login.radioButton_corrector.clicked.connect(self.changeType)
        self.login.radioButton_admin.clicked.connect(self.changeType)
        self.login.login_pushButton.clicked.connect(self.on_login)  
        self.login.projectName_lineEdit.returnPressed.connect(self.project_enter_pressed)
        self.login.username_edit.setPlaceholderText('Employee Number')
        self.login.username_edit.returnPressed.connect(self.on_login)
        self.login.username_label.setText('User*')
        self.login.password_edit.returnPressed.connect(self.on_login)
        
        self.login.login_pushButton.setAutoDefault(False)
        self.login.login_pushButton.setDefault(False)
        
        self.login.projectName_lineEdit.setFocus()
        
        self.setWindowIcon(QIcon(u":/<icon>/resource/EVA_logo_light_gray.png"))
        
    def project_enter_pressed(self):        
        self.login.username_edit.setFocus()        
        
    def changeType(self):        
        if self.login.radioButton_operator.isChecked():            
            self.login.password_edit.setEnabled(False)
            self.login.password_label.setEnabled(False)
            self.login.create_checkBox.setEnabled(False)
            self.login.username_label.setText('User*')
            self.login.password_label.setText('Password')
            self.login.username_edit.setPlaceholderText('Employee Number')
        elif self.login.radioButton_corrector.isChecked():             
            self.login.password_edit.setEnabled(False)
            self.login.password_label.setEnabled(False)
            self.login.create_checkBox.setEnabled(False)
            self.login.username_label.setText('User')
            self.login.password_label.setText('Password')
            self.login.username_edit.setPlaceholderText('Employee Number')
        elif self.login.radioButton_admin.isChecked():            
            self.login.password_edit.setEnabled(True)
            self.login.password_label.setEnabled(True)
            self.login.create_checkBox.setEnabled(True)
            self.login.username_label.setText('User*')
            self.login.password_label.setText('Password*')
            self.login.username_edit.setPlaceholderText('')
            
    def on_login(self):     
        self.projectName = self.login.projectName_lineEdit.text()   
        self.fullScreen = self.login.fullscreen_checkBox.isChecked()
        if self.projectName:
            
            if self.login.radioButton_operator.isChecked():  
                self.usertype = userType.Operator        
                self.username = self.login.username_edit.text()
                if self.username == '':
                    self.login.username_edit.setFocus()
                    self.login.username_edit.setPlaceholderText('Cannot be empty.')
                else:
                    self.accept()
                
            elif self.login.radioButton_corrector.isChecked():
                self.usertype = userType.Corrector
                self.username = self.login.username_edit.text()
                self.accept()
                
            elif self.login.radioButton_admin.isChecked():            
                self.usertype = userType.Admin
                
                self.newProject = True if self.login.create_checkBox.isChecked() else False                            
            
                self.username = self.login.username_edit.text()
                self.password = self.login.password_edit.text()
                                
                if self.username == adminuser and self.password == adminpw :
                    self.accept()                                  
                else:
                    if self.username == adminuser:
                        QMessageBox.warning(self, "Password incorrect", "Please enter the correct password!")
                    else:
                        QMessageBox.warning(self, "Password incorrect", "Please enter the correct user name!")    
        else:
            QMessageBox.critical(self, "Warning", "Please enter project name!")
            
                        

class StartProject(QDialog):
    def __init__(self,projectName):
        super().__init__()

        self.projectName = projectName
        self.productNumber = ""
        self.projectPath = ""
        self.imagesDir = ""
        self.imagesGoldenDir = ""
        self.labelsDir = ""
        self.labelsGoldenDir = ""
        self.labelListFile = ""
                
        self.dlg = Ui_SelectProduct()
        self.dlg.setupUi(self)

        self.dlg.sn_lineEdit.setAttribute(Qt.WA_InputMethodEnabled, False)

        self.dlg.buttonBox.accepted.connect(self.confirm)                
        self.dlg.sn_lineEdit.textChanged.connect(self.finePN)
        self.dlg.pn_lineEdit.textChanged.connect(self.enableUseExistImageCheckbox)
        self.dlg.useImage_checkBox.clicked.connect(self.useExistImage)
        self.dlg.imageLocation_toolButton.clicked.connect(self.chooseImageLocation) 
            
    def enableUseExistImageCheckbox(self):
        if self.dlg.pn_lineEdit.text():
            self.dlg.useImage_checkBox.setEnabled(True)
        else:
            self.dlg.useImage_checkBox.setEnabled(False)
    
    def useExistImage(self):
        if self.dlg.useImage_checkBox.isChecked():
            self.dlg.imageLocation_lineEdit.setEnabled(True)
            self.dlg.imageLocation_toolButton.setEnabled(True)
        else:
            self.dlg.imageLocation_lineEdit.setEnabled(False)
            self.dlg.imageLocation_toolButton.setEnabled(False)
            
    def switchSHIFTtoSN(self,serialString,lineEdit):
        fixed_text = ''.join(g_SHIFT_MAP.get(c, c) for c in serialString)
        
        if fixed_text != serialString:  # avoid loop
            lineEdit.blockSignals(True)
            lineEdit.setText(fixed_text)
            serialString = fixed_text
            lineEdit.blockSignals(False)
            
        return serialString
       
    def finePN(self,text):       
        widget = QApplication.focusWidget()  # 取得目前擁有焦點的 widget
        if isinstance(widget, QLineEdit):  # 確保它是 QLineEdit                          
            text = self.switchSHIFTtoSN(text,widget) 
        
        pn = findProductNum(text)
        
        # mabye need to compare with system setting product number (productNum_setting_lineEdit)
        
        # For Demo
        if isDEMO:
            if 'DIP' in self.projectName:
                pn = 'PN-demo'
        self.dlg.pn_lineEdit.setText(pn)

    def chooseImageLocation(self):
        dir = QFileDialog.getExistingDirectory(self,"Open Directory",options=QFileDialog.DontUseNativeDialog)
        if dir:
            self.dlg.imageLocation_lineEdit.setText(dir)

    def make_dir(self,path):
        if not os.path.exists(path):
            os.makedirs(path,exist_ok=True)
    
    def confirm(self):   
        self.productNumber = self.dlg.pn_lineEdit.text()
            
        if self.productNumber == "":            
            if self.dlg.sn_lineEdit:
                QMessageBox.critical(None,"Warning","Please confirm the SN!")
            else:
                QMessageBox.critical(None,"Warning","Plaese enter PN or SN!")
            return
                    
        self.projectPath = os.path.join(projectRoot,self.productNumber,self.projectName)  # ~/AAI/pn/projectNAme
        #iniFile = os.path.join(self.projectPath,self.proName+'.ini')
        settingFile = os.path.join(self.projectPath,'setting.json') #	~/AAI/pn/projectName/setting.json
        self.labelListFile = os.path.join(self.projectPath,'golden','labellist.txt')  # ~/AAI/pn/projectName/golden/labellist.txt
        self.imagesDir = os.path.join(self.projectPath,'train','images')  # ~/AAI/pn/projectName/train/images/<pn>_<timestamp>.png
        self.imagesGoldenDir = os.path.join(self.projectPath,"golden")      # ~/AAI/pn/projectName/golden/golden.png
        self.labelsDir = os.path.join(self.projectPath,'train','labels')    #  ~/AAI/pn/projectName/train/labels/<pn>_<timestamp>.txt
        self.labelsGoldenDir = os.path.join(self.projectPath,"golden")    # ~/AAI/pn/projectName/golden/golden.txt
        
        if os.path.exists(settingFile):
            with open(settingFile, 'r') as json_file:
                settings = json.load(json_file)
            if settings['projectName'] != self.projectName:
                QMessageBox.critical(None,"Critical",f"Please contact the administrator to confirm the project setting!\n- Project Name :{self.projectName}\nProject Name in setting: {settings['projectName']}")
                return self.reject()
            if settings['productNumber'] != self.productNumber:
                QMessageBox.critical(None,"Critical",f"Please contact the administrator to create the product number ({self.productNumber}) with this project ({self.projectName})!")
                return self.reject()
        else:
            QMessageBox.critical(None,"Warning","No matching setting file.\nPlease contact administrator to create the project settings by system settings!")
            return self.reject()
        
        self.make_dir(self.projectPath)        
        self.make_dir(self.imagesDir)
        self.make_dir(self.imagesGoldenDir)
        self.make_dir(self.labelsDir)
        self.make_dir(self.labelsGoldenDir)                        
        
        if not os.path.exists(self.labelListFile):
            f = open(self.labelListFile,"w")
            f.close()  


        srcImageDir = self.dlg.imageLocation_lineEdit.text()      
        stopped = False
        applyAll = False
        removeConfig = False
        replaced = False          
        if srcImageDir:  # src
            if os.path.exists(srcImageDir):

                for srcfile in os.listdir(srcImageDir):
                    
                    if stopped:
                        break
                    else:
                        filename, fileextension = os.path.splitext(srcfile)
                        if fileextension in support_image_list:  
                            if os.path.exists(os.path.join(self.imagesDir,srcfile)):
                                if applyAll:
                                    pass
                                    if replaced:
                                        if removeConfig:
                                            self.removeImageConfig(filename) 
                                        shutil.copy(os.path.join(srcImageDir,srcfile),self.imagesDir)
                                    else:
                                        stopped = True
                                else:
                                    fileconflict = FileConflict(srcfile)
                                    ret = fileconflict.exec_()
                                    applyAll = fileconflict.dlg.applyAll_checkBox.isChecked()
                                    if ret == QDialog.Accepted:
                                        replaced = True                        
                                        removeConfig = fileconflict.dlg.removeLabelInfo_checkBox.isChecked()
                                        shutil.copy(os.path.join(srcImageDir,srcfile),os.path.join(self.imagesDir,fileconflict.dlg.rename_lineEdit.text()))
                                        if removeConfig:
                                            self.removeImageConfig(filename)               
                                    else:
                                        stopped = fileconflict.stopped
                                        continue
                            else:
                                shutil.copy(os.path.join(srcImageDir,srcfile),self.imagesDir)
                
        self.accept()                  
                
    def removeImageConfig(self,filename):
        labedfile = os.path.join(self.labelsDir,f'{filename}.txt')
        if os.path.exists(labedfile):
            os.remove(labedfile)         



class Registration(QDialog):
    def __init__(self,positionImage,positionFile):
        super().__init__() 
        self.positionImage = positionImage
        self.positionFile = positionFile        
        self.positiondict = {}        
        
        self.dlg = Ui_RegistrationDialog()
        self.dlg.setupUi(self)         
        self.dlg.showImage_graphicsView.isPosition = True
        self.dlg.showImage_graphicsView.labelstring = ""
        self.dlg.showImage_graphicsView.labelTriggered.connect(self.getAnchorPoint)
                
        self.dlg.buttonBox.accepted.connect(self.confirm) 
                
        self.dlg.addpoint1_pushButton.clicked.connect(self.drawPoint1)
        self.dlg.addpoint2_pushButton.clicked.connect(self.drawPoint2)
        self.dlg.addpoint3_pushButton.clicked.connect(self.drawPoint3)
                
        self.initPosition()
        
        self.scaleOnce = True
       
    def initPosition(self):
        if os.path.exists(self.positionImage):
            pixmap = QPixmap(self.positionImage)
            self.dlg.showImage_graphicsView.set_image(pixmap)
            
        if os.path.exists(self.positionFile):
            
            pixmap = QPixmap(self.positionImage)            

            imageHeight = pixmap.height()
            imageWidth = pixmap.width()
            
            # read file
            with open(self.positionFile) as f:
                anchors = f.read().splitlines()             
            
            self.dlg.showImage_graphicsView.labelsInfo = []
            # get point1~3 normalize point
            for i in range(len(anchors)):
                anchor = anchors[i].split()
                if len(anchor) !=5:
                    continue

                self.positiondict[anchor[0]] = f'{anchor[1]} {anchor[2]} {anchor[3]} {anchor[4]}'
                
                # calculate start points and end points
                start_x = float(anchor[1])*imageWidth
                start_y = float(anchor[2])*imageHeight
                end_x = float(anchor[3])*imageWidth
                end_y = float(anchor[4])*imageHeight
                               
                
                if anchor[0] == 'point1':
                    self.dlg.point1_lineEdit.setText(f'({round(float(anchor[1]),3)},{round(float(anchor[2]),3)});({round(float(anchor[3]),3)},{round(float(anchor[4]),3)})')                   
                elif anchor[0] == 'point2':
                    self.dlg.point2_lineEdit.setText(f'({round(float(anchor[1]),3)},{round(float(anchor[2]),3)});({round(float(anchor[3]),3)},{round(float(anchor[4]),3)})') 
                elif anchor[0] == 'point3':
                    self.dlg.point3_lineEdit.setText(f'({round(float(anchor[1]),3)},{round(float(anchor[2]),3)});({round(float(anchor[3]),3)},{round(float(anchor[4]),3)})') 
                

                self.dlg.showImage_graphicsView.labelsInfo.append(f'{anchor[0]};({round(start_x)},{round(start_y)});({round(end_x)},{round(end_y)});{self.dlg.showImage_graphicsView.order};{self.dlg.showImage_graphicsView.duration}')
                
            self.dlg.showImage_graphicsView.drawallRect()
                      
        
    def resetImageLabel(self):     
        self.dlg.showImage_graphicsView.m_scene.clear()        
        
    def resetAnchorPoint(self):
        self.dlg.point1_lineEdit.clear()
        self.dlg.point2_lineEdit.clear()
        self.dlg.point3_lineEdit.clear()
                
    
    def drawPoint1(self):        
        self.dlg.showImage_graphicsView.enable_draw = True
        self.dlg.showImage_graphicsView.labelstring = "point1"                
    
    def drawPoint2(self):        
        self.dlg.showImage_graphicsView.enable_draw = True
        self.dlg.showImage_graphicsView.labelstring = "point2"                
        
    def drawPoint3(self):        
        self.dlg.showImage_graphicsView.enable_draw = True
        self.dlg.showImage_graphicsView.labelstring = "point3"                
    
    def getAnchorPoint(self):          
        rect = self.dlg.showImage_graphicsView.current_rectitem.rect().normalized()
        pixmap = self.dlg.showImage_graphicsView.pixmapItem.pixmap()
        
        start_x = rect.left()/pixmap.width()   
        start_y = rect.top()/pixmap.height() 
        end_x = rect.right()/pixmap.width() 
        end_y = rect.bottom()/pixmap.height() 
        
        lineText = f'({round(start_x,3)},{round(start_y,3)});({round(end_x,3)},{round(end_y,3)})'
        dictItem = f'{start_x} {start_y} {end_x} {end_y}'
        
        if self.dlg.showImage_graphicsView.labelstring == 'point1':            
            self.dlg.point1_lineEdit.setText(lineText)
            self.positiondict['point1'] = dictItem
        elif self.dlg.showImage_graphicsView.labelstring == 'point2':
            self.dlg.point2_lineEdit.setText(lineText)
            self.positiondict['point2'] = dictItem
        elif self.dlg.showImage_graphicsView.labelstring == 'point3':
            self.dlg.point3_lineEdit.setText(lineText)
            self.positiondict['point3'] = dictItem

        
    def confirm(self):      
        
        noAnchor = False
        message = ''
        
        if not self.dlg.point1_lineEdit.text():
            noAnchor = True
            message += 'Point1 '
        if not self.dlg.point2_lineEdit.text():
            noAnchor = True
            message += 'Point2 '
        if not self.dlg.point3_lineEdit.text():
            noAnchor = True
            message += 'Point3 '
            
        if noAnchor:                
            QMessageBox.critical(self,"Warning","Plaese add anchor point:\n"+message)
            return                        
                
        self.accept()
        
    

class FileConflict(QDialog):
    def __init__(self, filename):
        super().__init__()
        
        self.filename = filename
        self.stopped = False
        
        
        self.dlg = Ui_FileConflict()
        self.dlg.setupUi(self)
                
        self.dlg.buttonBox.rejected.connect(self.stopCopy)
        self.dlg.replace_pushButton.clicked.connect(self.accept)
        self.dlg.skip_pushButton.clicked.connect(self.reject)
        
        self.dlg.rename_checkBox.clicked.connect(self.enabledRename)
        self.dlg.applyAll_checkBox.clicked.connect(self.checkApplyAll)
        
        self.updateFilename()        
    
    def stopCopy(self):
        self.stopped = True
        self.reject()
        
    
        
    def updateFilename(self):
        title = self.dlg.title_label.text()
        newtitle= title.format(self.filename)
        self.dlg.title_label.setText(newtitle)
        self.dlg.rename_lineEdit.setText(self.filename)
        
    def enabledRename(self):
        self.dlg.rename_lineEdit.setEnabled(self.dlg.rename_checkBox.isChecked())
        
            
    def checkApplyAll(self):
        if self.dlg.applyAll_checkBox.isChecked():
            self.dlg.rename_checkBox.setEnabled(False)
            self.dlg.rename_lineEdit.setEnabled(False)
        else:
            self.dlg.rename_checkBox.setEnabled(True)
            self.dlg.rename_lineEdit.setEnabled(True)
        
class EditLabel(QDialog):
    def __init__(self, labelListFile):
        super().__init__()
        
        self.dlg = Ui_EditLabel_Dialog()
        self.dlg.setupUi(self)
        self.labelListFile = labelListFile
        self.dlg.buttonBox.accepted.connect(self.confirm)
        self.dlg.buttonBox.rejected.connect(self.reject)
        self.labels=[]
        self.showList()
        
        self.dlg.edit_pushButton.setVisible(False)        
        
        self.dlg.new_pushButton.clicked.connect(self.new)        
        self.dlg.delete_pushButton.clicked.connect(self.delete)
        
        
    def showList(self):
        if os.path.exists(self.labelListFile):
            with open(self.labelListFile) as f:
                self.labels = f.read().splitlines()            
            self.dlg.edit_listWidget.addItems(self.labels)
            
        for i in range(self.dlg.edit_listWidget.count()):
            item = self.dlg.edit_listWidget.item(i)            
            item.setFlags(item.flags() | Qt.ItemIsEditable)
        
    def new(self):
        row = self.dlg.edit_listWidget.count()
        self.dlg.edit_listWidget.addItem("")        
        self.dlg.edit_listWidget.setCurrentRow(row)
        item = self.dlg.edit_listWidget.currentItem()
        item.setFlags(item.flags() | Qt.ItemIsEditable)
        self.dlg.edit_listWidget.editItem(item)
    
    def edit(self):        
        item = self.dlg.edit_listWidget.currentItem()             
        self.dlg.edit_listWidget.editItem(item)
            
    def delete(self):        
        self.dlg.edit_listWidget.takeItem(self.dlg.edit_listWidget.currentRow())
        
    
    def confirm(self):
        self.labels=[]
        for i in range(self.dlg.edit_listWidget.count()):            
            self.labels.append(self.dlg.edit_listWidget.item(i).text())
            
        # save file
        self.accept()


class AutoLable(QDialog):
    def __init__(self,img,file):
        super().__init__()
        self.img=img
        self.dlg = Ui_AutoLabel_Widget()

        self.dlg.setupUi(self)
        self.dlg.graphicsView.set_image(img)
        self.dlg.area_pushButton.clicked.connect(self.selecArea)
        self.dlg.pattern_pushButton.clicked.connect(self.selecPattern)
        self.dlg.aotuLabel_pushButton.clicked.connect(self.aotuLabel)        
        self.dlg.buttonBox.button(QDialogButtonBox.Ok).setEnabled(False)
        self.dlg.buttonBox.accepted.connect(self.confirm)
        self.dlg.buttonBox.rejected.connect(self.close)
        self.dlg.graphicsView.readyTriggered.connect(self.enable_autoLabel)
        self.dlg.graphicsView.areaSelected.connect(self.set_area_position)
        self.dlg.graphicsView.patternSelected.connect(self.set_pattern_position)
        self.dlg.graphicsView.finishTriggered.connect(self.enable_accept)
        self.dlg.doubleSpinBox.valueChanged.connect(self.set_threahold)
        self.dlg.spinBox.valueChanged.connect(self.set_level)
        self.dlg.labellist_listWidget.itemClicked.connect(self.enableOK)

        self.loadLabelList(file)
        self.chooseLabel = None
        
        self.hasValue = False
    
    def loadLabelList(self,file):
        if os.path.exists(file):
            with open(file) as f:
                self.labels = f.read().splitlines()            
            self.dlg.labellist_listWidget.addItems(self.labels)
    
    def enableOK(self):        
        if self.hasValue:
            self.dlg.buttonBox.button(QDialogButtonBox.Ok).setEnabled(True)
        else:
            self.dlg.buttonBox.button(QDialogButtonBox.Ok).setEnabled(False)
        
    def confirm(self):
        self.chooseLabel = self.dlg.labellist_listWidget.currentItem().text()
        self.accept()                

    def selecArea(self):
        self.dlg.graphicsView.enable_draw("area")

    def selecPattern(self):
        self.dlg.graphicsView.enable_draw("pattern")

    def aotuLabel(self):
        self.dlg.graphicsView.auto_label()

    def getPositionList(self):
        return self.dlg.graphicsView.get_positions()

    def enable_autoLabel(self):
        self.dlg.aotuLabel_pushButton.setEnabled(True)

    def set_area_position(self,pos):
        self.dlg.search_lineEdit.setText(pos)

    def set_pattern_position(self,pos):
        self.dlg.obj_lineEdit.setText(pos)

    def enable_accept(self):        
        self.hasValue = True
        if self.dlg.labellist_listWidget.currentRow() > -1:
            self.dlg.buttonBox.button(QDialogButtonBox.Ok).setEnabled(True)

    def set_threahold(self,val):        
        self.dlg.graphicsView.threshold=val

    def set_level(self,val):
        self.dlg.graphicsView.overlap=val*5

class FloatDelegate(QStyledItemDelegate):
    def __init__(self, parent=None):
        super().__init__(parent)        
        self.validator = QDoubleValidator(0.0, 1.0, 10, parent)

    def createEditor(self, parent, option, index):
        editor = super().createEditor(parent, option, index)
        editor.setValidator(self.validator)
        return editor

class EditROINote(QDialog):
    def __init__(self, labelInfo_tableWidget:QTableWidget, GoldenImagePath:str, useOffset:bool, offset_threshold_jsonfile:str):
        super().__init__()
        
        self.dlg = Ui_EditROINote_Dialog()
        self.dlg.setupUi(self)    
        
        self.dlg.tableWidget.setColumnWidth(1,400)        
        self.dlg.buttonBox.accepted.connect(self.save)
        
        self.dlg.reset_threshold_pushButton.clicked.connect(self.resetThreshold)
        self.dlg.reset_passframe_pushButton.clicked.connect(self.resetPASSframe)
        self.dlg.clean_pushButton.clicked.connect(self.cleanThreshold)
        
        self.useOffset = useOffset
        self.jsonfile = offset_threshold_jsonfile
        
        self.pixmap = QPixmap(GoldenImagePath) 
        self.labelinfo, self.noteList, self.thresholdList, self.passframeList = self.getLabelInfo(labelInfo_tableWidget)
        
        header = self.dlg.tableWidget.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeToContents)    # Order            
        header.setSectionResizeMode(2, QHeaderView.Stretch)             # Note
        header.setSectionResizeMode(3, QHeaderView.ResizeToContents)    # Threshold
        header.setSectionResizeMode(4, QHeaderView.ResizeToContents)    # PASS frame
                        
        header_item = self.dlg.tableWidget.horizontalHeaderItem(3)
        if header_item:
            if useOffset:
                header_item.setText('The offset of the threshold')
                self.dlg.reset_threshold_pushButton.setText('Reset Offset')
                self.dlg.clean_pushButton.setText('Clean Offset')
            else:
                header_item.setText('Threshold')
                self.dlg.reset_threshold_pushButton.setText('Reset Threshold')
                self.dlg.clean_pushButton.setText('Clean Threshold')
                
        self.initTable() 
        
    def getLabelInfo(self,table:QTableWidget):
        labelinfo = []        
        noteList = []      
        thresholdList = []  
        passframeList = []
        
        for row in range(table.rowCount()):
            order = table.item(row,3).text()
            topLeft = table.item(row,1).text()
            bottomRight = table.item(row,2).text()
            if table.item(row,5):
                note = table.item(row,5).text()
            else:
                note = ''
            if table.item(row,6):
                threshold = table.item(row,6).text()
            else:
                threshold = default_threshold
            if table.item(row,7):
                passFrame = table.item(row,7).text()
            else:
                passFrame = default_pass_frame
                
            pixmap = self.getROIImage(topLeft,bottomRight)                     
            labelinfo.append([order,pixmap,note,threshold,passFrame])            
            noteList.append(note)
            thresholdList.append(threshold)
            passframeList.append(passFrame)
        return labelinfo, noteList, thresholdList, passframeList
    
    
    def getROIImage(self,topLeft,bottomRight):
        start_x, start_y = [int(match) for match in re.findall(r'\d+', topLeft)]
        end_x, end_y = [int(match) for match in re.findall(r'\d+', bottomRight)]                  
        start_point = QtCore.QPoint(start_x,start_y)
        end_point = QtCore.QPoint(end_x,end_y)
        rect = QtCore.QRect(start_point,end_point)
        return self.pixmap.copy(rect)
    
    def createNoteTextBrowser(self,row,column,noteString):        
        temp_textBrowser = QTextBrowser()        
        temp_textBrowser.setPlainText(noteString)
        temp_textBrowser.setReadOnly(False)
        temp_textBrowser.setFrameShape(QFrame.Shape.NoFrame)
        self.dlg.tableWidget.setCellWidget(row,column,temp_textBrowser)

    def initTable(self):        
        self.dlg.tableWidget.setRowCount(len(self.labelinfo))
        for index,row in enumerate(self.labelinfo):
            #order = row[0]
            #pixmap = row[1]
            #note = row[2]
            #threshold = row[3]
            #passframe = row[4]
            
            self.dlg.tableWidget.setItem(index,0,QTableWidgetItem(str(row[0])))                        
            self.dlg.tableWidget.item(index,0).setTextAlignment(Qt.AlignCenter)            
            self.dlg.tableWidget.item(index,0).setFlags(self.dlg.tableWidget.item(index,0).flags() ^ Qt.ItemIsEditable )
            self.createNoteTextBrowser(index,2,str(row[2]))
            self.dlg.tableWidget.setItem(index,3,QTableWidgetItem(str(row[3])))
            self.dlg.tableWidget.item(index,3).setTextAlignment(Qt.AlignCenter)            
            self.dlg.tableWidget.setItem(index,4,QTableWidgetItem(str(row[4])))
            self.dlg.tableWidget.item(index,4).setTextAlignment(Qt.AlignCenter)   
            
            image_label = QLabel()
            image_label.setAlignment(Qt.AlignCenter) 
            
            if row[1].width() > self.dlg.tableWidget.columnWidth(1):
                image_label.setPixmap(row[1].scaledToWidth(self.dlg.tableWidget.columnWidth(1)))        
            elif row[1].width() < self.dlg.tableWidget.columnWidth(1)/8:
                image_label.setPixmap(row[1].scaledToWidth(self.dlg.tableWidget.columnWidth(1)/8))
            else:
                image_label.setPixmap(row[1])
            self.dlg.tableWidget.setCellWidget(index,1,image_label)
            self.dlg.tableWidget.resizeRowToContents(index)
            
        float_delegate = FloatDelegate(self.dlg.tableWidget)
        self.dlg.tableWidget.setItemDelegateForColumn(3, float_delegate)
        
        self.dlg.tableWidget.setItemDelegateForColumn(4, ComBoxDelegate(self.dlg.tableWidget,['1','2','3','4','5']))
            
    def save(self):
        
        for row in range(self.dlg.tableWidget.rowCount()):            
            self.noteList[row] = self.dlg.tableWidget.cellWidget(row,2).toPlainText()
            self.labelinfo[row][2] = self.noteList[row] 
            self.thresholdList[row] = self.dlg.tableWidget.item(row,3).text()            
            self.labelinfo[row][3] = self.thresholdList[row] 
            self.passframeList[row] = self.dlg.tableWidget.item(row,4).text()
            self.labelinfo[row][4] = self.passframeList[row]                        
        
        self.accept()
        
    def resetThreshold(self):
        for row in range(self.dlg.tableWidget.rowCount()):
            self.dlg.tableWidget.item(row,3).setText(str(default_threshold))
            
    def resetPASSframe(self):
        for row in range(self.dlg.tableWidget.rowCount()):
            self.dlg.tableWidget.item(row,4).setText(str(default_pass_frame))
            
    def cleanThreshold(self):
        self.resetThreshold()
        
        if os.path.exists(self.jsonfile):
            os.remove(self.jsonfile)


class FilterLineEdit(QLineEdit):
    def __init__(self, allowed_list, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.allowed_list = allowed_list
        self.textEdited.connect(self.filter_input)
        self._last_valid = ""

    def filter_input(self, text):   
        # 如果輸入字串是允許的其中一項的「前綴」，就接受
        if any(item.startswith(text) for item in self.allowed_list):
            self._last_valid = text
        else:
            self.setText(self._last_valid)  # 還原成最後有效內容

class ErrorStepDialog(QDialog):
    def __init__(self):
        super().__init__()
        
        self.codeList = getErrorStepCodeTable().keys()
        
        self.dlg = Ui_ErrorStep_Dialog()
        self.dlg.setupUi(self)
        
        for item in self.codeList:
            if item != 'END':                                
                self.dlg.label_2.setText(self.dlg.label_2.text().replace('RESTART',item))
                
        self.dlg.enterCode_lineEdit.setFocus()        
        self.dlg.enterCode_lineEdit.textEdited.connect(self.checkErrorCode)                                
        self.dlg.enterCode_lineEdit.setPlaceholderText('/'.join(self.codeList))
        self._last_valid = ""
        
        self.isContinue = False
        
    def switchSHIFTtoSN(self,serialString,lineEdit):
        fixed_text = ''.join(g_SHIFT_MAP.get(c, c) for c in serialString)
        
        if fixed_text != serialString:  # avoid loop
            lineEdit.blockSignals(True)
            lineEdit.setText(fixed_text)
            serialString = fixed_text
            lineEdit.blockSignals(False)
            
        return serialString
        
    def checkErrorCode(self, text):         
        if any(item.startswith(text) for item in self.codeList):
            self._last_valid = text
        else:
            self.dlg.enterCode_lineEdit.setText(self._last_valid)
        
        if self._last_valid == 'END':
            self.isContinue = False                
            self.accept()
        elif self._last_valid in self.codeList: # RESTART
            self.isContinue = True
            self.accept()        
            
    def closeEvent(self, event):             
        QMessageBox.warning(self,'Warning','Please enter '+'/'.join(self.codeList)+' to close.') 
        event.ignore()  # Cannot close the Windows by "x".
        

class OvertimeErrorCodeDialog(QDialog):
    def __init__(self,errorCodetable:dict,overtimeData,user:str,currentNo,totalNo):
        super().__init__()
        
        # overtimeData format {'layer':layer, 'step':order, 'duration':duration, 'image':image}
        
        self.dlg = Ui_OvertimeStep_Dialog()
        self.dlg.setupUi(self)
        
        self.dlg.layer_step_label.setText(str(overtimeData['layer'])+' - '+ str(overtimeData['step']))
        self.dlg.overtime_label.setText(str(overtimeData['overtime'])+'s') 
        self.dlg.duration_label.setText(str(overtimeData['duration'])+'s')        
        
        self.dlg.user_label.setText(user)
        
        self.dlg.currentNumber_label.setText(str(currentNo))
        self.dlg.totalNumber_label.setText(str(totalNo))
        
        self.dlg.showImage_SOP_graphicsView.set_image(overtimeData['image'])
        
        self.dlg.enterCode_lineEdit.setFocus()        
        self.dlg.enterCode_lineEdit.textChanged.connect(self.checkErrorCode)        
        self.errorCodetable = errorCodetable  
        
        self.errorCodeList = None
        
#        self.setWindowFlags(self.windowFlags() & ~Qt.WindowCloseButtonHint)                
        
    def switchSHIFTtoSN(self,serialString,lineEdit):
        fixed_text = ''.join(g_SHIFT_MAP.get(c, c) for c in serialString)
        
        if fixed_text != serialString:  # avoid loop
            lineEdit.blockSignals(True)
            lineEdit.setText(fixed_text)
            serialString = fixed_text
            lineEdit.blockSignals(False)
            
        return serialString    
        
    def check_key_existence(self,input_str, keys_list):        
        if any(key.startswith(input_str) for key in keys_list):
            return True                
        return False

    def checkErrorCode(self,code):
             
        if code=='\n':        
            return
        
        widget = QApplication.focusWidget()  # 取得目前擁有焦點的 widget
        if isinstance(widget, QLineEdit):  # 確保它是 QLineEdit                          
            code = self.switchSHIFTtoSN(code,widget)
          
        done = False                            
        
        if self.check_key_existence(code, self.errorCodetable.keys()):
            if code == 'CLEAR':
               self.dlg.errorCodeList_textEdit.clear()
               done = True
            elif code == 'END':
                if self.dlg.errorCodeList_textEdit.toPlainText():                    
                    self.exit()                
                else:
                    QMessageBox.warning(self,'Error','Error root cause is empty!!!\nPlease scan error code.')
                done = True
            elif code in self.errorCodetable.keys():
                if self.errorCodetable[code]['en'] not in self.dlg.errorCodeList_textEdit.toPlainText():
                    self.dlg.errorCodeList_textEdit.append(self.errorCodetable[code]['en'])
                    done = True
        else:
            done = True
            
        if done:
            self.dlg.enterCode_lineEdit.clear()            
            self.dlg.enterCode_lineEdit.setFocus()            
        
    def exit(self):
        self.errorCodeList = self.dlg.errorCodeList_textEdit.toPlainText()
        self.accept()
        
    def closeEvent(self, event):        
        QMessageBox.warning(self,'Warning','Please scan "END" to close.') 
        event.ignore()  # Cannot close the Windows by "x".
        
class MainWindow(QMainWindow):        
    addOneInsepctRowTriggered = QtCore.Signal(list)         
    def __init__(self,username,projectName,usertype,newProject=False,fullScreen=False):
        super().__init__()
        self.live = False  # live camera flag. True: use camera; False: use static Image    
        self.imageDir = ""
        self.imageGoldenDir = ""
        self.labelsDir = ""
        self.labelsGoldenDir = ""
        self.labelListFile = ""      
        self.projectPath = ""
        self.positionDir = ""
        self.selectPic = False
        self.selectLabel = False     
        self.imageCount = 0      
        self.pageCount = 0
        self.currentPage = 0
        self.liveSrc = None        
        self.filelist = []
        self.ui = Ui_MainWindow()        
        self.ui.setupUi(self)
        self.is_running = True 
        self.scaleOnce = True
        self.isGolden = False    
        self.inference_pipeline = None
        self.SOP_train_okng_flag = ""
        
        self.setWindowIcon(QIcon(u":/<icon>/resource/EVA_logo_light_gray.png"))
        
        self.is_fullscreen = False
        if fullScreen:
            self.showFullScreen()
            self.is_fullscreen = True

        #data path for the inspection (each path sould conatin a project name)
        self.image_golden = None
        self.label_golden = None
        self.anchors_golden = None
        self.inspect_modelfile = None

        #the original image is shown on the centeral label
        self.oriCapturedPixmap = None

        self.triggertimer = None
        
        self.username = username  
        self.isNewProject = newProject
        self.projectName = projectName        
        self.settings = None
        
        self.worker_thread = None
        self.sound_thread = None
                        
                                               
        self.tabdict = {}
        for i in range(self.ui.tabWidget.count()):
            self.tabdict[self.ui.tabWidget.widget(i).objectName()] = i            
        
        for text in removeTab[usertype]:   
            if text in self.tabdict.keys():
                index = self.tabdict[text]         
                self.ui.tabWidget.setTabVisible(index,False)
                
        self.userType = usertype

        
        self.ui.tabWidget.currentChanged.connect(self.currentTab)
        self.currentTab()
            
        self.languageActionGroup = QActionGroup(self.ui.menuLanguage)
        self.languageActionGroup.addAction(self.ui.actionEnglish)        
        self.languageActionGroup.addAction(self.ui.actionChinese)
        self.languageActionGroup.triggered[QAction].connect(self.on_language_changed)
        self.ui.actionEnglish.setChecked(True)
        
        #TBD
        self.ui.menuLanguage.setVisible(False)
        self.ui.menubar.setVisible(False)
        
        self.ui.exit_pushButton.clicked.connect(self.exit)
        
       
        self.inferenceType ='DIP'
        self.current_layers = 1
        
######################### Tab 0 #########################
################## System Setting Mode ##################        
        
        self.ui.training_port_lineEdit.setValidator(QIntValidator(bottom=0, top=65535,parent=self))

        self.ui.projectName_setting_lineEdit.setText(self.projectName)
        self.ui.sn_setting_lineEdit.textChanged.connect(self.findProductNumberForSystemSetting)
        self.ui.productNum_setting_lineEdit.textChanged.connect(self.enableLoadSettings)
        
        self.ui.loadSettings_pushButton.clicked.connect(self.loadSetting)
        
        # TBD, retrain for DIP
        self.ui.retrain_groupBox.clicked.connect(self.searchRetrainData)
        self.ui.retrain_pushButton.clicked.connect(self.retrain)
        self.ui.retrain_groupBox.setVisible(False)
        #self.ui.line_10.setVisible(False)
        
        self.ui.SaveSetting_pushButton.clicked.connect(self.saveProjectSetting)
        
        self.ui.inference_comboBox.currentIndexChanged.connect(self.selectInferenceType)
        
        self.ui.storage_groupBox.setVisible(False)
        
        self.ui.testVideo_toolButton.clicked.connect(self.selectTestmp4Video)
        
        self.ui.rename_radioButton.clicked.connect(self.enableManageLineEdit)
        self.ui.copy_radioButton.clicked.connect(self.enableManageLineEdit)
        self.ui.duplicate_radioButton.clicked.connect(self.enableManageLineEdit)
        self.ui.newProjectName_lineEdit.textChanged.connect(self.enableManageSubmtButton)
        self.ui.newPN_lineEdit.textChanged.connect(self.enableManageSubmtButton)
        
        self.ui.submit_manage_project_pushButton.clicked.connect(self.manageProject)
        
        
######################### Tab 1 #########################
##################### Training Mode #####################
        # training mode
        
        self.ui.train_pushButton.setVisible(False)
        self.ui.calThreshold_pushButton.setVisible(False)        
                
        self.ui.importImage_pushButton.clicked.connect(self.importImage)
                
        self.ui.goldenmode_checkBox.stateChanged.connect(self.setGoldenMode)        
        self.ui.position_pushButton.clicked.connect(self.registrationTool)
        
        self.ui.start_pushButton.clicked.connect(self.start_offline)
        self.ui.train_pushButton.clicked.connect(self.trainProcess)
        
        
        self.ui.golden_tableWidget.setStyleSheet('QTableView::item {border-right: 1px solid #d6d9dc;}')
        self.ui.golden_tableWidget.cellClicked.connect(self.showGolden)
        
        self.ui.showImagelist_tableWidget.setStyleSheet('QTableView::item {border-right: 1px solid #d6d9dc;}')
        self.ui.showImagelist_tableWidget.cellClicked.connect(self.showImageFromTableList)
        self.ui.showImagelist_tableWidget.setContextMenuPolicy(Qt.CustomContextMenu)
        self.ui.showImagelist_tableWidget.customContextMenuRequested.connect(self.showContextMenu)
        self.ui.capture_pushButton.clicked.connect(self.showImageFromStreaming)
        
        self.ui.labelEdit_pushButton.clicked.connect(self.editlabel)
        self.ui.autoLable_pushButton.clicked.connect(self.autolabel)
        
         
                    
        self.ui.labelList_listWidget.clicked.connect(self.drawLabel)
        self.ui.orderList_listWidget.clicked.connect(self.drawLabel)
        self.ui.durationList_listWidget.clicked.connect(self.drawLabel)
        
        self.ui.saveLabel_pushButton.clicked.connect(self.saveLabel)         
        
        
        self.ui.next_pushButton.clicked.connect(self.nextPage)
        self.ui.back_pushButton.clicked.connect(self.backPage)
    
        font = QFont()
        font.setPointSize(8)
        self.ui.labelInfo_tableWidget.setFont(font)     
        self.ui.showImage_offline_graphicsView.labelTriggered.connect(self.addLabelInfoRow)
        self.ui.showImage_offline_graphicsView.movelabelTriggered.connect(self.updateSelectLabelInfoPosition)        
        self.ui.labelInfo_tableWidget.currentItemChanged.connect(self.selectLabelInfoRow)
        self.ui.labelInfo_tableWidget.cellDoubleClicked.connect(self.disabledSelectLabelInfoRow)
        self.ui.delete_pushButton.clicked.connect(self.deleteROI)
        self.isDeleteROI = False
        
        self.ui.export_pushButton.setVisible(False)    
        self.ui.device_offline_comboBox.currentIndexChanged.connect(self.setCurrentSourceType)                                            
        
        self.ui.showImage_offline_graphicsView.statusbar = self.ui.statusbar  
        
        self.ui.EditNote_pushButton.clicked.connect(self.editNote)
    
        self.ui.layerNo_comboBox.currentIndexChanged.connect(self.setGoldenWithLayer)
        
        self.ui.calThreshold_pushButton.clicked.connect(self.getROIcalculateThreshold)        
        
######################### Tab 2 #########################
#################### Inspection Mode ####################
        self.ui.FAIL_easy_label.setVisible(False)
        self.ui.PASS_easy_label.setVisible(False)
        
        self.ui.inspectResult_easy_tableWidget.horizontalHeader().setStretchLastSection(False)
        header = self.ui.inspectResult_easy_tableWidget.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeToContents)        
        header.setSectionResizeMode(1, QHeaderView.Stretch) 
        header.setSectionResizeMode(2, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(3, QHeaderView.ResizeToContents)
        
        self.ui.skip_easy_pushButton.clicked.connect(self.reset)        
        self.ui.sn_easy_lineEdit.textChanged.connect(self.findModel)        
        self.ui.on_off_easy_checkBox.clicked.connect(self.onoff) 
        self.ui.goverify_easy_pushButton.clicked.connect(self.goverify)  
        self.ui.onlyNG_easy_checkBox.clicked.connect(self.onlyNG)
        
        font = QFont()
        font.setPointSize(8)
        self.ui.inspectResult_easy_tableWidget.setFont(font) 
        self.ui.inspectResult_easy_tableWidget.itemSelectionChanged.connect(self.selectInspectRow)        
        
        self.ui.submit_easy_pushButton.clicked.connect(self.submitInspectResult)
        
        self.ui.back_easy_pushButton.clicked.connect(self.backShowROI)
        self.ui.next_easy_pushButton.clicked.connect(self.nextShowROI)

######################### Tab 3 #########################
#################### Reconfirm Mode #####################   

        self.ui.sn_confirm_lineEdit.textChanged.connect(self.searchReconfirmedInfo)     
        
        self.ui.inspectResult_confirm_tableWidget.horizontalHeader().setStretchLastSection(False)
        header = self.ui.inspectResult_confirm_tableWidget.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeToContents)        
        header.setSectionResizeMode(1, QHeaderView.Stretch) 
        header.setSectionResizeMode(2, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(3, QHeaderView.ResizeToContents) 
        
        self.ui.reset_confirm_pushButton.clicked.connect(self.reset)
        
        self.ui.inspectResult_confirm_tableWidget.itemSelectionChanged.connect(self.selectInspectRow)
        
        self.ui.back_confirm_pushButton.clicked.connect(self.backShowROI)
        self.ui.next_confirm_pushButton.clicked.connect(self.nextShowROI)
        
        self.ui.fail_confirm_pushButton.clicked.connect(self.confirmFALI)
        self.ui.repass_confirm_pushButton.clicked.connect(self.confirmPASS)
        
        self.ui.submit_confirm_pushButton.clicked.connect(self.submitConfirmResult)
        
######################### Tab 4 #########################
################ Advanced Operation Mode ################
        # opertation mode    
        self.ui.PASS_label.setVisible(False) 
        self.ui.FAIL_label.setVisible(False) 
        
        self.ui.inspectResult_tableWidget.horizontalHeader().setStretchLastSection(False)
        header = self.ui.inspectResult_tableWidget.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeToContents)        
        header.setSectionResizeMode(1, QHeaderView.Stretch) 
        header.setSectionResizeMode(2, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(3, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(4, QHeaderView.ResizeToContents)
        
        self.ui.inspectResult_tableWidget.cellDoubleClicked.connect(self.showAll)
        
        self.ui.on_off_checkBox.clicked.connect(self.onoff)                    
        self.ui.sn_online_lineEdit.textChanged.connect(self.findModel)                                
        self.ui.goverify_pushButton.clicked.connect(self.goverify)
        self.ui.reset_pushButton.clicked.connect(self.reset)
        font = QFont()
        font.setPointSize(8)
        self.ui.inspectResult_tableWidget.setFont(font) 
        self.ui.inspectResult_tableWidget.itemSelectionChanged.connect(self.selectInspectRow)        
                        
        self.addOneInsepctRowTriggered.connect(self.addOneRowtoInspectTable)                                                         
        self.temp_combo = None                
        
        self.ui.submit_pushButton.clicked.connect(self.submitInspectResult)
        
        
######################### Tab 5 #########################
################ SOP Mode ################
        # SOP mode        
        self.ui.note_SOP_textBrowser.setFontPointSize(18)
        
        if self.userType == userType.Admin:
            self.ui.play_SOP_pushButton.setVisible(True)
            self.ui.pause_SOP_pushButton.setVisible(True) 
            self.ui.stop_SOP_pushButton.setVisible(True)
            self.ui.start_SOP_pushButton.setVisible(True)            
        else:
            self.ui.play_SOP_pushButton.setVisible(False)            
            self.ui.pause_SOP_pushButton.setVisible(False)
            self.ui.stop_SOP_pushButton.setVisible(False)
            self.ui.start_SOP_pushButton.setVisible(False)            
                                    
        
        self.ui.sn_SOP_lineEdit.textChanged.connect(self.findModel)
        
        self.ui.start_SOP_pushButton.clicked.connect(self.startSOP)
        self.ui.play_SOP_pushButton.clicked.connect(self.playSOP)
        self.ui.pause_SOP_pushButton.clicked.connect(self.pauseSOP)
        self.ui.stop_SOP_pushButton.clicked.connect(self.stopSOP)                
        
        
        self.duration_timer = QtCore.QTimer()
        self.duration_timer.timeout.connect(self.update_countdown)
                
        self.duration_time = -1 # Ignore
        self.seconds_left = 0  # 倒數剩餘秒數
        self.seconds_time_out = 0 # 超時秒數
        
        self.current_state = 'PASS'
        
        self.timer = QtCore.QTimer()
        self.timer.setSingleShot(True)
        self.timer.timeout.connect(self.showMessageAfterTimeout)
        
        self.ui.terminate_pushButton.clicked.connect(lambda: self.TerminateSOPInspection('Terminate'))                        
        self.SOPInsepctionOvertimeData = []                        
        
        self.ui.sn_setting_lineEdit.setAttribute(Qt.WA_InputMethodEnabled, False)
        self.ui.sn_easy_lineEdit.setAttribute(Qt.WA_InputMethodEnabled, False)
        self.ui.sn_confirm_lineEdit.setAttribute(Qt.WA_InputMethodEnabled, False)
        self.ui.sn_online_lineEdit.setAttribute(Qt.WA_InputMethodEnabled, False)
        self.ui.sn_SOP_lineEdit.setAttribute(Qt.WA_InputMethodEnabled, False)
    
    def keyPressEvent(self, event):        
        if event.key() == Qt.Key_Escape:
            if self.is_fullscreen:
                self.showNormal()
                self.is_fullscreen = False
        if event.key() == Qt.Key_F11:
            if self.is_fullscreen:
                self.showNormal()
                self.is_fullscreen = False
            else:                
                self.showFullScreen()
                self.is_fullscreen = True
    
    def on_language_changed(self,action):
        result=False
        if action == self.ui.actionChinese:
            result= TRANSLATOR.load('translation_zh_TW')
        else:
            TRANSLATOR.load('')
                    
        self.ui.retranslateUi(self)
        

    def findmodelandLableList(self,copy=True):            
        rootPath = os.path.join(projectRoot, self.productNumber, self.projectName)
        target = os.path.join(rootPath,'models')
        target_path = pathlib.Path(target)
                
        if copy:            
            self.ui.statusbar.showMessage('Copying model files....')
            source = os.path.join(self.settings['training']['type'][self.settings['type']]['parm'][0]['trainingDataPath'],'latest')                
            source_path = pathlib.Path(source)
            if os.path.exists(source):
                if os.path.exists(target):
                    if not any(target_path.iterdir()):                                        
                            shutil.copytree(source,target,dirs_exist_ok=True)        
                            print('Downloaded the latest model files.')
                            self.ui.statusbar.showMessage(f'Downloaded the latest model files from {source}.')                
                    else:
                        # target path is not empty. 
                        # compare all files time
                        for source_file in source_path.iterdir():
                            #file_path = os.path.join(target,source_file.name)            
                            target_file = target_path / source_file.name            
                            
                            # Should remove ex... engine file.                            
                            if target_file.exists():
                                if source_file.stat().st_mtime > target_file.stat().st_mtime:                        
                                    shutil.copy2(source_file, target_file)
                                    print(f'Updated {target_file.name}')
                                    self.ui.statusbar.showMessage(f'Updated {target_file.name}')
                                else:
                                    print(f'No Updtaed. {target_file.name}')
                            else:                        
                                shutil.copy2(source_file, target_file)
                                print(f'Updated {target_file.name}')
                                self.ui.statusbar.showMessage(f'Updated {target_file.name}')
                    self.ui.statusbar.showMessage('Copied model files.')    
                                                                                                        
            else:
                print(f'The model path is incorrect.\nPath:{source}')
                return None

                                                                          
        self.inspect_modelfile = ''
        for file in target_path.rglob('*.engine'):
            # #~/AAI/pn/projectName/models/*.engine
            self.inspect_modelfile = file.resolve()     
            break
        
        # #~/AAI/pn/projectName/models/labellist.txt
        self.inspect_labelfile = os.path.join(rootPath, "models", "labellist.txt")        
        
        if self.inspect_modelfile:            
            timestamp_path = os.path.join(target,'timestamp')
            if os.path.exists(timestamp_path):
                with open(timestamp_path,'r') as file:
                    timestamp = file.read().splitlines()                
                return f'[{timestamp[0]}]{self.inspect_modelfile.name}'            
            else:
                return f'{self.inspect_modelfile.name}'                    
        
        
    
    def findProductNumberForSystemSetting(self,text):
        widget = QApplication.focusWidget()  # 取得目前擁有焦點的 widget
        if isinstance(widget, QLineEdit):  # 確保它是 QLineEdit                          
            text = self.switchSHIFTtoSN(text,widget)
            
        self.productNumber = findProductNum(text)
        
        # for demo                    
        if 'DIP' in self.projectName:
            self.productNumber = 'PN-demo'
            
        if self.productNumber:   
            self.ui.productNum_setting_lineEdit.setText(self.productNumber)  
            self.ui.loadSettings_pushButton.setFocus()  
        else:            
            self.ui.productNum_setting_lineEdit.clear()            
            self.ui.newProjectName_lineEdit.clear()  

    def generateGoldenParameter(self,rootPath):
        #~/AAI/pn/projectName/golden/golden.png
        self.image_golden = os.path.join(rootPath, "golden", golden_filename)  
        #~/AAI/pn/projectName/golden/golden.txt          
        self.label_golden = os.path.join(rootPath, "golden", golden_labelinfo)
        #~/AAI/pn/projectName/position/anchors.tx
        self.anchors_golden = os.path.join(rootPath, "position", "anchors.txt")
        
    def generateInspectAndConfirmedParameter(self,rootPath,serialnumber):
        self.inspect_filename = serialnumber # use serial number. it should be a uniqu id
        
        #~/AAI/pn/projectName/inspection/images/<sn>.png
        self.inspect_images_dir = os.path.join(rootPath, "inspection", "images")  
        #~/AAI/pn/projectName/inspection/labels/inferenceResult/<sn>.txt
        self.inspect_inferenctResult_dir = os.path.join(rootPath, "inspection","labels","inferenceResult")
        #~/AAI/pn/projectName/inspection/labels/confirmedResult/<sn>.txt
        self.inspect_confirmedResult_dir = os.path.join(rootPath, "inspection",'labels',"confirmedResult")
        
        self.make_dir(self.inspect_images_dir)
        self.make_dir(self.inspect_inferenctResult_dir)
        self.make_dir(self.inspect_confirmedResult_dir) 
                
        
        
    def generateThresholdParameter(self,rootPath):
        #~/AAI/pn/projectName/models/golden-roi-threshold.txt
        self.golden_roi_threshold = os.path.join(rootPath, "pattern_match", "golden-roi-threshold.txt")
        self.make_dir(os.path.join(rootPath, "pattern_match"))        
            
    def switchSHIFTtoSN(self,serialString,lineEdit):
        fixed_text = ''.join(g_SHIFT_MAP.get(c, c) for c in serialString)
        
        if fixed_text != serialString:  # avoid loop
            lineEdit.blockSignals(True)
            lineEdit.setText(fixed_text)
            serialString = fixed_text
            lineEdit.blockSignals(False)
            
        return serialString
        

    def findModel(self,serialnumber):                        
        widget = QApplication.focusWidget()  # 取得目前擁有焦點的 widget
        if isinstance(widget, QLineEdit):  # 確保它是 QLineEdit                          
            serialnumber = self.switchSHIFTtoSN(serialnumber,widget)
            
        self.productNumber = findProductNum(serialnumber)
                
            
        # for demo                    
        if 'DIP' in self.projectName:
            self.productNumber = 'PN-demo'
            
        if self.productNumber:                                               
            self.settings = self.getCurrentProjectJson()              
                
            if not self.settings:
                QMessageBox.critical(self,"Error","This project does not exist!\n\n 1.Please confirm that the project name is entered correctly.\n 2.If the project name is correct, please contact the administrator to generate the project settings file.")     
                return False
                        
            text = self.settings['training']['type'][self.settings['type']]['description']
            self.getInferenceType(text)
            isChangeTab = self.checkCurrentInferenceTypeUsingTab(text)                        
            
            self.updateUIbyInference()                        
            
            if self.tabName == tabNameList.training and isChangeTab:                
                return False
                
            
            #~/AAI/pn/projectName
            rootPath = os.path.join(projectRoot, self.productNumber, self.projectName)
            
            if self.tabName == tabNameList.inspection:
                if isChangeTab:
                    self.ui.sn_easy_lineEdit.setText(serialnumber)
                    return False
                                
                self.ui.on_off_easy_checkBox.setEnabled(True)
                self.ui.on_off_easy_label.setEnabled(True)
                self.ui.on_off_easy_checkBox.setFocus()
                
                self.make_dir(os.path.join(rootPath, "models"))                
                modelname = self.findmodelandLableList(copy=True)    
                if modelname:
                    self.ui.model_easy_lineEdit.setText(modelname)   
                    self.ui.model_easy_lineEdit.setCursorPosition(0)  
                
                if self.ui.on_off_easy_checkBox.isChecked():
                    self.ui.goverify_easy_pushButton.setEnabled(True) 
                                
            elif self.tabName == tabNameList.advancedOperation:   
                if isChangeTab:     
                    self.ui.sn_online_lineEdit.setText(serialnumber)
                    return False
                
                self.ui.on_off_checkBox.setEnabled(True)
                self.ui.on_off_label.setEnabled(True)
                self.ui.on_off_checkBox.setFocus()     
                self.make_dir(os.path.join(rootPath, "models"))                
                modelname = self.findmodelandLableList(copy=True)                 
                if modelname:
                    self.ui.model_lineEdit.setText(modelname)
                    self.ui.model_lineEdit.setCursorPosition(0) 
                    
                if self.ui.on_off_checkBox.isChecked():
                    self.ui.goverify_pushButton.setEnabled(True) 
                
            elif self.tabName == tabNameList.reconfirm:                           
                if isChangeTab:
                    self.ui.sn_confirm_lineEdit.setText(serialnumber)                    
                    return False
                
                self.ui.inspectResult_confirm_tableWidget.setFocus()
                modelname =self.findmodelandLableList(copy=False)  
                if modelname:
                    self.ui.model_confirm_lineEdit.setText(modelname)     
                    self.ui.model_confirm_lineEdit.setCursorPosition(0)
            
            elif self.tabName == tabNameList.sop:
                self.sw_sop_log =os.path.join(rootPath, "sop_log")
                self.make_dir(self.sw_sop_log)  # SW log
                
                ret, level, productCode, version = parsePN(self.productNumber)
                if ret: # for ADLINK format          
                    self.PN_sop_log = os.path.join(logRoot,level,productCode,version)                    
                else: # for other format
                    self.PN_sop_log = os.path.join(logRoot,self.productNumber)
                self.make_dir(os.path.join(self.PN_sop_log,'PASS'))
                self.make_dir(os.path.join(self.PN_sop_log,'FAIL'))                
                    
                if isChangeTab:
                    self.ui.sn_SOP_lineEdit.setText(serialnumber)
                    return False
                                
                #modelname = self.findmodelandLableList(copy=True)
                #if modelname:
                    #self.ui.model_SOP_lineEdit.setText(modelname)
                    #self.ui.model_SOP_lineEdit.setCursorPosition(0)
                if self.userType == userType.Admin:                                        
                    self.ui.start_SOP_pushButton.setEnabled(True)
                    self.ui.start_SOP_pushButton.setFocus()
                else:
                    self.generateGoldenParameter(rootPath)             
                    self.generateInspectAndConfirmedParameter(rootPath,serialnumber)
                    self.generateThresholdParameter(rootPath)
                    self.startSOP()
                    return True
                    
            
            self.generateGoldenParameter(rootPath)             
            self.generateInspectAndConfirmedParameter(rootPath,serialnumber)
            self.generateThresholdParameter(rootPath)
                
                
            return True        
        else:                       
            if not self.liveSrc:
                if self.tabName == tabNameList.inspection:                
                    self.ui.model_easy_lineEdit.setText('')
                    self.ui.on_off_easy_checkBox.setEnabled(False)
                    self.ui.on_off_easy_label.setEnabled(False)
                elif self.tabName == tabNameList.advancedOperation:                
                    self.ui.model_lineEdit.setText('')
                    self.ui.on_off_checkBox.setEnabled(False)
                    self.ui.on_off_label.setEnabled(False)                
                    
                self.image_golden = None
                self.label_golden = None
                self.anchors_golden = None
                self.inspect_modelfile = None             
                
            if self.tabName == tabNameList.reconfirm:
                self.ui.model_confirm_lineEdit.setText('')
                    
        return False  
    
    def make_dir(self,path):
        if not os.path.exists(path):
            os.makedirs(path,exist_ok=True)
        
    def exit(self):             # click Exit button to close
        if self.liveSrc:
            if self.liveSrc.pipeline:
                self.liveSrc.stop()
                        
            
        QApplication.instance().quit()    
    
    def closeEvent(self, event):  # click x to close        
        self.exit()        
        event.accept()
        return super().closeEvent(event)  
            
            
    def currentTab(self):        
        self.tabName = self.ui.tabWidget.currentWidget().objectName() 
        
        if self.tabName == tabNameList.systemSetting:
            self.ui.sn_setting_lineEdit.setFocus()
        elif self.tabName == tabNameList.training:
            self.ui.start_pushButton.setFocus()
        elif self.tabName == tabNameList.inspection:
            self.ui.sn_easy_lineEdit.setFocus()
        elif self.tabName == tabNameList.reconfirm:
            self.ui.sn_confirm_lineEdit.setFocus()
        elif self.tabName == tabNameList.advancedOperation:
            self.ui.sn_online_lineEdit.setFocus()
        elif self.tabName == tabNameList.sop:
            self.ui.sn_SOP_lineEdit.setFocus()
    
    def getInferenceType(self,text):
        if text=='Dual In Line Package Inspection':
            self.inferenceType = 'DIP'            
        elif text == 'Standard Operating Procedures Inspection':
            self.inferenceType = 'SOP'
            
    def checkCurrentInferenceTypeUsingTab(self,text):        
        if self.userType == userType.Trainer:
            tablist = trainingModeTab[self.inferenceType]['hide']
            
        elif self.userType == userType.Operator:
            tablist = inferenceModeTab[self.inferenceType]['hide']
            
        elif self.userType == userType.Admin:
            tablist = inferenceModeTab[self.inferenceType]['hide'] + trainingModeTab[self.inferenceType]['hide']
            
        if tablist:
            if self.tabName in tablist:            
                msg_box = QMessageBox()
                msg_box.setWindowTitle('Notification')
                msg_box.setText(f'Curret project use "{text}".\n\nThe software will automatically switch the tab pages.')
                                
                QtCore.QTimer.singleShot(3000,msg_box.accept)
                msg_box.exec_()
                               
                return True
        return False
        
    def setTabEnabled(self,hideList,showList):            
        if hideList:
            for tab in hideList:                    
                self.ui.tabWidget.setTabEnabled(self.tabdict[tab],False)                    
        if showList:
            for tab in showList:
                self.ui.tabWidget.setTabEnabled(self.tabdict[tab],True) 
            
                  
    def updateUIbyInference(self):
                
        self.setTrainingModeUIwithInference(self.isGolden)                      
        if self.userType == userType.Trainer:
            hideList = trainingModeTab[self.inferenceType]['hide']
            showList = trainingModeTab[self.inferenceType]['show']
            self.setTabEnabled(hideList,showList)            

        elif self.userType == userType.Operator:                        
            hideList = inferenceModeTab[self.inferenceType]['hide']            
            showList = inferenceModeTab[self.inferenceType]['show']
            self.setTabEnabled(hideList,showList)
                    
        elif self.userType == userType.Admin:
            hideList = trainingModeTab[self.inferenceType]['hide'] + inferenceModeTab[self.inferenceType]['hide']            
            if hideList:
                for tab in hideList:
                    self.ui.tabWidget.setTabEnabled(self.tabdict[tab],False)
                                
            showList = trainingModeTab[self.inferenceType]['show'] + inferenceModeTab[self.inferenceType]['show']            
            if showList:
                for tab in showList:
                    self.ui.tabWidget.setTabEnabled(self.tabdict[tab],True)               
                    
    def getCurrentProjectJson(self):
        settings = None
        settingsPath =  os.path.join(projectRoot,self.productNumber,self.projectName,'setting.json')
        if os.path.exists(settingsPath):                    
            with open(settingsPath,'r') as json_file:
                settings = json.load(json_file)  
        if settings:                                        
            if 'useOffsetTheshold' in settings.keys():
                self.useOffset = settings['useOffsetTheshold']
            else:
                self.useOffset = False
            
        return settings
    
    def setLayerComboItem(self,comboBox:QComboBox):
        if self.settings:
            if self.inferenceType == 'SOP':
                layers = self.settings['layers']
                comboBox.clear()
                                
                for i in range(1,layers+1):
                    comboBox.addItem(f'Layer {i}')
                comboBox.setCurrentIndex(0)
        else:
            print('[Error]Need to get setting.json.')
            
    def setCurrentLayer(self,index):        
        self.current_layers = index+1        
        
                            
####### tab 0 , setting #######    

    def enableLoadSettings(self):
        if self.ui.productNum_setting_lineEdit.text():
            self.ui.loadSettings_pushButton.setEnabled(True)            
        else:
            self.ui.loadSettings_pushButton.setEnabled(False)
            self.ui.SaveSetting_pushButton.setEnabled(False)
            self.ui.training_groupBox.setEnabled(False)
            self.ui.inspection_groupBox.setEnabled(False)
            self.ui.manage_groupBox.setEnabled(False)
            
    
    def getTemptateJson(self):
        settings = None
        template_jsonPath = os.path.join('config','template_system_setting.json')        
        if os.path.exists(template_jsonPath):
            with open(template_jsonPath,'r') as json_file:
                settings = json.load(json_file)
        return settings                
        
            
    def loadSetting(self):
        self.ui.training_groupBox.setEnabled(True)
        self.ui.inspection_groupBox.setEnabled(True)      
        self.ui.useTestVideo_groupBox.setEnabled(True)  
        self.ui.manage_groupBox.setEnabled(True)
        self.productNumber = self.ui.productNum_setting_lineEdit.text()                    
        if self.isNewProject:
            self.settings = self.getTemptateJson()     
            self.settings['projectName'] = self.projectName
            self.settings['productNumber'] = self.productNumber
            self.ui.statusbar.showMessage('Creating a new project....')
        else:
            if os.path.exists(os.path.join(projectRoot,self.productNumber,self.projectName)):
                self.settings = self.getCurrentProjectJson()  
                                                
                # check project_name and product number, need or not?             
                if self.settings['projectName']  != self.projectName or self.settings['productNumber'] != self.productNumber:
                    QMessageBox.critical(self,"Critical Issue", "The setting doesn't match the product and project, please contact the tachnical staff.")
                    self.exit()   
                self.ui.statusbar.showMessage('Loaded the project settings.')                                                     
            else:
                QMessageBox.critical(self,"Warning", "This project doesn't exist!\nThe application will create a new project!")
                self.settings = self.getTemptateJson()
                self.settings['projectName'] = self.projectName
                self.settings['productNumber'] = self.productNumber
                self.ui.statusbar.showMessage('Creating a new project....')
       
        if self.settings:
            self.setSystemSettingFields()
            text = self.settings['training']['type'][self.settings['type']]['description']
            self.getInferenceType(text)
            self.updateUIbyInference()            
            self.setLayerComboItem(self.ui.layerNo_comboBox)
            
        self.ui.SaveSetting_pushButton.setEnabled(True)
    
    def enableManageSubmtButton(self):
        self.ui.submit_manage_project_pushButton.setEnabled(False)
        if self.ui.newProjectName_lineEdit.text() or self.ui.newPN_lineEdit.text():            
            if self.ui.rename_radioButton.isChecked() or self.ui.copy_radioButton.isChecked() or self.ui.duplicate_radioButton.isChecked():
                self.ui.submit_manage_project_pushButton.setEnabled(True)          
                
    def enableManageLineEdit(self):  
        self.ui.newProjectName_lineEdit.clear()
        self.ui.newPN_lineEdit.clear()
        self.ui.newPN_lineEdit.setPlaceholderText('')
        self.ui.newProjectName_lineEdit.setPlaceholderText('')                      
        self.ui.newProjectName_lineEdit.setEnabled(True)
        if self.ui.rename_radioButton.isChecked() or self.ui.copy_radioButton.isChecked():                        
            self.ui.newPN_lineEdit.setEnabled(False)            
        elif self.ui.duplicate_radioButton.isChecked():            
            self.ui.newPN_lineEdit.setEnabled(True)            
                
    def manageProject(self):
        new_projectname = self.ui.newProjectName_lineEdit.text()
        current_path = os.path.join(projectRoot, self.productNumber, self.projectName)
        new_path = os.path.join(projectRoot, self.productNumber, new_projectname)        
        if self.ui.rename_radioButton.isChecked():
            if new_projectname == self.projectName:
                QMessageBox.warning(self,"Warning","Please rename a new project name!")
                self.ui.newProjectName_lineEdit.clear()
                return 
            
            if os.path.exists(new_path):
                QMessageBox.critical(self,"Error",f"{new_projectname} already exists!")
                self.ui.newProjectName_lineEdit.clear()
                return 
            self.ui.projectName_setting_lineEdit.setText(new_projectname)
            self.projectName = new_projectname
            self.settings['projectName'] = self.projectName
            
            settingsPath =  os.path.join(current_path,'setting.json')
            if os.path.exists(settingsPath):
                with open(settingsPath, 'w', encoding='utf-8') as file:
                    json.dump(self.settings, file, ensure_ascii=False,indent=4)
                                
            if os.path.exists(current_path):
                os.rename(current_path,new_path)
                    
            self.ui.statusbar.showMessage(f'Renamed the project name to {new_projectname}.')
        elif self.ui.copy_radioButton.isChecked():
            if os.path.exists(new_path):
                QMessageBox.critical(self,"Error",f"{new_projectname} already exists!")
                self.ui.newProjectName_lineEdit.clear()                               
                return
            if os.path.exists(current_path):
                self.make_dir(new_path)
                self.copyGoldenFolden(current_path,new_path,new_projectname)
            self.ui.statusbar.showMessage(f'Copied the settings from {self.projectName} to {new_projectname}.')    
        elif self.ui.duplicate_radioButton.isChecked():
            self.ui.newProjectName_lineEdit.setPlaceholderText('')
            if new_projectname == '':
                new_projectname = self.ui.projectName_setting_lineEdit.text()
                self.ui.newProjectName_lineEdit.setPlaceholderText(f'{new_projectname}')                            
            new_productnumber = self.ui.newPN_lineEdit.text()
            if new_productnumber:
                self.ui.newPN_lineEdit.setPlaceholderText('')
                new_path = os.path.join(projectRoot, new_productnumber, new_projectname)            
                if os.path.exists(new_path):
                    QMessageBox.critical(self,"Error",f"{new_productnumber}/{new_projectname} already exists!")
                    self.ui.newProjectName_lineEdit.clear()
                    self.ui.newPN_lineEdit.clear()
                    self.ui.newProjectName_lineEdit.setPlaceholderText('')
                    return 
                self.make_dir(new_path)
                self.copyGoldenFolden(current_path,new_path,new_projectname,new_productnumber)
                
                self.ui.statusbar.showMessage(f'Duplicated the settings from {self.productNumber}/{self.projectName} to {new_productnumber}/{new_projectname}.')    
            else:
                QMessageBox.critical(self,"Error", "New product number cannot be empty.")
                self.ui.newPN_lineEdit.setPlaceholderText('Required. Cannot be empty!')

    def copyGoldenFolden(self,current_path, new_path, new_projectname, new_productnumber=''):
        # Golden
        shutil.copytree(os.path.join(current_path,'golden'),os.path.join(new_path,'golden'),dirs_exist_ok=True)
        
        # registration
        shutil.copytree(os.path.join(current_path,'position'),os.path.join(new_path,'position'),dirs_exist_ok=True)
        
        # settings
        settingsPath =  os.path.join(current_path,'setting.json')                   
        settings = []
        if os.path.exists(settingsPath):
            with open(settingsPath,'r') as json_file:
                settings = json.load(json_file)
        if settings:
            if new_productnumber:            
                settings['productNumber'] = new_productnumber
            settings['projectName'] = new_projectname
            settings['serialNumber'] = ''
            
            settingsPath =  os.path.join(new_path,'setting.json')        
            with open(settingsPath, 'w', encoding='utf-8') as file:
                json.dump(settings, file, ensure_ascii=False,indent=4)
                
    
    def setSystemSettingFields(self):   
        self.ui.training_ip_lineEdit.setText(self.settings['training']['server']['ip'])
        self.ui.training_port_lineEdit.setText(str(self.settings['training']['server']['port']))
        self.ui.training_account_lineEdit.setText(self.settings['training']['server']['account'])
        self.ui.training_pw_lineEdit.setText(self.settings['training']['server']['password'])
        
        self.ui.showlist_spinBox.setValue(self.settings['training']['imagetable_column_count'])
        
        self.ui.inference_comboBox.setCurrentIndex(self.settings['type'])
        # confirm, need or not?
        if self.settings['training']['type'][self.settings['type']]['description'] != self.ui.inference_comboBox.currentText():
            print('Confirm the inference type!')
            
        if self.settings['type'] == 0: 
            # DIP      
            parm = self.settings['training']['type'][self.settings['type']]['parm']
            if parm:
                self.ui.exortNVEngine_checkBox.setChecked(parm[0]['exportNVEngine'])
                self.ui.epoch_spinBox.setValue(parm[0]['epoch'])
                self.ui.traingPath_lineEdit.setText(parm[0]['trainingDataRootPath'])
        elif self.settings['type'] == 1:
            self.ui.boradno_spinBox.setValue(self.settings['layers'])
            parm = self.settings['training']['type'][self.settings['type']]['parm']
            if parm:                                
                self.ui.traingPath_lineEdit.setText(parm[0]['trainingDataRootPath'])
                    
                
        # Storage setting
        self.ui.storage_ip_lineEdit.setText(self.settings['storage']['server']['ip'])
        self.ui.storage_account_lineEdit.setText(self.settings['storage']['server']['account'])
        self.ui.storage_pw_lineEdit.setText(self.settings['storage']['server']['password'])
        self.ui.storage_path_lineEdit.setText(self.settings['storage']['server']['path'])        
        
        # Inspection setting
        if 'inspection' in self.settings.keys():
            self.ui.useTestVideo_groupBox.setChecked(self.settings['inspection']['useTestVideo'])
            self.ui.testVideo_filePath_lineEdit.setText(self.settings['inspection']['filePath'])
        else:
           self.settings['inspection'] = {"useTestVideo":False,"filePath":""}

    def searchRetrainData(self):
        
        if self.ui.retrain_groupBox.isChecked():
            # scan inspection folder
            # create retrain_treeWidget
            #  All data
            #   - Date
            #      - sn
            print('[TBD] Enable retrain')
        else:
            # reset selected treewidget item
            print('[TBD] Disable retrain')
        
    def retrain(self):
        # copy selected item from retrain_treeWidget to training server
        # retrain model
        print('[TBD] click retrain')
    
    def saveProjectSetting(self):
        self.settings['serialNumber'] = self.ui.sn_setting_lineEdit.text()
        
        if self.ui.training_ip_lineEdit.text():
            self.settings['training']['server']['ip'] = self.ui.training_ip_lineEdit.text()
        else:
            QMessageBox.warning(self,'Warning','Please enter the training server IP address.')
            self.ui.training_ip_lineEdit.setFocus()
            return
        self.settings['training']['server']['port'] = int(self.ui.training_port_lineEdit.text())
        self.settings['training']['server']['account'] = self.ui.training_account_lineEdit.text()
        self.settings['training']['server']['password'] = self.ui.training_pw_lineEdit.text()
        
        self.settings['training']['imagetable_column_count'] = self.ui.showlist_spinBox.value()
        
        self.settings['type'] = self.ui.inference_comboBox.currentIndex()                
            
        if self.settings['type'] == 0:          
            # DIP
            parm = self.settings['training']['type'][self.settings['type']]['parm']
            if parm:
                parm[0]['exportNVEngine'] = self.ui.exortNVEngine_checkBox.isChecked()
                parm[0]['epoch'] = self.ui.epoch_spinBox.value()
                if self.ui.traingPath_lineEdit.text():
                    parm[0]['trainingDataRootPath'] = self.ui.traingPath_lineEdit.text()
                    parm[0]['trainingDataPath'] = os.path.join(self.ui.traingPath_lineEdit.text(),self.productNumber,self.projectName)
                else:
                    QMessageBox.warning(self,'Warning','Please enter the training data path.')
                    self.ui.traingPath_lineEdit.setFocus()
                    return
        elif self.settings['type'] == 1: 
            # SOP
            parm = self.settings['training']['type'][self.settings['type']]['parm']
            if parm:
                if self.ui.traingPath_lineEdit.text():
                    parm[0]['trainingDataRootPath'] = self.ui.traingPath_lineEdit.text()
                    parm[0]['trainingDataPath'] = os.path.join(self.ui.traingPath_lineEdit.text(),self.productNumber,self.projectName)
                else:
                    QMessageBox.warning(self,'Warning','Please enter the training data path.')
                    self.ui.traingPath_lineEdit.setFocus()
                    return
                self.settings['layers'] = self.ui.boradno_spinBox.value()

                                            
                
        # Storage setting
        self.settings['storage']['server']['ip'] = self.ui.storage_ip_lineEdit.text()
        self.settings['storage']['server']['account'] = self.ui.storage_account_lineEdit.text()
        self.settings['storage']['server']['password'] = self.ui.storage_pw_lineEdit.text()
        self.settings['storage']['server']['path'] = self.ui.storage_path_lineEdit.text()
        
        # Inspection setting
        if self.ui.useTestVideo_groupBox.isChecked():
            if mimetypes.guess_type(self.ui.testVideo_filePath_lineEdit.text())[0] != 'video/mp4':                                        
                QMessageBox.warning(self,'Warning','Please select a mp4 video file.')
                self.ui.testVideo_filePath_lineEdit.setFocus()
                return        
        self.settings['inspection']['useTestVideo']=self.ui.useTestVideo_groupBox.isChecked()
        self.settings['inspection']['filePath']=self.ui.testVideo_filePath_lineEdit.text()
        
        settingsPath =  os.path.join(projectRoot,self.productNumber,self.projectName,'setting.json')
        self.make_dir(os.path.join(projectRoot,self.productNumber,self.projectName))        
        
        with open(settingsPath, 'w', encoding='utf-8') as file:
            json.dump(self.settings, file, ensure_ascii=False,indent=4)
                    
        self.ui.statusbar.showMessage('Saved this project.')   
    
    def selectInferenceType(self,index):        
        
        text = self.ui.inference_comboBox.itemText(index)        
        self.getInferenceType(text)        
        self.updateUIbyInference()
        
        if self.inferenceType == 'DIP':
            self.ui.boradno_label.setVisible(False)
            self.ui.boradno_spinBox.setVisible(False)
            self.ui.dip_groupBox.setVisible(True)
        elif self.inferenceType == 'SOP':
            self.ui.boradno_label.setVisible(True)
            self.ui.boradno_spinBox.setVisible(True)
            self.ui.dip_groupBox.setVisible(False)  
            self.ui.training_ip_lineEdit.setText("0.0.0.0")          
    
    def selectTestmp4Video(self):
        video,_ = QFileDialog.getOpenFileName(self,filter="Video Files (*.mp4 )",options=QFileDialog.DontUseNativeDialog)
        if video:
            self.ui.testVideo_filePath_lineEdit.setText(video)
        else:
            print('please select a mp4 format video')
        
#######  tab 2,4 online (operation mode/Insepction mode) #######
    def onoff(self):
        
        self.scaleOnce = True
        if self.liveSrc:            
            self.liveSrc.stop()
            self.liveSrc = None          

        if self.settings:
            type_index = self.settings['type']                          
            nickname = self.settings['training']['type'][type_index]['nickname']
            global pipeline_command_operation
            pipeline_command_operation = self.settings['pipeline']['operation'][nickname]['source']
            
                    
        if self.tabName == tabNameList.inspection:
            if self.ui.on_off_easy_checkBox.isChecked():
                self.ui.goverify_easy_pushButton.setEnabled(True)    
                self.ui.skip_easy_pushButton.setEnabled(True)    
                #index = self.ui.device_easy_comboBox.currentIndex()
                text = self.ui.device_easy_comboBox.currentText()
                status = self.startInspectLiveSrc(text,self.ui.showFocus_easy_graphicsView)   
                self.ui.cameraStatus_easy_label.setText(status)
                if status.lower() == 'stop':
                    self.ui.on_off_easy_checkBox.setChecked(False)
                    #self.ui.device_easy_comboBox.setCurrentIndex(0)
                
            else:
                self.ui.goverify_easy_pushButton.setEnabled(False)  
                self.ui.skip_easy_pushButton.setEnabled(False)  
                self.ui.cameraStatus_easy_label.setText('Stop')                   
                self.reset()     
                            
        elif self.tabName == tabNameList.advancedOperation:        
            if self.ui.on_off_checkBox.isChecked():                          
                self.ui.goverify_pushButton.setEnabled(True)
                self.ui.reset_pushButton.setEnabled(True)                                            
                                 
                text = self.ui.device_easy_comboBox.currentText()
                status = self.startInspectLiveSrc(text,self.ui.showimage_online_graphicsView)   
                self.ui.currentstatus_label.setText(status)
                if status.lower() == 'stop':
                    self.ui.on_off_checkBox.setChecked(False)
                    self.ui.device_offline_comboBox.setCurrentIndex(0)                          
            else:
                self.ui.goverify_pushButton.setEnabled(False)
                self.ui.reset_pushButton.setEnabled(False)            
                self.ui.currentstatus_label.setText('Stop')                 
                self.reset()
                               
    def startInspectLiveSrc(self,currenttext:str,graphics):
        self.liveSrc = None
        status = 'Fail'
        cmd = ""
        
        if currenttext.lower() == cameraType.web.lower():        
            if cameraType.web in  pipeline_command_operation.keys():
                cmd = pipeline_command_operation[cameraType.web]
                self.liveSrc = LiveStream(gstcmd=cmd)            
                self.liveSrc.new_frame.connect(lambda image:self.update_view_operation(image,graphics))
        elif currenttext.lower() == cameraType.basler.lower():
            if cameraType.basler in pipeline_command_operation.keys():
                cmd = pipeline_command_operation[cameraType.basler]
                self.liveSrc = LiveStream(gstcmd=cmd)
                self.liveSrc.new_frame.connect(lambda image:self.update_view_operation(image,graphics))
        elif currenttext.lower() == cameraType.usb3.lower():
            if cameraType.usb3 in  pipeline_command_operation.keys():
                cmd = pipeline_command_operation[cameraType.usb3]
                self.liveSrc = LiveStream(gstcmd=cmd)            
                self.liveSrc.new_frame.connect(lambda image:self.update_view_operation(image,graphics))        
            
        if cmd:        
            print(f'source pipeline:\n{cmd}')
        else:
            self.ui.statusbar.showMessage('Failed to find the camera command, please confirm the setting.json!',timeout=5000)                   
            self.liveSrc = None
            return 'Stop'
        
        if self.liveSrc:                    
            self.liveSrc.graphics =  graphics 
            if self.liveSrc.parseLaunch():                
                if not self.liveSrc.play():                    
                    self.ui.statusbar.showMessage('Failed to start the camare, please confirm the envirionment!',timeout=5000)                    
                    self.liveSrc.stop()
                    self.liveSrc = None                   
                    status = 'Stop'
                    self.scaleOnce = True
                else:
                    self.ui.statusbar.showMessage('Current Status: Playing live stream.')                
                    status = 'Playing'

            else:
                print('parse failed')
                self.liveSrc = None             
                status = 'Fail'
                self.scaleOnce = True        
            
        return status
        
    def update_view_operation(self,image,graphics):         
        pixmap = QPixmap.fromImage(image)            
        if self.scaleOnce:            
            graphics.set_image(pixmap)
            self.scaleOnce = False            
        else:
            graphics.addImage(pixmap) 
    

    def generateThresholdFile(self,threshold_file:str,threshold_dict:dict):        
        with open(threshold_file,'w') as file:
            for key, value in threshold_dict.items():
                line = f'{key[0]};{key[1]};{value}\n'
                file.write(line)
    
    def createThresholdDict(self,threshold_file):        
        golden_roi_threshold_dict = {}        
        with open(threshold_file) as file:
            lines = file.read().splitlines()
                    
        for line in lines:
            item = line.split(';')
            golden_roi_threshold_dict[(item[0],item[1])]=item[2]
        return golden_roi_threshold_dict
    
    def initThresholdFile(self):
        self.golden_roi_threshold_dict = {}
        if not os.path.exists(self.golden_roi_threshold) and os.path.exists(self.label_golden) and self.golden_postion_dict:                       
            for pos in self.golden_postion_dict.keys():                
                p = pos.strip('()').split(',')
                # start = '(x1, y1)' 
                # end = '(x2, y2)'
                start = f'({p[0]}, {p[1]})'
                end = f'({p[2]}, {p[3]})'
                
                # dict format: (start, end) : score
                # for example, ()
                self.golden_roi_threshold_dict[(start,end)]=default_threshold
            self.generateThresholdFile(self.golden_roi_threshold,self.golden_roi_threshold_dict)
        elif os.path.exists(self.golden_roi_threshold) and os.path.exists(self.label_golden) and self.golden_postion_dict:
            self.golden_roi_threshold_dict = self.createThresholdDict(self.golden_roi_threshold)
    
    def inference(self, oriimg):    
        self.getOKfromGoldenLabel()   
        self.getGoldenLabelPosition(self.label_golden) 
        pipeline = None
        
        type_index = self.settings['type']                          
        nickname = self.settings['training']['type'][type_index]['nickname']
                        
        self.initThresholdFile()
                
        
        try:            
            if self.image_golden and self.anchors_golden and self.label_golden and self.inspect_modelfile and self.inspect_labelfile:                                            
                # if os.path.exists(self.golden_roi_threshold):
                #     cmd = str(self.settings['pipeline']['operation'][nickname]['inference']['insepctionWithThreshold'])                                        
                #     cmd = cmd.format(self.image_golden,self.anchors_golden,self.label_golden, self.inspect_modelfile,self.inspect_labelfile,self.golden_roi_threshold)                    
                #     # pipeline = Gst.parse_launch(f"appsrc name=src ! videoconvert ! \
                #     #     adalign gold-image-path={self.image_golden} anchor-pattern-file-path={self.anchors_golden} \
                #     #             golden-labeled-file-path={self.label_golden} save-result=True search-width=500 search-height=500 ! \
                #     #     convert_roi ! \
                #     #     adrt model={self.inspect_modelfile} rgbconv=True scale=0.0039 query=//alignment engine-id=//adrt ! \
                #     #     adtrans_classifier label={self.inspect_labelfile} ! \
                #     #     admetafilter identify-string=lower-than-roi-threshold roi-threshold-file-path={self.golden_roi_threshold} ! \
                #     #     videoconvert ! appsink name=sink")
                # else:
                #     cmd = str(self.settings['pipeline']['operation'][nickname]['inference']['inspection'])
                #     cmd = cmd.format(self.image_golden,self.anchors_golden,self.label_golden, self.inspect_modelfile,self.inspect_labelfile)                
                #     # pipeline = Gst.parse_launch(f'appsrc name=src ! videoconvert ! \
                #     #     adalign gold-image-path={self.image_golden} anchor-pattern-file-path={self.anchors_golden} \
                #     #     golden-labeled-file-path={self.label_golden} save-result=True search-width=500 search-height=500 ! \
                #     #     convert_roi ! \
                #     #     adrt model={self.inspect_modelfile} rgbconv=True scale=0.0039 query="//alignment" engine-id="//adrt" ! \
                #     #     adtrans_classifier label={self.inspect_labelfile} ! \
                #     #     videoconvert ! appsink name=sink')     
                cmd = str(self.settings['pipeline']['operation'][nickname]['inference']['inspection'])
                cmd = cmd.format(self.image_golden,self.anchors_golden,self.label_golden, self.inspect_modelfile,self.inspect_labelfile)           
                
                print(f'\npipeline:\n{cmd}\n')
                pipeline = Gst.parse_launch(cmd)  
                self.inference_pipeline = pipeline              
            else:
                print('[Error] No model for the inference')
            #for testing appsrc
            #pipeline = Gst.parse_launch('appsrc name=src emit-signals=True ! videoconvert ! jpegenc ! filesink location="789.jpg"')
        except:
            print('[Error] parse Failed')
            return False 
        
        if not pipeline:
            return False
        
        #get appsrc&appsink from gst pipe
        appsrc = pipeline.get_by_name('src')       
        appsink = pipeline.get_by_name('sink')

        if appsrc:            
            appsrc.set_property("format", Gst.Format.TIME)         
            appsrc.set_property("block", True)           
            appsrc.set_property("emit-signals", True)
        else:
            return False

        if appsink:            
            appsink.set_property("emit-signals", True)
            appsink.connect('new-sample', self.outputinferenceret, None)            

        pipeline.set_state(Gst.State.PLAYING)        

        #appsrc push buffer manually        
        #img = QImage('/tmp/adregister/test-images/TO-00001-0009_ori.jpg')
        img = oriimg.convertToFormat(QImage.Format_BGR888)        
        #configure cap
        caps_in=Gst.Caps.from_string(f'video/x-raw,format=BGR,width={img.width()},height={img.height()}')
        appsrc.set_property("caps", caps_in)

        #generate the gst buffer. no need to set the pts and duration
        array = np.frombuffer(img.bits(), dtype=np.uint8)   
        buffer = Gst.Buffer.new_wrapped(array.tobytes())
        appsrc.emit("push-buffer", buffer)  
        appsrc.emit("end-of-stream") 
        time.sleep(.1)     

        return True


    def outputinferenceret(self, sink, data) -> Gst.FlowReturn:        
        sample = sink.emit('pull-sample')
        
        image_data = sample_to_numpy(sample)
        fmt = get_sample_format(sample)
        self.liveSrc.setImage(image_data, fmt)
        # get detection inference result
        buffer_data = adroi.gst_buffer_adroi_query(hash(sample.get_buffer()), '//')
        if buffer_data is None or len(buffer_data) == 0:
            print("query is empty from frame meta in get classification.")
            return Gst.FlowReturn.OK        
        
        if self.tabName == tabNameList.advancedOperation:        
            pixmap = self.ui.showimage_online_graphicsView.pixmapItem.pixmap()            
        elif self.tabName == tabNameList.inspection:            
            pixmap = self.ui.showFocus_easy_graphicsView.pixmapItem.pixmap()
            
        width = pixmap.width()
        height = pixmap.height()
        
        self.inferenceInspectReuslt = []
        self.confirmedInspectResult = []
        
        theFirstShow = -1
        for roi in buffer_data[0].rois:
            if roi.category == 'box':
                for subroi in roi.sub_rois:
                    box = subroi.to_box()
                    x1, y1, x2, y2 = box.x1, box.y1, box.x2, box.y2
                    labelInfo = ''
                    if len(box.datas) > 0 and box.datas[0].category == 'classification':
                        labelInfo = box.datas[0].label                    
                    #labelposstr = f'{labelInfo};({round(x1*rect.width())},{round(y1*rect.height())});({round(x2*rect.width())},{round(y2*rect.height())});ignore;ignore'                    
                    correctLabel = ''
                    #score = '1'
                    if box.events:
                        if len(box.events) > 0 and 'golden position' in str(box.events[0]):
                            match = re.search(r'\(([^)]+)\)',box.events[0])                            
                            if match:
                                golden_pos = match.group(0)                    
                                correctLabel = self.parseGoldenROILabelName(golden_pos)
                        #if len(box.events) > 1 and 'score' in str(box.events[1]):
                        #    score = str(box.events[1]).split('=')[1]                                                  
                        
                    ng_ok_status = 'OK' if labelInfo == correctLabel else 'NG'
                    #ng_ok_status = 'OK' if labelInfo in self.ok_list else 'NG'                                                
                    labelposstr = f'{labelInfo};({round(x1*width)},{round(y1*height)});({round(x2*width)},{round(y2*height)});ignore;ignore;{ng_ok_status}'
                    
                    confidence = str(box.datas[0].confidence)     
                    
                    row_data = [ng_ok_status,labelInfo,                                        
                                f'{round(x1*width),round(y1*height)}',
                                f'{round(x2*width),round(y2*height)}',
                                confidence]   
                    
                    self.addOneInsepctRowTriggered.emit(row_data)                                                           
                    #self.ui.showimage_online_label.labelsInfo.append(labelposstr)
                    if self.tabName == tabNameList.advancedOperation:
                        self.ui.showimage_online_graphicsView.labelsInfo.append(labelposstr)
                    elif self.tabName == tabNameList.inspection:
                        self.ui.showFocus_easy_graphicsView.labelsInfo.append(labelposstr)
                    #print('Detection result: prob={:.3f}, coordinate=({:.2f},{:.2f}) to ({:.2f},{:.2f})), Index = {}, Label = {}'.format(labelInfo.confidence, x1, y1, x2, y2, labelInfo.label_id, labelInfo.label))
                                                                                                    
                    
                    
                                        
                    self.inferenceInspectReuslt.append([labelInfo,                                        
                                f'{round(x1*width),round(y1*height)}',
                                f'{round(x2*width),round(y2*height)}',
                                'ignore','ignore',ng_ok_status,golden_pos,
                                f'{confidence}'])
                                #confidence])
                    
                    
                    self.confirmedInspectResult.append([labelInfo,                                        
                                f'{round(x1*width),round(y1*height)}',
                                f'{round(x2*width),round(y2*height)}',
                                'ignore','ignore',ng_ok_status,golden_pos])
                    
                    if theFirstShow == -1:
                        if self.ui.onlyNG_easy_checkBox.isChecked():                            
                            if ng_ok_status == 'NG':                                
                                theFirstShow = len(self.inferenceInspectReuslt) -1
                        else:
                            theFirstShow = 0                    
                        overall_x1 = round(x1*width)
                        overall_y1 = round(y1*height)
                        overall_x2 = round(x2*width)
                        overall_y2 = round(y2*height)
                            
                            
                        
             
                #here is the only one roi currently
                break
        #self.ui.showimage_online_label.update()
        if self.tabName == tabNameList.advancedOperation:
            self.ui.showimage_online_graphicsView.drawTriggered.emit()                        
        elif self.tabName == tabNameList.inspection:      
            self.ui.next_easy_pushButton.setEnabled(True)
            self.ui.back_easy_pushButton.setEnabled(True)
                        
            self.ui.showFocus_easy_graphicsView.drawSelectTriggered.emit(theFirstShow)
            if theFirstShow != -1:                                                        
                self.ui.showOverall_easy_graphicsView.drawOverallTrigger.emit(pixmap,overall_x1,overall_y1,overall_x2,overall_y2)  
            
                                                            
                     
        return Gst.FlowReturn.OK        
        

        
    def parseGoldenROILabelName(self,golden_pos:str):        
        if  golden_pos.replace(" ","") in self.golden_postion_dict.keys():
            return self.golden_postion_dict[golden_pos.replace(" ","")]
        return ""
    
    def getGoldenLabelPosition(self,label_golden):
        # {"(x,y,x1,y1)":"labelstring"}
        self.golden_postion_dict={}
        if os.path.exists(label_golden):
            with open(label_golden) as f:
                lines = f.read().splitlines()
            if lines:
                for info in lines:
                    item = info.split(';')
                    t1 = tuple(map(int, item[1].strip("()").replace(" ","").split(',')))
                    t2 = tuple(map(int, item[2].strip("()").replace(" ","").split(',')))
                    self.golden_postion_dict[str(t1+t2).replace(" ","")] = item[0]
        
    def getOKfromGoldenLabel(self):
        self.ok_list = set()
        if os.path.exists(self.label_golden):
            with open(self.label_golden) as f:
                lines = f.read().splitlines()
            if lines:
                for info in lines: 
                    item = info.split(';')
                    self.ok_list.add(item[0])    
                    
    def updateNGOKstate(self,text,row):
                
        golden_pos = self.inferenceInspectReuslt[row][6]
        correctLabel = self.parseGoldenROILabelName(golden_pos)
        if correctLabel: # if selected label in golden list but it is incorrect type. still show 'NG'
            state = 'OK' if text == correctLabel else 'NG'
        else:
            state = 'OK' if text in self.ok_list else 'NG'
            print("[ERROR] Cannot find the correct answer from golde.txt. pleases contact the technical staff")
            print(f"-- Probelmatic Golden Position:{golden_pos}")
            print(f"-- Golden txt:{self.label_golden}")
            print(f"-- Golden Position list:{self.golden_postion_dict.keys()}")
        
        if self.tabName == tabNameList.advancedOperation:
            self.ui.inspectResult_tableWidget.item(row,0).setText(state)
            self.calculatePASSFAIL()
            labelstring = self.ui.inspectResult_tableWidget.cellWidget(row,1).currentText()
            self.ui.showimage_online_graphicsView.updateROI(state,row,labelstring)
        
            
    def calculatePASSFAIL(self):
        if self.tabName == tabNameList.advancedOperation:
            row = self.ui.inspectResult_tableWidget.rowCount()
            fail_state = False
            for i in range(row):                
                if self.ui.inspectResult_tableWidget.item(i,0).text() == 'NG':
                    fail_state = True
                    break
            
            if fail_state:
                self.ui.FAIL_label.setVisible(True)
                self.ui.PASS_label.setVisible(False)
            else:
                self.ui.FAIL_label.setVisible(False)
                self.ui.PASS_label.setVisible(True)
        elif self.tabName == tabNameList.inspection:
            row = self.ui.inspectResult_easy_tableWidget.rowCount()
            fail_state = False
            for i in range(row):
                if self.ui.inspectResult_easy_tableWidget.item(i,0).text() == 'NG':
                    fail_state = True
                    break
            
            if fail_state:
                self.ui.FAIL_easy_label.setVisible(True)
                self.ui.PASS_easy_label.setVisible(False)
            else:
                self.ui.FAIL_easy_label.setVisible(False)
                self.ui.PASS_easy_label.setVisible(True)    
            
    def createInspectLabelComboBox(self,row,column,labelInfo):        
        
        if os.path.exists(self.inspect_labelfile):
            with open(self.inspect_labelfile) as f:
                labels = f.read().splitlines()     
            temp_combo = QComboBox()
            temp_combo.addItems(labels)               
            index = temp_combo.findText(labelInfo)  
            if index > -1:
                temp_combo.setCurrentIndex(index)   
                if self.tabName == tabNameList.advancedOperation:
                    self.ui.inspectResult_tableWidget.setCellWidget(row,column,temp_combo)
                elif self.tabName == tabNameList.inspection:
                    self.ui.inspectResult_easy_tableWidget.setCellWidget(row,column,temp_combo)
            temp_combo.currentTextChanged.connect(lambda text: self.updateNGOKstate(text,row))
    
    def addOneRowtoInspectTable(self,row_data):      
        
        if self.tabName == tabNameList.advancedOperation:
            self.ui.submit_pushButton.setEnabled(True)
            
            row = self.ui.inspectResult_tableWidget.rowCount()
            self.addRowToInspectResult(row,self.ui.inspectResult_tableWidget,row_data)            
                    
            self.createInspectLabelComboBox(row,1,row_data[1])
            self.calculatePASSFAIL()    
        elif self.tabName == tabNameList.inspection:
            self.ui.submit_easy_pushButton.setEnabled(True) 
            row = self.ui.inspectResult_easy_tableWidget.rowCount()
            self.addRowToInspectResult(row,self.ui.inspectResult_easy_tableWidget,row_data)                        
            
            if self.ui.onlyNG_easy_checkBox.isChecked():
                if str(row_data[0]).upper() == 'OK':
                    self.ui.inspectResult_easy_tableWidget.hideRow(row)
            
            if not self.ui.inspectResult_easy_tableWidget.isRowHidden(row) and self.ui.inspectResult_easy_tableWidget.currentRow() == -1:                                                           
                self.ui.inspectResult_easy_tableWidget.setCurrentCell(row,0)   
                                             
            self.calculatePASSFAIL()             
                                                         
        elif self.tabName == tabNameList.reconfirm:
        
            row = self.ui.inspectResult_confirm_tableWidget.rowCount()
            self.addRowToInspectResult(row,self.ui.inspectResult_confirm_tableWidget,row_data)    
            self.ui.inspectResult_confirm_tableWidget.hideColumn(0)
            if str(row_data[0]).upper() == 'OK':
                self.ui.inspectResult_confirm_tableWidget.hideRow(row)
            
            
    
    def addRowToInspectResult(self,row,table,row_data):         
        table.setRowCount(row+1)        
        table.setItem(row,0,QTableWidgetItem(str(row_data[0])))            
        table.setItem(row,1,QTableWidgetItem(str(row_data[1])))
        table.item(row,0).setTextAlignment(Qt.AlignCenter)
        table.item(row,1).setTextAlignment(Qt.AlignCenter)
        table.item(row,0).setFlags(table.item(row,0).flags() ^ Qt.ItemIsEditable )
        table.item(row,1).setFlags(table.item(row,1).flags() ^ Qt.ItemIsEditable )      
            
        if table.columnCount() > 4 :
            table.setItem(row,2,QTableWidgetItem(str(row_data[4])))
            table.setItem(row,3,QTableWidgetItem(str(row_data[2])))
            table.setItem(row,4,QTableWidgetItem(str(row_data[3])))
            
            table.item(row,2).setTextAlignment(Qt.AlignCenter)
            table.item(row,3).setTextAlignment(Qt.AlignCenter)  
            table.item(row,4).setTextAlignment(Qt.AlignCenter)
            
            table.item(row,2).setFlags(table.item(row,2).flags() ^ Qt.ItemIsEditable )
            table.item(row,3).setFlags(table.item(row,3).flags() ^ Qt.ItemIsEditable )
            table.item(row,4).setFlags(table.item(row,4).flags() ^ Qt.ItemIsEditable )
        else:            
            
            table.setItem(row,2,QTableWidgetItem(str(row_data[2])))
            table.setItem(row,3,QTableWidgetItem(str(row_data[3])))
            
            table.item(row,2).setTextAlignment(Qt.AlignCenter)
            table.item(row,3).setTextAlignment(Qt.AlignCenter)  
            
            table.item(row,2).setFlags(table.item(row,2).flags() ^ Qt.ItemIsEditable )
            table.item(row,3).setFlags(table.item(row,3).flags() ^ Qt.ItemIsEditable )
            
    def onlyNG(self):        
        row = self.ui.inspectResult_easy_tableWidget.rowCount()
        if self.ui.onlyNG_easy_checkBox.isChecked(): # only NG
            for index in range(row):
                if self.ui.inspectResult_easy_tableWidget.item(index,0).text().upper() == 'OK':
                    self.ui.inspectResult_easy_tableWidget.hideRow(index)
        else:  # OK+NG
            for index in range(row):
                if self.ui.inspectResult_easy_tableWidget.isRowHidden(index):
                    self.ui.inspectResult_easy_tableWidget.showRow(index)

    def showAll(self):
        if self.tabName == tabNameList.advancedOperation:            
            self.ui.showimage_online_graphicsView.selectlabelInfo = -1
            self.ui.inspectResult_tableWidget.clearSelection()
            self.ui.showimage_online_graphicsView.showAllItem()
            
            
    def selectInspectRow(self): 
        if self.tabName == tabNameList.advancedOperation:
            self.ui.showimage_online_graphicsView.selectlabelInfo = self.ui.inspectResult_tableWidget.currentRow()        
            #self.ui.showimage_online_graphicsView.showSelect()
            self.ui.showimage_online_graphicsView.onlyShowSelect(self.ui.showimage_online_graphicsView.selectlabelInfo)
        elif self.tabName == tabNameList.inspection:                                           
            current_row = self.ui.inspectResult_easy_tableWidget.currentRow()
                
            if current_row > -1:                
                self.ui.showFocus_easy_graphicsView.onlyShowSelect(current_row)
                self.showFocusInOverall(current_row)
        elif self.tabName == tabNameList.reconfirm:
            current_row = self.ui.inspectResult_confirm_tableWidget.currentRow()
                
            if current_row > -1:                
                self.ui.showimage_confirm_graphicsView.onlyShowSelect(current_row)
                self.showFocusInOverall(current_row)
                

    def showFocusInOverall(self,current_row):
        if self.tabName == tabNameList.inspection:
            pixmap = self.ui.showFocus_easy_graphicsView.pixmapItem.pixmap()
            item =  self.ui.inspectResult_easy_tableWidget.item(current_row,2).text()
            start_x, start_y = [int(match) for match in re.findall(r'\d+', item)]
            item =  self.ui.inspectResult_easy_tableWidget.item(current_row,3).text()
            end_x, end_y = [int(match) for match in re.findall(r'\d+', item)]                              
            self.ui.showOverall_easy_graphicsView.drawOverall(pixmap,start_x,start_y,end_x,end_y)
        else:
            pixmap = self.ui.showimage_confirm_graphicsView.pixmapItem.pixmap()
            item =  self.ui.inspectResult_confirm_tableWidget.item(current_row,2).text()
            start_x, start_y = [int(match) for match in re.findall(r'\d+', item)]
            item =  self.ui.inspectResult_confirm_tableWidget.item(current_row,3).text()
            end_x, end_y = [int(match) for match in re.findall(r'\d+', item)]                              
            self.ui.showOverall_confirm_graphicsView.drawOverall(pixmap,start_x,start_y,end_x,end_y)
            
    def backShowROI(self):
        if self.tabName == tabNameList.inspection:
            current_row = self.ui.inspectResult_easy_tableWidget.currentRow()
            
            while True:                        
                if current_row == 0:
                    current_row = self.ui.inspectResult_easy_tableWidget.rowCount()-1
                else:
                    current_row = current_row - 1    
                    
                if not self.ui.inspectResult_easy_tableWidget.isRowHidden(current_row):
                    break      
                                    
                
            self.ui.inspectResult_easy_tableWidget.selectRow(current_row)
            self.ui.inspectResult_easy_tableWidget.scrollToItem(self.ui.inspectResult_easy_tableWidget.item(current_row,0))
            self.selectInspectRow()
        elif self.tabName == tabNameList.reconfirm:
            current_row = self.ui.inspectResult_confirm_tableWidget.currentRow()
            
            while True:                        
                if current_row == 0:
                    current_row = self.ui.inspectResult_confirm_tableWidget.rowCount()-1
                else:
                    current_row = current_row - 1                        
                    
                if not self.ui.inspectResult_confirm_tableWidget.isRowHidden(current_row):
                    break      
                                    
                            
            self.ui.inspectResult_confirm_tableWidget.selectRow(current_row)
            self.ui.inspectResult_confirm_tableWidget.scrollToItem(self.ui.inspectResult_confirm_tableWidget.item(current_row,0))
            self.selectInspectRow()
    
    
            
        
    def nextShowROI(self):
        if self.tabName == tabNameList.inspection:
            current_row = self.ui.inspectResult_easy_tableWidget.currentRow()
            
            while True:
                if current_row == self.ui.inspectResult_easy_tableWidget.rowCount()-1 :
                    current_row = 0
                else:
                    current_row = current_row +1 
            
                if not self.ui.inspectResult_easy_tableWidget.isRowHidden(current_row):
                    break                                
                
            self.ui.inspectResult_easy_tableWidget.selectRow(current_row)
            self.ui.inspectResult_easy_tableWidget.scrollToItem(self.ui.inspectResult_easy_tableWidget.item(current_row,0))
            self.selectInspectRow()
            
        elif self.tabName == tabNameList.reconfirm:
            current_row = self.ui.inspectResult_confirm_tableWidget.currentRow()
            
            while True:
                if current_row == self.ui.inspectResult_confirm_tableWidget.rowCount()-1 :
                    current_row = 0
                else:
                    current_row = current_row +1 
            
                if not self.ui.inspectResult_confirm_tableWidget.isRowHidden(current_row):
                    break                                
                            
            self.ui.inspectResult_confirm_tableWidget.selectRow(current_row)
            self.ui.inspectResult_confirm_tableWidget.scrollToItem(self.ui.inspectResult_confirm_tableWidget.item(current_row,0))
            self.selectInspectRow()
        
    def goverify(self):        
        self.livefreeze()        
        if hasattr(self.liveSrc, 'oriImage'):
            self.inference(self.liveSrc.oriImage)   
            self.inspect_timestamp = time.strftime("%Y%m%d%H%M%S", time.localtime()) 
            if self.tabName == tabNameList.inspection:
                self.ui.inspectResult_easy_tableWidget.setFocus()                         
                self.ui.goverify_easy_pushButton.setEnabled(False)
            elif self.tabName == tabNameList.advancedOperation:
                self.ui.inspectResult_tableWidget.setFocus()                         
                self.ui.goverify_pushButton.setEnabled(False)

    def reset(self):
        #self.ui.showimage_online_label.clearall()        
        #pixmap = self.ui.showimage_online_graphicsView.pixmapItem.pixmap()
        if self.tabName == tabNameList.advancedOperation:     
            if self.inference_pipeline:
                self.inference_pipeline.set_state(Gst.State.NULL)              
                self.inference_pipeline = None
                
            self.ui.showimage_online_graphicsView.clearall()
            #self.ui.showimage_online_graphicsView.resetImage(QPixmap(self.liveSrc.oriImage))
            self.ui.sn_online_lineEdit.clear()
            self.ui.inspectResult_tableWidget.setRowCount(0)
            if self.liveSrc:
                self.liveSrc.play() 
                self.ui.currentstatus_label.setText('Playing')            
            self.ui.submit_pushButton.setEnabled(False)
            self.ui.PASS_label.setVisible(False)
            self.ui.FAIL_label.setVisible(False)
            self.ui.goverify_pushButton.setEnabled(False)
        elif self.tabName == tabNameList.inspection: 
            if self.inference_pipeline:                
                self.inference_pipeline.set_state(Gst.State.NULL)  
                self.inference_pipeline = None
                       
            self.ui.showFocus_easy_graphicsView.clearall()            
            self.ui.showOverall_easy_graphicsView.clearall()
            self.ui.showOverall_easy_graphicsView.m_scene.clear()
            self.ui.sn_easy_lineEdit.clear()            
            self.ui.inspectResult_easy_tableWidget.setRowCount(0)            
            if self.liveSrc:
                self.liveSrc.play() 
                self.ui.currentstatus_label.setText('Playing')                            
                                
            self.ui.submit_easy_pushButton.setEnabled(False)
            self.ui.PASS_easy_label.setVisible(False)
            self.ui.FAIL_easy_label.setVisible(False)
            self.ui.sn_easy_lineEdit.setFocus()
            
            self.ui.goverify_easy_pushButton.setEnabled(False)
        elif self.tabName == tabNameList.reconfirm:
            self.ui.showimage_confirm_graphicsView.clearall()
            self.ui.showimage_confirm_graphicsView.m_scene.clear()
            self.ui.showOverall_confirm_graphicsView.clearall()
            self.ui.showOverall_confirm_graphicsView.m_scene.clear()
            self.ui.sn_confirm_lineEdit.clear() 
            self.ui.model_confirm_lineEdit.clear()
            self.ui.inspectResult_confirm_tableWidget.setRowCount(0)
            self.ui.fail_confirm_pushButton.setEnabled(False)
            self.ui.repass_confirm_pushButton.setEnabled(False)
            self.ui.back_confirm_pushButton.setEnabled(False)
            self.ui.next_confirm_pushButton.setEnabled(False)
            self.ui.submit_confirm_pushButton.setEnabled(False)
            self.ui.reset_confirm_pushButton.setEnabled(False)
            self.ui.sn_confirm_lineEdit.setFocus()
            
    def submitInspectResult(self):                
        # save image
        imagefilename = f'{self.inspect_filename}.png'
        if self.tabName == tabNameList.advancedOperation:
            pixmap = self.ui.showimage_online_graphicsView.pixmapItem.pixmap()
        elif self.tabName == tabNameList.inspection:
            pixmap = self.ui.showFocus_easy_graphicsView.pixmapItem.pixmap()
            
        imagefilepath = os.path.join(self.inspect_images_dir,imagefilename)
        # if os.path.exists(imagefilepath):
        #     os.rename(imagefilepath,os.path.join(self.inspect_images_dir,f'{self.inspect_filename}_{self.inspect_timestamp}.png'))
        image = pixmap.toImage()
        image.save(imagefilepath)
        
        # save inference information                
        filename = f'{self.inspect_filename}.txt'
        
        # inference_filepath = os.path.join(self.inspect_inferenctResult_dir,filename)
        # if os.path.exists(inference_filepath):
        #     os.rename(filename,os.path.join(self.inspect_inferenctResult_dir,f'{self.inspect_filename}_{self.inspect_timestamp}.txt'))
        
        if os.path.exists(self.inspect_inferenctResult_dir):                        
            with open(os.path.join(self.inspect_inferenctResult_dir,filename),'w') as file:
                for item in self.inferenceInspectReuslt:      
                    line = ';'.join(item)          
                    file.write(f'{line}\n')
        else:
            QMessageBox.critical(self,"Warning",f"Please confirm the application has the permission.\n{self.inspect_inferenctResult_dir} doesn't exist!")
            return
        
                    
        # save confirmed information
        self.getConfirmedInspectResultFromTable()                
        if os.path.exists(self.inspect_confirmedResult_dir):                                    
            with open(os.path.join(self.inspect_confirmedResult_dir,filename),'w') as file:
                for item in self.confirmedInspectResult:                
                    line = ';'.join(item)
                    file.write(f'{line}\n')
            QMessageBox.information(self,"Inforamtion","Done!\nSaved the confirmed inpsection resutl.")
        else:
            QMessageBox.critical(self,"Warning",f"Please confirm the application has the permission.\n{self.inspect_confirmedResult_dir} doesn't exist!")
            return
        
        self.reset()
        
    def getConfirmedInspectResultFromTable(self):
        if self.tabName == tabNameList.advancedOperation:
            rows = self.ui.inspectResult_tableWidget.rowCount()
            
            # update name and ok/ng
            for row in range(rows):
                ng_ok_state = self.ui.inspectResult_tableWidget.item(row,0).text()
                labelname = self.ui.inspectResult_tableWidget.cellWidget(row,1).currentText()   
                self.confirmedInspectResult[row][0] = labelname
                self.confirmedInspectResult[row][5] = ng_ok_state                                
            
######## Tab3: Reconfirm mode #######
    
    def searchReconfirmedInfo(self,sn):            
        self.ui.inspectResult_confirm_tableWidget.setRowCount(0)
        self.ui.showOverall_confirm_graphicsView.clearall()
        self.ui.showOverall_confirm_graphicsView.m_scene.clear()
        self.ui.submit_confirm_pushButton.setEnabled(False)
        self.ui.next_confirm_pushButton.setEnabled(False)
        self.ui.back_confirm_pushButton.setEnabled(False)
        if not sn:
            return
        if self.findModel(sn):                
            self.getGoldenLabelPosition(self.label_golden)    
            pixmap = None
            imagepath = os.path.join(self.inspect_images_dir,f'{sn}.png')
            
            if os.path.exists(imagepath):
                pixmap = QPixmap(imagepath)
                self.ui.showimage_confirm_graphicsView.set_image(pixmap)
            else:
                QMessageBox.critical(self,"Warning",f"Please confirm the serial number has been inspected.")
                return
            
            inference_filename = f'{sn}.txt'    
            inference_filepath = os.path.join(self.inspect_inferenctResult_dir,inference_filename)       
            if os.path.exists(inference_filepath):                      
                
                self.inferenceInspectReuslt = []               
                with open(inference_filepath,'r') as file:
                    lines = file.read().splitlines()                                                  
                
                for line in lines:
                    item = line.split(';')
                                        
                    self.inferenceInspectReuslt.append([item[0],item[1],item[2],item[3],item[4],item[5],item[6],item[7]])    
                                                        # labelInfo, start_point, end_point, order, duration, ng_ok, golden_pos, score
                            
            confirm_filename = f'{sn}.txt'    
            confirm_filepath = os.path.join(self.inspect_confirmedResult_dir,confirm_filename)       
            if os.path.exists(confirm_filepath):                      
                
                self.confirmedInspectResult = []               
                with open(confirm_filepath,'r') as file:
                    lines = file.read().splitlines()  
                                
                thereIsNG = False
                theFirstShow = -1
                self.ui.showimage_confirm_graphicsView.labelsInfo = lines
                
                for index,line in enumerate(lines):
                    item = line.split(';')
                                        
                    self.confirmedInspectResult.append([item[0],item[1],item[2],item[3],item[4],item[5],item[6]])    
                                                        # labelInfo, start_point, end_point, order, duration, ng_ok, golden_pos                    
                    row_data = [item[5],item[0],item[1],item[2]]
                    
                                        
                    self.addOneRowtoInspectTable(row_data)  
                    if item[5].upper() == 'NG':
                        thereIsNG = True
                        if theFirstShow == -1:
                            theFirstShow = index                                                        
                                                            
                
                self.ui.reset_confirm_pushButton.setEnabled(True)                      
                if thereIsNG:
                    self.ui.showimage_confirm_graphicsView.drawSelectRect(theFirstShow)        
                    self.ui.inspectResult_confirm_tableWidget.selectRow(theFirstShow)                   
                    self.selectInspectRow()
                    self.ui.fail_confirm_pushButton.setEnabled(True)
                    self.ui.repass_confirm_pushButton.setEnabled(True)
                    self.ui.back_confirm_pushButton.setEnabled(True)
                    self.ui.next_confirm_pushButton.setEnabled(True)                    
                    self.ui.submit_confirm_pushButton.setEnabled(True)
                else:
                    self.ui.showimage_confirm_graphicsView.drawallRect()
                    self.ui.fail_confirm_pushButton.setEnabled(False)
                    self.ui.repass_confirm_pushButton.setEnabled(False)
                    self.ui.back_confirm_pushButton.setEnabled(False)
                    self.ui.next_confirm_pushButton.setEnabled(False)                    
                    self.ui.submit_confirm_pushButton.setEnabled(False)
                    #self.calculateGoldenThreshold()                    
            else:
                self.ui.fail_confirm_pushButton.setEnabled(False)
                self.ui.repass_confirm_pushButton.setEnabled(False)
                self.ui.back_confirm_pushButton.setEnabled(False)
                self.ui.next_confirm_pushButton.setEnabled(False)
                self.ui.reset_confirm_pushButton.setEnabled(False)
                self.ui.submit_confirm_pushButton.setEnabled(False)
                
                QMessageBox.critical(self,"Warning",f"Please confirm the application has the permission.\n{self.inspect_confirmedResult_dir} doesn't exist!")
                return
        else:
            self.ui.statusbar.showMessage(f'This serinal number is not include the project {self.projectName}!')
            

    def confirmFALI(self):
        # keep NG, search next
        self.nextShowROI()
    
    
    def confirmPASS(self):
        current_row = self.ui.inspectResult_confirm_tableWidget.currentRow()        
            
        self.confirmedInspectResult[current_row][0] = self.parseGoldenROILabelName(self.confirmedInspectResult[current_row][6])
        self.confirmedInspectResult[current_row][5] = 'OK'   
        
        self.ui.inspectResult_confirm_tableWidget.item(current_row,0).setText('OK')
        self.ui.inspectResult_confirm_tableWidget.item(current_row,1).setText(self.confirmedInspectResult[current_row][0])
                     
        
        self.nextShowROI()
    
    def submitConfirmResult(self):
        filename = f'{self.inspect_filename}.txt'
        if os.path.exists(self.inspect_confirmedResult_dir):                                    
            with open(os.path.join(self.inspect_confirmedResult_dir,filename),'w') as file:
                for item in self.confirmedInspectResult:                
                    line = ';'.join(item)
                    file.write(f'{line}\n')
            QMessageBox.information(self,"Inforamtion","Done!\nSaved the confirmed inpsection resutl.")
            
            self.compareConfirmAndInsepct()
            
            self.reset()
        else:
            QMessageBox.critical(self,"Warning",f"Please confirm the application has the permission.\n{self.inspect_confirmedResult_dir} doesn't exist!")
            return    
        
    def compareConfirmAndInsepct(self):
        
        self.initThresholdFile()
        
        for item_confirm, item_inference in zip(self.confirmedInspectResult,self.inferenceInspectReuslt):
            if item_confirm[5] == 'OK' and item_inference[5] == 'NG':                
                p = item_inference[6].strip('()').replace(" ","").split(',')                
                start = f'({p[0]}, {p[1]})'
                end = f'({p[2]}, {p[3]})'
                score = item_inference[7]                
                
                if (start,end) in self.golden_roi_threshold_dict.keys():
                    threshold = self.golden_roi_threshold_dict[(start,end)]                    
                    if float(score) < float(threshold):
                        self.golden_roi_threshold_dict[(start,end)] = score
                        
        self.generateThresholdFile(self.golden_roi_threshold,self.golden_roi_threshold_dict)
        
                
    def calculateGoldenThreshold(self):
        threasholdRecommander = ThresholdRecommander(self.inspect_inferenctResult_dir, self.inspect_confirmedResult_dir, self.label_golden, objective='preventLeakage')
        threasholdRecommander.generate('DIP')
        print(f'generated threshold = {threasholdRecommander.ROIThresholds}')
        
        saveROIRecommandThresholdPath = self.golden_roi_threshold
        threasholdRecommander.save(saveROIRecommandThresholdPath) 
    
####### Tab 1:  offline (training mode) ######
    
    def registrationTool(self):
        
        if not os.path.exists(self.currentImage_offline_golden):
            QMessageBox.warning(self, "No Golden Image", "Please capture an image for golden image!")
        else:
            position_dialog = Registration(self.currentImage_offline_golden,self.positionFile)
            if position_dialog.exec_() == QDialog.Accepted:            
                                                    
                file = open(self.positionFile,'w')
                
                for l in position_dialog.positiondict.keys():
                    file.write(f'{l} {position_dialog.positiondict[l]}\n')
                    
                file.close()
    
    def clearLabelToolList(self):
        self.ui.labelList_listWidget.clear()
        
    def resetImageTable(self):          # clear image list
        self.ui.showImagelist_tableWidget.setColumnCount(0)  
    
    def resetLabelInfoTable(self):      # clear label information
        self.ui.labelInfo_tableWidget.setRowCount(0) 
        self.ui.saveLabel_pushButton.setEnabled(False)
        self.ui.EditNote_pushButton.setEnabled(False) 
##golden##        self.ui.saveasgolden_pushButton.setEnabled(False)
        self.ui.delete_pushButton.setEnabled(False)

    def resetPaintedLabel(self):        # clear PaintEvent
        #self.ui.showImage_offline_label.clearall() 
        self.ui.showImage_offline_graphicsView.clearall()        
        
    def clearTrainingShowImage(self):  # clear image, Paintevent
        #self.ui.showImage_offline_label.clear()
        self.currentImage_offline = ""        
        self.ui.showImage_offline_graphicsView.m_scene.clear()        
        self.resetPaintedLabel()
    
    def clearAllLabeledInfo(self):  # only keep image.
        self.resetPaintedLabel()        
        self.resetLabelInfoTable()
                  

    def start_offline(self):
        start_dialog = StartProject(self.projectName)
        if start_dialog.exec_() == QDialog.Accepted:     
            
            self.enabled_button()
            self.imageDir = start_dialog.imagesDir                                                             
            self.imageGoldenDir = start_dialog.imagesGoldenDir
            self.labelsDir = start_dialog.labelsDir 
            self.labelsGoldenDir = start_dialog.labelsGoldenDir 
            self.labelListFile = start_dialog.labelListFile
            self.projectPath = start_dialog.projectPath
            self.currentImage_offline_golden = os.path.join(self.imageGoldenDir,golden_filename)
            self.currentImage_labelconfig_offline_golden = os.path.join(self.labelsGoldenDir,"golden.txt")
            self.makePositionDir()
            self.productNumber = start_dialog.productNumber            
            self.clearTrainingShowImage()            
            self.clearLabelToolList()           
            self.resetLabelInfoTable()
            self.selectLabel = False 
            self.selectPic = False     
            self.drawLabel()  
            
            self.settings = self.getCurrentProjectJson()
            if self.settings:
                global maxIndex
                maxIndex = self.settings['training']['imagetable_column_count']
                
                #print(self.settings['pipeline']['trainging'])
                global pipeline_command_trainning
                pipeline_command_trainning = self.settings['pipeline']['trainging']
                
                text = self.settings['training']['type'][self.settings['type']]['description']
                self.getInferenceType(text)                
                
                self.updateUIbyInference()
                self.setLayerComboItem(self.ui.layerNo_comboBox)                            
                                        
            self.setInitGoldenState()            
            self.showlabelList()            
            self.setGoldenImage()
            
            # Training mode
            self.setGoldenWithLayer(self.ui.layerNo_comboBox.currentIndex())
            self.resetImageTable() 
            self.ui.statusbar.showMessage('Loading images...')      
            self.filelist=[]
            QtCore.QTimer.singleShot(0,self.Initialimagelist)                                      

            if self.worker_thread:
                self.worker_thread.stop()
                self.worker_thread = None
            
    def setInitGoldenState(self):
        if os.path.exists(self.currentImage_offline_golden) and os.path.exists(self.currentImage_labelconfig_offline_golden) and os.path.exists(self.labelListFile):
            self.ui.goldenmode_checkBox.setChecked(False)                
        else:
            self.ui.goldenmode_checkBox.setChecked(True)
            
        self.setGoldenMode()
            
    def setGoldenImage(self):
        self.ui.golden_tableWidget.clear()
        if os.path.exists(self.currentImage_labelconfig_offline_golden):
            label_flag = labled_flag[1]  # Labeled
        else:
            label_flag = labled_flag[0]  # Unlabeled
        
        if self.isGolden:                
            self.clearTrainingShowImage()   
                
        if os.path.exists(self.currentImage_offline_golden):              
                      
            self.oriCapturedPixmap = QPixmap(self.currentImage_offline_golden)
            _, golden_filename = os.path.split(self.currentImage_offline_golden)
            # image
            if self.isGolden:       
                if self.liveSrc:
                    self.liveSrc.stop()
                    self.liveSrc = None
                self.ui.device_offline_comboBox.setCurrentIndex(0)         
                self.ui.showImage_offline_graphicsView.set_image(self.oriCapturedPixmap)    
                self.selectPic = True  
                self.drawLabel()        
            
            
            # table            
            image_label = QLabel()
            image_label.setAlignment(Qt.AlignCenter) 
            image_label.setPixmap(self.oriCapturedPixmap.scaledToHeight(self.ui.golden_tableWidget.rowHeight(2)))        
            self.ui.golden_tableWidget.setColumnCount(1)
            self.ui.golden_tableWidget.setItem(0,0,QTableWidgetItem(label_flag))
            self.ui.golden_tableWidget.setItem(1,0,QTableWidgetItem(golden_filename))
            self.ui.golden_tableWidget.setCellWidget(2,0,image_label)
            self.ui.golden_tableWidget.item(0,0).setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
            self.ui.golden_tableWidget.item(1,0).setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
            self.ui.golden_tableWidget.resizeColumnToContents(0)     
            self.ui.golden_tableWidget.resizeRowsToContents() 
        else:
            self.oriCapturedPixmap = None
            
    def setTrainingModeUIwithInference(self,isGolden=True):
                
        if self.inferenceType == 'DIP':
            self.ui.layerNo_comboBox.setVisible(False)
            self.ui.train_pushButton.setVisible(True)
            
            self.ui.line.setVisible(False)
            self.ui.orderList_label.setVisible(False)
            self.ui.orderList_listWidget.setVisible(False)
            self.ui.line_5.setVisible(False)
            self.ui.durationList_label.setVisible(False)
            self.ui.durationList_listWidget.setVisible(False)
            
            self.ui.EditNote_pushButton.setVisible(False)
            if isGolden:
                self.ui.position_pushButton.setVisible(True)                
                self.ui.line_4.setVisible(True)                                                     
            else:
                self.ui.position_pushButton.setVisible(False)
                self.ui.line_4.setVisible(False)             
            
        elif self.inferenceType == 'SOP':
            
            self.switchSOPLabelInfoTable(isGolden)
            self.ui.layerNo_comboBox.setVisible(True)
            self.ui.train_pushButton.setVisible(False)
            if isGolden:
                self.ui.calThreshold_pushButton.setVisible(False)                             
                self.ui.position_pushButton.setVisible(True)                                                
                self.ui.line_4.setVisible(True)
                
                self.ui.autoLable_pushButton.setVisible(True)
                self.ui.line.setVisible(True)
                self.ui.orderList_label.setVisible(True)
                self.ui.orderList_listWidget.setVisible(True)
                self.ui.line_5.setVisible(True)
                self.ui.durationList_label.setVisible(True)
                self.ui.durationList_listWidget.setVisible(True) 
                
                self.ui.EditNote_pushButton.setVisible(True)
                
                if self.useOffset:
                    self.ui.EditNote_pushButton.setText('Edit Note/Offset')
                else:
                    self.ui.EditNote_pushButton.setText('Edit Note/Threshold')
                                
            else:
                self.ui.calThreshold_pushButton.setVisible(True)                
                self.ui.position_pushButton.setVisible(False)                   
                self.ui.line_4.setVisible(False)
                
                self.ui.autoLable_pushButton.setVisible(False)
                self.ui.line.setVisible(False)
                self.ui.orderList_label.setVisible(False)
                self.ui.orderList_listWidget.setVisible(False)
                self.ui.line_5.setVisible(False)
                self.ui.durationList_label.setVisible(False)
                self.ui.durationList_listWidget.setVisible(False)
                
                self.ui.EditNote_pushButton.setVisible(False)

    def switchSOPLabelInfoTable(self,isGolden=False):        
        #if isGolden:            
            font = QFont()
            font.setPointSize(8)
            if self.ui.labelInfo_tableWidget.columnCount() == 5:                
                self.ui.labelInfo_tableWidget.setColumnCount(8)                
                item = QTableWidgetItem('Note')
                item.setFont(font)
                self.ui.labelInfo_tableWidget.setHorizontalHeaderItem(5,item)                
                item = QTableWidgetItem('Threshold')
                item.setFont(font)
                self.ui.labelInfo_tableWidget.setHorizontalHeaderItem(6,item) 
                item = QTableWidgetItem('PASS-frame')
                item.setFont(font)
                self.ui.labelInfo_tableWidget.setHorizontalHeaderItem(7,item)
                
            if  self.ui.labelInfo_tableWidget.columnCount() == 8:
                self.ui.labelInfo_tableWidget.setColumnCount(9)
                item = QTableWidgetItem('Golden Position')
                item.setFont(font)
                self.ui.labelInfo_tableWidget.setHorizontalHeaderItem(8,item)
                
            if self.ui.labelInfo_tableWidget.columnCount() > 6:
                if isGolden:
                    self.ui.labelInfo_tableWidget.showColumn(3) # Order
                    self.ui.labelInfo_tableWidget.showColumn(4) # Duration
                    self.ui.labelInfo_tableWidget.showColumn(5) # Note
                    if self.useOffset:  # Threshold/Offset
                        self.ui.labelInfo_tableWidget.horizontalHeaderItem(6).setText('Offset')
                    else:
                        self.ui.labelInfo_tableWidget.horizontalHeaderItem(6).setText('Threshold')
                    self.ui.labelInfo_tableWidget.showColumn(7)  # PASS-frame
                    self.ui.labelInfo_tableWidget.removeColumn(8) # Golden Postion
                else: # train mode
                    self.ui.labelInfo_tableWidget.hideColumn(3) # Order
                    self.ui.labelInfo_tableWidget.hideColumn(4) # Duration
                    self.ui.labelInfo_tableWidget.hideColumn(5) # Note   
                    self.ui.labelInfo_tableWidget.horizontalHeaderItem(6).setText('Threshold') 
                    self.ui.labelInfo_tableWidget.hideColumn(7) # PASS-frame
                    self.ui.labelInfo_tableWidget.hideColumn(8) # Golden Postion               
        
    def setGoldenMode(self):  
        self.ui.golden_tableWidget.clearSelection()        
        self.ui.showImagelist_tableWidget.clearSelection()        
        self.resetLabelSelection()      
       
        if self.ui.goldenmode_checkBox.isChecked():                   
            self.isGolden = True            
            self.setTrainingModeUIwithInference(self.isGolden)
            self.ui.labelEdit_pushButton.setVisible(True)            
            self.ui.showImagelist_tableWidget.setEnabled(False)
            self.ui.widget_4.setEnabled(False)            
            self.setGoldenImage()
            self.InitialLabelInfo()
            self.updateLabelROI()            
            
        else:                       
            self.isGolden = False            
            self.setTrainingModeUIwithInference(self.isGolden)            
            self.ui.labelEdit_pushButton.setVisible(False)            
            self.ui.showImagelist_tableWidget.setEnabled(True)
            self.ui.widget_4.setEnabled(True)
            self.clearTrainingShowImage()
            self.selectPic = False 
            self.drawLabel()
            self.resetLabelInfoTable()                                          
    
    def showGolden(self):        
        self.ui.goldenmode_checkBox.setChecked(True)              
        #self.setGoldenMode()   
        self.ui.golden_tableWidget.clearFocus()
        
        
    def importImage(self):
        image,_ = QFileDialog.getOpenFileName(self,filter="Image Files (*.png *.jpg *.bmp )",options=QFileDialog.DontUseNativeDialog)
        if image:     
            self.ui.statusbar.showMessage('Current Status: Imported the iamge.')           
            if self.isGolden:                        
                source_image = QImage(image)
                source_image.save(self.currentImage_offline_golden,format="PNG")                
                self.setGoldenMode()
            else:                
                 
                _,filename = os.path.split(image)
                
                filename, fileextension = os.path.splitext(filename)        
                if self.inferenceType == 'SOP':
                    if filename.split('_')[-1] != str(self.current_layers):
                        filename = f"{filename}_{self.current_layers}"
                
                self.currentImage_labelconfig_offline = os.path.join(self.labelsDir,f"{filename}.txt")  
                self.currentImage_offline = os.path.join(self.imageDir,f"{filename}.png")                  
                self.oriCapturedPixmap = QPixmap(QImage(image))
                
                self.oriCapturedPixmap.save(self.currentImage_offline,format="PNG")                
                
                self.setImageToTableList(self.oriCapturedPixmap,filename)
                                
                self.showImageFromTableList(self.ui.showImagelist_tableWidget.currentRow(),self.ui.showImagelist_tableWidget.currentColumn())
                
    def setGoldenWithLayer(self,index):
        self.setCurrentLayer(index)
                
        if self.inferenceType == 'SOP':
            # update Golden image file, golden label file, and anchor file.
            self.updateGoldenFiles()
                    
    def updateGoldenFiles(self):                                      
                
        if self.current_layers < 1:
            return
        
        self.clearTrainingShowImage()
        self.clearAllLabeledInfo()
        self.currentImage_offline_golden = os.path.join(self.imageGoldenDir,f'golden_{self.current_layers}.png')
        self.currentImage_labelconfig_offline_golden = os.path.join(self.labelsGoldenDir,f"golden_{self.current_layers}.txt")
        self.positionFile = os.path.join(self.positionDir,f'anchors_{self.current_layers}.txt')                
                                                                                       
        self.setGoldenImage()                        
        self.setGoldenMode()        
        self.getGoldenLabelPosition(self.currentImage_labelconfig_offline_golden)    
        
        
        
            
    
    def makePositionDir(self):
        self.positionDir = os.path.join(self.projectPath,"position")
        self.make_dir(self.positionDir)
            
        self.positionFile = os.path.join(self.positionDir,'anchors.txt')        
        self.positionImage = self.currentImage_offline_golden
        
                        
    def enabled_button(self):
        #self.ui.capture_pushButton.setEnabled(True)
        #self.ui.autoLabel_pushButton.setEnabled(True)     
        self.ui.goldenmode_checkBox.setEnabled(True)   
        self.ui.device_offline_comboBox.setEnabled(True)
        self.ui.importImage_pushButton.setEnabled(True)
        self.ui.export_pushButton.setEnabled(True)
        self.ui.train_pushButton.setEnabled(True)
        self.ui.calThreshold_pushButton.setEnabled(True)        
        self.ui.labelEdit_pushButton.setEnabled(True)
        #self.ui.saveLabel_pushButton.setEnabled(True)
        self.ui.page_lineEdit.setEnabled(True)      
        self.ui.position_pushButton.setEnabled(True)  
        self.ui.layerNo_comboBox.setEnabled(True)
         
        
    def Initialimagelist(self):         
        filelist = natsorted(os.listdir(self.imageDir))        
        self.imageCount = 0
        for file in filelist:
            for extension in support_image_list:
                if extension in file:                    
                    self.filelist.append(file)
                    self.imageCount += 1                            
        
        self.pageCount = math.ceil(self.imageCount/maxIndex)
        self.ui.pageOf_label.setText(f'of {self.pageCount}')
        self.currentPage = 1 if self.imageCount > 0 else 0
        self.ui.page_lineEdit.setText(f'{self.currentPage}')                
        onlyInt = QIntValidator(bottom=1, top=self.pageCount,parent=self)        
        self.ui.page_lineEdit.setValidator(onlyInt)                        
        
        if self.imageCount > 0:
            self.showImagelist(1,maxIndex)
            
        self.ui.back_pushButton.setEnabled(False)
        if self.pageCount > 1:
            self.ui.next_pushButton.setEnabled(True)  
        self.ui.statusbar.clearMessage()                     
    
    def showlabelList(self):
        self.clearLabelToolList()        
        if os.path.exists(self.labelListFile):            
            with open(self.labelListFile) as f:
                labels = f.read().splitlines()            
            self.ui.labelList_listWidget.addItems(labels)
            
    def setCurrentSourceType(self,index):  
        self.clearAllLabeledInfo()             
        self.clearTrainingShowImage()        
        self.scaleOnce = True        
        if self.liveSrc:            
            self.liveSrc.stop()
            self.ui.on_off_checkBox.setChecked(False)
                
        if index == 0:
            self.ui.importImage_pushButton.setEnabled(True)            
            self.ui.capture_pushButton.setEnabled(False)
            self.live = False            
            self.liveSrc = None            
            self.selectPic = False
            self.drawLabel()  
            if self.isGolden:                
                self.setGoldenImage()
        else:
            self.ui.importImage_pushButton.setEnabled(False)            
            self.ui.capture_pushButton.setEnabled(True)
            self.live = True
            self.selectPic = False
            self.drawLabel()
                        
            current_text = self.ui.device_offline_comboBox.currentText()
            if current_text.lower() == cameraType.usb3.lower():
                camera_type = cameraType.usb3
            elif current_text.lower() == cameraType.web.lower():
                camera_type = cameraType.web
            elif current_text.lower() == cameraType.basler.lower():
                camera_type = cameraType.basler
            else:
                camera_type = ""
                
            if camera_type in pipeline_command_trainning.keys():
                gstcmd = pipeline_command_trainning[camera_type]
            else:
                gstcmd = None
                
            if gstcmd:
                self.liveSrc = LiveStream(gstcmd=pipeline_command_trainning[camera_type])
                self.liveSrc.new_frame.connect(self.update_view)
            else:
                self.liveSrc = None           
                
            if self.liveSrc:            
                self.liveSrc.graphics = self.ui.showImage_offline_graphicsView
                if self.liveSrc.parseLaunch():                
                    if not self.liveSrc.play():                    
                        self.ui.statusbar.showMessage('Failed to start the camare, please confirm the envirionment!',timeout=5000)                    
                        self.liveSrc.stop()
                        self.liveSrc = None  
                        self.ui.device_offline_comboBox.setCurrentIndex(0)
                        self.live = False
                        self.scaleOnce = True
                    else:
                        self.ui.statusbar.showMessage('Current Status: Playing live stream.')

                else:
                    print('parse failed')
                    self.liveSrc = None 
                    self.live = False
                    self.scaleOnce = True
            else:
                self.ui.statusbar.showMessage('Failed to find the camera command, please confirm the setting.json!',timeout=5000)                    
                self.ui.device_offline_comboBox.setCurrentIndex(0)
                self.live = False
                self.scaleOnce = True
                            
    
    def update_view(self,image):
        pixmap = QPixmap.fromImage(image)
        if self.scaleOnce:            
            self.ui.showImage_offline_graphicsView.set_image(pixmap)
            self.scaleOnce = False
        else:
            self.ui.showImage_offline_graphicsView.addImage(pixmap)
                                        
            
    def showImagelist(self, page, max):  
        self.resetImageTable()        
        stop = max*page if max*page < self.imageCount else self.imageCount
        for index in range(max*(page-1),stop):                     
            file = self.filelist[index]            
            _,filename = os.path.split(file)
            labelconfig = os.path.join(self.labelsDir,f'{os.path.splitext(filename)[0]}.txt')                      
            if os.path.exists(labelconfig):              
                labeled=labled_flag[1]                         
            else:                      
                labeled=labled_flag[0]                       
            
                                        
            pixmap =  QPixmap(os.path.join(self.imageDir,filename)).scaledToHeight(self.ui.showImagelist_tableWidget.rowHeight(2))
            image = QLabel()    
            image.setAlignment(Qt.AlignCenter) 
            image.setPixmap(pixmap)
            
            self.addOneColunmtoImageTable([labeled,filename,image])
    
          
    def changePage(self,currentPage):        
        if currentPage > self.pageCount:
            return False        
        elif currentPage < self.pageCount:
            self.ui.next_pushButton.setEnabled(True)
            if currentPage == 1:                
                self.ui.back_pushButton.setEnabled(False)
            elif currentPage > 1:
                self.ui.back_pushButton.setEnabled(True)                        
            elif currentPage < 1:
                return False
        elif currentPage == self.pageCount:
            self.ui.next_pushButton.setEnabled(False)
            if currentPage == 1:
                self.ui.back_pushButton.setEnabled(False)    
            else:
                self.ui.back_pushButton.setEnabled(True)
                        
        return True
            
    def nextPage(self):                
        if self.changePage(self.currentPage+1):            
            self.currentPage += 1
            self.showImagelist(self.currentPage,maxIndex)
            self.ui.page_lineEdit.setText(f'{self.currentPage}')                                                        
        
    def backPage(self):        
        if self.changePage(self.currentPage-1):
            self.currentPage -= 1
            self.showImagelist(self.currentPage,maxIndex)
            self.ui.page_lineEdit.setText(f'{self.currentPage}') 
    
            
    def addOneColunmtoImageTable(self,column_data):        
        column = self.ui.showImagelist_tableWidget.columnCount()        
        self.ui.showImagelist_tableWidget.setColumnCount(column+1)
        self.ui.showImagelist_tableWidget.horizontalHeaderItem(column)
        self.ui.showImagelist_tableWidget.setItem(0,column,QTableWidgetItem(str(column_data[0])))
        self.ui.showImagelist_tableWidget.setItem(1,column,QTableWidgetItem(str(column_data[1])))
        self.ui.showImagelist_tableWidget.setCellWidget(2,column,column_data[2])        
        self.ui.showImagelist_tableWidget.item(0,column).setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.ui.showImagelist_tableWidget.item(1,column).setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.ui.showImagelist_tableWidget.resizeColumnToContents(column)     
        self.ui.showImagelist_tableWidget.resizeRowsToContents()                                                           
            
            
    def parseTrainFilename(self,imageFilename):        
        path , file = os.path.split(imageFilename)        
        filename, _ = os.path.splitext(file)        
        pattern = rf"^(.*?)(?:_(ok|ng|OK|NG))?_(\d+)$"
    
        match = re.match(pattern,filename)        
        
        if match:
            name = match.group(1)  # 第一部分 (如 abc, cde)
            flag = match.group(2) or ""  # 第二部分 (如 ok, ng，若無則為空字串)
            layerNo = match.group(3)  # 第三部分 (如 1, 2)
            return path,name,flag,int(layerNo)
        else:
            return path, filename, "", -1
        
        
        
    def showImageFromTableList(self,row, column):                 
                                    
        self.clearAllLabeledInfo()
        self.clearTrainingShowImage()        
        self.resetLabelSelection()
        self.ui.device_offline_comboBox.setCurrentIndex(0)        
                
        
        currentImage_offline = os.path.join(self.imageDir,self.ui.showImagelist_tableWidget.item(1,column).text())                              
        path, filename, flag, layerNo = self.parseTrainFilename(currentImage_offline)                
        
        if self.inferenceType == 'SOP':  
                               
            if layerNo != -1 and layerNo <= int(self.settings['layers']):
                self.current_layers = layerNo
                self.ui.layerNo_comboBox.setCurrentIndex(self.current_layers-1) 
        
        _ , file = os.path.split(currentImage_offline)        
        filename, _ = os.path.splitext(file)      
        print(currentImage_offline)            
        self.currentImage_offline = currentImage_offline
        self.currentImage_labelconfig_offline = os.path.join(self.labelsDir,f'{filename}.txt')  
        self.oriCapturedPixmap = QPixmap(self.currentImage_offline)                
        self.ui.showImage_offline_graphicsView.set_image(self.oriCapturedPixmap)
                
        
  
        self.selectPic = True           
        self.drawLabel()     
        self.InitialLabelInfo()     
        self.updateLabelROI()          
        
    def deleteThresholdLog(self,file):
        if self.inferenceType == 'SOP':
            _, _, _, layer = self.parseTrainFilename(file)            
            filename = os.path.splitext(file)[0]
            
            if layer > 0:
                threshold_dict = self.readOffsetInfo(layer)
                for value in threshold_dict.values():                    
                    if filename in value["OK-Files"]:
                        index = value["OK-Files"].index(filename)
                        del value["OK-Threshold-List"][index]
                        del value["OK-Files"][index]                    
                    if filename in value["NG-Files"]:
                        index = value["NG-Files"].index(filename)
                        del value["NG-Threshold-List"][index]
                        del value["NG-Files"][index]    
                        
                
                self.writeOffsetInfo(threshold_dict,layer)           
        
     
    def showContextMenu(self,pos):        
  
        index = self.ui.showImagelist_tableWidget.indexAt(pos)
        if not index.isValid():
            return  
        col = index.column()
        menu = QMenu()

        action_delete = menu.addAction("delete")
        action = menu.exec_(self.ui.showImagelist_tableWidget.viewport().mapToGlobal(pos))  # 顯示選單

        if action == action_delete:            
            self.clearTrainingShowImage()            
            self.resetLabelInfoTable()
            filename = self.ui.showImagelist_tableWidget.item(1,col).text()       
            self.deleteThresholdLog(filename)
            currentImage = os.path.join(self.imageDir,f"{filename}")
            labelconfig = os.path.join(self.labelsDir,f"{os.path.splitext(filename)[0]}.txt")
            
            if os.path.exists(labelconfig):
                os.remove(labelconfig)
            if os.path.exists(currentImage):
                os.remove(currentImage)
                
            self.ui.showImagelist_tableWidget.removeColumn(col)  # 刪除行
            index = 10*(self.currentPage - 1) + col            
            del self.filelist[index]                          
            self.imageCount -=1      
            if self.imageCount == 0:
                self.currentPage = 0
                self.ui.page_lineEdit.setText(f'{self.currentPage}')
            else:        
                self.pageCount = math.ceil(self.imageCount/maxIndex)
                self.ui.pageOf_label.setText(f'of {self.pageCount}')   
                if self.currentPage > self.pageCount:
                    self.currentPage = self.pageCount    
                    self.ui.page_lineEdit.setText(f'{self.currentPage}')                    
                self.showImagelist(self.currentPage,maxIndex)
                
                self.changePage(self.currentPage)
    
    def drawLabel(self):              
        if self.inferenceType == 'SOP':
            if self.isGolden:
                order = self.ui.orderList_listWidget.currentItem().text()
                duration = self.ui.durationList_listWidget.currentItem().text()          
            else:                
                self.ui.showImage_offline_graphicsView.enable_draw = False    
                return        
        else:
            order = "Ignore"
            duration = "Ignore"
                        
                
        if(self.ui.labelList_listWidget.currentItem()):                        
            self.ui.showImage_offline_graphicsView.labelstring = self.ui.labelList_listWidget.currentItem().text()
            self.selectLabel = True
        else:                                  
            self.ui.showImage_offline_graphicsView.labelstring = None
            self.selectLabel = False
            
        if self.selectPic:
            self.ui.autoLable_pushButton.setEnabled(True)
        else:
            self.ui.autoLable_pushButton.setEnabled(False)
            
        if self.selectLabel and self.selectPic:
            self.ui.showImage_offline_graphicsView.enable_draw = True            
            self.ui.showImage_offline_graphicsView.order = order       
            self.ui.showImage_offline_graphicsView.duration = duration            
        else:                                        
            self.ui.showImage_offline_graphicsView.enable_draw = False            
       
    def resetLabelSelection(self):
        self.ui.labelList_listWidget.clearSelection()
        self.ui.labelList_listWidget.setCurrentItem(None)
        self.selectLabel = False
        self.drawLabel()
            
    def InitialLabelInfo(self):        
        self.resetLabelInfoTable()
        if self.isGolden:
            labelconfig = self.currentImage_labelconfig_offline_golden
        else:
            labelconfig = self.currentImage_labelconfig_offline
                    
        if os.path.exists(labelconfig):            
            with open(labelconfig,"r",encoding='utf-8') as f:
                labelsInfo = f.read().splitlines()
                                                     
            for _,info in enumerate(labelsInfo):                                                
                data = info.split(';')

                self.addOneRowtoLabelTable(data) 
            
            
            
    def updateLabelROI(self):    
        data = []  
        
        for i in range(self.ui.labelInfo_tableWidget.rowCount()):                        
            row_data = ""
            if self.ui.labelInfo_tableWidget.columnCount() > 5:
                col = 5
            else:
                col = self.ui.labelInfo_tableWidget.columnCount()
                
            for j in range(col):
                
                item = self.ui.labelInfo_tableWidget.item(i,j)                
                if item is None:
                    continue
                    
                row_data += item.text()                 
                if j!=col-1:                    
                    row_data += ';'
            
            data.append(row_data)                      
                
        self.ui.showImage_offline_graphicsView.clearall()        
        self.ui.showImage_offline_graphicsView.resetImage(self.oriCapturedPixmap)
        self.ui.showImage_offline_graphicsView.labelsInfo = data          
        self.ui.showImage_offline_graphicsView.drawTriggered.emit()
        
        if data:
            self.ui.saveLabel_pushButton.setEnabled(True) 
            self.ui.EditNote_pushButton.setEnabled(True)       
        
            
    def selectLabelInfoRow(self,current_item,previous_item):                        
        if self.isDeleteROI:
            self.isDeleteROI = False
            return
        if current_item:            
            r = self.ui.labelInfo_tableWidget.row(current_item)                   
            self.ui.showImage_offline_graphicsView.selectlabelInfo = r        
            self.ui.showImage_offline_graphicsView.drawSelect(moved=True)
            self.ui.showImage_offline_graphicsView.enable_move = True
            self.ui.delete_pushButton.setEnabled(True)        
        
    def disabledSelectLabelInfoRow(self,r,c):
        if c != 3:
            self.ui.labelInfo_tableWidget.clearSelection()
            self.ui.showImage_offline_graphicsView.resetUnMoved()  
            self.ui.showImage_offline_graphicsView.showAllItem()      
        
    
    def deleteROI(self):
        self.isDeleteROI = True  
        row = self.ui.labelInfo_tableWidget.currentRow()        
        self.ui.labelInfo_tableWidget.removeRow(row)            
        self.ui.showImage_offline_graphicsView.resetImage(self.oriCapturedPixmap)
        self.updateLabelROI()             
        self.ui.labelInfo_tableWidget.clearSelection() 
        self.ui.labelInfo_tableWidget.setCurrentItem(None)
        self.ui.showImage_offline_graphicsView.selectlabelInfo = -1  
        self.ui.showImage_offline_graphicsView.enable_move = False          
        self.ui.delete_pushButton.setEnabled(False)
        
        
        if(self.ui.labelList_listWidget.currentItem()):    
            self.ui.showImage_offline_graphicsView.labelstring = self.ui.labelList_listWidget.currentItem().text()
                        
    def livefreeze(self):
        if self.liveSrc:
            self.liveSrc.pause()

    def defineSavedFilename(self):
        timestamp = time.strftime("%Y%m%d%H%M%S", time.localtime())
        
        if self.inferenceType == 'SOP':
            filename = f"{self.projectName}_{timestamp}_{self.current_layers}"
        else:            
            filename = f"{self.projectName}_{timestamp}"
            
        return filename
        
    def showImageFromStreaming(self):   
        # add re-capture                
        if self.liveSrc:      
            if self.liveSrc.isPause():       
                self.liveSrc.play()
                
                sleep(1)
                
            self.clearAllLabeledInfo()  # keep image        
            self.liveSrc.pause()
            self.selectPic = True   
            self.drawLabel()            
            filename=self.defineSavedFilename() 
            
            remove = False         
            
            #Image from live streaming    
            if self.isGolden:                 
                reply = QMessageBox.question(self, "Confirm", "Would you like to keep the golden settings and registration anchors?",  QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        
                if reply == QMessageBox.Yes:
                    remove = False                    
                else:
                    remove = True
                    
                if remove:
                    ret = QMessageBox.warning(self,"Warning","Click 'OK' will reset the golden setting and registration anchors", QMessageBox.Ok, QMessageBox.Cancel)                                
                    if ret == QMessageBox.Cancel:                        
                        self.liveSrc.play()
                        return
                else:
                    QMessageBox.information(self,"Notification","Keep the golden settings and registration anchors.", QMessageBox.Ok)                                
                
            self.oriCapturedPixmap = QPixmap(self.liveSrc.oriImage)
            self.ui.statusbar.showMessage('Current Status: Captured the iamge.')            
            
            ## save directly
                        
            if self.isGolden:                                                                                   
                self.liveSrc.oriImage.save(self.currentImage_offline_golden, format="PNG") 
                if remove:
                    if os.path.exists(self.currentImage_labelconfig_offline_golden):
                        os.remove(self.currentImage_labelconfig_offline_golden)    
                    if os.path.exists(self.positionFile):
                        os.remove(self.positionFile)                                    
                             
                self.setGoldenMode()
            else:
                self.currentImage_labelconfig_offline = os.path.join(self.labelsDir,f"{filename}.txt")  
                self.currentImage_offline = os.path.join(self.imageDir,f"{filename}.png")
                self.oriCapturedPixmap.save(self.currentImage_offline)
                self.setImageToTableList(self.oriCapturedPixmap,filename)
            
        
    def editlabel(self):        
        editLabel_dialog = EditLabel(self.labelListFile)
        if editLabel_dialog.exec_() == QDialog.Accepted:            
            self.clearLabelToolList()
            self.ui.labelList_listWidget.addItems(editLabel_dialog.labels)
            file = open(self.labelListFile,'w')
            for label in editLabel_dialog.labels:
                file.write(label+'\n')
            file.close()

    def autolabel(self):
        if not os.path.exists(self.labelListFile):
            QMessageBox.critical(self,"Warning","please create the label list first!")
            return
        
        autolabel_Widget = AutoLable(self.oriCapturedPixmap,self.labelListFile)
        
        if autolabel_Widget.exec_() == QDialog.Accepted:

            list=autolabel_Widget.getPositionList()
            if(len(list)>0):
                labelstring = autolabel_Widget.chooseLabel
                for pos in list:
                    
                    row_data=[labelstring,
                              f'{int(pos[0][0]), int(pos[0][1])}',
                              f'{int(pos[1][0]), int(pos[1][1])}',
                              self.ui.showImage_offline_graphicsView.order,
                              self.ui.showImage_offline_graphicsView.duration
                              ]

                    self.addOneRowtoLabelTable(row_data)

                self.updateLabelROI()                      
            
    def setImageToTableList(self,pixmap,filename):
        image = QLabel()    
        image.setAlignment(Qt.AlignCenter) 
        image.setPixmap(pixmap.scaledToHeight(self.ui.showImagelist_tableWidget.rowHeight(2)))        
        self.addOneColunmtoImageTable([labled_flag[0],f"{filename}.png",image])
        self.filelist.append(f"{filename}.png")
        self.imageCount = len(self.filelist)
        self.pageCount = math.ceil(self.imageCount/maxIndex)
        self.ui.pageOf_label.setText(f'of {self.pageCount}')
        self.currentPage = self.pageCount
        self.ui.page_lineEdit.setText(f'{self.currentPage}') 
        self.changePage(self.currentPage)                               
        self.showImagelist(self.currentPage,maxIndex)                                  
        self.ui.showImagelist_tableWidget.setCurrentCell(0,self.ui.showImagelist_tableWidget.columnCount()-1)        
        
    def saveLabeldata(self, labelfilepath):     
        labelstatus = False    
        if self.ui.labelInfo_tableWidget.rowCount() > 0:                
            file = open(labelfilepath,'w',encoding="utf-8")                
            
            for i in range(self.ui.labelInfo_tableWidget.rowCount()):                        
                for j in range(self.ui.labelInfo_tableWidget.columnCount()):                
                    item = self.ui.labelInfo_tableWidget.item(i,j)
                    if item:
                        if j == 5:
                            file.write(repr(item.text()))
                        else:
                            file.write(item.text())
                        if j!=self.ui.labelInfo_tableWidget.columnCount()-1:
                            file.write(';')
                if i != self.ui.labelInfo_tableWidget.rowCount()-1:
                    file.write('\n')                                
            file.close()
            labelstatus = True
             
            QMessageBox.information(self,"Inforamtion","Done!\nSaved the label information.")
            self.ui.statusbar.showMessage("Current Status: Saved the label information.")
        
        else:  # no label info
            if os.path.exists(labelfilepath):
                os.remove(labelfilepath)
            labelstatus = False
               
        if self.isGolden:            
            self.ui.device_offline_comboBox.setCurrentIndex(0)
            self.setGoldenMode()
        else:
            if self.live: 
                self.liveSrc.play()  
                self.selectPic = False   
                self.drawLabel()                  
                self.clearAllLabeledInfo()                
                self.ui.showImage_offline_graphicsView.clearall()                
                self.ui.saveLabel_pushButton.setEnabled(False) 
                self.ui.EditNote_pushButton.setEnabled(False)               
                self.timer.start(5000)

        return labelstatus

    def saveGolden(self):       
        if not self.oriCapturedPixmap:        
            return
        
        image = self.oriCapturedPixmap.toImage()
        image.save(self.currentImage_offline_golden,format='PNG')        
        self.saveLabeldata(self.currentImage_labelconfig_offline_golden)

    def show_message_box(self):
        # 建立 QMessageBox
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Question)
        msg_box.setWindowTitle("Confirm image")
        msg_box.setText("Is the ROI of the image all OK or all NG?")
        
        # 添加自訂按鈕                
        btn_ok = msg_box.addButton("All &OK", QMessageBox.AcceptRole)        
        btn_ng = msg_box.addButton("All &NG", QMessageBox.RejectRole)
        
        btn_cancle = msg_box.addButton(QMessageBox.Cancel)
        
        msg_box.setDefaultButton(btn_cancle)
        
        msg_box.setStyleSheet("""
        QMessageBox {
            text-align: center;
        }
        QMessageBox QPushButton {
            min-width: 80px;
        }
        QMessageBox QPushButton:nth-child(3) {
            margin-left: auto;
        }
        QMessageBox QPushButton:nth-child(1),
        QMessageBox QPushButton:nth-child(2) {
            margin-right: auto;
        }
        """)

        # 顯示訊息框並等待使用者選擇
        msg_box.exec_()
        
        # 根據按鈕執行動作
        if msg_box.clickedButton() == btn_ok:
            self.SOP_train_okng_flag = 'OK'
        elif msg_box.clickedButton() == btn_ng:            
            self.SOP_train_okng_flag = 'NG'
        else:            
            self.SOP_train_okng_flag = ""
            
    def readOffsetInfo(self,layer=0):
        offset_dict = {}
        if layer == 0:
            layer = self.current_layers
        elif layer == -1:
            return offset_dict
            
        json_file = os.path.join(projectRoot, self.productNumber, self.projectName,"threshold",f"offset_{layer}.json")                
        
        if os.path.exists(json_file):
            with open(json_file,'r',encoding='utf-8') as file:
                offset_dict = json.load(file)

        return offset_dict
    
    def writeOffsetInfo(self,offset_dict:dict,layer=0):
        
        if layer == 0:
            layer = self.current_layers
        elif layer == -1:
            return
            
        json_file = os.path.join(projectRoot, self.productNumber, self.projectName,"threshold",f"offset_{layer}.json")                
        if offset_dict:
            with open(json_file,'w',encoding='utf-8') as file:
                json.dump(offset_dict, file,ensure_ascii=False, indent=4)
                    
        
    def createThresholdOffsetFile(self):        
        self.make_dir(os.path.join(projectRoot, self.productNumber, self.projectName,"threshold"))
                                       
        offset_dict = self.readOffsetInfo()                          
        
        ret,lines = self.getLabelFileToList(self.currentImage_labelconfig_offline_golden)
        if ret:                    
            if lines:
                for info in lines:
                    item = info.split(';')
                    t1 = tuple(map(int, item[1].strip("()").replace(" ","").split(',')))
                    t2 = tuple(map(int, item[2].strip("()").replace(" ","").split(',')))
                    key = str(t1+t2).replace(" ","")
                    if key in offset_dict.keys():      
                        if self.useOffset:                  
                            offset_dict[key]["offset"] =float(item[6])
                        else:
                            offset_dict[key]["threshold"] = float(item[6])
                    else:
                        offset_dict[key] = {}                                                
                        if self.useOffset:
                            offset_dict[key]["offset"] = float(item[6])
                        else:
                            offset_dict[key]["threshold"] = float(item[6])                            
                        offset_dict[key]["OK"]=default_ok_threshold
                        offset_dict[key]["NG"]=default_ng_threshold
                        offset_dict[key]["OK-Files"]=[]
                        offset_dict[key]["OK-Threshold-List"]=[]
                        offset_dict[key]["NG-Files"]=[]
                        offset_dict[key]["NG-Threshold-List"]=[]
                            
        self.writeOffsetInfo(offset_dict)
    
    def calculateThresholdOffset(self,ok_score:float,ng_score_list:list):
        offset = float(default_threshold)
        average = default_ng_threshold
        
        if ng_score_list:
            if all(isinstance(item, (int,float)) for item in ng_score_list): # checl ng_score_list is integer or float
                average = np.mean(ng_score_list)
                offset = ok_score-average    
                return True, offset, average
            return False, offset, average
        else:            
            offset = ok_score-average
            return True, offset, average
        
                    
    
    def updateThresholdOffsetFile(self,filename:str):
        
        offset_dict = self.readOffsetInfo()        
        
        ret, lines = self.getLabelFileToList(self.currentImage_labelconfig_offline)
        if ret:
            if lines:
                for info in lines:
                    item = info.split(';')
                    key = item[7].replace(" ","")   # golden pos
                    if key in offset_dict.keys():
                        if 'OK' in offset_dict[key]:
                            ok_score = offset_dict[key]['OK']
                        else:
                            ok_score = default_ok_threshold
                            
                        if 'NG-Threshold-List' in offset_dict[key]:                            
                            ng_list = offset_dict[key]['NG-Threshold-List']
                        else:                            
                            ng_list = []                        
                                                
                        if self.SOP_train_okng_flag == 'OK':                            
                            ok_score = float(item[6])                        
                            
                            if 'OK-Files' in offset_dict[key]:
                                if filename in offset_dict[key]['OK-Files']:
                                    index = offset_dict[key]['OK-Files'].index(filename)
                                    offset_dict[key]['OK-Threshold-List'][index] = ok_score    
                                else:
                                    offset_dict[key]['OK-Files'].append(filename)
                                    offset_dict[key]['OK-Threshold-List'].append(ok_score)
                            else:
                                offset_dict[key]['OK-Files'] = [filename]
                                offset_dict[key]['OK-Threshold-List'] = [ok_score]
                            
                            ok_score = min(offset_dict[key]['OK-Threshold-List'])
                            offset_dict[key]['OK'] = ok_score                              
                            ret, offset,average = self.calculateThresholdOffset(ok_score,ng_list)                                                        
                            
                        elif self.SOP_train_okng_flag == 'NG':
                            ng_score = float(item[6])                            
                            if 'NG-Files' in offset_dict[key]:                                
                                if filename in offset_dict[key]['NG-Files']:                                        
                                    index = offset_dict[key]['NG-Files'].index(filename)
                                    offset_dict[key]['NG-Threshold-List'][index] = ng_score
                                else:                                    
                                    offset_dict[key]['NG-Files'].append(filename)
                                    offset_dict[key]['NG-Threshold-List'].append(ng_score)                                                                                                                                           
                            else:
                                offset_dict[key]['NG-Files'] = [filename]
                                offset_dict[key]['NG-Threshold-List'] = [ng_score]
                            
                            ng_list = offset_dict[key]['NG-Threshold-List']                                
                            ret, offset,average = self.calculateThresholdOffset(ok_score,ng_list)
                                                                                
                        if self.useOffset:                        
                            if ret:
                                offset_dict[key]['NG'] = average    
                                if 'offset' in offset_dict[key]:
                                    if offset < offset_dict[key]['offset']:
                                        offset_dict[key]['offset'] = round(offset,3)
                                else:
                                    offset_dict[key]['offset'] = round(offset,3)
                        
                        else:
                            if offset_dict[key]['OK-Threshold-List']:
                                minOKThreshold = round(min(offset_dict[key]['OK-Threshold-List'])*0.999,3)
                            else:
                                minOKThreshold = default_ok_threshold
                                
                            if offset_dict[key]['NG-Threshold-List']:
                                maxNGThreshold = round(max(offset_dict[key]['NG-Threshold-List'])*1.001,3)
                            else:
                                maxNGThreshold = default_ng_threshold
                            
                            threshold = minOKThreshold if minOKThreshold >= maxNGThreshold else maxNGThreshold
                            if offset_dict[key]['threshold'] > threshold:
                                offset_dict[key]['threshold'] = threshold
                                                               
                        self.writeOffsetInfo(offset_dict)
        return offset_dict
                    
    def updateGoldenThresholdOffset(self,offset_dict:dict):
        if offset_dict:
            ret,lines = self.getLabelFileToList(self.currentImage_labelconfig_offline_golden)
            if ret:
                if lines:
                    for index, info in enumerate(lines):
                        item = info.split(';')
                        t1 = tuple(map(int, item[1].strip("()").replace(" ","").split(',')))
                        t2 = tuple(map(int, item[2].strip("()").replace(" ","").split(',')))
                        key = str(t1+t2).replace(" ","")
                        if key in offset_dict.keys():
                            if self.useOffset:
                                offset = offset_dict[key]["offset"]
                                item[6] = str(offset)
                            else:
                                threshold = offset_dict[key]["threshold"]
                                item[6] = str(threshold)
                            lines[index] = ";".join(item)+"\n"
                    
                    lines[-1] = lines[-1].rstrip("\n") 
                    
                    with open(self.currentImage_labelconfig_offline_golden,'w',encoding='utf-8') as file:
                        file.writelines(lines)
                    
            
    def saveLabel(self):    
                
        if self.isGolden:
            labelconfig = self.currentImage_labelconfig_offline_golden
            table = self.ui.golden_tableWidget
            col = 0
        else:                                      
            col = self.ui.showImagelist_tableWidget.currentColumn()  
                
            if self.inferenceType == 'SOP':
                
                                
                path, filename, flag, layerNo = self.parseTrainFilename(self.currentImage_offline)                                
                                
                passLayer = False
                passFlag = False
                if layerNo == -1:
                    layerNo == self.current_layers
                else:
                    passLayer = True    
                
                if flag == "":                                    
                    self.show_message_box()
                    if self.SOP_train_okng_flag:
                        flag = self.SOP_train_okng_flag
                    else:
                        QMessageBox.warning(self,"Warning","Label information has not been saved!")
                        return
                else:
                    self.SOP_train_okng_flag = flag.upper()
                    passFlag = True
                    
                new_filename = f"{filename}_{flag}_{layerNo}"     
                if not (passLayer and passFlag):
                                            
                    ## 更改png,txt,table上面顯示的名字                                
                    self.currentImage_offline = rename_file_with_pathlib(self.currentImage_offline,new_filename)
                    self.currentImage_labelconfig_offline = rename_file_with_pathlib(self.currentImage_labelconfig_offline,new_filename)
                    self.ui.showImagelist_tableWidget.item(1,col).setText(new_filename+os.path.splitext(self.currentImage_offline)[1])
                    index = 10*(int(self.ui.page_lineEdit.text()) - 1) + col                    
                    self.filelist[index] = new_filename+os.path.splitext(self.currentImage_offline)[1]
                    
                                        
                
            labelconfig = self.currentImage_labelconfig_offline
            table = self.ui.showImagelist_tableWidget        
                    
                
                
                                                
            
        if self.saveLabeldata(labelconfig): # labeled            
            item = table.item(0,col)
            item.setText(labled_flag[1])
        else: # Unlabeled
            item=table.item(0,col)
            item.setText(labled_flag[0])
            
        if self.inferenceType == 'SOP':
            # 更新Threshold
            if self.isGolden:
                self.createThresholdOffsetFile()
                self.getGoldenLabelPosition(labelconfig)
            else:                
                offset_dict = self.updateThresholdOffsetFile(new_filename)
                self.updateGoldenThresholdOffset(offset_dict)
                
        if self.isGolden:
            if not os.path.exists(self.positionFile ):
                QMessageBox.warning(self,"Warning", "Please set registration anchor!")
                self.registrationTool()
            
    def showMessageAfterTimeout(self):
            self.ui.statusbar.showMessage("Current Status: playing the live stream.")
            
    def getRectRation(self, targetrect, originalrect):        
        x_ration = targetrect.width()/originalrect.width()
        y_ration = targetrect.height()/originalrect.height()
        return x_ration, y_ration
        
    def addLabelInfoRow(self):
        self.ui.saveLabel_pushButton.setEnabled(True)
        self.ui.EditNote_pushButton.setEnabled(True)         
        rect = self.ui.showImage_offline_graphicsView.current_rectitem.rect()        
        
        row_data=[self.ui.showImage_offline_graphicsView.labelstring
                  ,f'{round(rect.left()),round(rect.top())}'
                  ,f'{round(rect.right()),round(rect.bottom())}'
                  ,self.ui.showImage_offline_graphicsView.order,
                  self.ui.showImage_offline_graphicsView.duration]
        self.addOneRowtoLabelTable(row_data)

    def addOneRowtoLabelTable(self,row_data):
        row = self.ui.labelInfo_tableWidget.rowCount()        
        self.ui.labelInfo_tableWidget.setRowCount(row+1)        
        self.ui.labelInfo_tableWidget.setItem(row,0,QTableWidgetItem(str(row_data[0])))
        self.ui.labelInfo_tableWidget.setItem(row,1,QTableWidgetItem(str(row_data[1])))
        self.ui.labelInfo_tableWidget.setItem(row,2,QTableWidgetItem(str(row_data[2])))
        self.ui.labelInfo_tableWidget.setItem(row,3,QTableWidgetItem(str(row_data[3])))                   
        self.ui.labelInfo_tableWidget.setItem(row,4,QTableWidgetItem(str(row_data[4]))) 
        self.ui.labelInfo_tableWidget.item(row,1).setTextAlignment(Qt.AlignCenter)
        self.ui.labelInfo_tableWidget.item(row,2).setTextAlignment(Qt.AlignCenter)
        self.ui.labelInfo_tableWidget.item(row,3).setTextAlignment(Qt.AlignCenter)
        self.ui.labelInfo_tableWidget.item(row,4).setTextAlignment(Qt.AlignCenter)        
        self.ui.labelInfo_tableWidget.item(row,0).setFlags(self.ui.labelInfo_tableWidget.item(row,0).flags() ^ Qt.ItemIsEditable )
        self.ui.labelInfo_tableWidget.item(row,1).setFlags(self.ui.labelInfo_tableWidget.item(row,1).flags() ^ Qt.ItemIsEditable )
        self.ui.labelInfo_tableWidget.item(row,2).setFlags(self.ui.labelInfo_tableWidget.item(row,2).flags() ^ Qt.ItemIsEditable )
        self.ui.labelInfo_tableWidget.item(row,3).setFlags(self.ui.labelInfo_tableWidget.item(row,3).flags())
        self.ui.labelInfo_tableWidget.item(row,4).setFlags(self.ui.labelInfo_tableWidget.item(row,4).flags())                
                   
        self.ui.labelInfo_tableWidget.resizeColumnsToContents()
        self.ui.labelInfo_tableWidget.resizeRowsToContents()        
        self.ui.labelInfo_tableWidget.horizontalHeader().setStretchLastSection(True)  
                
        if self.inferenceType == 'SOP':
            if self.isGolden:
                self.ui.labelInfo_tableWidget.setItemDelegateForColumn(3, ComBoxDelegate(self.ui.labelInfo_tableWidget,comboxItemList1))
                self.ui.labelInfo_tableWidget.setItemDelegateForColumn(4, ComBoxDelegate(self.ui.labelInfo_tableWidget,comboxItemList2))                                
                
            if self.ui.labelInfo_tableWidget.columnCount() > 6:
                if len(row_data) > 5 and row_data[5]: # note                        
                    note = eval(row_data[5]).strip("'")                                                                
                else:
                    note = ''
                self.ui.labelInfo_tableWidget.setItem(row,5,QTableWidgetItem(str(note)))
                self.ui.labelInfo_tableWidget.resizeColumnToContents(5)
                self.ui.labelInfo_tableWidget.resizeRowsToContents()
                self.ui.labelInfo_tableWidget.item(row,5).setFlags(self.ui.labelInfo_tableWidget.item(row,5).flags() ^ Qt.ItemIsEditable )
                
                if len(row_data) > 6 and row_data[6]: # threshold/offset
                    threshold = row_data[6]
                else:
                    threshold = default_threshold                                              
                            
                self.ui.labelInfo_tableWidget.setItem(row,6,QTableWidgetItem(str(threshold)))
                self.ui.labelInfo_tableWidget.resizeColumnToContents(6)                    
                self.ui.labelInfo_tableWidget.item(row,6).setFlags(self.ui.labelInfo_tableWidget.item(row,6).flags() ^ Qt.ItemIsEditable )
                    
                if len(row_data) > 7 and row_data[7]: # PASS-frame
                    passFrame = row_data[7]
                else:
                    passFrame = default_pass_frame
                self.ui.labelInfo_tableWidget.setItem(row,7,QTableWidgetItem(str(passFrame)))
                self.ui.labelInfo_tableWidget.resizeColumnToContents(7)
                self.ui.labelInfo_tableWidget.item(row,7).setFlags(self.ui.labelInfo_tableWidget.item(row,7).flags() ^ Qt.ItemIsEditable )
                    
            if not self.isGolden and len(row_data) > 8 and self.ui.labelInfo_tableWidget.columnCount() > 8:  # golden postion
                self.ui.labelInfo_tableWidget.setItem(row,8,QTableWidgetItem(row_data[7]))
                self.ui.labelInfo_tableWidget.resizeColumnToContents(8)
                self.ui.labelInfo_tableWidget.item(row,8).setFlags(self.ui.labelInfo_tableWidget.item(row,8).flags() ^ Qt.ItemIsEditable )
                
                                                 
        else:
            self.ui.labelInfo_tableWidget.item(row,3).setFlags(self.ui.labelInfo_tableWidget.item(row,3).flags() ^ Qt.ItemIsEditable )
            self.ui.labelInfo_tableWidget.item(row,4).setFlags(self.ui.labelInfo_tableWidget.item(row,4).flags() ^ Qt.ItemIsEditable )
        
    def updateSelectLabelInfoPosition(self):
        row = self.ui.labelInfo_tableWidget.currentRow()
        rect = self.ui.showImage_offline_graphicsView.moved_rect
        
        self.ui.labelInfo_tableWidget.item(row,1).setText(f'{round(rect.left()),round(rect.top())}')
        self.ui.labelInfo_tableWidget.item(row,2).setText(f'{round(rect.right()),round(rect.bottom())}')
        self.ui.labelInfo_tableWidget.resizeColumnToContents(1)
        self.ui.labelInfo_tableWidget.resizeColumnToContents(2)

    def trainProcess(self):
        train.show_info_message(self,"AI Model Selector", "Would you like to train as following configuration?")
    
    def on_cancel_clicked(self):
        print("Cancel clicked")                
        self.worker_thread.stop()
        #self.is_running = False    
        
    def editNote(self):
        json_file = os.path.join(projectRoot, self.productNumber, self.projectName,"threshold",f"offset_{self.current_layers}.json")         
        
        editROINote_dialog = EditROINote(self.ui.labelInfo_tableWidget,self.currentImage_offline_golden,self.useOffset, json_file)
        if editROINote_dialog.exec_() == QDialog.Accepted:                         
            if self.ui.labelInfo_tableWidget.columnCount() > 5:
                for row in range(self.ui.labelInfo_tableWidget.rowCount()):
                    self.ui.labelInfo_tableWidget.setItem(row,5,QTableWidgetItem(editROINote_dialog.noteList[row]))
                    self.ui.labelInfo_tableWidget.resizeColumnToContents(5)
                    self.ui.labelInfo_tableWidget.resizeRowsToContents()
                    self.ui.labelInfo_tableWidget.item(row,5).setFlags(self.ui.labelInfo_tableWidget.item(row,5).flags() ^ Qt.ItemIsEditable )
                    
                    self.ui.labelInfo_tableWidget.setItem(row,6,QTableWidgetItem(editROINote_dialog.thresholdList[row]))
                    self.ui.labelInfo_tableWidget.resizeColumnToContents(6)
                    self.ui.labelInfo_tableWidget.item(row,6).setFlags(self.ui.labelInfo_tableWidget.item(row,6).flags() ^ Qt.ItemIsEditable )
                    
                    self.ui.labelInfo_tableWidget.setItem(row,7,QTableWidgetItem(editROINote_dialog.passframeList[row]))
                    self.ui.labelInfo_tableWidget.resizeColumnToContents(7)
                    self.ui.labelInfo_tableWidget.item(row,7).setFlags(self.ui.labelInfo_tableWidget.item(row,7).flags() ^ Qt.ItemIsEditable )
                    
                self.saveLabel()
        
    def getROIcalculateThreshold(self):       
        
        if self.ui.device_offline_comboBox.currentIndex() != 0:            
            self.ui.device_offline_comboBox.setCurrentIndex(0)        
            self.showImageFromTableList(self.ui.showImagelist_tableWidget.currentRow(),self.ui.showImagelist_tableWidget.currentColumn())
                    
        self.resetLabelInfoTable() 
        
        print(self.currentImage_offline)
        if  not hasattr(self,'currentImage_offline') or not os.path.exists(self.currentImage_offline):             
            QMessageBox.warning(self, "No image", "Please select an image.")               
            return
        if not os.path.exists(self.currentImage_offline_golden):
            QMessageBox.warning(self, "No golden image", "Please choose an image in golden mode.")            
            self.ui.goldenmode_checkBox.setChecked(True)                  
            return
        if not os.path.exists(self.currentImage_labelconfig_offline_golden):
            QMessageBox.warning(self, "No golden sop information", "Please set the sop information in golden mode.")                                      
            return
        if not os.path.exists(self.positionFile):
            QMessageBox.warning(self, "No resigistration anchor", "Please set registration anchor points in golden mode.")              
            self.ui.position_pushButton.setFocus()            
            return                            
        
        # call pipeline 
        self.getSOPROIThreshold()                                

        
    def getSOPROIThreshold(self):
        
        type_index = self.settings['type']                          
        nickname = self.settings['training']['type'][type_index]['nickname']
        cmd = str(self.settings['pipeline']['operation'][nickname]['training'])
               
        cmd = cmd.format(self.currentImage_offline, self.currentImage_offline_golden,self.currentImage_labelconfig_offline_golden,self.positionFile)
        print(f'pipeline:\n{cmd}')                
        
        if self.liveSrc:
            self.liveSrc.stop()
            self.liveSrc = None
            
        self.liveSrc = LiveStream(gstcmd=cmd)
        self.liveSrc.newSample.connect(self.parseSOPBufferforThreshold)
        if self.liveSrc: 
            if not self.liveSrc.parseLaunch():
                print('parse failed')
                self.liveSrc = None 
            else:
                if not self.liveSrc.play():
                    self.liveSrc.stop()
                    self.liveSrc = None
            self.liveSrc.stop()
            self.liveSrc = None                    
                
    def parseSOPBufferforThreshold(self,sample):
                                                                
        buffer_data = adroi.gst_buffer_adroi_query(hash(sample.get_buffer()), '//')
        if buffer_data is None or len(buffer_data) == 0:
            print("query is empty from frame meta in get classification.")
            return

        width = self.oriCapturedPixmap.width()
        height = self.oriCapturedPixmap.height()        
                        
        
        for roi in buffer_data[0].rois:                            
            if roi.category == 'box':                       
                for subroi in roi.sub_rois:                    
                    box = subroi.to_box()
                    x1, y1, x2, y2 = box.x1, box.y1, box.x2, box.y2                                                                                                    
                    if (x1,y1,x2,y2) != (0.0,0.0,1.0,1.0):                                                                        
                        if box.events:                                                        
                            if len(box.events) > 0:
                                pos = str(box.events[0])
                                if 'golden position' in pos:
                                    match = re.search(r'\(([^)]+)\)',pos)                            
                                    if match:
                                        golden_pos = match.group(0)                                                                                
                                        correctLabel = self.parseGoldenROILabelName(golden_pos)                            
                                else:
                                    return
                            
                            threshold = default_threshold
                            if len(box.events) > 1:
                                t = str(box.events[1])
                                if 'threshold' in t:
                                    threshold = str(t.split('=')[1])                                                                                                                
                                    
                            data=[correctLabel,
                                  f'({round(x1*width)}, {round(y1*height)})',
                                  f'({round(x2*width)}, {round(y2*height)})',
                                  'Ignore','Ignore',
                                  '',threshold,golden_pos]                            
                            
                            self.addOneRowtoLabelTable(data)                            
                            self.updateLabelROI()                                        

        
###### tab 5, SOP inspection ######
    def update_countdown(self):        
        if self.current_sop_status=='play':
            if self.seconds_left > 0:
                self.seconds_left -= 1
                self.update_label()
            else:            
                self.seconds_time_out +=1                
                self.update_label_timeout()
            
    def update_label(self):              
        self.ui.state_SOP_label.setText(f"{self.seconds_left}s")
        
    def update_label_timeout(self):
        self.ui.state_SOP_label.setStyleSheet("background-color: red; color: white; font-size: 24px;") 
        self.ui.state_SOP_label.setText(f"time out:{self.seconds_time_out}s") 
        if self.sound_thread:
            self.sound_thread.stop()                    
        self.sound_thread = SoundThread("sound/timeout.mp3")
        self.sound_thread.start()           
        
    def getLabelFileToList(self,label_golden):
        if os.path.isfile(label_golden):
            with open(label_golden,"r",encoding='utf-8') as f:
                labelsInfo = f.read().splitlines()
            if labelsInfo:
                return True,labelsInfo
            else:
                return False,"Nothing to note." 
        else:
            return False,"Can not find golden label information!"
        
    def getSOPGoldenParameter(self,layer):
        
        rootPath = os.path.join(projectRoot, self.productNumber, self.projectName)    
        golden_filename = f'golden_{layer}.png'
        golden_labelinfo = f'golden_{layer}.txt'
        golden_anchors = f'anchors_{layer}.txt'

        image_golden = os.path.join(rootPath, "golden", golden_filename)
        label_golden = os.path.join(rootPath, "golden", golden_labelinfo)
        anchors_golden = os.path.join(rootPath, "position", golden_anchors)
        return image_golden,label_golden,anchors_golden

    def switchSOPStateFalg(self,state:str): 
        
        if state.upper() == 'MONITOR':              
            if self.duration_time == -1:
                self.ui.state_SOP_label.setText("MONITOR") 
                self.ui.state_SOP_label.setStyleSheet("background-color: orange; color: white; font-size: 24px;")               
            else:
                if self.current_state != "MONITOR":
                    self.current_state = "MONITOR"
                    self.seconds_left = self.duration_time
                    self.seconds_time_out = 0
                    self.duration_timer.start(1000)
                    self.update_label()
                    self.ui.state_SOP_label.setStyleSheet("background-color: orange; color: white; font-size: 24px;")
            
        elif state.upper() == 'PASS':
            self.duration_timer.stop() 
            self.seconds_time_out = 0
            #self.ui.state_SOP_label.setStyleSheet("background-color: green; color: white; font-size: 24px;")
            #self.ui.state_SOP_label.setText("PASS")            
            self.current_state = "PASS"
            self.duration_time = -1            
            
        elif state.upper() == 'FAIL':
            self.duration_timer.stop() 
            self.seconds_time_out = 0
            self.ui.state_SOP_label.setStyleSheet("background-color: red; color: white; font-size: 24px;")    
            self.ui.state_SOP_label.setText("FAIL")            
            self.current_state = "FAIL"
            self.duration_time = -1
            
        elif state.upper() == 'DONE':
            self.ui.state_SOP_label.setStyleSheet("background-color: green; color: white; font-size: 24px;")
            self.ui.state_SOP_label.setText("ALL PASS")
            self.current_state = "PASS"
               
    def saveOvertimeData(self, layer,order,overtime,duration,image):
        
        data = {'layer':layer, 'step':order, 'overtime': overtime, 'duration':duration, 'image':image}
        
        self.SOPInsepctionOvertimeData.append(data)
        

    def showCurrentROIImageNoteDuration(self,layer:str,golden_roi_pos:str):
        # layer: '1'~
        # order: '1'~
        # golden_roi_pos: '(x1,y1,x2,y2)'
        image_golden,label_golden,_ = self.getSOPGoldenParameter(layer)
        
        if os.path.isfile(image_golden):
            pixmap = self.getROIImage(image_golden,golden_roi_pos)            
            if pixmap.width() > self.ui.Image_SOP_label.width():
                self.ui.Image_SOP_label.setPixmap(pixmap.scaledToWidth(self.ui.Image_SOP_label.width()))                
                #self.ui.Image_SOP_label.setPixmap(pixmap.scaled(self.ui.Image_SOP_label.size(),Qt.KeepAspectRatio))
            elif pixmap.width() < self.ui.Image_SOP_label.width()/5:
                self.ui.Image_SOP_label.setPixmap(pixmap.scaledToWidth(self.ui.Image_SOP_label.width()/8))
            else:
                self.ui.Image_SOP_label.setPixmap(pixmap)                            
            
        else:
            self.ui.Image_SOP_label.setText('Can not find golden image!')
                       
        ret, labelsInfo = self.golden_labelinfo_dict[str(layer)]#self.getGoldenFileToList(label_golden)
        if ret:            
                noteString = self.findNote(golden_roi_pos,labelsInfo)
                self.duration_time = self.findDuration(golden_roi_pos,labelsInfo)
        else:
                noteString = labelsInfo
                self.duration_time = -1
                
               
        self.ui.note_SOP_textBrowser.setText(noteString)
            

        
    def getROIImage(self,imagepath,position:str):
        pixmap = QPixmap(imagepath)
        start_x, start_y, end_x, end_y = map(int, position.strip("()").replace(" ", "").split(','))
        start_x = start_x -50 if start_x > 50 else 0
        start_y = start_y -50 if start_y > 50 else 0
        end_x = end_x + 50 if end_x+50 < pixmap.size().width() else pixmap.size().width()
        end_y = end_y + 50 if end_y+50 < pixmap.size().height() else pixmap.size().height()
        start_point = QtCore.QPoint(start_x,start_y)
        end_point = QtCore.QPoint(end_x,end_y)
        rect = QtCore.QRect(start_point,end_point)
        
        return pixmap.copy(rect)
        
        
    def findNote(self,position:str,labelsInfo:list):
        # position = '(x1,y1,x2,y2)'
        x1,y1,x2,y2 = position.strip("()").replace(" ", "").split(",")
        pattern = rf"\({x1}, {y1}\);\({x2}, {y2}\)"
        
        for data in labelsInfo:
            match = re.search(pattern, data)            
            if match:
                note = eval(data.split(";")[5]).strip("'")                                
                return note
        return None
    
    def findDuration(self,position:str,labelsInfo:list):
        x1,y1,x2,y2 = position.strip("()").replace(" ", "").split(",")
        pattern = rf"\({x1}, {y1}\);\({x2}, {y2}\);.*;(.*?);'.*?'"
        
        for data in labelsInfo:
            match = re.search(pattern, data)
            if match:
                duration = match.group(1)
                if str(duration).lower() == 'ignore':
                    return -1
                else:
                    return int(duration)
        return -1
        
    def updateSOPStateInfo(self,order:str,state:str):        
        
        timestamp = time.strftime("[%Y-%m-%d %H:%M:%S]", time.localtime())
        new_state = f'{timestamp} Step {order}: {state}'        
                        
        self.ui.stateInfo_SOP_textBrowser.clear()        
        if state.upper() == 'MONITOR':   
            new_state = f'{timestamp} Step {order}: <span style="color: orange;">{state}</span>'                                    
            self.ui.stateInfo_SOP_textBrowser.append("<br>".join(self.sop_state))
            self.ui.stateInfo_SOP_textBrowser.append(new_state)            
            self.monitor_step = order
            
        elif state.upper() == 'FAIL':   
            if self.sound_thread:
                self.sound_thread.stop()
                self.sound_thread.join()
            self.sound_thread = SoundThread("sound/fail.mp3")
            self.sound_thread.start()
            
            dt = datetime.strptime(timestamp.strip("[]"), "%Y-%m-%d %H:%M:%S")
            self.current_fail_timestamp = dt.strftime("%Y%m%d%H%M%S")
            new_state = f'{timestamp} Step {order}: <span style="color: red;">{state}</span>'                                    
            self.ui.stateInfo_SOP_textBrowser.append("<br>".join(self.sop_state))
            self.ui.stateInfo_SOP_textBrowser.append(new_state)    
            self.sop_state.append(new_state)                     
            self.saveCurrentImage(self.current_insepct_layer,order,state.upper())                        
            
        elif state.upper() == 'PASS': 
            if self.sound_thread:
                self.sound_thread.stop()             
                self.sound_thread.join()       
            self.sound_thread = SoundThread("sound/pass.mp3")
            self.sound_thread.start()
            
            if self.seconds_time_out==0:
                new_state = f'{timestamp} Step {order}: <span style="color: green;">{state}</span>'
                self.saveCurrentImage(self.current_insepct_layer,order,state.upper())                
            else:
                new_state = f'{timestamp} Step {order}: <span style="color: red;">Over time</span>, {self.seconds_time_out}s'                                                               
                self.saveCurrentImage(self.current_insepct_layer,order,'OVERTIME')     
                self.saveOvertimeData(self.current_insepct_layer,order,self.seconds_time_out,self.duration_time,self.lastpixmap)
                                                     
            self.ui.stateInfo_SOP_textBrowser.append("<br>".join(self.sop_state))        
            self.ui.stateInfo_SOP_textBrowser.append(new_state)
            self.sop_state.append(new_state)          
                        
            
    

    def updateCurrentLayerToStateInfo(self,layer:str):                  
        if self.current_insepct_layer != int(layer):
            self.ui.stateInfo_SOP_textBrowser.clear()       
            self.current_insepct_layer = int(layer)            
            string = f'<span style="color: blue;">Layer: {layer}</span>'            
            self.ui.stateInfo_SOP_textBrowser.append("<br>".join(self.sop_state))
            self.ui.stateInfo_SOP_textBrowser.append(string)
            self.sop_state.append(string)
            
            
    def saveCurrentImage(self,layerNo,stepNo:str, ret_state:str):
                
        #PASS
        # GO log: \\{IP}\FT_Report\AVI_log\{專案資料夾}\Level\Product_Code\Version\PASS\{SN}_{SWPN}_{LayerNo}_{StepNo}.png
        # ========> ~/SOPLog/LevelProduct_Code/Version/PASS/{imagefile}
        # ========> self.PN_sop_log\PASS\{imagefile}
        # sw log: ~AAI\PN\SWProjectName\sop_log\{timestamp}\PASS\{imagefile}
        # ========> self.sw_sop_log\{timestamp}\PASS\{imagefile}
        
        #FAIL
        # GO log: \\{IP}\FT_Report\AVI_log\{專案資料夾}\Level\Product_Code\Version\PASS\{SN}_{Timestamp}_{SWPN}_{LayerNo}_{StepNo}.png
        # ========> ~/SOPLog/LevelProduct_Code/Version/FAIL/{imagefile}
        # ========> self.PN_sop_log\FAIL\{imagefile}
        # sw log: ~AAI\PN\SWProjectName\sop_log\{timestamp}\FAIL\{imagefile}
        # ========> self.sw_sop_log\{timestamp}\FAIL\{imagefile}
        
        #OVERTIME      
        # GO LOG:
        #   PASS: \\{IP}\FT_Report\AVI_log\{專案資料夾}\Level\Product_Code\Version\PASS\{SN}_{SWPN}_{LayerNo}_{StepNo}_OVERTIME.png
        #   FAIL: \\{IP}\FT_Report\AVI_log\{專案資料夾}\Level\Product_Code\Version\PASS\{SN}_{Timestamp}_{SWPN}_{LayerNo}_{StepNo}_OVERTIME.png
        # 
        # sw log: ~AAI\PN\SWProjectName\sop_log\{timestamp}\OVERTIME\{imagefile}
        # ========> self.sw_sop_log\{timestamp}\OVERTIME\{imagefile}
        
        SN = self.ui.sn_SOP_lineEdit.text()
        self.make_dir(os.path.join(self.sw_sop_log,self.current_timestamp,ret_state))
        path = None       
        image = QPixmap(self.liveSrc.oriImage) 
        
        if ret_state == 'PASS':
            image_filename = f"{SN}_{self.projectName}_{layerNo}_{stepNo}.png"
            path = os.path.join(self.sw_sop_log,self.current_timestamp,'PASS',image_filename)
        
        elif ret_state == 'FAIL':  # FAIL format: SN_timeStamp            
            image_filename = f"{SN}_{self.current_fail_timestamp}_{self.projectName}_{layerNo}_{stepNo}.png"
            path = os.path.join(self.sw_sop_log,self.current_timestamp,'FAIL',image_filename)                        
        
        elif ret_state == 'OVERTIME':            
            image_filename = f"{SN}_{self.projectName}_{layerNo}_{stepNo}_OVERTIME.png"            
            path = os.path.join(self.sw_sop_log,self.current_timestamp,'OVERTIME',image_filename)                    
        
        if path:
            #self.liveSrc.oriImage.save(path,format='PNG')          
            #image = QPixmap(self.liveSrc.oriImage)
            
            self.saveimage_thread = SaveImageThread(image, path)            
            self.saveimage_thread.start()
            self.lastpixmap = image
              
                                        
            
    def saveCurrentMonitorImage(self):        

        
        self.make_dir(os.path.join(self.sw_sop_log,self.current_timestamp,'FAIL'))
        image_filename = f"{self.ui.sn_SOP_lineEdit.text()}_{self.current_timestamp}_{self.projectName}_{self.current_insepct_layer}_{self.monitor_step}.png"
        path = os.path.join(self.sw_sop_log,self.current_timestamp,'FAIL',image_filename)
        
        self.liveSrc.oriImage.save(path,format='PNG')
        self.lastpixmap = QPixmap(path)               
        
        if self.seconds_time_out > 0:
            self.saveOvertimeData(self.current_insepct_layer,self.monitor_step,self.seconds_time_out,self.duration_time,self.lastpixmap)
        else:
            self.saveOvertimeData(self.current_insepct_layer,self.monitor_step,0,0,self.lastpixmap)            
        
                                      
            
    def saveSOPLog(self,state):
        # \\{IP}\FT_Report\AVI_log\{專案資料夾}\Level\Product_Code\Version\record\{SN}_{SWPN}_{Timestamp}.log
        # =====> self.PN_sop_log\record\{filename}
        # sw log: ~AAI\PN\SWProject\sop_log\{timestamp}\record\{SN}_{SWPN}_{Timestamp}.log
        # =====> self.sw_sop_log\{timestamp}\record\{SN}_{SWPN}_{Timestamp}.log
        self.pauseSOP()        
        
        log_dir = os.path.join(self.PN_sop_log,'record')
        self.make_dir(log_dir)
        
        sw_log_dir = os.path.join(self.sw_sop_log,self.current_timestamp,'record')
        self.make_dir(sw_log_dir)
        
        SN = self.ui.sn_SOP_lineEdit.text()
        log_filename = f'{SN}_{self.projectName}_{self.current_timestamp}.log'
        sw_log_path = os.path.join(sw_log_dir,log_filename)    
                
        # ==== SOP LOG ====
        # User: 
        # Serial Number: 
        # Product Number: 
        # Start Time:    
        # Resutl: PASS/FAIL
        # State Information:
        # ---
        # Layer (x)
        # [time] step (y) : PASS/FAIL/OVERTIME (n)s
        # ---
        dt = datetime.strptime(self.current_timestamp, "%Y%m%d%H%M%S")
        start_time = dt.strftime("%Y-%m-%d %H:%M:%S")

        
        with open(sw_log_path, 'w', encoding='utf-8') as file:
            file.write(f'User: {self.username}\n')
            file.write(f'Serial Number: {SN}\n')
            file.write(f'Product Number: {self.productNumber}\n')            
            file.write(f'Start Time: {start_time}\n')
            if state == 'DONE':
                file.write('Result: ALL PASS\n')
            elif state == 'FAIL':
                file.write('Result: FAIL\n')
            elif state == 'Terminate':
                file.write('Reuslt: Terminate\n')
            file.write('\nState Information:\n---\n')
            file.write(self.ui.stateInfo_SOP_textBrowser.toPlainText())
            file.write('\n---\n')
            
            ## TBD: ADD OVERTIME LOG TEXT
            #data = {'layer':layer, 'step':order, 'overtime': overtime, 'duration':duration, 'image':image}
            #self.SOPInsepctionOvertimeData[i]['errorCodeList']
            if self.SOPInsepctionOvertimeData:
                file.write('\n======================================\n')
                file.write('Overtime Error Root Cause\n---')
                for i in range(len(self.SOPInsepctionOvertimeData)):    
                    data = self.SOPInsepctionOvertimeData[i]
                    layer = data['layer']
                    step = data['step']
                    overtime = data['overtime']
                    duration = data['duration']
                    errorCodeList = str(data['errorCodeList']).replace('\n','\n  ')
                                        
                    file.write(f'\nLayer:{layer}, Step:{step}\n')
                    file.write(f'Overtime: {overtime}s\n')
                    file.write(f'Setup time: {duration}s\n')
                    file.write(f'Root Case:\n  {errorCodeList}\n')                
                    
                    file.write('---\n')
                file.write('======================================\n')
        shutil.copytree(sw_log_dir,log_dir,dirs_exist_ok=True)
                                        
        
        # move sw log to GO log
        # DONE => all PASS
        # 1. copy PASS images:  (self.sw_sop_log\{timestamp}\PASS) to (self.PN_sop_log\PASS)
        # 2. copy OVERTIME images (self.sw_sop_log\{timestamp}\OVERTIME) to (self.PN_sop_log\PASS)
        # 3. (new) copy FAIL images (self.sw_sop_log\{timestamp}\FAIL) to self.PN_sop_log\FAIL
        # FAIL => copy FAIL and OVERTIME
        # 1. copy FAIL image (self.sw_sop_log\{timestamp}\FAIL) to self.PN_sop_log\FAIL
        # 2. rename OVERTIME images to {SN}_{Timestamp}_{SWPN}_{LayerNo}_{StepNo}_OVERTIME.png  (Add timestamp after SN before SWPN)
        # 3. copy OVERTIME images (self.sw_sop_log\{timestamp}\OVERTIME) to (self.PN_sop_log\FAIL)    
        # Terminate => copy FAIL and OVERTIME
        # 1. copy FAIL image (self.sw_sop_log\{timestamp}\FAIL) to self.PN_sop_log\FAIL
        # 2. rename OVERTIME images to {SN}_{Timestamp}_{SWPN}_{LayerNo}_{StepNo}_OVERTIME.png  (Add timestamp after SN before SWPN)
        # 3. copy OVERTIME images (self.sw_sop_log\{timestamp}\OVERTIME) to (self.PN_sop_log\FAIL)    
        pass_dir = os.path.join(self.sw_sop_log,self.current_timestamp,'PASS')
        overtime_dir = os.path.join(self.sw_sop_log,self.current_timestamp,'OVERTIME')
        fail_dir = os.path.join(self.sw_sop_log,self.current_timestamp,'FAIL')
        if state == 'DONE':
            if os.path.exists(pass_dir):
                shutil.copytree(pass_dir,os.path.join(self.PN_sop_log,'PASS'),dirs_exist_ok=True)            
            if os.path.exists(overtime_dir):
                shutil.copytree(overtime_dir,os.path.join(self.PN_sop_log,'PASS'),dirs_exist_ok=True)
            if os.path.exists(fail_dir):
                shutil.copytree(fail_dir,os.path.join(self.PN_sop_log,'FAIL'),dirs_exist_ok=True)
            
            if self.sound_thread:
                self.sound_thread.stop()         
                self.sound_thread.join()            
            self.sound_thread = SoundThread("sound/done.mp3")
            self.sound_thread.start()   
                                    
            self.ui.statusbar.showMessage('Inspection PASS! Clear after 3 seconds') 
            QtCore.QTimer.singleShot(3000,self.stopSOP)            
        
        elif state == 'FAIL':
            if os.path.exists(fail_dir):
                shutil.copytree(fail_dir,os.path.join(self.PN_sop_log,'FAIL'),dirs_exist_ok=True)
            if os.path.exists(overtime_dir):
                self.renameOVERTIMEImage(overtime_dir)
                shutil.copytree(overtime_dir,os.path.join(self.PN_sop_log,'FAIL'),dirs_exist_ok=True)                

            self.ui.statusbar.showMessage('Inspection FAIL')                         
            QtCore.QTimer.singleShot(0,self.stopFailSOP)
            
        elif state == 'Terminate':
            if os.path.exists(fail_dir):
                shutil.copytree(fail_dir,os.path.join(self.PN_sop_log,'FAIL'),dirs_exist_ok=True)
            if os.path.exists(overtime_dir):
                self.renameOVERTIMEImage(overtime_dir)
                shutil.copytree(overtime_dir,os.path.join(self.PN_sop_log,'FAIL'),dirs_exist_ok=True)
                
            self.ui.statusbar.showMessage('Inspection Terminate!')                         
            QtCore.QTimer.singleShot(0,self.stopFailSOP)
        
        # keepLog = false, remove sw log        
        if not self.keepLog:
            print(f'remove sw log.\n Folder:{self.sw_sop_log}/{self.current_timestamp}')
            shutil.rmtree(os.path.join(self.sw_sop_log,self.current_timestamp))
            
        
        
    def renameOVERTIMEImage(self,overtime_dir):
        for filename in os.listdir(overtime_dir):
            if filename.endswith('_OVERTIME.png'):
                parts = filename.split('_')
                if len(parts) == 5:
                    new_filename = f'{parts[0]}_{self.current_timestamp}_{parts[1]}_{parts[2]}_{parts[3]}_{parts[4]}'                    
                    os.rename(os.path.join(overtime_dir,filename),os.path.join(overtime_dir,new_filename))
                    

    def parseBuffer(self,sample,graphics):
        
        graphics.clearall()
        graphics.m_scene.clear()  
        
        image_data = sample_to_numpy(sample)
        fmt = get_sample_format(sample)     
        if not self.liveSrc:
            return
        self.liveSrc.setImage(image_data, fmt)
        self.update_view_operation(self.liveSrc.oriImage,graphics)
        
        
        buffer_data = adroi.gst_buffer_adroi_query(hash(sample.get_buffer()), '//')
        if buffer_data is None or len(buffer_data) == 0:
            print("query is empty from frame meta in get classification.")
            return

                        
        for roi in buffer_data[0].rois:    
            if roi.category == 'box':
                for subroi in roi.sub_rois:
                    box = subroi.to_box()
                    
                    x1, y1, x2, y2 = box.x1, box.y1, box.x2, box.y2                    
                    if (x1,y1,x2,y2) == (0.0,0.0,1.0,1.0):
                                                                      
                        if len(box.events):             
                            if box.id == 'inspection':               
                                layer = box.events[0]           # current layer (string)('1','2','3'...)
                                order = box.events[1]           # current order (string)('1','2','3'...)
                                golden_roi_pos = box.events[2]  # Golden, ROI position (string)('(x1,y1,x2,y2)')
                                state = box.events[3]           # current state, PASS or FAIL
                                                                                        
                                self.showCurrentROIImageNoteDuration(layer,golden_roi_pos)
                                self.updateCurrentLayerToStateInfo(layer)
                                self.updateSOPStateInfo(order,state)         
                                self.switchSOPStateFalg(state)         
                                if state == 'FAIL':
                                    self.fail_order = int(order)
                                    self.TerminateSOPInspection('FAIL')                                    
                            elif box.id == 'DONE':   # mean all PASS   
                                self.TerminateSOPInspection(box.id)                           
                                self.switchSOPStateFalg(box.id)
                                
                                
    def cleanSOP(self):        
        self.duration_time = -1
        self.seconds_time_out = 0
        self.seconds_left = 0
        self.ui.Image_SOP_label.clear()
        self.ui.note_SOP_textBrowser.clear()
        self.ui.state_SOP_label.setText('')
        self.ui.stateInfo_SOP_textBrowser.clear()
        self.current_state = 'PASS'
        
        
    def startSOP(self):   
        
        self.cleanSOP()    
               
        self.SOPInsepctionOvertimeData = []        
        self.current_sop_status = None
        self.removeBoxFile()
        self.sop_state = []
        self.current_insepct_layer = 0
        
        if self.liveSrc:
            self.liveSrc.stop()
            self.liveSrc = None
                    
        self.settings = self.getCurrentProjectJson()  # for update pipeline cmd        
        
        ## getting golden info once
        layers = int(self.settings['layers'])
        self.golden_labelinfo_dict = {}
        for i in range(1,layers+1):
            _,label_golden,_ = self.getSOPGoldenParameter(str(i))
            ret, labelinfos = self.getLabelFileToList(label_golden)
            self.golden_labelinfo_dict[f'{i}'] = (ret,labelinfos)                    
                
        type_index = self.settings['type']                          
        nickname = self.settings['training']['type'][type_index]['nickname']

        rootPath = os.path.join(projectRoot, self.productNumber, self.projectName)                    
        image_golden = os.path.join(rootPath, "golden")
        label_golden = os.path.join(rootPath, "golden")
        anchors_golden = os.path.join(rootPath, "position")

        if 'inspection' in self.settings.keys():
            useTestVideo = self.settings['inspection']['useTestVideo']        
        else:
            useTestVideo = False    
        
        if self.userType == userType.Admin and useTestVideo:
            testVideofilePath = self.settings['inspection']['filePath']
            print(testVideofilePath)
            if mimetypes.guess_type(testVideofilePath)[0] != "video/mp4":
                QMessageBox.warning(self,'Warning','Please select a mp4 video file.')
                self.ui.testVideo_filePath_lineEdit.setFocus()
                return            
            if self.useOffset:
                cmd = str(self.settings['pipeline']['operation'][nickname]['offsetTestVideo'])
            else:
                cmd = str(self.settings['pipeline']['operation'][nickname]['testVideo'])
            cmd = cmd.format(testVideofilePath,image_golden,label_golden,anchors_golden)
        else:
            if self.useOffset:
                cmd = str(self.settings['pipeline']['operation'][nickname]['offsetInsepction'])
            else:
                cmd = str(self.settings['pipeline']['operation'][nickname]['inspection'])
            cmd = cmd.format(image_golden,label_golden,anchors_golden)
                
        print(f'\npipeline:\n{cmd}\n')
        self.restartFail_cmd = cmd

        if 'keep_log' in self.settings.keys():                    
            self.keepLog = self.settings['keep_log'] 
        else:
            self.keepLog = False
        
        graphics = self.ui.showImage_SOP_graphicsView
        self.liveSrc = LiveStream(gstcmd=cmd)
        self.liveSrc.newSample.connect(lambda sample:self.parseBuffer(sample,graphics))                
        if self.liveSrc:                    
           self.liveSrc.graphics =  self.ui.showImage_SOP_graphicsView
           if not self.liveSrc.parseLaunch():
                print('parse failed')
                self.liveSrc = None                             
                self.launchparsed = False
                self.scaleOnce = True
                self.ui.statusbar.showMessage('Failed to launch the pipeline, please confirm the envirionment!',timeout=5000)                
                QMessageBox.critical(self, "Warning", "Cannot launch the stream, please contact the technical staff!")
           else:
                self.launchparsed = True
                self.ui.start_SOP_pushButton.setEnabled(False)        
                self.ui.play_SOP_pushButton.setEnabled(True)
                self.ui.pause_SOP_pushButton.setEnabled(False)
                self.ui.stop_SOP_pushButton.setEnabled(True)
                self.ui.statusbar.showMessage('Current Status: Launched the pipeline, please click "Play" to start')                    
                self.ui.play_SOP_pushButton.setFocus() 
                self.current_sop_status = 'start'
                if self.userType != userType.Admin:
                    self.playSOP()
    
    def playSOP(self):
        self.ui.start_SOP_pushButton.setEnabled(False)        
        
        self.ui.play_SOP_pushButton.setEnabled(False)
        self.ui.pause_SOP_pushButton.setEnabled(True)
        self.ui.stop_SOP_pushButton.setEnabled(True)
        
        if self.liveSrc and self.launchparsed:
            if not self.liveSrc.play():                    
                self.ui.statusbar.showMessage('Failed to start the pipeline, please confirm the envirionment!',timeout=5000)                    
                self.liveSrc.stop()
                self.liveSrc = None     
                self.current_sop_status = 'stop'                                                            
            else:
                if self.current_sop_status == 'start':
                    # create timestamp folder
                    rootPath = os.path.join(projectRoot, self.productNumber, self.projectName)                    
                    self.current_timestamp = time.strftime("%Y%m%d%H%M%S", time.localtime()) 
                    self.current_log_path = os.path.join(rootPath,'sop_log',self.current_timestamp)
                    self.make_dir(os.path.join(rootPath,'sop_log',self.current_log_path))
                self.ui.statusbar.showMessage('Current Status: Playing live stream.')                                                
                self.current_sop_status = 'play'
                
                self.ui.terminate_pushButton.setEnabled(True)
                
                if self.userType == userType.Admin:
                    self.ui.pause_SOP_pushButton.setFocus() 
                else:                    
                    self.ui.terminate_pushButton.setFocus()                 
        
    def pauseSOP(self):
        self.ui.start_SOP_pushButton.setEnabled(False)        
        
        self.ui.play_SOP_pushButton.setEnabled(True)
        self.ui.pause_SOP_pushButton.setEnabled(False)
        self.ui.stop_SOP_pushButton.setEnabled(True)
        
        if self.liveSrc:            
            self.liveSrc.pause()                        
            self.ui.statusbar.showMessage('Current Status: Paused live stream.')  
            self.ui.play_SOP_pushButton.setFocus()   
            self.current_sop_status = 'pause'
    
    def restartSOP(self):                        
        self.current_insepct_layer = 0                              
        # stop live src
        
        if self.liveSrc:  
            self.liveSrc.stop()   
            self.liveSrc = None       
            self.scaleOnce = True
            self.ui.sn_SOP_lineEdit.setFocus()
        
        self.duration_timer.stop()
        
        if self.sound_thread:
            self.sound_thread.stop()
            self.sound_thread = None  
            
        self.cleanSOP()
        self.restartFail_removeBoxFile()                                         
        
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        new_state = f'<b>Restart Time: {timestamp} </b><br>---'
        self.ui.stateInfo_SOP_textBrowser.append("<br>".join(self.sop_state))
        self.ui.stateInfo_SOP_textBrowser.append(new_state)
        self.sop_state.append(new_state)                
        
        
        graphics = self.ui.showImage_SOP_graphicsView
        self.liveSrc = LiveStream(gstcmd=self.restartFail_cmd)
        self.liveSrc.newSample.connect(lambda sample:self.parseBuffer(sample,graphics))                
        if self.liveSrc:                    
           self.liveSrc.graphics =  self.ui.showImage_SOP_graphicsView
           if not self.liveSrc.parseLaunch():
                print('parse failed')
                self.liveSrc = None                             
                self.launchparsed = False
                self.scaleOnce = True
                self.ui.statusbar.showMessage('Failed to launch the pipeline, please confirm the envirionment!',timeout=5000)                
                QMessageBox.critical(self, "Warning", "Cannot launch the stream, please contact the technical staff!")
           else:
                self.launchparsed = True
                self.ui.start_SOP_pushButton.setEnabled(False)        
                self.ui.play_SOP_pushButton.setEnabled(True)
                self.ui.pause_SOP_pushButton.setEnabled(False)
                self.ui.stop_SOP_pushButton.setEnabled(True)
                self.ui.statusbar.showMessage('Current Status: Launched the pipeline, please click "Play" to start')                    
                self.ui.play_SOP_pushButton.setFocus() 
                self.current_sop_status = 'restart'
                self.playSOP()
        
    def stopSOP(self):
        self.ui.sn_SOP_lineEdit.clear()
        self.ui.start_SOP_pushButton.setEnabled(False)        
        
        self.ui.play_SOP_pushButton.setEnabled(False)
        self.ui.pause_SOP_pushButton.setEnabled(False)
        self.ui.stop_SOP_pushButton.setEnabled(False)
                
        if self.liveSrc:            
            self.liveSrc.stop()
            self.liveSrc = None
            self.ui.statusbar.showMessage('Current Status: Stopped live stream.')                
            self.scaleOnce = True
            self.ui.sn_SOP_lineEdit.setFocus()
            self.current_sop_status = 'stop'
        
        self.duration_timer.stop()
        
        self.cleanSOP()
        
        self.removeBoxFile()                
        
        if self.sound_thread:
            self.sound_thread.stop()
            self.sound_thread = None    
            
        self.ui.terminate_pushButton.setEnabled(False)
        
    def stopFailSOP(self):
                
        self.ui.sn_SOP_lineEdit.clear()
        self.ui.start_SOP_pushButton.setEnabled(False)        
        
        self.ui.play_SOP_pushButton.setEnabled(False)
        self.ui.pause_SOP_pushButton.setEnabled(False)
        self.ui.stop_SOP_pushButton.setEnabled(False)
                
        if self.liveSrc:            
            #self.liveSrc.stop()
            #self.liveSrc = None
            #self.ui.statusbar.showMessage('Current Status: Fail step occurred.')                
            self.scaleOnce = True
            self.ui.sn_SOP_lineEdit.setFocus()            
        
        self.duration_timer.stop()
        
        self.removeBoxFile()                
                
        
        QtCore.QTimer.singleShot(1000,self.setFailImage)
        self.ui.terminate_pushButton.setEnabled(False)
            
        
    def setFailImage(self):        
        self.ui.showImage_SOP_graphicsView.set_image(self.lastpixmap)
    
    def removeBoxFile(self):
        
        filelist = ['current_box.txt','adalign_frame_max_tracking.json','adalign_frame_tracking.json', 'current_layer.txt','layer_files.pkl']
        
        for file in filelist:
            if os.path.exists(file):
                try:
                    os.remove(file)                            
                except PermissionError:
                    print(f"[Error] Can not delete {file}. Permision issue.")
                except Exception as e:
                    print(f"[Error] Delete {file} failed. {e}")
                    
    def restartFail_removeBoxFile(self):
        
        filelist = ['current_box.txt','adalign_frame_max_tracking.json','adalign_frame_tracking.json']
        
        for file in filelist:
            if os.path.exists(file):
                try:
                    os.remove(file)                            
                except PermissionError:
                    print(f"[Error] Can not delete {file}. Permision issue.")
                except Exception as e:
                    print(f"[Error] Delete {file} failed. {e}")                            
        
        with open('current_box.txt', 'w', encoding='utf-8') as file:
            file.write(str(self.fail_order-1))
                    
    def TerminateSOPInspection(self,state):
        errorCodetable = getErrorCodeTable()        
        self.pauseSOP()        
        isContinue = False
        if state == 'Terminate':
            self.saveCurrentMonitorImage()
            self.ui.state_SOP_label.setText("TERMINATE")         
        elif state == 'FAIL':                                    
            correctErrorStep_dialog = ErrorStepDialog()
            if correctErrorStep_dialog.exec_() == QDialog.Accepted:
                isContinue = correctErrorStep_dialog.isContinue
        
        if isContinue:
            print('restart inspecting from fail step')            
                        
            self.ui.stateInfo_SOP_textBrowser.clear()                           
            self.ui.stateInfo_SOP_textBrowser.append("<br>".join(self.sop_state))
            self.ui.stateInfo_SOP_textBrowser.append('---<br>')    
            self.sop_state.append('---<br>')
                                  
            self.restartSOP()          
        else:
            if self.SOPInsepctionOvertimeData:                
                total = len(self.SOPInsepctionOvertimeData)                        
                for i in range(total):                                        
                    overtimeData =  self.SOPInsepctionOvertimeData[i]
                    dialog = OvertimeErrorCodeDialog(errorCodetable,overtimeData,self.username,i+1,total)
                            
                    if dialog.exec_() == QDialog.Accepted:                    
                        self.SOPInsepctionOvertimeData[i]['errorCodeList'] = dialog.errorCodeList                                    
                
            self.saveSOPLog(state)
    
    
if __name__ == "__main__":
    Gst.init([])
    
    app = QApplication([])
    
    app.installTranslator(TRANSLATOR)
    
    parser = argparse.ArgumentParser(description="Login by args")
    parser.add_argument("-j", "--projectname", type=str, help="Enter the project name")
    parser.add_argument("-t", "--usertype", type=int, default=2, help="<0>:admin; <1>:trainer; <2>:operator")
    parser.add_argument("-u", "--user", type=str, default='', help="Enter user")
    parser.add_argument("-p", "--password", type=str, help="If user type is Adminsitrator, enter the password.")        
    parser.add_argument("-n", "--newproject", type=bool, default=False, help="<True>:Create a new project; <False>: Use an exist project")
    parser.add_argument("-f", "--fullscreen", type=bool, default=False, help="<True>:Show full screen; <False>:Show windows screen.")
    
    args = parser.parse_args()  
    
    if args.projectname:
        
        projectName = args.projectname
        
        if args.usertype == 0 :
            usertype = userType.Admin
            print('Current user type is "Administrator".')
        elif args.usertype == 1:
            usertype = userType.Trainer
            print('Current user type is "Trainer".')
        elif args.usertype == 2:
            usertype = userType.Operator
            print('Current user type is "Opertator".')
        else:            
            print('[ERROR] Please enter correct user type')
            sys.exit()
            
        if usertype == userType.Admin:            
            if args.user == adminuser and args.password == adminpw:
                username = args.user
                password = args.password
            else:                
                print('[ERROR] Please enter the correct user name and password.')
                sys.exit()
        else:            
            username = args.user
            if usertype == userType.Operator:
                if username == '':                    
                    print('[ERROR] Please enter the user name.')
                    sys.exit()
                    
        newProject = args.newproject
        fullScreen = args.fullscreen
        
    else:                    
        login_dialog = LoginDialog()
        if login_dialog.exec_() == QDialog.Accepted:
            username = login_dialog.username
            projectName = login_dialog.projectName
            usertype = login_dialog.usertype
            newProject = login_dialog.newProject
            fullScreen = login_dialog.fullScreen
        else:
            sys.exit()
            
    #main_window = MainWindow(login_dialog.username,login_dialog.projectName ,login_dialog.usertype,login_dialog.newProject)
    main_window = MainWindow(username,projectName ,usertype,newProject,fullScreen)
    main_window.show()
    app.exec_()
