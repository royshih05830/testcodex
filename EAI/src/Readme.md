# AI automatic Inspection UI source code

## Language
- Python 3.8 (depends on EVA 4.0)
- PySide2
- Qt 5.12 or higher

## Install software package (Linux 20.04)
- Install EVA R4.0
- Install Qt5
    ```
    sudo apt-get install qt5-default
    ```

    reference: https://wiki.qt.io/Install_Qt_5_on_Ubuntu
- Install python package
    ```
    pip3 install -r requirement.txt
    ```
    
- If Qt Designer didn't exist, please download and install.
    https://www.pythonguis.com/installation/install-qt-designer-standalone/

# How to Run?
```sh
source /opt/adlink/eva/scripts/setup_eva_envs.sh
python3 start.py
```

- Administrator Username/Password : admin/admin. (目前寫在程式中, 建議未來移至設定檔如ini等檔案中)

# Details
## File structure
- /gui : 儲存ui檔案, 使用Qt Designer設計產生.
    - login.ui : 登入視窗
    - mian.ui : 主視窗
    - selectproduct.ui : 選擇專案視窗
    - fileconflict.ui : 開啟窗案時選擇匯入現有圖片, 若檔案已存在實的提示視窗
    - editlabel.ui: 編輯Label列表視窗
    - positiontool.ui: 建立三個錨點的定位工具視窗
- /ui : 儲存ui轉成pyside2語法的python檔案
    - login.py : 登入視窗
    - mian.py : 主視窗
    - selectproduct.py : training mode開啟專案視窗
    - fileconflict.py : 開啟窗案時選擇匯入現有圖片, 若檔案已存在實的提示視窗
    - editlabel.py: 編輯Label列表視窗
    - positiontool.py: 建立三個錨點的定位工具視窗
- generateui.sh : 使用pyside2-uic將ui檔案轉成py檔案, 此腳本以只需要輸入ui檔名, 例如: 產生/gui/main.ui的python檔
    ```
    ./generateui.sh main
    ```

    ※ Qt-Designer可能會自行產生python檔案, 也可以手動改檔名並複製到/ui目錄下
    ※ 也可以使用下列指令自行產生python檔案
    ```
    pyside2-uic gui/main.ui > ui/main.py
    ```
- /resource: 存放UI所需要的圖檔. 在Qt Designer的Resource Browser中, 設定所需要的檔案至resources.qrc中. 
- resources.qrc : Qt Designer的資源設定檔, 儲存後Qt Designer會自動產生resources_rc.py. 可以在UI或程式中引用圖檔, 如:EVA_logo
- /config: 存放UI內不需要使用的設定檔案
    - 目前存放pnlist.json, 序號(SN)對應的品號(PN), 為暫時性檔案, 需與GO現有的功能整合(取得SN後找出對應的PN)
- python source code:
    1. start.py : 主程式
    2. gst_helper.py : 使用GStreamer所需
    3. drawshapes.py : 繼承QLabel, 在QLabel中繪畫矩形(ROI)
        用法: 在Qt Designer建立一個Label, 設定Promoted Widgets為DrawShapes.
        要透過enable_draw = True, 才會開始畫圖
    4. liveStream.py : 讀取Gstreamer pipeline appsink, 並呈現於Qlabel中, 用法如下
        
        ```python
        liveSrc = LiveStream(gstcmd='v4l2src ! videoconvert ! video/x-raw,format=BGR, width=1280, height=960 ! appsink emit-signals=True')
        liveSrc.label = xxxLabel
        liveSrc.play()
        liveSrc.pause()
        liveSrc.stop()
        ```  
        
## Translator/Multi-Language
Reference: https://tpdc-km.adlinktech.com:8443/display/S2/GUI+survey+log#GUIsurveylog-Qtranslator

### 第一次建立步驟如下: 詳細內容請參考上述連結的Confluence內容
1. 建立project檔案
    ```
    FORMS = testTranslator.ui
    TRANSLATIONS = translation_en_to_zh_TW.ts
    CODECFORTR = UTF-8
    CODECFORSRC = UTF-8
    ```

2. 產生ts檔案(xml格式)
    ```
    pyside2-lupdate translation.pro
    ```

3. 使用Qt Linguist編輯翻譯文字, 儲存ts檔案

4. 產生qm檔案 (程式碼實際使用的翻譯檔案)
    - File→ Release

5. 程式碼使用QTranslator
    ```python
    from PySide2.QtWidgets import QApplication, QMainWindow,QActionGroup,QAction
    from PySide2 import QtCore
    from ui.testTranslator_ui import Ui_MainWindow
 
    TRANSLATOR = QtCore.QTranslator()
 
    class MainWindow(QMainWindow):
        def __init__(self):
            super().__init__()
 
            self.ui = Ui_MainWindow()       
            self.ui.setupUi(self)
             
            self.languageActionGroup = QActionGroup(self.ui.menuLanguage)
            self.languageActionGroup.addAction(self.ui.actionEnglish)       
            self.languageActionGroup.addAction(self.ui.actionChinese)
            self.languageActionGroup.triggered[QAction].connect(self.on_language_changed)
            self.ui.actionEnglish.setChecked(True)
 
        def on_language_changed(self,action):
            result=False
            if action == self.ui.actionChinese:
                result= TRANSLATOR.load('translation_en_to_zh_TW')
            else:
                TRANSLATOR.load('')
                 
            print(result)
            self.ui.retranslateUi(self)
     
    app = QApplication([])
     
    app.installTranslator(TRANSLATOR)
         
    main_window = MainWindow()
    main_window.show()
    app.exec_()
    ```

### 修改UI後, 如何更新編譯內容:
1. 產生新的ts檔案(請勿覆蓋原本的ts檔案)
2. 開啟ts檔案, 將新增的XML內容貼入舊有的ts檔案
3. 使用Qt Linguist開啟ts檔案, 編輯翻譯內容
若很了解ts檔案結構, 可以直接修改ts檔案的內容
翻譯內容將存於<translation></translation>
4. 產生qm檔案



## Traning mode下的檔案產生在何處?
建立於{HOME}/AAI/train/{PojectNumber}
- /images: 存放圖片
- /labels: 存放對應圖片標記的內容
- /position: 存放三個錨點的座標位置及圖片
- {ProjectNumber}.ini : 存放此專案的相關資訊, 目前只存Project name
- labellist.txt: 儲存此專案的Class list

# TO-DO-LIST
1. training mode下, 現在畫好的框取出的start/end座標為Qlabel的絕對位置(QPoint), 要另處理存成相對位置(0~1), 存入label資訊及label檔案, 注意在繪圖時要轉換回原位置(QPoint)給drawshapes繪圖使用
2. operation mode下, 尚未實作讀取EVA gstreamer ROI資訊, 可參考以下內容:
    - EVA IDE, ROI Viewer的source code.
        -  class ROIViewerInfo in UIGstreamerPeepNode.py
    - EVA adroi pybind
        - http://gitlab.adlinktech.com/VPD-SW2-Vision/EVA_SREP/blob/4.0.2/src/plugins/common/adroi/adroi_pybind.cpp
        - reference:Structual representation in https://tpdc-km.adlinktech.com:8443/display/S2/EVA+R4+detail+requirements
    - EVA draw roi python sample
        - http://gitlab.adlinktech.com/VPD-SW2-Vision/EVA_SREP/blob/4.0.2/src/plugins/adlink/python/draw_roi.py 
