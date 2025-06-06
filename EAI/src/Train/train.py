from PySide2.QtWidgets import QApplication, QMainWindow,QFileDialog,QLabel \
                              ,QTableWidgetItem,QDialog,QMessageBox, QStatusBar \
                              ,QActionGroup,QAction \
                              ,QPushButton,QProgressDialog
from PySide2.QtCore import Qt, QTimer
from PySide2.QtCore import Qt, QThread, QTimer, Signal
from PySide2.QtCore import Qt, Slot
from PySide2.QtGui import QMovie
import os
import requests
import json

#Defince the api name
API_TRAIN_DUAL_IN_LINE_PACKAGE_INSPECTION = "/train/DualInLinePackageInspection"
API_TRAIN_ANOMALY_DETECTION = "/train/AnomalyDetection"
setting_config = None

class AnimatedDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.resize(100, 100)
        self.setWindowFlags(Qt.FramelessWindowHint) 
        self.setStyleSheet("background: transparent;")
        self.setWindowOpacity(0)  
        self.label_animation = QLabel(self)
        self.label_animation.setGeometry(50, 50, 200, 200)

        relative_path = os.path.join(os.path.dirname(__file__), "gif", "loading.gif")
        self.movie = QMovie(relative_path)
        self.label_animation.setMovie(self.movie)
        self.movie.start()

def read_server_config(config_file):
    # try:
    #     with open(config_file, 'r') as f:
    #         config = json.load(f)
    #         server_ip = config['server']['ip']
    #         server_port = config['server']['port']
    #         api_list = config['api']
    #         return server_ip, server_port, api_list
    # except FileNotFoundError:
    #     print(f"Config file '{config_file}' not found.")
    #     return None, None
    # except KeyError:
    #     print("Invalid JSON format or missing required fields.")
    #     return None, None
    
    if config_file:
        server_ip = config_file['training']['server']['ip']
        server_port = config_file['training']['server']['port']
        api_list = config_file['training']['type']
        return server_ip, server_port, api_list
    else:
        print("Please confirm the project's config file")
        return None, None, None

class WorkerThread(QThread):
    update_progress = Signal(int)
    set_range = Signal(int, int)
    set_button = Signal(QPushButton )

    def __init__(self, projName=None,productNum=""):
        super().__init__()
        self.is_running = True
        self.projName = projName
        self.productNum = productNum

    def run(self):
        count = 0
        while self.is_running: 
            #self.update_progress.emit(count)
            result = get_train_status()
            count += 10
            if result:
                print(f"status: {result['code']}")
                print(f"code: {result['message']}")
                if result['code'] == 0:
                    self.msleep(500)
                elif result['code'] == 1:
                    self.set_range.emit(1,100)
                    self.set_button.emit(None)
                    for i in range(0, 101, 10):
                        self.update_progress.emit(i)
                        self.msleep(250)
                    self.is_running = False
            else:
                print("can not get response")
            #print(count)
            '''if(count >= 25):
                self.set_range.emit(1,100)
                #count = 0
                self.update_progress.emit(count)
            if(count >100):
                self.update_progress.emit(100)
                self.is_running = False'''
            self.msleep(250)
        self.finished.emit()

    def stop(self):
        self.is_running = False
        #print(self.is_running)  

def show_info_message(self,title, message):
    app = QApplication.instance()
    if app is None:
        app = QApplication([])

    msg_box = QMessageBox()
    msg_box.setWindowTitle(title)
    msg_box.setText(message)

    # Center the message box relative to the parent window
    msg_box.setGeometry(
        self.geometry().center().x() - msg_box.sizeHint().width() // 2,
        self.geometry().center().y() - msg_box.sizeHint().height() // 2,
        msg_box.sizeHint().width(),
            msg_box.sizeHint().height()
    )

    msg_box.setStandardButtons(QMessageBox.Abort | QMessageBox.Ok)
    result = msg_box.exec()
    
    global setting_config
    setting_config = self.settings
    
    if result == QMessageBox.Ok:
       
        self.worker_thread = WorkerThread(projName=setting_config['projectName'], productNum=setting_config['productNumber'])
        
        index = setting_config['type']
        #Get api category (TBD)
        rest_api_name, api_index, export_nv_engine, path, project, projectNum, epochNum  = get_api_name(index)
        print(rest_api_name)
        if rest_api_name == API_TRAIN_DUAL_IN_LINE_PACKAGE_INSPECTION:
           if export_nv_engine is not None:
                # self.projectPath , self.projName, self.projName'
                result = start_dual_inline_package_inspection(self, path, project, projectNum, export_nv_engine, epochNum)
        else:
            show_error_message(self, "Information", f"Error: {rest_api_name} is not supported.")
            result = None

        if result:
            print(f"status: {result['code']}")
            print(f"message: {result['message']}")
            on_training_started(self, result['code'], result['message'], rest_api_name)
        else:
            print("train error")
        #show_progress_dialog(self)

def show_error_message(self, title, message):
        msg_box = QMessageBox(self)
        msg_box.setIcon(QMessageBox.Icon.Warning)
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
        msg_box.exec()

def get_api_name(index):
    #sysconfig = os.path.join('config', 'system.json')
    
    server_ip, server_port, api_list = read_server_config(setting_config)
    project = setting_config['projectName']
    productNum = setting_config['productNumber']    
    if api_list and len(api_list) > index:
        api_info = api_list[index]
        api_name = api_info['name']
        api_index = api_info['index']
        export_nv_engine = None
        if 'parm' in api_info and len(api_info['parm']) > 0 and 'exportNVEngine' in api_info['parm'][0]:
            export_nv_engine = api_info['parm'][0]['exportNVEngine']
            trainingDataPath = api_info['parm'][0]['trainingDataPath']            
            epochNum = api_info['parm'][0]['epoch']
        return api_name, api_index, export_nv_engine, trainingDataPath , project, productNum, epochNum
    else:
        return None, None, None, None , None
    '''if api_list and len(api_list) > 0:
        return api_list[index]['name'] , api_list[index]['index']
    else:
        return None'''

def show_progress_dialog(self, dialog_title):
    progress_dialog = QProgressDialog("Processing...", "cancel", 0, 100, self)
    progress_dialog.setWindowTitle(dialog_title)
    progress_dialog.setWindowFlags(Qt.Dialog | Qt.CustomizeWindowHint | Qt.WindowTitleHint)
    progress_dialog.setWindowModality(Qt.NonModal) #.setWindowModality(Qt.WindowModal)
    progress_dialog.setAutoClose(True)
    progress_dialog.setAutoReset(True)
    progress_dialog.resize(400, 100)
    progress_dialog.setStyleSheet("QProgressBar::chunk { background-color: #00BFFF; }"
                              "QProgressBar { text-align: none; }"
                              "QProgressBar QLabel { font-size: 0px; }")
    progress_dialog.setRange(0, 0) 

    #animated_dialog = AnimatedDialog(self)
    #animated_dialog.exec()

    #progress_dialog.canceled.connect(self.on_progress_dialog_closed)
    #
    progress_dialog.setMinimumDuration(0)
    progress_dialog.setValue(0)
    
    #REST Thread 
    self.worker_thread.update_progress.connect(progress_dialog.setValue)
    self.worker_thread.set_range.connect(progress_dialog.setRange)
    self.worker_thread.set_button.connect(progress_dialog.setCancelButton)
    self.worker_thread.start()
    progress_dialog.canceled.connect(self.on_cancel_clicked)

def on_progress_dialog_closed(self): 
    print("Abort the train process")

def get_train_status():
    
    #sysconfig = os.path.join('config','system.json')
    server_ip, server_port, api_list = read_server_config(setting_config)
    if server_ip is None or server_port is None:
        return None

    base_url = f"http://{server_ip}:{server_port}/train/status"
    index = setting_config['type']
    
    rest_api_name, api_index, export_nv_engine, path, projectNam, productNum, epochNum  = get_api_name(index)
   
    params = {
        "project": projectNam,
        "productnum": productNum
    }
    
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        
        data = response.json()
        return data
    
    except requests.RequestException as e:
        print(f"Error: {e}")
        return None

def call_train_api(self, api_name, payload):
    #sysconfig = os.path.join('config', 'system.json')
    server_ip, server_port, api_list = read_server_config(setting_config)

    if server_ip is None or server_port is None:
        return None
    
    url = f"http://{server_ip}:{server_port}{api_name}"

    try:
        response = requests.put(url, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        show_error_message(self, "Information", f"Error: {e}")
        print(f"Error: {e}")
        return None


def start_dual_inline_package_inspection(self, training_data_path, project, product_num, export_flag, epoch):
    
    api_path = API_TRAIN_DUAL_IN_LINE_PACKAGE_INSPECTION
    payload = {
        "trainingDataPath": training_data_path, #training_data_path
        "epoch": epoch,
        "exportNVEngine": export_flag,
        "project": project,
        "productNum": product_num
    }
    return call_train_api(self, api_path, payload)

def on_training_started(self, code, message, api):
        actions = {
            0: lambda: show_progress_dialog(self, api),
            -1: lambda: show_error_message(self, "Warning", f"code: {code}, message: {message}"),
            -2: lambda: show_error_message(self, "Warning", f"code: {code}, message: {message}"),
            -3: lambda: show_error_message(self, "Warning", f"code: {code}, message: {message}"),
        }
        action = actions.get(code, lambda: show_error_message(self, "Warning", f"code: {code}, message: {message}"))
        action()
