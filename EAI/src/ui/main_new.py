# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_new.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from qtwidgets import Toggle
from qtwidgets import PasswordEdit
from drawshapesgraphics import DrawShapesGraphics

import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1431, 860)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.actionEnglish = QAction(MainWindow)
        self.actionEnglish.setObjectName(u"actionEnglish")
        self.actionEnglish.setCheckable(True)
        self.actionChinese = QAction(MainWindow)
        self.actionChinese.setObjectName(u"actionChinese")
        self.actionChinese.setCheckable(True)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_8 = QGridLayout(self.centralwidget)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.ADLINK_label = QLabel(self.centralwidget)
        self.ADLINK_label.setObjectName(u"ADLINK_label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.ADLINK_label.sizePolicy().hasHeightForWidth())
        self.ADLINK_label.setSizePolicy(sizePolicy1)
        self.ADLINK_label.setMaximumSize(QSize(206, 60))
        self.ADLINK_label.setPixmap(QPixmap(u":/<logo>/resource/cropped-adlink-logo.png"))
        self.ADLINK_label.setScaledContents(True)

        self.gridLayout_8.addWidget(self.ADLINK_label, 1, 2, 1, 1)

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy2)
        self.tab_setting = QWidget()
        self.tab_setting.setObjectName(u"tab_setting")
        self.horizontalLayout_11 = QHBoxLayout(self.tab_setting)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.gridLayout_11 = QGridLayout()
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.label_4 = QLabel(self.tab_setting)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_11.addWidget(self.label_4, 2, 0, 1, 1)

        self.sn_setting_lineEdit = QLineEdit(self.tab_setting)
        self.sn_setting_lineEdit.setObjectName(u"sn_setting_lineEdit")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.sn_setting_lineEdit.sizePolicy().hasHeightForWidth())
        self.sn_setting_lineEdit.setSizePolicy(sizePolicy3)
        self.sn_setting_lineEdit.setMinimumSize(QSize(300, 0))

        self.gridLayout_11.addWidget(self.sn_setting_lineEdit, 1, 2, 1, 1)

        self.productNum_setting_lineEdit = QLineEdit(self.tab_setting)
        self.productNum_setting_lineEdit.setObjectName(u"productNum_setting_lineEdit")
        sizePolicy3.setHeightForWidth(self.productNum_setting_lineEdit.sizePolicy().hasHeightForWidth())
        self.productNum_setting_lineEdit.setSizePolicy(sizePolicy3)
        self.productNum_setting_lineEdit.setMinimumSize(QSize(300, 0))

        self.gridLayout_11.addWidget(self.productNum_setting_lineEdit, 2, 2, 1, 1)

        self.label_3 = QLabel(self.tab_setting)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_11.addWidget(self.label_3, 0, 0, 1, 1)

        self.projectName_setting_lineEdit = QLineEdit(self.tab_setting)
        self.projectName_setting_lineEdit.setObjectName(u"projectName_setting_lineEdit")
        sizePolicy3.setHeightForWidth(self.projectName_setting_lineEdit.sizePolicy().hasHeightForWidth())
        self.projectName_setting_lineEdit.setSizePolicy(sizePolicy3)
        self.projectName_setting_lineEdit.setMinimumSize(QSize(300, 0))
        self.projectName_setting_lineEdit.setFrame(False)
        self.projectName_setting_lineEdit.setReadOnly(True)

        self.gridLayout_11.addWidget(self.projectName_setting_lineEdit, 0, 2, 1, 1)

        self.sn_setting_label = QLabel(self.tab_setting)
        self.sn_setting_label.setObjectName(u"sn_setting_label")
        self.sn_setting_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_11.addWidget(self.sn_setting_label, 1, 0, 1, 1)


        self.verticalLayout_4.addLayout(self.gridLayout_11)

        self.loadSettings_pushButton = QPushButton(self.tab_setting)
        self.loadSettings_pushButton.setObjectName(u"loadSettings_pushButton")
        self.loadSettings_pushButton.setEnabled(False)
        self.loadSettings_pushButton.setMinimumSize(QSize(0, 35))

        self.verticalLayout_4.addWidget(self.loadSettings_pushButton)

        self.line_10 = QFrame(self.tab_setting)
        self.line_10.setObjectName(u"line_10")
        self.line_10.setFrameShape(QFrame.HLine)
        self.line_10.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_4.addWidget(self.line_10)


        self.verticalLayout_5.addLayout(self.verticalLayout_4)

        self.manage_groupBox = QGroupBox(self.tab_setting)
        self.manage_groupBox.setObjectName(u"manage_groupBox")
        self.manage_groupBox.setEnabled(False)
        sizePolicy4 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.manage_groupBox.sizePolicy().hasHeightForWidth())
        self.manage_groupBox.setSizePolicy(sizePolicy4)
        self.manage_groupBox.setStyleSheet(u"QGroupBox{\n"
"border-width:1px;\n"
"border-style:solid;\n"
"border-radius: 10px;\n"
"border-color:gray;\n"
"margin-top:1ex;\n"
"}\n"
"QGroupBox::title{\n"
"subcontrol-origin:margin;\n"
"subcontrol-position:top left;\n"
"left:15px;\n"
"margin-left:2px;\n"
"padding:0 1px;\n"
"}")
        self.verticalLayout_14 = QVBoxLayout(self.manage_groupBox)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.rename_radioButton = QRadioButton(self.manage_groupBox)
        self.rename_radioButton.setObjectName(u"rename_radioButton")

        self.verticalLayout_13.addWidget(self.rename_radioButton)

        self.copy_radioButton = QRadioButton(self.manage_groupBox)
        self.copy_radioButton.setObjectName(u"copy_radioButton")

        self.verticalLayout_13.addWidget(self.copy_radioButton)

        self.duplicate_radioButton = QRadioButton(self.manage_groupBox)
        self.duplicate_radioButton.setObjectName(u"duplicate_radioButton")

        self.verticalLayout_13.addWidget(self.duplicate_radioButton)


        self.verticalLayout_14.addLayout(self.verticalLayout_13)

        self.gridLayout_19 = QGridLayout()
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.newProjectName_label = QLabel(self.manage_groupBox)
        self.newProjectName_label.setObjectName(u"newProjectName_label")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.newProjectName_label.sizePolicy().hasHeightForWidth())
        self.newProjectName_label.setSizePolicy(sizePolicy5)
        self.newProjectName_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_19.addWidget(self.newProjectName_label, 0, 0, 1, 1)

        self.newProjectName_lineEdit = QLineEdit(self.manage_groupBox)
        self.newProjectName_lineEdit.setObjectName(u"newProjectName_lineEdit")
        self.newProjectName_lineEdit.setEnabled(False)
        sizePolicy3.setHeightForWidth(self.newProjectName_lineEdit.sizePolicy().hasHeightForWidth())
        self.newProjectName_lineEdit.setSizePolicy(sizePolicy3)
        self.newProjectName_lineEdit.setMinimumSize(QSize(250, 0))

        self.gridLayout_19.addWidget(self.newProjectName_lineEdit, 0, 1, 1, 1)

        self.newPN_label = QLabel(self.manage_groupBox)
        self.newPN_label.setObjectName(u"newPN_label")
        self.newPN_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_19.addWidget(self.newPN_label, 1, 0, 1, 1)

        self.newPN_lineEdit = QLineEdit(self.manage_groupBox)
        self.newPN_lineEdit.setObjectName(u"newPN_lineEdit")
        self.newPN_lineEdit.setEnabled(False)
        sizePolicy3.setHeightForWidth(self.newPN_lineEdit.sizePolicy().hasHeightForWidth())
        self.newPN_lineEdit.setSizePolicy(sizePolicy3)
        self.newPN_lineEdit.setMinimumSize(QSize(250, 0))

        self.gridLayout_19.addWidget(self.newPN_lineEdit, 1, 1, 1, 1)


        self.verticalLayout_14.addLayout(self.gridLayout_19)

        self.submit_manage_project_pushButton = QPushButton(self.manage_groupBox)
        self.submit_manage_project_pushButton.setObjectName(u"submit_manage_project_pushButton")
        self.submit_manage_project_pushButton.setEnabled(False)
        sizePolicy6 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.submit_manage_project_pushButton.sizePolicy().hasHeightForWidth())
        self.submit_manage_project_pushButton.setSizePolicy(sizePolicy6)
        self.submit_manage_project_pushButton.setMinimumSize(QSize(0, 35))

        self.verticalLayout_14.addWidget(self.submit_manage_project_pushButton)


        self.verticalLayout_5.addWidget(self.manage_groupBox)

        self.retrain_groupBox = QGroupBox(self.tab_setting)
        self.retrain_groupBox.setObjectName(u"retrain_groupBox")
        self.retrain_groupBox.setEnabled(False)
        sizePolicy4.setHeightForWidth(self.retrain_groupBox.sizePolicy().hasHeightForWidth())
        self.retrain_groupBox.setSizePolicy(sizePolicy4)
        self.retrain_groupBox.setStyleSheet(u"QGroupBox{\n"
"border-width:1px;\n"
"border-style:solid;\n"
"border-radius: 10px;\n"
"border-color:gray;\n"
"margin-top:1ex;\n"
"}\n"
"QGroupBox::title{\n"
"subcontrol-origin:margin;\n"
"subcontrol-position:top left;\n"
"left:15px;\n"
"margin-left:2px;\n"
"padding:0 1px;\n"
"}")
        self.retrain_groupBox.setCheckable(True)
        self.retrain_groupBox.setChecked(False)
        self.gridLayout_18 = QGridLayout(self.retrain_groupBox)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.retrain_pushButton = QPushButton(self.retrain_groupBox)
        self.retrain_pushButton.setObjectName(u"retrain_pushButton")
        self.retrain_pushButton.setMinimumSize(QSize(0, 35))
        self.retrain_pushButton.setStyleSheet(u"background-color: rgb(252, 175, 62);")

        self.gridLayout_18.addWidget(self.retrain_pushButton, 2, 0, 1, 1)

        self.retrain_treeWidget = QTreeWidget(self.retrain_groupBox)
        __qtreewidgetitem = QTreeWidgetItem(self.retrain_treeWidget)
        __qtreewidgetitem.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled|Qt.ItemIsTristate);
        __qtreewidgetitem.setCheckState(0, Qt.Checked);
        __qtreewidgetitem1 = QTreeWidgetItem(__qtreewidgetitem)
        __qtreewidgetitem1.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled|Qt.ItemIsTristate);
        __qtreewidgetitem1.setCheckState(0, Qt.Checked);
        __qtreewidgetitem2 = QTreeWidgetItem(__qtreewidgetitem1)
        __qtreewidgetitem2.setCheckState(0, Qt.Checked);
        __qtreewidgetitem3 = QTreeWidgetItem(__qtreewidgetitem1)
        __qtreewidgetitem3.setCheckState(0, Qt.Checked);
        __qtreewidgetitem4 = QTreeWidgetItem(__qtreewidgetitem)
        __qtreewidgetitem4.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled|Qt.ItemIsTristate);
        __qtreewidgetitem4.setCheckState(0, Qt.Checked);
        __qtreewidgetitem5 = QTreeWidgetItem(__qtreewidgetitem4)
        __qtreewidgetitem5.setCheckState(0, Qt.Checked);
        self.retrain_treeWidget.setObjectName(u"retrain_treeWidget")
        self.retrain_treeWidget.setMinimumSize(QSize(0, 200))
        self.retrain_treeWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.retrain_treeWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.retrain_treeWidget.header().setVisible(False)

        self.gridLayout_18.addWidget(self.retrain_treeWidget, 1, 0, 1, 1)


        self.verticalLayout_5.addWidget(self.retrain_groupBox)

        self.verticalSpacer_8 = QSpacerItem(17, 285, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_8)


        self.horizontalLayout_11.addLayout(self.verticalLayout_5)

        self.line_2 = QFrame(self.tab_setting)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_11.addWidget(self.line_2)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.training_groupBox = QGroupBox(self.tab_setting)
        self.training_groupBox.setObjectName(u"training_groupBox")
        self.training_groupBox.setEnabled(False)
        sizePolicy5.setHeightForWidth(self.training_groupBox.sizePolicy().hasHeightForWidth())
        self.training_groupBox.setSizePolicy(sizePolicy5)
        self.training_groupBox.setStyleSheet(u"QGroupBox{\n"
"border-width:1px;\n"
"border-style:solid;\n"
"border-radius: 10px;\n"
"border-color:gray;\n"
"margin-top:2.5ex;\n"
"}\n"
"QGroupBox::title{\n"
"subcontrol-origin:margin;\n"
"subcontrol-position:top center;\n"
"padding:0 1x;\n"
"}")
        self.gridLayout_17 = QGridLayout(self.training_groupBox)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.dip_groupBox = QGroupBox(self.training_groupBox)
        self.dip_groupBox.setObjectName(u"dip_groupBox")
        self.dip_groupBox.setStyleSheet(u"QGroupBox{\n"
"border-width:1px;\n"
"border-style:solid;\n"
"border-radius: 10px;\n"
"border-color:gray;\n"
"margin-top:1ex;\n"
"}\n"
"QGroupBox::title{\n"
"subcontrol-origin:margin;\n"
"subcontrol-position:top left;\n"
"left:15px;\n"
"margin-left:2px;\n"
"padding:0 1px;\n"
"}")
        self.gridLayout_14 = QGridLayout(self.dip_groupBox)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.training_modelConfig_label = QLabel(self.dip_groupBox)
        self.training_modelConfig_label.setObjectName(u"training_modelConfig_label")
        sizePolicy.setHeightForWidth(self.training_modelConfig_label.sizePolicy().hasHeightForWidth())
        self.training_modelConfig_label.setSizePolicy(sizePolicy)
        self.training_modelConfig_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_8.addWidget(self.training_modelConfig_label)

        self.epoch_spinBox = QSpinBox(self.dip_groupBox)
        self.epoch_spinBox.setObjectName(u"epoch_spinBox")
        self.epoch_spinBox.setAlignment(Qt.AlignCenter)
        self.epoch_spinBox.setMinimum(1)
        self.epoch_spinBox.setMaximum(16777215)
        self.epoch_spinBox.setValue(2)

        self.horizontalLayout_8.addWidget(self.epoch_spinBox)


        self.gridLayout_14.addLayout(self.horizontalLayout_8, 2, 0, 1, 1)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label = QLabel(self.dip_groupBox)
        self.label.setObjectName(u"label")
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)

        self.horizontalLayout_9.addWidget(self.label)

        self.traingPath_lineEdit = QLineEdit(self.dip_groupBox)
        self.traingPath_lineEdit.setObjectName(u"traingPath_lineEdit")

        self.horizontalLayout_9.addWidget(self.traingPath_lineEdit)


        self.gridLayout_14.addLayout(self.horizontalLayout_9, 3, 0, 1, 2)

        self.exortNVEngine_checkBox = QCheckBox(self.dip_groupBox)
        self.exortNVEngine_checkBox.setObjectName(u"exortNVEngine_checkBox")
        self.exortNVEngine_checkBox.setTristate(False)

        self.gridLayout_14.addWidget(self.exortNVEngine_checkBox, 1, 0, 1, 1)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_14.addItem(self.horizontalSpacer_10, 2, 1, 1, 1)


        self.gridLayout_17.addWidget(self.dip_groupBox, 5, 0, 1, 2)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.boradno_label = QLabel(self.training_groupBox)
        self.boradno_label.setObjectName(u"boradno_label")

        self.horizontalLayout_12.addWidget(self.boradno_label)

        self.boradno_spinBox = QSpinBox(self.training_groupBox)
        self.boradno_spinBox.setObjectName(u"boradno_spinBox")
        self.boradno_spinBox.setAlignment(Qt.AlignCenter)
        self.boradno_spinBox.setMinimum(1)
        self.boradno_spinBox.setMaximum(10)
        self.boradno_spinBox.setValue(1)

        self.horizontalLayout_12.addWidget(self.boradno_spinBox)


        self.gridLayout_17.addLayout(self.horizontalLayout_12, 9, 0, 1, 1)

        self.line_6 = QFrame(self.training_groupBox)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.HLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.gridLayout_17.addWidget(self.line_6, 1, 0, 1, 2)

        self.horizontalSpacer_8 = QSpacerItem(200, 17, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_17.addItem(self.horizontalSpacer_8, 0, 1, 1, 1)

        self.line_9 = QFrame(self.training_groupBox)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setFrameShape(QFrame.HLine)
        self.line_9.setFrameShadow(QFrame.Sunken)

        self.gridLayout_17.addWidget(self.line_9, 3, 0, 1, 2)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.training_savePath_label_2 = QLabel(self.training_groupBox)
        self.training_savePath_label_2.setObjectName(u"training_savePath_label_2")
        self.training_savePath_label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_6.addWidget(self.training_savePath_label_2)

        self.showlist_spinBox = QSpinBox(self.training_groupBox)
        self.showlist_spinBox.setObjectName(u"showlist_spinBox")
        self.showlist_spinBox.setMinimum(1)
        self.showlist_spinBox.setMaximum(15)
        self.showlist_spinBox.setValue(6)

        self.horizontalLayout_6.addWidget(self.showlist_spinBox)


        self.gridLayout_17.addLayout(self.horizontalLayout_6, 2, 0, 1, 1)

        self.gridLayout_13 = QGridLayout()
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.training_ip_lineEdit = QLineEdit(self.training_groupBox)
        self.training_ip_lineEdit.setObjectName(u"training_ip_lineEdit")

        self.gridLayout_13.addWidget(self.training_ip_lineEdit, 0, 1, 1, 1)

        self.training_ip_label = QLabel(self.training_groupBox)
        self.training_ip_label.setObjectName(u"training_ip_label")
        self.training_ip_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_13.addWidget(self.training_ip_label, 0, 0, 1, 1)

        self.label_12 = QLabel(self.training_groupBox)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_13.addWidget(self.label_12, 1, 0, 1, 1)

        self.training_pw_label = QLabel(self.training_groupBox)
        self.training_pw_label.setObjectName(u"training_pw_label")
        self.training_pw_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_13.addWidget(self.training_pw_label, 4, 0, 1, 1)

        self.training_account_label = QLabel(self.training_groupBox)
        self.training_account_label.setObjectName(u"training_account_label")
        self.training_account_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_13.addWidget(self.training_account_label, 2, 0, 1, 1)

        self.training_pw_lineEdit = PasswordEdit(self.training_groupBox)
        self.training_pw_lineEdit.setObjectName(u"training_pw_lineEdit")

        self.gridLayout_13.addWidget(self.training_pw_lineEdit, 4, 1, 1, 1)

        self.training_account_lineEdit = QLineEdit(self.training_groupBox)
        self.training_account_lineEdit.setObjectName(u"training_account_lineEdit")

        self.gridLayout_13.addWidget(self.training_account_lineEdit, 2, 1, 1, 1)

        self.training_port_lineEdit = QLineEdit(self.training_groupBox)
        self.training_port_lineEdit.setObjectName(u"training_port_lineEdit")

        self.gridLayout_13.addWidget(self.training_port_lineEdit, 1, 1, 1, 1)


        self.gridLayout_17.addLayout(self.gridLayout_13, 0, 0, 1, 1)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.training_savePath_label = QLabel(self.training_groupBox)
        self.training_savePath_label.setObjectName(u"training_savePath_label")
        sizePolicy.setHeightForWidth(self.training_savePath_label.sizePolicy().hasHeightForWidth())
        self.training_savePath_label.setSizePolicy(sizePolicy)
        self.training_savePath_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.training_savePath_label)

        self.inference_comboBox = QComboBox(self.training_groupBox)
        self.inference_comboBox.addItem("")
        self.inference_comboBox.addItem("")
        self.inference_comboBox.setObjectName(u"inference_comboBox")

        self.horizontalLayout_7.addWidget(self.inference_comboBox)


        self.gridLayout_17.addLayout(self.horizontalLayout_7, 4, 0, 1, 2)


        self.verticalLayout_6.addWidget(self.training_groupBox)

        self.verticalSpacer_6 = QSpacerItem(17, 285, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_6)


        self.horizontalLayout_10.addLayout(self.verticalLayout_6)

        self.line_8 = QFrame(self.tab_setting)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setFrameShape(QFrame.VLine)
        self.line_8.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_10.addWidget(self.line_8)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.storage_groupBox = QGroupBox(self.tab_setting)
        self.storage_groupBox.setObjectName(u"storage_groupBox")
        self.storage_groupBox.setEnabled(False)
        sizePolicy5.setHeightForWidth(self.storage_groupBox.sizePolicy().hasHeightForWidth())
        self.storage_groupBox.setSizePolicy(sizePolicy5)
        self.storage_groupBox.setStyleSheet(u"QGroupBox{\n"
"border-width:1px;\n"
"border-style:solid;\n"
"border-radius: 10px;\n"
"border-color:gray;\n"
"margin-top:2.5ex;\n"
"}\n"
"QGroupBox::title{\n"
"subcontrol-origin:margin;\n"
"subcontrol-position:top center;\n"
"padding:0 1x;\n"
"}")
        self.gridLayout_12 = QGridLayout(self.storage_groupBox)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.storage_ip_lineEdit = QLineEdit(self.storage_groupBox)
        self.storage_ip_lineEdit.setObjectName(u"storage_ip_lineEdit")

        self.gridLayout_12.addWidget(self.storage_ip_lineEdit, 1, 1, 1, 1)

        self.storage_account_lineEdit = QLineEdit(self.storage_groupBox)
        self.storage_account_lineEdit.setObjectName(u"storage_account_lineEdit")

        self.gridLayout_12.addWidget(self.storage_account_lineEdit, 2, 1, 1, 1)

        self.storage_ip_label = QLabel(self.storage_groupBox)
        self.storage_ip_label.setObjectName(u"storage_ip_label")
        self.storage_ip_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_12.addWidget(self.storage_ip_label, 1, 0, 1, 1)

        self.storage_account_label = QLabel(self.storage_groupBox)
        self.storage_account_label.setObjectName(u"storage_account_label")
        self.storage_account_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_12.addWidget(self.storage_account_label, 2, 0, 1, 1)

        self.storage_pw_label = QLabel(self.storage_groupBox)
        self.storage_pw_label.setObjectName(u"storage_pw_label")
        self.storage_pw_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_12.addWidget(self.storage_pw_label, 3, 0, 1, 1)

        self.storage_path_lineEdit = QLineEdit(self.storage_groupBox)
        self.storage_path_lineEdit.setObjectName(u"storage_path_lineEdit")
        self.storage_path_lineEdit.setMinimumSize(QSize(250, 0))

        self.gridLayout_12.addWidget(self.storage_path_lineEdit, 4, 1, 1, 2)

        self.horizontalSpacer_6 = QSpacerItem(100, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_12.addItem(self.horizontalSpacer_6, 2, 2, 1, 1)

        self.storage_pw_lineEdit = PasswordEdit(self.storage_groupBox)
        self.storage_pw_lineEdit.setObjectName(u"storage_pw_lineEdit")

        self.gridLayout_12.addWidget(self.storage_pw_lineEdit, 3, 1, 1, 1)

        self.storage_path_label = QLabel(self.storage_groupBox)
        self.storage_path_label.setObjectName(u"storage_path_label")
        self.storage_path_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_12.addWidget(self.storage_path_label, 4, 0, 1, 1)

        self.label_2 = QLabel(self.storage_groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_12.addWidget(self.label_2, 0, 0, 1, 1)

        self.comboBox = QComboBox(self.storage_groupBox)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.gridLayout_12.addWidget(self.comboBox, 0, 1, 1, 1)


        self.verticalLayout_7.addWidget(self.storage_groupBox)

        self.inspection_groupBox = QGroupBox(self.tab_setting)
        self.inspection_groupBox.setObjectName(u"inspection_groupBox")
        self.inspection_groupBox.setEnabled(False)
        self.inspection_groupBox.setStyleSheet(u"QGroupBox{\n"
"border-width:1px;\n"
"border-style:solid;\n"
"border-radius: 10px;\n"
"border-color:gray;\n"
"margin-top:2.5ex;\n"
"}\n"
"QGroupBox::title{\n"
"subcontrol-origin:margin;\n"
"subcontrol-position:top center;\n"
"padding:0 1x;\n"
"}")
        self.gridLayout_24 = QGridLayout(self.inspection_groupBox)
        self.gridLayout_24.setObjectName(u"gridLayout_24")
        self.useTestVideo_groupBox = QGroupBox(self.inspection_groupBox)
        self.useTestVideo_groupBox.setObjectName(u"useTestVideo_groupBox")
        self.useTestVideo_groupBox.setStyleSheet(u"QGroupBox{\n"
"border-width:1px;\n"
"border-style:solid;\n"
"border-radius: 10px;\n"
"border-color:gray;\n"
"margin-top:1ex;\n"
"}\n"
"QGroupBox::title{\n"
"subcontrol-origin:margin;\n"
"subcontrol-position:top left;\n"
"left:15px;\n"
"margin-left:2px;\n"
"padding:0 1px;\n"
"}")
        self.useTestVideo_groupBox.setCheckable(True)
        self.useTestVideo_groupBox.setChecked(False)
        self.verticalLayout_12 = QVBoxLayout(self.useTestVideo_groupBox)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.testVideo_filePath_label = QLabel(self.useTestVideo_groupBox)
        self.testVideo_filePath_label.setObjectName(u"testVideo_filePath_label")

        self.horizontalLayout_17.addWidget(self.testVideo_filePath_label)

        self.testVideo_filePath_lineEdit = QLineEdit(self.useTestVideo_groupBox)
        self.testVideo_filePath_lineEdit.setObjectName(u"testVideo_filePath_lineEdit")
        self.testVideo_filePath_lineEdit.setMinimumSize(QSize(260, 0))

        self.horizontalLayout_17.addWidget(self.testVideo_filePath_lineEdit)

        self.testVideo_toolButton = QToolButton(self.useTestVideo_groupBox)
        self.testVideo_toolButton.setObjectName(u"testVideo_toolButton")

        self.horizontalLayout_17.addWidget(self.testVideo_toolButton)


        self.verticalLayout_12.addLayout(self.horizontalLayout_17)


        self.gridLayout_24.addWidget(self.useTestVideo_groupBox, 0, 0, 1, 1)


        self.verticalLayout_7.addWidget(self.inspection_groupBox)

        self.verticalSpacer_7 = QSpacerItem(20, 471, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_7)


        self.horizontalLayout_10.addLayout(self.verticalLayout_7)


        self.verticalLayout_8.addLayout(self.horizontalLayout_10)

        self.line_7 = QFrame(self.tab_setting)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.HLine)
        self.line_7.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_8.addWidget(self.line_7)

        self.SaveSetting_pushButton = QPushButton(self.tab_setting)
        self.SaveSetting_pushButton.setObjectName(u"SaveSetting_pushButton")
        self.SaveSetting_pushButton.setEnabled(False)
        sizePolicy7 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.SaveSetting_pushButton.sizePolicy().hasHeightForWidth())
        self.SaveSetting_pushButton.setSizePolicy(sizePolicy7)
        self.SaveSetting_pushButton.setMinimumSize(QSize(150, 40))
        self.SaveSetting_pushButton.setStyleSheet(u"background-color: rgb(205, 249, 161);")

        self.verticalLayout_8.addWidget(self.SaveSetting_pushButton)


        self.horizontalLayout_11.addLayout(self.verticalLayout_8)

        self.tabWidget.addTab(self.tab_setting, "")
        self.tab_training = QWidget()
        self.tab_training.setObjectName(u"tab_training")
        self.gridLayout_16 = QGridLayout(self.tab_training)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.start_pushButton = QPushButton(self.tab_training)
        self.start_pushButton.setObjectName(u"start_pushButton")
        self.start_pushButton.setMinimumSize(QSize(0, 40))
        self.start_pushButton.setStyleSheet(u"background-color: rgb(205, 249, 161);")

        self.horizontalLayout_2.addWidget(self.start_pushButton)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_9)

        self.goldenmode_checkBox = QCheckBox(self.tab_training)
        self.goldenmode_checkBox.setObjectName(u"goldenmode_checkBox")
        self.goldenmode_checkBox.setEnabled(False)

        self.horizontalLayout_2.addWidget(self.goldenmode_checkBox)

        self.horizontalSpacer_13 = QSpacerItem(100, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_13)

        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.device_offline_comboBox = QComboBox(self.tab_training)
        self.device_offline_comboBox.addItem("")
        self.device_offline_comboBox.addItem("")
        self.device_offline_comboBox.addItem("")
        self.device_offline_comboBox.addItem("")
        self.device_offline_comboBox.setObjectName(u"device_offline_comboBox")
        self.device_offline_comboBox.setEnabled(False)
        self.device_offline_comboBox.setMinimumSize(QSize(0, 30))

        self.gridLayout_7.addWidget(self.device_offline_comboBox, 0, 1, 1, 1)

        self.device_offline_label = QLabel(self.tab_training)
        self.device_offline_label.setObjectName(u"device_offline_label")
        self.device_offline_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_7.addWidget(self.device_offline_label, 0, 0, 1, 1)

        self.importImage_pushButton = QPushButton(self.tab_training)
        self.importImage_pushButton.setObjectName(u"importImage_pushButton")
        self.importImage_pushButton.setEnabled(False)
        self.importImage_pushButton.setMinimumSize(QSize(0, 40))

        self.gridLayout_7.addWidget(self.importImage_pushButton, 0, 2, 1, 1)


        self.horizontalLayout_2.addLayout(self.gridLayout_7)

        self.capture_pushButton = QPushButton(self.tab_training)
        self.capture_pushButton.setObjectName(u"capture_pushButton")
        self.capture_pushButton.setEnabled(False)
        self.capture_pushButton.setMinimumSize(QSize(0, 40))

        self.horizontalLayout_2.addWidget(self.capture_pushButton)

        self.horizontalSpacer_2 = QSpacerItem(200, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.calThreshold_pushButton = QPushButton(self.tab_training)
        self.calThreshold_pushButton.setObjectName(u"calThreshold_pushButton")
        self.calThreshold_pushButton.setEnabled(False)
        self.calThreshold_pushButton.setMinimumSize(QSize(0, 40))
        self.calThreshold_pushButton.setStyleSheet(u"background-color: rgb(252, 233, 79);")

        self.horizontalLayout_2.addWidget(self.calThreshold_pushButton)

        self.export_pushButton = QPushButton(self.tab_training)
        self.export_pushButton.setObjectName(u"export_pushButton")
        self.export_pushButton.setEnabled(False)
        self.export_pushButton.setMinimumSize(QSize(0, 40))

        self.horizontalLayout_2.addWidget(self.export_pushButton)

        self.train_pushButton = QPushButton(self.tab_training)
        self.train_pushButton.setObjectName(u"train_pushButton")
        self.train_pushButton.setEnabled(False)
        self.train_pushButton.setMinimumSize(QSize(0, 40))
        self.train_pushButton.setStyleSheet(u"background-color: rgb(252, 175, 62);")

        self.horizontalLayout_2.addWidget(self.train_pushButton)


        self.gridLayout_16.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)

        self.line_3 = QFrame(self.tab_training)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.gridLayout_16.addWidget(self.line_3, 1, 0, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.widget_3 = QWidget(self.tab_training)
        self.widget_3.setObjectName(u"widget_3")
        sizePolicy8 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy8)
        self.widget_3.setMaximumSize(QSize(190, 16777215))
        self.gridLayout_10 = QGridLayout(self.widget_3)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.label_groupBox = QGroupBox(self.widget_3)
        self.label_groupBox.setObjectName(u"label_groupBox")
        sizePolicy8.setHeightForWidth(self.label_groupBox.sizePolicy().hasHeightForWidth())
        self.label_groupBox.setSizePolicy(sizePolicy8)
        self.label_groupBox.setMaximumSize(QSize(190, 16777215))
        self.label_groupBox.setStyleSheet(u"QGroupBox{\n"
"border-width:1px;\n"
"border-style:solid;\n"
"border-radius: 10px;\n"
"border-color:gray;\n"
"margin-top:2.5ex;\n"
"}\n"
"QGroupBox::title{\n"
"subcontrol-origin:margin;\n"
"subcontrol-position:top center;\n"
"padding:0 1px;\n"
"}")
        self.label_groupBox.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.gridLayout_3 = QGridLayout(self.label_groupBox)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.orderList_label = QLabel(self.label_groupBox)
        self.orderList_label.setObjectName(u"orderList_label")
        self.orderList_label.setMaximumSize(QSize(16777215, 20))
        self.orderList_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.orderList_label)

        self.orderList_listWidget = QListWidget(self.label_groupBox)
        __qlistwidgetitem = QListWidgetItem(self.orderList_listWidget)
        __qlistwidgetitem.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem1 = QListWidgetItem(self.orderList_listWidget)
        __qlistwidgetitem1.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem2 = QListWidgetItem(self.orderList_listWidget)
        __qlistwidgetitem2.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem3 = QListWidgetItem(self.orderList_listWidget)
        __qlistwidgetitem3.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem4 = QListWidgetItem(self.orderList_listWidget)
        __qlistwidgetitem4.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem5 = QListWidgetItem(self.orderList_listWidget)
        __qlistwidgetitem5.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem6 = QListWidgetItem(self.orderList_listWidget)
        __qlistwidgetitem6.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem7 = QListWidgetItem(self.orderList_listWidget)
        __qlistwidgetitem7.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem8 = QListWidgetItem(self.orderList_listWidget)
        __qlistwidgetitem8.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem9 = QListWidgetItem(self.orderList_listWidget)
        __qlistwidgetitem9.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem10 = QListWidgetItem(self.orderList_listWidget)
        __qlistwidgetitem10.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem11 = QListWidgetItem(self.orderList_listWidget)
        __qlistwidgetitem11.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem12 = QListWidgetItem(self.orderList_listWidget)
        __qlistwidgetitem12.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem13 = QListWidgetItem(self.orderList_listWidget)
        __qlistwidgetitem13.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem14 = QListWidgetItem(self.orderList_listWidget)
        __qlistwidgetitem14.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem15 = QListWidgetItem(self.orderList_listWidget)
        __qlistwidgetitem15.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem16 = QListWidgetItem(self.orderList_listWidget)
        __qlistwidgetitem16.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem17 = QListWidgetItem(self.orderList_listWidget)
        __qlistwidgetitem17.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem18 = QListWidgetItem(self.orderList_listWidget)
        __qlistwidgetitem18.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem19 = QListWidgetItem(self.orderList_listWidget)
        __qlistwidgetitem19.setTextAlignment(Qt.AlignCenter);
        self.orderList_listWidget.setObjectName(u"orderList_listWidget")
        self.orderList_listWidget.setMinimumSize(QSize(0, 0))
        self.orderList_listWidget.setMaximumSize(QSize(16777215, 150))

        self.verticalLayout_3.addWidget(self.orderList_listWidget)


        self.gridLayout_3.addLayout(self.verticalLayout_3, 5, 0, 1, 1)

        self.line_5 = QFrame(self.label_groupBox)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.VLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.gridLayout_3.addWidget(self.line_5, 5, 1, 1, 1)

        self.labelList_listWidget = QListWidget(self.label_groupBox)
        self.labelList_listWidget.setObjectName(u"labelList_listWidget")

        self.gridLayout_3.addWidget(self.labelList_listWidget, 1, 0, 1, 3)

        self.line = QFrame(self.label_groupBox)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout_3.addWidget(self.line, 3, 0, 1, 3)

        self.labelEdit_pushButton = QPushButton(self.label_groupBox)
        self.labelEdit_pushButton.setObjectName(u"labelEdit_pushButton")
        self.labelEdit_pushButton.setEnabled(False)

        self.gridLayout_3.addWidget(self.labelEdit_pushButton, 0, 1, 1, 2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.durationList_label = QLabel(self.label_groupBox)
        self.durationList_label.setObjectName(u"durationList_label")
        self.durationList_label.setMaximumSize(QSize(16777215, 20))
        self.durationList_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.durationList_label)

        self.durationList_listWidget = QListWidget(self.label_groupBox)
        __qlistwidgetitem20 = QListWidgetItem(self.durationList_listWidget)
        __qlistwidgetitem20.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem21 = QListWidgetItem(self.durationList_listWidget)
        __qlistwidgetitem21.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem22 = QListWidgetItem(self.durationList_listWidget)
        __qlistwidgetitem22.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem23 = QListWidgetItem(self.durationList_listWidget)
        __qlistwidgetitem23.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem24 = QListWidgetItem(self.durationList_listWidget)
        __qlistwidgetitem24.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem25 = QListWidgetItem(self.durationList_listWidget)
        __qlistwidgetitem25.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem26 = QListWidgetItem(self.durationList_listWidget)
        __qlistwidgetitem26.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem27 = QListWidgetItem(self.durationList_listWidget)
        __qlistwidgetitem27.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem28 = QListWidgetItem(self.durationList_listWidget)
        __qlistwidgetitem28.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem29 = QListWidgetItem(self.durationList_listWidget)
        __qlistwidgetitem29.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem30 = QListWidgetItem(self.durationList_listWidget)
        __qlistwidgetitem30.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem31 = QListWidgetItem(self.durationList_listWidget)
        __qlistwidgetitem31.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem32 = QListWidgetItem(self.durationList_listWidget)
        __qlistwidgetitem32.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem33 = QListWidgetItem(self.durationList_listWidget)
        __qlistwidgetitem33.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem34 = QListWidgetItem(self.durationList_listWidget)
        __qlistwidgetitem34.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem35 = QListWidgetItem(self.durationList_listWidget)
        __qlistwidgetitem35.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem36 = QListWidgetItem(self.durationList_listWidget)
        __qlistwidgetitem36.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem37 = QListWidgetItem(self.durationList_listWidget)
        __qlistwidgetitem37.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem38 = QListWidgetItem(self.durationList_listWidget)
        __qlistwidgetitem38.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem39 = QListWidgetItem(self.durationList_listWidget)
        __qlistwidgetitem39.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem40 = QListWidgetItem(self.durationList_listWidget)
        __qlistwidgetitem40.setTextAlignment(Qt.AlignCenter);
        self.durationList_listWidget.setObjectName(u"durationList_listWidget")
        self.durationList_listWidget.setMinimumSize(QSize(0, 0))
        self.durationList_listWidget.setMaximumSize(QSize(16777215, 150))

        self.verticalLayout.addWidget(self.durationList_listWidget)


        self.gridLayout_3.addLayout(self.verticalLayout, 5, 2, 1, 1)

        self.labelList_label = QLabel(self.label_groupBox)
        self.labelList_label.setObjectName(u"labelList_label")

        self.gridLayout_3.addWidget(self.labelList_label, 0, 0, 1, 1)

        self.autoLable_pushButton = QPushButton(self.label_groupBox)
        self.autoLable_pushButton.setObjectName(u"autoLable_pushButton")
        self.autoLable_pushButton.setEnabled(False)
        self.autoLable_pushButton.setMinimumSize(QSize(0, 40))

        self.gridLayout_3.addWidget(self.autoLable_pushButton, 2, 0, 1, 3)


        self.gridLayout_10.addWidget(self.label_groupBox, 3, 0, 1, 1)

        self.position_pushButton = QPushButton(self.widget_3)
        self.position_pushButton.setObjectName(u"position_pushButton")
        self.position_pushButton.setEnabled(False)
        self.position_pushButton.setMinimumSize(QSize(0, 40))

        self.gridLayout_10.addWidget(self.position_pushButton, 0, 0, 1, 1)

        self.line_4 = QFrame(self.widget_3)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.gridLayout_10.addWidget(self.line_4, 2, 0, 1, 1)

        self.layerNo_comboBox = QComboBox(self.widget_3)
        self.layerNo_comboBox.addItem("")
        self.layerNo_comboBox.setObjectName(u"layerNo_comboBox")
        self.layerNo_comboBox.setEnabled(False)
        self.layerNo_comboBox.setMinimumSize(QSize(0, 40))

        self.gridLayout_10.addWidget(self.layerNo_comboBox, 1, 0, 1, 1)


        self.horizontalLayout_5.addWidget(self.widget_3)

        self.widget_6 = QWidget(self.tab_training)
        self.widget_6.setObjectName(u"widget_6")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.showImage_offline_graphicsView = DrawShapesGraphics(self.widget_6)
        self.showImage_offline_graphicsView.setObjectName(u"showImage_offline_graphicsView")

        self.horizontalLayout_3.addWidget(self.showImage_offline_graphicsView)


        self.horizontalLayout_5.addWidget(self.widget_6)

        self.widget_2 = QWidget(self.tab_training)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy8.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy8)
        self.widget_2.setMinimumSize(QSize(300, 0))
        self.gridLayout_9 = QGridLayout(self.widget_2)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.saveLabel_pushButton = QPushButton(self.widget_2)
        self.saveLabel_pushButton.setObjectName(u"saveLabel_pushButton")
        self.saveLabel_pushButton.setEnabled(False)
        self.saveLabel_pushButton.setMinimumSize(QSize(0, 40))
        self.saveLabel_pushButton.setStyleSheet(u"background-color: rgb(252, 202, 202);")

        self.gridLayout_9.addWidget(self.saveLabel_pushButton, 2, 0, 1, 1)

        self.labelInfo_groupBox = QGroupBox(self.widget_2)
        self.labelInfo_groupBox.setObjectName(u"labelInfo_groupBox")
        sizePolicy.setHeightForWidth(self.labelInfo_groupBox.sizePolicy().hasHeightForWidth())
        self.labelInfo_groupBox.setSizePolicy(sizePolicy)
        self.labelInfo_groupBox.setMinimumSize(QSize(300, 0))
        self.labelInfo_groupBox.setStyleSheet(u"QGroupBox{\n"
"border-width:1px;\n"
"border-style:solid;\n"
"border-radius: 10px;\n"
"border-color:gray;\n"
"margin-top:2.5ex;\n"
"}\n"
"QGroupBox::title{\n"
"subcontrol-origin:margin;\n"
"subcontrol-position:top center;\n"
"padding:0 1x;\n"
"}")
        self.gridLayout_5 = QGridLayout(self.labelInfo_groupBox)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.delete_pushButton = QPushButton(self.labelInfo_groupBox)
        self.delete_pushButton.setObjectName(u"delete_pushButton")
        self.delete_pushButton.setEnabled(False)
        self.delete_pushButton.setMinimumSize(QSize(0, 40))

        self.gridLayout_5.addWidget(self.delete_pushButton, 1, 0, 1, 2)

        self.labelInfo_tableWidget = QTableWidget(self.labelInfo_groupBox)
        if (self.labelInfo_tableWidget.columnCount() < 5):
            self.labelInfo_tableWidget.setColumnCount(5)
        font = QFont()
        font.setPointSize(8)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font);
        self.labelInfo_tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font);
        self.labelInfo_tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font);
        self.labelInfo_tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font);
        self.labelInfo_tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font);
        self.labelInfo_tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.labelInfo_tableWidget.setObjectName(u"labelInfo_tableWidget")
        sizePolicy9 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.labelInfo_tableWidget.sizePolicy().hasHeightForWidth())
        self.labelInfo_tableWidget.setSizePolicy(sizePolicy9)
        self.labelInfo_tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.labelInfo_tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.labelInfo_tableWidget.horizontalHeader().setMinimumSectionSize(30)

        self.gridLayout_5.addWidget(self.labelInfo_tableWidget, 0, 0, 1, 2)


        self.gridLayout_9.addWidget(self.labelInfo_groupBox, 0, 0, 1, 1)

        self.EditNote_pushButton = QPushButton(self.widget_2)
        self.EditNote_pushButton.setObjectName(u"EditNote_pushButton")
        self.EditNote_pushButton.setEnabled(False)
        self.EditNote_pushButton.setMinimumSize(QSize(0, 40))

        self.gridLayout_9.addWidget(self.EditNote_pushButton, 1, 0, 1, 1)


        self.horizontalLayout_5.addWidget(self.widget_2)


        self.gridLayout_16.addLayout(self.horizontalLayout_5, 2, 0, 1, 1)

        self.widget_5 = QWidget(self.tab_training)
        self.widget_5.setObjectName(u"widget_5")
        sizePolicy10 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.widget_5.sizePolicy().hasHeightForWidth())
        self.widget_5.setSizePolicy(sizePolicy10)
        self.widget_5.setMaximumSize(QSize(16777215, 150))
        self.gridLayout_15 = QGridLayout(self.widget_5)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.showImagelist_tableWidget = QTableWidget(self.widget_5)
        if (self.showImagelist_tableWidget.rowCount() < 3):
            self.showImagelist_tableWidget.setRowCount(3)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.showImagelist_tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.showImagelist_tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.showImagelist_tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem7)
        self.showImagelist_tableWidget.setObjectName(u"showImagelist_tableWidget")
        self.showImagelist_tableWidget.setEnabled(True)
        sizePolicy10.setHeightForWidth(self.showImagelist_tableWidget.sizePolicy().hasHeightForWidth())
        self.showImagelist_tableWidget.setSizePolicy(sizePolicy10)
        self.showImagelist_tableWidget.setMaximumSize(QSize(16777215, 150))
        self.showImagelist_tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.showImagelist_tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.showImagelist_tableWidget.setSelectionBehavior(QAbstractItemView.SelectColumns)
        self.showImagelist_tableWidget.setShowGrid(False)
        self.showImagelist_tableWidget.horizontalHeader().setVisible(False)
        self.showImagelist_tableWidget.horizontalHeader().setMinimumSectionSize(80)
        self.showImagelist_tableWidget.verticalHeader().setVisible(False)
        self.showImagelist_tableWidget.verticalHeader().setStretchLastSection(True)

        self.gridLayout_15.addWidget(self.showImagelist_tableWidget, 0, 1, 1, 1)

        self.widget_4 = QWidget(self.widget_5)
        self.widget_4.setObjectName(u"widget_4")
        sizePolicy3.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy3)
        self.widget_4.setMinimumSize(QSize(120, 0))
        self.widget_4.setMaximumSize(QSize(16777215, 150))
        self.verticalLayout_2 = QVBoxLayout(self.widget_4)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.next_pushButton = QPushButton(self.widget_4)
        self.next_pushButton.setObjectName(u"next_pushButton")
        self.next_pushButton.setEnabled(False)
        sizePolicy6.setHeightForWidth(self.next_pushButton.sizePolicy().hasHeightForWidth())
        self.next_pushButton.setSizePolicy(sizePolicy6)
        self.next_pushButton.setMinimumSize(QSize(0, 30))

        self.verticalLayout_2.addWidget(self.next_pushButton)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setSizeConstraint(QLayout.SetMinimumSize)
        self.page_label = QLabel(self.widget_4)
        self.page_label.setObjectName(u"page_label")
        self.page_label.setMaximumSize(QSize(50, 16777215))
        self.page_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.page_label)

        self.page_lineEdit = QLineEdit(self.widget_4)
        self.page_lineEdit.setObjectName(u"page_lineEdit")
        self.page_lineEdit.setEnabled(False)
        self.page_lineEdit.setMaximumSize(QSize(25, 16777215))
        self.page_lineEdit.setReadOnly(True)

        self.horizontalLayout_4.addWidget(self.page_lineEdit)

        self.pageOf_label = QLabel(self.widget_4)
        self.pageOf_label.setObjectName(u"pageOf_label")
        self.pageOf_label.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_4.addWidget(self.pageOf_label)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.back_pushButton = QPushButton(self.widget_4)
        self.back_pushButton.setObjectName(u"back_pushButton")
        self.back_pushButton.setEnabled(False)
        sizePolicy6.setHeightForWidth(self.back_pushButton.sizePolicy().hasHeightForWidth())
        self.back_pushButton.setSizePolicy(sizePolicy6)
        self.back_pushButton.setMinimumSize(QSize(0, 30))

        self.verticalLayout_2.addWidget(self.back_pushButton)


        self.gridLayout_15.addWidget(self.widget_4, 0, 2, 1, 1)

        self.golden_tableWidget = QTableWidget(self.widget_5)
        if (self.golden_tableWidget.rowCount() < 3):
            self.golden_tableWidget.setRowCount(3)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.golden_tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.golden_tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.golden_tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem10)
        self.golden_tableWidget.setObjectName(u"golden_tableWidget")
        self.golden_tableWidget.setMinimumSize(QSize(0, 0))
        self.golden_tableWidget.setMaximumSize(QSize(150, 16777215))
        self.golden_tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.golden_tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.golden_tableWidget.setSelectionBehavior(QAbstractItemView.SelectColumns)
        self.golden_tableWidget.setShowGrid(False)
        self.golden_tableWidget.horizontalHeader().setVisible(False)
        self.golden_tableWidget.horizontalHeader().setStretchLastSection(True)
        self.golden_tableWidget.verticalHeader().setVisible(False)
        self.golden_tableWidget.verticalHeader().setStretchLastSection(True)

        self.gridLayout_15.addWidget(self.golden_tableWidget, 0, 0, 1, 1)


        self.gridLayout_16.addWidget(self.widget_5, 3, 0, 1, 1)

        self.tabWidget.addTab(self.tab_training, "")
        self.tab_inspection = QWidget()
        self.tab_inspection.setObjectName(u"tab_inspection")
        self.horizontalLayout_30 = QHBoxLayout(self.tab_inspection)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.verticalLayout_22 = QVBoxLayout()
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.widget_13 = QWidget(self.tab_inspection)
        self.widget_13.setObjectName(u"widget_13")
        sizePolicy5.setHeightForWidth(self.widget_13.sizePolicy().hasHeightForWidth())
        self.widget_13.setSizePolicy(sizePolicy5)
        self.widget_13.setMaximumSize(QSize(16777215, 110))
        self.gridLayout_41 = QGridLayout(self.widget_13)
        self.gridLayout_41.setObjectName(u"gridLayout_41")
        self.goverify_easy_pushButton = QPushButton(self.widget_13)
        self.goverify_easy_pushButton.setObjectName(u"goverify_easy_pushButton")
        self.goverify_easy_pushButton.setEnabled(False)
        self.goverify_easy_pushButton.setMinimumSize(QSize(120, 80))
        self.goverify_easy_pushButton.setStyleSheet(u"background-color: rgb(79, 226, 239);\n"
"font: 16pt \"Ubuntu\";")

        self.gridLayout_41.addWidget(self.goverify_easy_pushButton, 0, 4, 1, 1)

        self.gridLayout_42 = QGridLayout()
        self.gridLayout_42.setObjectName(u"gridLayout_42")
        self.model_easy_label = QLabel(self.widget_13)
        self.model_easy_label.setObjectName(u"model_easy_label")
        sizePolicy1.setHeightForWidth(self.model_easy_label.sizePolicy().hasHeightForWidth())
        self.model_easy_label.setSizePolicy(sizePolicy1)
        self.model_easy_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_42.addWidget(self.model_easy_label, 2, 0, 1, 1)

        self.sn_easy_label = QLabel(self.widget_13)
        self.sn_easy_label.setObjectName(u"sn_easy_label")
        sizePolicy1.setHeightForWidth(self.sn_easy_label.sizePolicy().hasHeightForWidth())
        self.sn_easy_label.setSizePolicy(sizePolicy1)
        self.sn_easy_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_42.addWidget(self.sn_easy_label, 1, 0, 1, 1)

        self.device_easy_comboBox = QComboBox(self.widget_13)
        self.device_easy_comboBox.addItem("")
        self.device_easy_comboBox.addItem("")
        self.device_easy_comboBox.addItem("")
        self.device_easy_comboBox.setObjectName(u"device_easy_comboBox")
        sizePolicy5.setHeightForWidth(self.device_easy_comboBox.sizePolicy().hasHeightForWidth())
        self.device_easy_comboBox.setSizePolicy(sizePolicy5)
        self.device_easy_comboBox.setMaximumSize(QSize(200, 16777215))

        self.gridLayout_42.addWidget(self.device_easy_comboBox, 0, 1, 1, 1)

        self.device_easy_label = QLabel(self.widget_13)
        self.device_easy_label.setObjectName(u"device_easy_label")
        sizePolicy1.setHeightForWidth(self.device_easy_label.sizePolicy().hasHeightForWidth())
        self.device_easy_label.setSizePolicy(sizePolicy1)
        self.device_easy_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_42.addWidget(self.device_easy_label, 0, 0, 1, 1)

        self.model_easy_lineEdit = QLineEdit(self.widget_13)
        self.model_easy_lineEdit.setObjectName(u"model_easy_lineEdit")
        sizePolicy1.setHeightForWidth(self.model_easy_lineEdit.sizePolicy().hasHeightForWidth())
        self.model_easy_lineEdit.setSizePolicy(sizePolicy1)
        self.model_easy_lineEdit.setMinimumSize(QSize(180, 0))
        self.model_easy_lineEdit.setMaximumSize(QSize(250, 16777215))

        self.gridLayout_42.addWidget(self.model_easy_lineEdit, 2, 1, 1, 1)

        self.sn_easy_lineEdit = QLineEdit(self.widget_13)
        self.sn_easy_lineEdit.setObjectName(u"sn_easy_lineEdit")
        sizePolicy1.setHeightForWidth(self.sn_easy_lineEdit.sizePolicy().hasHeightForWidth())
        self.sn_easy_lineEdit.setSizePolicy(sizePolicy1)
        self.sn_easy_lineEdit.setMinimumSize(QSize(180, 0))
        self.sn_easy_lineEdit.setMaximumSize(QSize(250, 16777215))

        self.gridLayout_42.addWidget(self.sn_easy_lineEdit, 1, 1, 1, 1)


        self.gridLayout_41.addLayout(self.gridLayout_42, 0, 0, 2, 1)

        self.horizontalSpacer_27 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_41.addItem(self.horizontalSpacer_27, 0, 1, 1, 1)

        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.on_off_easy_label = QLabel(self.widget_13)
        self.on_off_easy_label.setObjectName(u"on_off_easy_label")
        self.on_off_easy_label.setEnabled(False)
        self.on_off_easy_label.setStyleSheet(u"font: 13pt \"Ubuntu\";")

        self.horizontalLayout_25.addWidget(self.on_off_easy_label)

        self.on_off_easy_checkBox = Toggle(self.widget_13)
        self.on_off_easy_checkBox.setObjectName(u"on_off_easy_checkBox")
        self.on_off_easy_checkBox.setEnabled(False)
        self.on_off_easy_checkBox.setMinimumSize(QSize(70, 0))
        self.on_off_easy_checkBox.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_25.addWidget(self.on_off_easy_checkBox)


        self.verticalLayout_19.addLayout(self.horizontalLayout_25)

        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.status_Label_3 = QLabel(self.widget_13)
        self.status_Label_3.setObjectName(u"status_Label_3")
        sizePolicy5.setHeightForWidth(self.status_Label_3.sizePolicy().hasHeightForWidth())
        self.status_Label_3.setSizePolicy(sizePolicy5)
        self.status_Label_3.setStyleSheet(u"font: 13pt \"Ubuntu\";")
        self.status_Label_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_26.addWidget(self.status_Label_3)

        self.cameraStatus_easy_label = QLabel(self.widget_13)
        self.cameraStatus_easy_label.setObjectName(u"cameraStatus_easy_label")
        sizePolicy5.setHeightForWidth(self.cameraStatus_easy_label.sizePolicy().hasHeightForWidth())
        self.cameraStatus_easy_label.setSizePolicy(sizePolicy5)
        self.cameraStatus_easy_label.setStyleSheet(u"font: 13pt \"Ubuntu\";")

        self.horizontalLayout_26.addWidget(self.cameraStatus_easy_label)


        self.verticalLayout_19.addLayout(self.horizontalLayout_26)


        self.gridLayout_41.addLayout(self.verticalLayout_19, 0, 2, 1, 1)

        self.PASS_easy_label = QLabel(self.widget_13)
        self.PASS_easy_label.setObjectName(u"PASS_easy_label")
        self.PASS_easy_label.setStyleSheet(u"font: 36pt;\n"
"color: rgb(78, 154, 6);")

        self.gridLayout_41.addWidget(self.PASS_easy_label, 0, 8, 1, 1)

        self.FAIL_easy_label = QLabel(self.widget_13)
        self.FAIL_easy_label.setObjectName(u"FAIL_easy_label")
        self.FAIL_easy_label.setMinimumSize(QSize(120, 0))
        self.FAIL_easy_label.setStyleSheet(u"font: 36pt;\n"
"color: rgb(204, 0, 0);")
        self.FAIL_easy_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_41.addWidget(self.FAIL_easy_label, 0, 7, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 3, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_41.addItem(self.verticalSpacer_3, 1, 2, 1, 1)

        self.horizontalSpacer_28 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_41.addItem(self.horizontalSpacer_28, 0, 6, 1, 1)

        self.horizontalSpacer_29 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_41.addItem(self.horizontalSpacer_29, 0, 3, 1, 1)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_41.addItem(self.horizontalSpacer_11, 0, 9, 1, 1)


        self.verticalLayout_22.addWidget(self.widget_13)

        self.widget_16 = QWidget(self.tab_inspection)
        self.widget_16.setObjectName(u"widget_16")
        self.verticalLayout_20 = QVBoxLayout(self.widget_16)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.showFocus_easy_graphicsView = DrawShapesGraphics(self.widget_16)
        self.showFocus_easy_graphicsView.setObjectName(u"showFocus_easy_graphicsView")

        self.verticalLayout_20.addWidget(self.showFocus_easy_graphicsView)


        self.verticalLayout_22.addWidget(self.widget_16)


        self.horizontalLayout_30.addLayout(self.verticalLayout_22)

        self.widget_17 = QWidget(self.tab_inspection)
        self.widget_17.setObjectName(u"widget_17")
        sizePolicy5.setHeightForWidth(self.widget_17.sizePolicy().hasHeightForWidth())
        self.widget_17.setSizePolicy(sizePolicy5)
        self.widget_17.setMinimumSize(QSize(380, 0))
        self.widget_17.setMaximumSize(QSize(500, 16777215))
        self.gridLayout_45 = QGridLayout(self.widget_17)
        self.gridLayout_45.setObjectName(u"gridLayout_45")
        self.inspect_groupBox_4 = QGroupBox(self.widget_17)
        self.inspect_groupBox_4.setObjectName(u"inspect_groupBox_4")
        sizePolicy5.setHeightForWidth(self.inspect_groupBox_4.sizePolicy().hasHeightForWidth())
        self.inspect_groupBox_4.setSizePolicy(sizePolicy5)
        self.inspect_groupBox_4.setMinimumSize(QSize(350, 0))
        self.inspect_groupBox_4.setStyleSheet(u"QGroupBox{\n"
"border-width:1px;\n"
"border-style:solid;\n"
"border-radius: 10px;\n"
"border-color:gray;\n"
"margin-top:2.5ex;\n"
"}\n"
"QGroupBox::title{\n"
"subcontrol-origin:margin;\n"
"subcontrol-position:top center;\n"
"padding:0 1px;\n"
"}")
        self.inspect_groupBox_4.setCheckable(False)
        self.verticalLayout_21 = QVBoxLayout(self.inspect_groupBox_4)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.horizontalLayout_29 = QHBoxLayout()
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.onlyNG_easy_checkBox = QCheckBox(self.inspect_groupBox_4)
        self.onlyNG_easy_checkBox.setObjectName(u"onlyNG_easy_checkBox")
        self.onlyNG_easy_checkBox.setChecked(True)

        self.horizontalLayout_29.addWidget(self.onlyNG_easy_checkBox)

        self.horizontalSpacer_22 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_29.addItem(self.horizontalSpacer_22)

        self.skip_easy_pushButton = QPushButton(self.inspect_groupBox_4)
        self.skip_easy_pushButton.setObjectName(u"skip_easy_pushButton")
        self.skip_easy_pushButton.setEnabled(False)
        self.skip_easy_pushButton.setMinimumSize(QSize(0, 40))

        self.horizontalLayout_29.addWidget(self.skip_easy_pushButton)


        self.verticalLayout_21.addLayout(self.horizontalLayout_29)

        self.inspectResult_easy_tableWidget = QTableWidget(self.inspect_groupBox_4)
        if (self.inspectResult_easy_tableWidget.columnCount() < 4):
            self.inspectResult_easy_tableWidget.setColumnCount(4)
        __qtablewidgetitem11 = QTableWidgetItem()
        __qtablewidgetitem11.setFont(font);
        self.inspectResult_easy_tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        __qtablewidgetitem12.setFont(font);
        self.inspectResult_easy_tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        __qtablewidgetitem13.setFont(font);
        self.inspectResult_easy_tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        __qtablewidgetitem14.setFont(font);
        self.inspectResult_easy_tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem14)
        self.inspectResult_easy_tableWidget.setObjectName(u"inspectResult_easy_tableWidget")
        sizePolicy2.setHeightForWidth(self.inspectResult_easy_tableWidget.sizePolicy().hasHeightForWidth())
        self.inspectResult_easy_tableWidget.setSizePolicy(sizePolicy2)
        self.inspectResult_easy_tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.inspectResult_easy_tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.inspectResult_easy_tableWidget.horizontalHeader().setDefaultSectionSize(80)
        self.inspectResult_easy_tableWidget.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_21.addWidget(self.inspectResult_easy_tableWidget)

        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.back_easy_pushButton = QPushButton(self.inspect_groupBox_4)
        self.back_easy_pushButton.setObjectName(u"back_easy_pushButton")
        self.back_easy_pushButton.setEnabled(False)
        self.back_easy_pushButton.setMinimumSize(QSize(0, 40))

        self.horizontalLayout_28.addWidget(self.back_easy_pushButton)

        self.horizontalSpacer_32 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_28.addItem(self.horizontalSpacer_32)

        self.next_easy_pushButton = QPushButton(self.inspect_groupBox_4)
        self.next_easy_pushButton.setObjectName(u"next_easy_pushButton")
        self.next_easy_pushButton.setEnabled(False)
        self.next_easy_pushButton.setMinimumSize(QSize(0, 40))

        self.horizontalLayout_28.addWidget(self.next_easy_pushButton)


        self.verticalLayout_21.addLayout(self.horizontalLayout_28)


        self.gridLayout_45.addWidget(self.inspect_groupBox_4, 0, 0, 1, 1)

        self.showOverall_easy_graphicsView = DrawShapesGraphics(self.widget_17)
        self.showOverall_easy_graphicsView.setObjectName(u"showOverall_easy_graphicsView")
        sizePolicy2.setHeightForWidth(self.showOverall_easy_graphicsView.sizePolicy().hasHeightForWidth())
        self.showOverall_easy_graphicsView.setSizePolicy(sizePolicy2)
        self.showOverall_easy_graphicsView.setMinimumSize(QSize(0, 250))

        self.gridLayout_45.addWidget(self.showOverall_easy_graphicsView, 1, 0, 1, 1)

        self.submit_easy_pushButton = QPushButton(self.widget_17)
        self.submit_easy_pushButton.setObjectName(u"submit_easy_pushButton")
        self.submit_easy_pushButton.setEnabled(False)
        self.submit_easy_pushButton.setMinimumSize(QSize(200, 60))
        self.submit_easy_pushButton.setStyleSheet(u"background-color: rgb(251, 235, 145);\n"
"font: 16pt \"Ubuntu\";")

        self.gridLayout_45.addWidget(self.submit_easy_pushButton, 2, 0, 1, 1)


        self.horizontalLayout_30.addWidget(self.widget_17)

        self.tabWidget.addTab(self.tab_inspection, "")
        self.tab_reconfirm = QWidget()
        self.tab_reconfirm.setObjectName(u"tab_reconfirm")
        self.gridLayout_44 = QGridLayout(self.tab_reconfirm)
        self.gridLayout_44.setObjectName(u"gridLayout_44")
        self.widget_15 = QWidget(self.tab_reconfirm)
        self.widget_15.setObjectName(u"widget_15")
        self.gridLayout_43 = QGridLayout(self.widget_15)
        self.gridLayout_43.setObjectName(u"gridLayout_43")
        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.showimage_confirm_graphicsView = DrawShapesGraphics(self.widget_15)
        self.showimage_confirm_graphicsView.setObjectName(u"showimage_confirm_graphicsView")

        self.verticalLayout_18.addWidget(self.showimage_confirm_graphicsView)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalSpacer_24 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_23.addItem(self.horizontalSpacer_24)

        self.fail_confirm_pushButton = QPushButton(self.widget_15)
        self.fail_confirm_pushButton.setObjectName(u"fail_confirm_pushButton")
        self.fail_confirm_pushButton.setEnabled(False)
        self.fail_confirm_pushButton.setMinimumSize(QSize(120, 60))
        self.fail_confirm_pushButton.setStyleSheet(u"font: 16pt \"Ubuntu\";\n"
"background-color: rgb(252, 202, 202);")

        self.horizontalLayout_23.addWidget(self.fail_confirm_pushButton)

        self.horizontalSpacer_23 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_23.addItem(self.horizontalSpacer_23)

        self.repass_confirm_pushButton = QPushButton(self.widget_15)
        self.repass_confirm_pushButton.setObjectName(u"repass_confirm_pushButton")
        self.repass_confirm_pushButton.setEnabled(False)
        self.repass_confirm_pushButton.setMinimumSize(QSize(120, 60))
        self.repass_confirm_pushButton.setStyleSheet(u"font: 16pt \"Ubuntu\";\n"
"background-color: rgb(205, 249, 161);")

        self.horizontalLayout_23.addWidget(self.repass_confirm_pushButton)

        self.horizontalSpacer_25 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_23.addItem(self.horizontalSpacer_25)


        self.verticalLayout_18.addLayout(self.horizontalLayout_23)


        self.gridLayout_43.addLayout(self.verticalLayout_18, 0, 0, 1, 1)


        self.gridLayout_44.addWidget(self.widget_15, 0, 0, 1, 1)

        self.widget_14 = QWidget(self.tab_reconfirm)
        self.widget_14.setObjectName(u"widget_14")
        self.gridLayout_40 = QGridLayout(self.widget_14)
        self.gridLayout_40.setObjectName(u"gridLayout_40")
        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.horizontalLayout_31 = QHBoxLayout()
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.gridLayout_38 = QGridLayout()
        self.gridLayout_38.setObjectName(u"gridLayout_38")
        self.sn_confirm_lineEdit = QLineEdit(self.widget_14)
        self.sn_confirm_lineEdit.setObjectName(u"sn_confirm_lineEdit")
        sizePolicy5.setHeightForWidth(self.sn_confirm_lineEdit.sizePolicy().hasHeightForWidth())
        self.sn_confirm_lineEdit.setSizePolicy(sizePolicy5)

        self.gridLayout_38.addWidget(self.sn_confirm_lineEdit, 0, 1, 1, 1)

        self.model_confirm_lineEdit = QLineEdit(self.widget_14)
        self.model_confirm_lineEdit.setObjectName(u"model_confirm_lineEdit")
        sizePolicy5.setHeightForWidth(self.model_confirm_lineEdit.sizePolicy().hasHeightForWidth())
        self.model_confirm_lineEdit.setSizePolicy(sizePolicy5)

        self.gridLayout_38.addWidget(self.model_confirm_lineEdit, 1, 1, 1, 1)

        self.sn_online_label_3 = QLabel(self.widget_14)
        self.sn_online_label_3.setObjectName(u"sn_online_label_3")
        self.sn_online_label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_38.addWidget(self.sn_online_label_3, 0, 0, 1, 1)

        self.model_online_label_3 = QLabel(self.widget_14)
        self.model_online_label_3.setObjectName(u"model_online_label_3")
        self.model_online_label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_38.addWidget(self.model_online_label_3, 1, 0, 1, 1)


        self.horizontalLayout_31.addLayout(self.gridLayout_38)

        self.reset_confirm_pushButton = QPushButton(self.widget_14)
        self.reset_confirm_pushButton.setObjectName(u"reset_confirm_pushButton")
        self.reset_confirm_pushButton.setEnabled(False)
        self.reset_confirm_pushButton.setMinimumSize(QSize(0, 50))

        self.horizontalLayout_31.addWidget(self.reset_confirm_pushButton)


        self.verticalLayout_17.addLayout(self.horizontalLayout_31)

        self.line_19 = QFrame(self.widget_14)
        self.line_19.setObjectName(u"line_19")
        self.line_19.setFrameShape(QFrame.HLine)
        self.line_19.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_17.addWidget(self.line_19)

        self.inspect_groupBox_3 = QGroupBox(self.widget_14)
        self.inspect_groupBox_3.setObjectName(u"inspect_groupBox_3")
        sizePolicy.setHeightForWidth(self.inspect_groupBox_3.sizePolicy().hasHeightForWidth())
        self.inspect_groupBox_3.setSizePolicy(sizePolicy)
        self.inspect_groupBox_3.setMinimumSize(QSize(350, 0))
        self.inspect_groupBox_3.setMaximumSize(QSize(350, 16777215))
        self.inspect_groupBox_3.setStyleSheet(u"QGroupBox{\n"
"border-width:1px;\n"
"border-style:solid;\n"
"border-radius: 10px;\n"
"border-color:gray;\n"
"margin-top:2.5ex;\n"
"}\n"
"QGroupBox::title{\n"
"subcontrol-origin:margin;\n"
"subcontrol-position:top center;\n"
"padding:0 1px;\n"
"}")
        self.inspect_groupBox_3.setCheckable(False)
        self.gridLayout_39 = QGridLayout(self.inspect_groupBox_3)
        self.gridLayout_39.setObjectName(u"gridLayout_39")
        self.inspectResult_confirm_tableWidget = QTableWidget(self.inspect_groupBox_3)
        if (self.inspectResult_confirm_tableWidget.columnCount() < 4):
            self.inspectResult_confirm_tableWidget.setColumnCount(4)
        __qtablewidgetitem15 = QTableWidgetItem()
        __qtablewidgetitem15.setFont(font);
        self.inspectResult_confirm_tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        __qtablewidgetitem16.setFont(font);
        self.inspectResult_confirm_tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        __qtablewidgetitem17.setFont(font);
        self.inspectResult_confirm_tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        __qtablewidgetitem18.setFont(font);
        self.inspectResult_confirm_tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem18)
        self.inspectResult_confirm_tableWidget.setObjectName(u"inspectResult_confirm_tableWidget")
        sizePolicy2.setHeightForWidth(self.inspectResult_confirm_tableWidget.sizePolicy().hasHeightForWidth())
        self.inspectResult_confirm_tableWidget.setSizePolicy(sizePolicy2)
        self.inspectResult_confirm_tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.inspectResult_confirm_tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.inspectResult_confirm_tableWidget.horizontalHeader().setDefaultSectionSize(80)
        self.inspectResult_confirm_tableWidget.horizontalHeader().setStretchLastSection(True)

        self.gridLayout_39.addWidget(self.inspectResult_confirm_tableWidget, 0, 0, 1, 2)

        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.back_confirm_pushButton = QPushButton(self.inspect_groupBox_3)
        self.back_confirm_pushButton.setObjectName(u"back_confirm_pushButton")
        self.back_confirm_pushButton.setEnabled(False)
        self.back_confirm_pushButton.setMinimumSize(QSize(0, 40))

        self.horizontalLayout_24.addWidget(self.back_confirm_pushButton)

        self.horizontalSpacer_26 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_26)

        self.next_confirm_pushButton = QPushButton(self.inspect_groupBox_3)
        self.next_confirm_pushButton.setObjectName(u"next_confirm_pushButton")
        self.next_confirm_pushButton.setEnabled(False)
        self.next_confirm_pushButton.setMinimumSize(QSize(0, 40))

        self.horizontalLayout_24.addWidget(self.next_confirm_pushButton)


        self.gridLayout_39.addLayout(self.horizontalLayout_24, 2, 0, 1, 2)


        self.verticalLayout_17.addWidget(self.inspect_groupBox_3)

        self.line_20 = QFrame(self.widget_14)
        self.line_20.setObjectName(u"line_20")
        self.line_20.setFrameShape(QFrame.HLine)
        self.line_20.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_17.addWidget(self.line_20)

        self.showOverall_confirm_graphicsView = DrawShapesGraphics(self.widget_14)
        self.showOverall_confirm_graphicsView.setObjectName(u"showOverall_confirm_graphicsView")
        sizePolicy9.setHeightForWidth(self.showOverall_confirm_graphicsView.sizePolicy().hasHeightForWidth())
        self.showOverall_confirm_graphicsView.setSizePolicy(sizePolicy9)
        self.showOverall_confirm_graphicsView.setMinimumSize(QSize(0, 250))

        self.verticalLayout_17.addWidget(self.showOverall_confirm_graphicsView)

        self.submit_confirm_pushButton = QPushButton(self.widget_14)
        self.submit_confirm_pushButton.setObjectName(u"submit_confirm_pushButton")
        self.submit_confirm_pushButton.setEnabled(False)
        self.submit_confirm_pushButton.setMinimumSize(QSize(0, 60))
        self.submit_confirm_pushButton.setStyleSheet(u"background-color: rgb(251, 235, 145);\n"
"font: 16pt \"Ubuntu\";")

        self.verticalLayout_17.addWidget(self.submit_confirm_pushButton)


        self.gridLayout_40.addLayout(self.verticalLayout_17, 0, 0, 1, 1)


        self.gridLayout_44.addWidget(self.widget_14, 0, 1, 1, 1)

        self.tabWidget.addTab(self.tab_reconfirm, "")
        self.tab_online = QWidget()
        self.tab_online.setObjectName(u"tab_online")
        self.gridLayout_6 = QGridLayout(self.tab_online)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.on_off_checkBox = Toggle(self.tab_online)
        self.on_off_checkBox.setObjectName(u"on_off_checkBox")
        self.on_off_checkBox.setEnabled(False)
        self.on_off_checkBox.setMinimumSize(QSize(70, 0))
        self.on_off_checkBox.setLayoutDirection(Qt.LeftToRight)

        self.gridLayout_6.addWidget(self.on_off_checkBox, 0, 1, 1, 1)

        self.on_off_label = QLabel(self.tab_online)
        self.on_off_label.setObjectName(u"on_off_label")
        self.on_off_label.setEnabled(False)
        self.on_off_label.setStyleSheet(u"font: 13pt \"Ubuntu\";")

        self.gridLayout_6.addWidget(self.on_off_label, 0, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(654, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer, 0, 2, 1, 1)

        self.showimage_online_graphicsView = DrawShapesGraphics(self.tab_online)
        self.showimage_online_graphicsView.setObjectName(u"showimage_online_graphicsView")

        self.gridLayout_6.addWidget(self.showimage_online_graphicsView, 1, 0, 1, 3)

        self.widget = QWidget(self.tab_online)
        self.widget.setObjectName(u"widget")
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMaximumSize(QSize(360, 16777215))
        self.gridLayout_4 = QGridLayout(self.widget)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.sn_online_label = QLabel(self.widget)
        self.sn_online_label.setObjectName(u"sn_online_label")
        self.sn_online_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.sn_online_label, 2, 0, 1, 1)

        self.model_lineEdit = QLineEdit(self.widget)
        self.model_lineEdit.setObjectName(u"model_lineEdit")

        self.gridLayout.addWidget(self.model_lineEdit, 3, 1, 1, 1)

        self.device_online_label = QLabel(self.widget)
        self.device_online_label.setObjectName(u"device_online_label")
        self.device_online_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.device_online_label, 1, 0, 1, 1)

        self.model_online_label = QLabel(self.widget)
        self.model_online_label.setObjectName(u"model_online_label")
        self.model_online_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.model_online_label, 3, 0, 1, 1)

        self.sn_online_lineEdit = QLineEdit(self.widget)
        self.sn_online_lineEdit.setObjectName(u"sn_online_lineEdit")
        sizePolicy5.setHeightForWidth(self.sn_online_lineEdit.sizePolicy().hasHeightForWidth())
        self.sn_online_lineEdit.setSizePolicy(sizePolicy5)

        self.gridLayout.addWidget(self.sn_online_lineEdit, 2, 1, 1, 1)

        self.device_online_comboBox = QComboBox(self.widget)
        self.device_online_comboBox.addItem("")
        self.device_online_comboBox.addItem("")
        self.device_online_comboBox.setObjectName(u"device_online_comboBox")
        sizePolicy1.setHeightForWidth(self.device_online_comboBox.sizePolicy().hasHeightForWidth())
        self.device_online_comboBox.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.device_online_comboBox, 1, 1, 1, 1)

        self.status_Label = QLabel(self.widget)
        self.status_Label.setObjectName(u"status_Label")
        self.status_Label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.status_Label, 0, 0, 1, 1)

        self.currentstatus_label = QLabel(self.widget)
        self.currentstatus_label.setObjectName(u"currentstatus_label")

        self.gridLayout.addWidget(self.currentstatus_label, 0, 1, 1, 1)


        self.gridLayout_4.addLayout(self.gridLayout, 0, 0, 1, 2)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_4.addItem(self.verticalSpacer, 1, 0, 1, 1)

        self.inspect_groupBox = QGroupBox(self.widget)
        self.inspect_groupBox.setObjectName(u"inspect_groupBox")
        sizePolicy.setHeightForWidth(self.inspect_groupBox.sizePolicy().hasHeightForWidth())
        self.inspect_groupBox.setSizePolicy(sizePolicy)
        self.inspect_groupBox.setMinimumSize(QSize(350, 0))
        self.inspect_groupBox.setMaximumSize(QSize(350, 16777215))
        self.inspect_groupBox.setStyleSheet(u"QGroupBox{\n"
"border-width:1px;\n"
"border-style:solid;\n"
"border-radius: 10px;\n"
"border-color:gray;\n"
"margin-top:2.5ex;\n"
"}\n"
"QGroupBox::title{\n"
"subcontrol-origin:margin;\n"
"subcontrol-position:top center;\n"
"padding:0 1px;\n"
"}")
        self.inspect_groupBox.setCheckable(False)
        self.gridLayout_2 = QGridLayout(self.inspect_groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.PASS_label = QLabel(self.inspect_groupBox)
        self.PASS_label.setObjectName(u"PASS_label")
        self.PASS_label.setMinimumSize(QSize(120, 0))
        self.PASS_label.setStyleSheet(u"font: 20pt;\n"
"color: rgb(78, 154, 6);")
        self.PASS_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.PASS_label, 0, 3, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_3, 0, 1, 1, 1)

        self.inspectResult_tableWidget = QTableWidget(self.inspect_groupBox)
        if (self.inspectResult_tableWidget.columnCount() < 5):
            self.inspectResult_tableWidget.setColumnCount(5)
        __qtablewidgetitem19 = QTableWidgetItem()
        __qtablewidgetitem19.setFont(font);
        self.inspectResult_tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        __qtablewidgetitem20.setFont(font);
        self.inspectResult_tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        __qtablewidgetitem21.setFont(font);
        self.inspectResult_tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        __qtablewidgetitem22.setFont(font);
        self.inspectResult_tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        __qtablewidgetitem23.setFont(font);
        self.inspectResult_tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem23)
        self.inspectResult_tableWidget.setObjectName(u"inspectResult_tableWidget")
        sizePolicy2.setHeightForWidth(self.inspectResult_tableWidget.sizePolicy().hasHeightForWidth())
        self.inspectResult_tableWidget.setSizePolicy(sizePolicy2)
        self.inspectResult_tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.inspectResult_tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.inspectResult_tableWidget.horizontalHeader().setDefaultSectionSize(80)
        self.inspectResult_tableWidget.horizontalHeader().setStretchLastSection(True)

        self.gridLayout_2.addWidget(self.inspectResult_tableWidget, 1, 0, 1, 4)

        self.goverify_pushButton = QPushButton(self.inspect_groupBox)
        self.goverify_pushButton.setObjectName(u"goverify_pushButton")
        self.goverify_pushButton.setEnabled(False)
        self.goverify_pushButton.setMinimumSize(QSize(0, 40))
        self.goverify_pushButton.setStyleSheet(u"background-color: rgb(79, 226, 239);")

        self.gridLayout_2.addWidget(self.goverify_pushButton, 0, 0, 1, 1)

        self.FAIL_label = QLabel(self.inspect_groupBox)
        self.FAIL_label.setObjectName(u"FAIL_label")
        self.FAIL_label.setMinimumSize(QSize(120, 0))
        self.FAIL_label.setStyleSheet(u"font: 20pt;\n"
"color: rgb(204, 0, 0);")
        self.FAIL_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.FAIL_label, 0, 2, 1, 1)


        self.gridLayout_4.addWidget(self.inspect_groupBox, 2, 0, 1, 2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.reset_pushButton = QPushButton(self.widget)
        self.reset_pushButton.setObjectName(u"reset_pushButton")
        self.reset_pushButton.setEnabled(False)
        self.reset_pushButton.setMinimumSize(QSize(0, 40))

        self.horizontalLayout.addWidget(self.reset_pushButton)

        self.horizontalSpacer_4 = QSpacerItem(57, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)

        self.submit_pushButton = QPushButton(self.widget)
        self.submit_pushButton.setObjectName(u"submit_pushButton")
        self.submit_pushButton.setEnabled(False)
        self.submit_pushButton.setMinimumSize(QSize(0, 40))
        self.submit_pushButton.setStyleSheet(u"background-color: rgb(205, 249, 161);")

        self.horizontalLayout.addWidget(self.submit_pushButton)


        self.gridLayout_4.addLayout(self.horizontalLayout, 3, 0, 1, 2)


        self.gridLayout_6.addWidget(self.widget, 0, 3, 2, 1)

        self.tabWidget.addTab(self.tab_online, "")
        self.tab_sop = QWidget()
        self.tab_sop.setObjectName(u"tab_sop")
        self.horizontalLayout_16 = QHBoxLayout(self.tab_sop)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.widget_8 = QWidget(self.tab_sop)
        self.widget_8.setObjectName(u"widget_8")
        self.gridLayout_23 = QGridLayout(self.widget_8)
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.verticalSpacer_4 = QSpacerItem(20, 15, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_23.addItem(self.verticalSpacer_4, 0, 0, 1, 1)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.play_SOP_pushButton = QPushButton(self.widget_8)
        self.play_SOP_pushButton.setObjectName(u"play_SOP_pushButton")
        self.play_SOP_pushButton.setEnabled(False)
        self.play_SOP_pushButton.setMinimumSize(QSize(100, 40))
        font1 = QFont()
        font1.setPointSize(13)
        self.play_SOP_pushButton.setFont(font1)
        self.play_SOP_pushButton.setStyleSheet(u"background-color: rgb(205, 249, 161);")

        self.horizontalLayout_14.addWidget(self.play_SOP_pushButton)

        self.pause_SOP_pushButton = QPushButton(self.widget_8)
        self.pause_SOP_pushButton.setObjectName(u"pause_SOP_pushButton")
        self.pause_SOP_pushButton.setEnabled(False)
        self.pause_SOP_pushButton.setMinimumSize(QSize(100, 40))
        self.pause_SOP_pushButton.setFont(font1)
        self.pause_SOP_pushButton.setStyleSheet(u"background-color: rgb(251, 235, 145);")

        self.horizontalLayout_14.addWidget(self.pause_SOP_pushButton)

        self.stop_SOP_pushButton = QPushButton(self.widget_8)
        self.stop_SOP_pushButton.setObjectName(u"stop_SOP_pushButton")
        self.stop_SOP_pushButton.setEnabled(False)
        self.stop_SOP_pushButton.setMinimumSize(QSize(100, 40))
        self.stop_SOP_pushButton.setFont(font1)
        self.stop_SOP_pushButton.setStyleSheet(u"background-color: rgb(249, 122, 122);")

        self.horizontalLayout_14.addWidget(self.stop_SOP_pushButton)


        self.gridLayout_23.addLayout(self.horizontalLayout_14, 1, 2, 1, 1)

        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_23.addItem(self.horizontalSpacer_15, 1, 3, 1, 1)

        self.state_SOP_label = QLabel(self.widget_8)
        self.state_SOP_label.setObjectName(u"state_SOP_label")
        self.state_SOP_label.setMinimumSize(QSize(150, 80))
        self.state_SOP_label.setStyleSheet(u"background-color: red; color: white; font-size: 24px;")
        self.state_SOP_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_23.addWidget(self.state_SOP_label, 0, 5, 3, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 15, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_23.addItem(self.verticalSpacer_2, 2, 0, 1, 1)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_23.addItem(self.horizontalSpacer_12, 1, 1, 1, 1)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.gridLayout_20 = QGridLayout()
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.sn_SOP_label = QLabel(self.widget_8)
        self.sn_SOP_label.setObjectName(u"sn_SOP_label")
        self.sn_SOP_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_20.addWidget(self.sn_SOP_label, 1, 0, 1, 1)

        self.sn_SOP_lineEdit = QLineEdit(self.widget_8)
        self.sn_SOP_lineEdit.setObjectName(u"sn_SOP_lineEdit")
        sizePolicy5.setHeightForWidth(self.sn_SOP_lineEdit.sizePolicy().hasHeightForWidth())
        self.sn_SOP_lineEdit.setSizePolicy(sizePolicy5)
        self.sn_SOP_lineEdit.setMinimumSize(QSize(0, 36))

        self.gridLayout_20.addWidget(self.sn_SOP_lineEdit, 1, 1, 1, 1)


        self.verticalLayout_11.addLayout(self.gridLayout_20)


        self.horizontalLayout_15.addLayout(self.verticalLayout_11)

        self.horizontalSpacer_14 = QSpacerItem(13, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_14)

        self.start_SOP_pushButton = QPushButton(self.widget_8)
        self.start_SOP_pushButton.setObjectName(u"start_SOP_pushButton")
        self.start_SOP_pushButton.setEnabled(False)
        self.start_SOP_pushButton.setMinimumSize(QSize(100, 40))
        self.start_SOP_pushButton.setFont(font1)
        self.start_SOP_pushButton.setStyleSheet(u"background-color: rgb(204, 251, 244);")

        self.horizontalLayout_15.addWidget(self.start_SOP_pushButton)


        self.gridLayout_23.addLayout(self.horizontalLayout_15, 1, 0, 1, 1)


        self.verticalLayout_9.addWidget(self.widget_8)

        self.widget_9 = QWidget(self.tab_sop)
        self.widget_9.setObjectName(u"widget_9")
        self.gridLayout_22 = QGridLayout(self.widget_9)
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.showImage_SOP_graphicsView = DrawShapesGraphics(self.widget_9)
        self.showImage_SOP_graphicsView.setObjectName(u"showImage_SOP_graphicsView")

        self.gridLayout_22.addWidget(self.showImage_SOP_graphicsView, 0, 0, 1, 1)


        self.verticalLayout_9.addWidget(self.widget_9)


        self.horizontalLayout_16.addLayout(self.verticalLayout_9)

        self.widget_7 = QWidget(self.tab_sop)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setMaximumSize(QSize(350, 16777215))
        self.gridLayout_21 = QGridLayout(self.widget_7)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.Image_SOP_label = QLabel(self.widget_7)
        self.Image_SOP_label.setObjectName(u"Image_SOP_label")
        sizePolicy2.setHeightForWidth(self.Image_SOP_label.sizePolicy().hasHeightForWidth())
        self.Image_SOP_label.setSizePolicy(sizePolicy2)
        self.Image_SOP_label.setMinimumSize(QSize(0, 150))
        self.Image_SOP_label.setFrameShape(QFrame.Box)
        self.Image_SOP_label.setFrameShadow(QFrame.Raised)
        self.Image_SOP_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.Image_SOP_label)

        self.note_SOP_textBrowser = QTextBrowser(self.widget_7)
        self.note_SOP_textBrowser.setObjectName(u"note_SOP_textBrowser")
        self.note_SOP_textBrowser.setMinimumSize(QSize(0, 120))

        self.verticalLayout_10.addWidget(self.note_SOP_textBrowser)

        self.stateInfo_SOP_groupBox = QGroupBox(self.widget_7)
        self.stateInfo_SOP_groupBox.setObjectName(u"stateInfo_SOP_groupBox")
        self.stateInfo_SOP_groupBox.setMinimumSize(QSize(0, 0))
        self.stateInfo_SOP_groupBox.setMaximumSize(QSize(350, 16777215))
        self.stateInfo_SOP_groupBox.setStyleSheet(u"QGroupBox{\n"
"border-width:1px;\n"
"border-style:solid;\n"
"border-radius: 10px;\n"
"border-color:gray;\n"
"margin-top:2.5ex;\n"
"}\n"
"QGroupBox::title{\n"
"subcontrol-origin:margin;\n"
"subcontrol-position:top center;\n"
"padding:0 1px;\n"
"}")
        self.horizontalLayout_13 = QHBoxLayout(self.stateInfo_SOP_groupBox)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.stateInfo_SOP_textBrowser = QTextBrowser(self.stateInfo_SOP_groupBox)
        self.stateInfo_SOP_textBrowser.setObjectName(u"stateInfo_SOP_textBrowser")

        self.horizontalLayout_13.addWidget(self.stateInfo_SOP_textBrowser)


        self.verticalLayout_10.addWidget(self.stateInfo_SOP_groupBox)


        self.gridLayout_21.addLayout(self.verticalLayout_10, 0, 0, 1, 1)

        self.terminate_pushButton = QPushButton(self.widget_7)
        self.terminate_pushButton.setObjectName(u"terminate_pushButton")
        self.terminate_pushButton.setEnabled(False)
        self.terminate_pushButton.setMinimumSize(QSize(0, 40))
        self.terminate_pushButton.setStyleSheet(u"background-color: rgb(252, 175, 62);")

        self.gridLayout_21.addWidget(self.terminate_pushButton, 1, 0, 1, 1)


        self.horizontalLayout_16.addWidget(self.widget_7)

        self.tabWidget.addTab(self.tab_sop, "")

        self.gridLayout_8.addWidget(self.tabWidget, 0, 0, 1, 6)

        self.horizontalSpacer_5 = QSpacerItem(800, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_5, 1, 3, 1, 1)

        self.exit_pushButton = QPushButton(self.centralwidget)
        self.exit_pushButton.setObjectName(u"exit_pushButton")
        self.exit_pushButton.setMinimumSize(QSize(0, 40))

        self.gridLayout_8.addWidget(self.exit_pushButton, 1, 5, 1, 1)

        self.logo_label = QLabel(self.centralwidget)
        self.logo_label.setObjectName(u"logo_label")
        self.logo_label.setMaximumSize(QSize(120, 60))
        self.logo_label.setPixmap(QPixmap(u":/<logo>/resource/EVA_logo"))
        self.logo_label.setScaledContents(True)

        self.gridLayout_8.addWidget(self.logo_label, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1431, 22))
        self.menuLanguage = QMenu(self.menubar)
        self.menuLanguage.setObjectName(u"menuLanguage")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.tabWidget, self.projectName_setting_lineEdit)
        QWidget.setTabOrder(self.projectName_setting_lineEdit, self.sn_setting_lineEdit)
        QWidget.setTabOrder(self.sn_setting_lineEdit, self.productNum_setting_lineEdit)
        QWidget.setTabOrder(self.productNum_setting_lineEdit, self.loadSettings_pushButton)
        QWidget.setTabOrder(self.loadSettings_pushButton, self.retrain_treeWidget)
        QWidget.setTabOrder(self.retrain_treeWidget, self.retrain_pushButton)
        QWidget.setTabOrder(self.retrain_pushButton, self.training_ip_lineEdit)
        QWidget.setTabOrder(self.training_ip_lineEdit, self.training_account_lineEdit)
        QWidget.setTabOrder(self.training_account_lineEdit, self.training_pw_lineEdit)
        QWidget.setTabOrder(self.training_pw_lineEdit, self.showlist_spinBox)
        QWidget.setTabOrder(self.showlist_spinBox, self.inference_comboBox)
        QWidget.setTabOrder(self.inference_comboBox, self.exortNVEngine_checkBox)
        QWidget.setTabOrder(self.exortNVEngine_checkBox, self.epoch_spinBox)
        QWidget.setTabOrder(self.epoch_spinBox, self.traingPath_lineEdit)
        QWidget.setTabOrder(self.traingPath_lineEdit, self.boradno_spinBox)
        QWidget.setTabOrder(self.boradno_spinBox, self.comboBox)
        QWidget.setTabOrder(self.comboBox, self.storage_ip_lineEdit)
        QWidget.setTabOrder(self.storage_ip_lineEdit, self.storage_account_lineEdit)
        QWidget.setTabOrder(self.storage_account_lineEdit, self.storage_pw_lineEdit)
        QWidget.setTabOrder(self.storage_pw_lineEdit, self.storage_path_lineEdit)
        QWidget.setTabOrder(self.storage_path_lineEdit, self.SaveSetting_pushButton)
        QWidget.setTabOrder(self.SaveSetting_pushButton, self.start_pushButton)
        QWidget.setTabOrder(self.start_pushButton, self.goldenmode_checkBox)
        QWidget.setTabOrder(self.goldenmode_checkBox, self.device_offline_comboBox)
        QWidget.setTabOrder(self.device_offline_comboBox, self.importImage_pushButton)
        QWidget.setTabOrder(self.importImage_pushButton, self.capture_pushButton)
        QWidget.setTabOrder(self.capture_pushButton, self.position_pushButton)
        QWidget.setTabOrder(self.position_pushButton, self.layerNo_comboBox)
        QWidget.setTabOrder(self.layerNo_comboBox, self.labelEdit_pushButton)
        QWidget.setTabOrder(self.labelEdit_pushButton, self.labelList_listWidget)
        QWidget.setTabOrder(self.labelList_listWidget, self.autoLable_pushButton)
        QWidget.setTabOrder(self.autoLable_pushButton, self.orderList_listWidget)
        QWidget.setTabOrder(self.orderList_listWidget, self.durationList_listWidget)
        QWidget.setTabOrder(self.durationList_listWidget, self.golden_tableWidget)
        QWidget.setTabOrder(self.golden_tableWidget, self.showImagelist_tableWidget)
        QWidget.setTabOrder(self.showImagelist_tableWidget, self.showImage_offline_graphicsView)
        QWidget.setTabOrder(self.showImage_offline_graphicsView, self.labelInfo_tableWidget)
        QWidget.setTabOrder(self.labelInfo_tableWidget, self.delete_pushButton)
        QWidget.setTabOrder(self.delete_pushButton, self.saveLabel_pushButton)
        QWidget.setTabOrder(self.saveLabel_pushButton, self.next_pushButton)
        QWidget.setTabOrder(self.next_pushButton, self.page_lineEdit)
        QWidget.setTabOrder(self.page_lineEdit, self.back_pushButton)
        QWidget.setTabOrder(self.back_pushButton, self.train_pushButton)
        QWidget.setTabOrder(self.train_pushButton, self.device_easy_comboBox)
        QWidget.setTabOrder(self.device_easy_comboBox, self.sn_easy_lineEdit)
        QWidget.setTabOrder(self.sn_easy_lineEdit, self.model_easy_lineEdit)
        QWidget.setTabOrder(self.model_easy_lineEdit, self.on_off_easy_checkBox)
        QWidget.setTabOrder(self.on_off_easy_checkBox, self.goverify_easy_pushButton)
        QWidget.setTabOrder(self.goverify_easy_pushButton, self.back_easy_pushButton)
        QWidget.setTabOrder(self.back_easy_pushButton, self.next_easy_pushButton)
        QWidget.setTabOrder(self.next_easy_pushButton, self.onlyNG_easy_checkBox)
        QWidget.setTabOrder(self.onlyNG_easy_checkBox, self.skip_easy_pushButton)
        QWidget.setTabOrder(self.skip_easy_pushButton, self.showFocus_easy_graphicsView)
        QWidget.setTabOrder(self.showFocus_easy_graphicsView, self.inspectResult_easy_tableWidget)
        QWidget.setTabOrder(self.inspectResult_easy_tableWidget, self.showOverall_easy_graphicsView)
        QWidget.setTabOrder(self.showOverall_easy_graphicsView, self.sn_confirm_lineEdit)
        QWidget.setTabOrder(self.sn_confirm_lineEdit, self.model_confirm_lineEdit)
        QWidget.setTabOrder(self.model_confirm_lineEdit, self.inspectResult_confirm_tableWidget)
        QWidget.setTabOrder(self.inspectResult_confirm_tableWidget, self.back_confirm_pushButton)
        QWidget.setTabOrder(self.back_confirm_pushButton, self.next_confirm_pushButton)
        QWidget.setTabOrder(self.next_confirm_pushButton, self.fail_confirm_pushButton)
        QWidget.setTabOrder(self.fail_confirm_pushButton, self.repass_confirm_pushButton)
        QWidget.setTabOrder(self.repass_confirm_pushButton, self.submit_confirm_pushButton)
        QWidget.setTabOrder(self.submit_confirm_pushButton, self.reset_confirm_pushButton)
        QWidget.setTabOrder(self.reset_confirm_pushButton, self.showimage_confirm_graphicsView)
        QWidget.setTabOrder(self.showimage_confirm_graphicsView, self.showOverall_confirm_graphicsView)
        QWidget.setTabOrder(self.showOverall_confirm_graphicsView, self.device_online_comboBox)
        QWidget.setTabOrder(self.device_online_comboBox, self.sn_online_lineEdit)
        QWidget.setTabOrder(self.sn_online_lineEdit, self.model_lineEdit)
        QWidget.setTabOrder(self.model_lineEdit, self.on_off_checkBox)
        QWidget.setTabOrder(self.on_off_checkBox, self.goverify_pushButton)
        QWidget.setTabOrder(self.goverify_pushButton, self.submit_pushButton)
        QWidget.setTabOrder(self.submit_pushButton, self.reset_pushButton)
        QWidget.setTabOrder(self.reset_pushButton, self.inspectResult_tableWidget)
        QWidget.setTabOrder(self.inspectResult_tableWidget, self.showimage_online_graphicsView)
        QWidget.setTabOrder(self.showimage_online_graphicsView, self.exit_pushButton)
        QWidget.setTabOrder(self.exit_pushButton, self.export_pushButton)
        QWidget.setTabOrder(self.export_pushButton, self.EditNote_pushButton)
        QWidget.setTabOrder(self.EditNote_pushButton, self.submit_easy_pushButton)
        QWidget.setTabOrder(self.submit_easy_pushButton, self.sn_SOP_lineEdit)
        QWidget.setTabOrder(self.sn_SOP_lineEdit, self.start_SOP_pushButton)
        QWidget.setTabOrder(self.start_SOP_pushButton, self.play_SOP_pushButton)
        QWidget.setTabOrder(self.play_SOP_pushButton, self.pause_SOP_pushButton)
        QWidget.setTabOrder(self.pause_SOP_pushButton, self.stop_SOP_pushButton)
        QWidget.setTabOrder(self.stop_SOP_pushButton, self.showImage_SOP_graphicsView)
        QWidget.setTabOrder(self.showImage_SOP_graphicsView, self.note_SOP_textBrowser)
        QWidget.setTabOrder(self.note_SOP_textBrowser, self.stateInfo_SOP_textBrowser)

        self.menubar.addAction(self.menuLanguage.menuAction())
        self.menuLanguage.addAction(self.actionEnglish)
        self.menuLanguage.addAction(self.actionChinese)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)
        self.orderList_listWidget.setCurrentRow(0)
        self.durationList_listWidget.setCurrentRow(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"ADLINK AI Automatic Inspection", None))
        self.actionEnglish.setText(QCoreApplication.translate("MainWindow", u"English", None))
        self.actionChinese.setText(QCoreApplication.translate("MainWindow", u"Chinese", None))
        self.ADLINK_label.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Product Number*:", None))
        self.sn_setting_lineEdit.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Project Name:", None))
        self.projectName_setting_lineEdit.setText("")
        self.sn_setting_label.setText(QCoreApplication.translate("MainWindow", u"Serial Number:", None))
        self.loadSettings_pushButton.setText(QCoreApplication.translate("MainWindow", u"Load Settings", None))
#if QT_CONFIG(tooltip)
        self.manage_groupBox.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>This function can manage project names, copy the current projects to the same product or another product.</p><p>The copy includes the project system settings, the gold settings, and registration information.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.manage_groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Project Management", None))
#if QT_CONFIG(tooltip)
        self.rename_radioButton.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Rename the current project name.</p><p>The system settings will be updated synchronously</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.rename_radioButton.setText(QCoreApplication.translate("MainWindow", u"Rename the current project", None))
#if QT_CONFIG(tooltip)
        self.copy_radioButton.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Copy the settings to another project.</p><p>The new project belongs to the same product as the current project</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.copy_radioButton.setText(QCoreApplication.translate("MainWindow", u"Copy  the current project to new project", None))
#if QT_CONFIG(tooltip)
        self.duplicate_radioButton.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Copy the settings to another product number.</p><p>If &quot;New Project Name&quot; is empty, the project name will use the current project name.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.duplicate_radioButton.setText(QCoreApplication.translate("MainWindow", u"Duplicate the current project to another product", None))
        self.newProjectName_label.setText(QCoreApplication.translate("MainWindow", u"New Project Name:", None))
        self.newPN_label.setText(QCoreApplication.translate("MainWindow", u"New Product Number:", None))
        self.submit_manage_project_pushButton.setText(QCoreApplication.translate("MainWindow", u"Submit", None))
        self.retrain_groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Re-Train", None))
        self.retrain_pushButton.setText(QCoreApplication.translate("MainWindow", u"Re-Train", None))
#if QT_CONFIG(shortcut)
        self.retrain_pushButton.setShortcut(QCoreApplication.translate("MainWindow", u"T", None))
#endif // QT_CONFIG(shortcut)
        ___qtreewidgetitem = self.retrain_treeWidget.headerItem()
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"Inspection data", None));

        __sortingEnabled = self.retrain_treeWidget.isSortingEnabled()
        self.retrain_treeWidget.setSortingEnabled(False)
        ___qtreewidgetitem1 = self.retrain_treeWidget.topLevelItem(0)
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("MainWindow", u"All Date", None));
        ___qtreewidgetitem2 = ___qtreewidgetitem1.child(0)
        ___qtreewidgetitem2.setText(0, QCoreApplication.translate("MainWindow", u"2024/8/14", None));
        ___qtreewidgetitem3 = ___qtreewidgetitem2.child(0)
        ___qtreewidgetitem3.setText(0, QCoreApplication.translate("MainWindow", u"xx-xx-xxxx_20240814144722", None));
        ___qtreewidgetitem4 = ___qtreewidgetitem2.child(1)
        ___qtreewidgetitem4.setText(0, QCoreApplication.translate("MainWindow", u"xx-xx-xxxx_20240807151931", None));
        ___qtreewidgetitem5 = ___qtreewidgetitem1.child(1)
        ___qtreewidgetitem5.setText(0, QCoreApplication.translate("MainWindow", u"2024/8/15", None));
        ___qtreewidgetitem6 = ___qtreewidgetitem5.child(0)
        ___qtreewidgetitem6.setText(0, QCoreApplication.translate("MainWindow", u"xx-xx-xxxx_20240815125329", None));
        self.retrain_treeWidget.setSortingEnabled(__sortingEnabled)

        self.training_groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Training Setting", None))
        self.dip_groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Inference Parameter", None))
        self.training_modelConfig_label.setText(QCoreApplication.translate("MainWindow", u"epoch", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Training data root path*", None))
        self.traingPath_lineEdit.setText(QCoreApplication.translate("MainWindow", u"/app/data", None))
        self.exortNVEngine_checkBox.setText(QCoreApplication.translate("MainWindow", u"Export NVIDAI Engine", None))
        self.boradno_label.setText(QCoreApplication.translate("MainWindow", u"Number of assembly layer", None))
#if QT_CONFIG(tooltip)
        self.boradno_spinBox.setToolTip(QCoreApplication.translate("MainWindow", u"1~10", None))
#endif // QT_CONFIG(tooltip)
        self.training_savePath_label_2.setText(QCoreApplication.translate("MainWindow", u"Number of image column", None))
        self.training_ip_label.setText(QCoreApplication.translate("MainWindow", u"IP Address*", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Port", None))
        self.training_pw_label.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.training_account_label.setText(QCoreApplication.translate("MainWindow", u"Account", None))
        self.training_savePath_label.setText(QCoreApplication.translate("MainWindow", u"Inference Type", None))
        self.inference_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Dual In Line Package Inspection", None))
        self.inference_comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Standard Operating Procedures Inspection", None))

        self.storage_groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Storage Server", None))
        self.storage_ip_label.setText(QCoreApplication.translate("MainWindow", u"IP Address", None))
        self.storage_account_label.setText(QCoreApplication.translate("MainWindow", u"Account", None))
        self.storage_pw_label.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.storage_path_label.setText(QCoreApplication.translate("MainWindow", u"Path", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Protocal", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Samba", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"FTP", None))

        self.inspection_groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Inspection Setting", None))
        self.useTestVideo_groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Use a test video (Administrator)", None))
        self.testVideo_filePath_label.setText(QCoreApplication.translate("MainWindow", u"File path(*.mp4)", None))
        self.testVideo_toolButton.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.SaveSetting_pushButton.setText(QCoreApplication.translate("MainWindow", u"Save Settings for Porject", None))
#if QT_CONFIG(shortcut)
        self.SaveSetting_pushButton.setShortcut(QCoreApplication.translate("MainWindow", u"Space", None))
#endif // QT_CONFIG(shortcut)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_setting), QCoreApplication.translate("MainWindow", u"&System Setting", None))
        self.start_pushButton.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.goldenmode_checkBox.setText(QCoreApplication.translate("MainWindow", u"Golden Mode", None))
        self.device_offline_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Static Image", None))
        self.device_offline_comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"USB3 Camera", None))
        self.device_offline_comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Web Camera", None))
        self.device_offline_comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Basler Camera", None))

        self.device_offline_label.setText(QCoreApplication.translate("MainWindow", u"Select Source", None))
        self.importImage_pushButton.setText(QCoreApplication.translate("MainWindow", u"Import Image", None))
        self.capture_pushButton.setText(QCoreApplication.translate("MainWindow", u"Capture Image", None))
        self.calThreshold_pushButton.setText(QCoreApplication.translate("MainWindow", u"Calculate Threshold", None))
        self.export_pushButton.setText(QCoreApplication.translate("MainWindow", u"Export", None))
        self.train_pushButton.setText(QCoreApplication.translate("MainWindow", u"Train", None))
        self.label_groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Label Tool", None))
        self.orderList_label.setText(QCoreApplication.translate("MainWindow", u"Order", None))

        __sortingEnabled1 = self.orderList_listWidget.isSortingEnabled()
        self.orderList_listWidget.setSortingEnabled(False)
        ___qlistwidgetitem = self.orderList_listWidget.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qlistwidgetitem1 = self.orderList_listWidget.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qlistwidgetitem2 = self.orderList_listWidget.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qlistwidgetitem3 = self.orderList_listWidget.item(3)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("MainWindow", u"4", None));
        ___qlistwidgetitem4 = self.orderList_listWidget.item(4)
        ___qlistwidgetitem4.setText(QCoreApplication.translate("MainWindow", u"5", None));
        ___qlistwidgetitem5 = self.orderList_listWidget.item(5)
        ___qlistwidgetitem5.setText(QCoreApplication.translate("MainWindow", u"6", None));
        ___qlistwidgetitem6 = self.orderList_listWidget.item(6)
        ___qlistwidgetitem6.setText(QCoreApplication.translate("MainWindow", u"7", None));
        ___qlistwidgetitem7 = self.orderList_listWidget.item(7)
        ___qlistwidgetitem7.setText(QCoreApplication.translate("MainWindow", u"8", None));
        ___qlistwidgetitem8 = self.orderList_listWidget.item(8)
        ___qlistwidgetitem8.setText(QCoreApplication.translate("MainWindow", u"9", None));
        ___qlistwidgetitem9 = self.orderList_listWidget.item(9)
        ___qlistwidgetitem9.setText(QCoreApplication.translate("MainWindow", u"10", None));
        ___qlistwidgetitem10 = self.orderList_listWidget.item(10)
        ___qlistwidgetitem10.setText(QCoreApplication.translate("MainWindow", u"11", None));
        ___qlistwidgetitem11 = self.orderList_listWidget.item(11)
        ___qlistwidgetitem11.setText(QCoreApplication.translate("MainWindow", u"12", None));
        ___qlistwidgetitem12 = self.orderList_listWidget.item(12)
        ___qlistwidgetitem12.setText(QCoreApplication.translate("MainWindow", u"13", None));
        ___qlistwidgetitem13 = self.orderList_listWidget.item(13)
        ___qlistwidgetitem13.setText(QCoreApplication.translate("MainWindow", u"14", None));
        ___qlistwidgetitem14 = self.orderList_listWidget.item(14)
        ___qlistwidgetitem14.setText(QCoreApplication.translate("MainWindow", u"15", None));
        ___qlistwidgetitem15 = self.orderList_listWidget.item(15)
        ___qlistwidgetitem15.setText(QCoreApplication.translate("MainWindow", u"16", None));
        ___qlistwidgetitem16 = self.orderList_listWidget.item(16)
        ___qlistwidgetitem16.setText(QCoreApplication.translate("MainWindow", u"17", None));
        ___qlistwidgetitem17 = self.orderList_listWidget.item(17)
        ___qlistwidgetitem17.setText(QCoreApplication.translate("MainWindow", u"18", None));
        ___qlistwidgetitem18 = self.orderList_listWidget.item(18)
        ___qlistwidgetitem18.setText(QCoreApplication.translate("MainWindow", u"19", None));
        ___qlistwidgetitem19 = self.orderList_listWidget.item(19)
        ___qlistwidgetitem19.setText(QCoreApplication.translate("MainWindow", u"20", None));
        self.orderList_listWidget.setSortingEnabled(__sortingEnabled1)

        self.labelEdit_pushButton.setText(QCoreApplication.translate("MainWindow", u"Edit ", None))
        self.durationList_label.setText(QCoreApplication.translate("MainWindow", u"Duration", None))

        __sortingEnabled2 = self.durationList_listWidget.isSortingEnabled()
        self.durationList_listWidget.setSortingEnabled(False)
        ___qlistwidgetitem20 = self.durationList_listWidget.item(0)
        ___qlistwidgetitem20.setText(QCoreApplication.translate("MainWindow", u"Ignore", None));
        ___qlistwidgetitem21 = self.durationList_listWidget.item(1)
        ___qlistwidgetitem21.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qlistwidgetitem22 = self.durationList_listWidget.item(2)
        ___qlistwidgetitem22.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qlistwidgetitem23 = self.durationList_listWidget.item(3)
        ___qlistwidgetitem23.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qlistwidgetitem24 = self.durationList_listWidget.item(4)
        ___qlistwidgetitem24.setText(QCoreApplication.translate("MainWindow", u"4", None));
        ___qlistwidgetitem25 = self.durationList_listWidget.item(5)
        ___qlistwidgetitem25.setText(QCoreApplication.translate("MainWindow", u"5", None));
        ___qlistwidgetitem26 = self.durationList_listWidget.item(6)
        ___qlistwidgetitem26.setText(QCoreApplication.translate("MainWindow", u"6", None));
        ___qlistwidgetitem27 = self.durationList_listWidget.item(7)
        ___qlistwidgetitem27.setText(QCoreApplication.translate("MainWindow", u"7", None));
        ___qlistwidgetitem28 = self.durationList_listWidget.item(8)
        ___qlistwidgetitem28.setText(QCoreApplication.translate("MainWindow", u"8", None));
        ___qlistwidgetitem29 = self.durationList_listWidget.item(9)
        ___qlistwidgetitem29.setText(QCoreApplication.translate("MainWindow", u"9", None));
        ___qlistwidgetitem30 = self.durationList_listWidget.item(10)
        ___qlistwidgetitem30.setText(QCoreApplication.translate("MainWindow", u"10", None));
        ___qlistwidgetitem31 = self.durationList_listWidget.item(11)
        ___qlistwidgetitem31.setText(QCoreApplication.translate("MainWindow", u"11", None));
        ___qlistwidgetitem32 = self.durationList_listWidget.item(12)
        ___qlistwidgetitem32.setText(QCoreApplication.translate("MainWindow", u"12", None));
        ___qlistwidgetitem33 = self.durationList_listWidget.item(13)
        ___qlistwidgetitem33.setText(QCoreApplication.translate("MainWindow", u"13", None));
        ___qlistwidgetitem34 = self.durationList_listWidget.item(14)
        ___qlistwidgetitem34.setText(QCoreApplication.translate("MainWindow", u"14", None));
        ___qlistwidgetitem35 = self.durationList_listWidget.item(15)
        ___qlistwidgetitem35.setText(QCoreApplication.translate("MainWindow", u"15", None));
        ___qlistwidgetitem36 = self.durationList_listWidget.item(16)
        ___qlistwidgetitem36.setText(QCoreApplication.translate("MainWindow", u"16", None));
        ___qlistwidgetitem37 = self.durationList_listWidget.item(17)
        ___qlistwidgetitem37.setText(QCoreApplication.translate("MainWindow", u"17", None));
        ___qlistwidgetitem38 = self.durationList_listWidget.item(18)
        ___qlistwidgetitem38.setText(QCoreApplication.translate("MainWindow", u"18", None));
        ___qlistwidgetitem39 = self.durationList_listWidget.item(19)
        ___qlistwidgetitem39.setText(QCoreApplication.translate("MainWindow", u"19", None));
        ___qlistwidgetitem40 = self.durationList_listWidget.item(20)
        ___qlistwidgetitem40.setText(QCoreApplication.translate("MainWindow", u"20", None));
        self.durationList_listWidget.setSortingEnabled(__sortingEnabled2)

        self.labelList_label.setText(QCoreApplication.translate("MainWindow", u"Label List", None))
        self.autoLable_pushButton.setText(QCoreApplication.translate("MainWindow", u"Pattern Label", None))
        self.position_pushButton.setText(QCoreApplication.translate("MainWindow", u"Registration Anchor", None))
        self.layerNo_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Layer 1", None))

        self.saveLabel_pushButton.setText(QCoreApplication.translate("MainWindow", u"Save Label Result", None))
        self.labelInfo_groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Label Information", None))
        self.delete_pushButton.setText(QCoreApplication.translate("MainWindow", u"Delete Selected Item", None))
        ___qtablewidgetitem = self.labelInfo_tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem1 = self.labelInfo_tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Start", None));
#if QT_CONFIG(tooltip)
        ___qtablewidgetitem1.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Upper left conrner</p><p>(x1,y1)</p></body></html>", None));
#endif // QT_CONFIG(tooltip)
        ___qtablewidgetitem2 = self.labelInfo_tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"End", None));
#if QT_CONFIG(tooltip)
        ___qtablewidgetitem2.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Lower right conrner</p><p>(x2,y2)</p></body></html>", None));
#endif // QT_CONFIG(tooltip)
        ___qtablewidgetitem3 = self.labelInfo_tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Order", None));
        ___qtablewidgetitem4 = self.labelInfo_tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Duration(s)", None));
        self.EditNote_pushButton.setText(QCoreApplication.translate("MainWindow", u"Edit Note/Offset", None))
        ___qtablewidgetitem5 = self.showImagelist_tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Labeled/Unlabeled", None));
        ___qtablewidgetitem6 = self.showImagelist_tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Filename", None));
        ___qtablewidgetitem7 = self.showImagelist_tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Image", None));
        self.next_pushButton.setText(QCoreApplication.translate("MainWindow", u"&Next", None))
        self.page_label.setText(QCoreApplication.translate("MainWindow", u"Page", None))
        self.pageOf_label.setText(QCoreApplication.translate("MainWindow", u"of 1", None))
        self.back_pushButton.setText(QCoreApplication.translate("MainWindow", u"&Back", None))
        ___qtablewidgetitem8 = self.golden_tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Labeled/Unlabeled", None));
        ___qtablewidgetitem9 = self.golden_tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Filename", None));
        ___qtablewidgetitem10 = self.golden_tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Image", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_training), QCoreApplication.translate("MainWindow", u"&Training Mode", None))
#if QT_CONFIG(tooltip)
        self.goverify_easy_pushButton.setToolTip(QCoreApplication.translate("MainWindow", u"shortcut: Enter", None))
#endif // QT_CONFIG(tooltip)
        self.goverify_easy_pushButton.setText(QCoreApplication.translate("MainWindow", u"Go verify", None))
#if QT_CONFIG(shortcut)
        self.goverify_easy_pushButton.setShortcut(QCoreApplication.translate("MainWindow", u"Return", None))
#endif // QT_CONFIG(shortcut)
        self.model_easy_label.setText(QCoreApplication.translate("MainWindow", u"Model:", None))
        self.sn_easy_label.setText(QCoreApplication.translate("MainWindow", u"Serial Number:", None))
        self.device_easy_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"USB3 Camera", None))
        self.device_easy_comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Web Camera", None))
        self.device_easy_comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Basler Camera", None))

        self.device_easy_label.setText(QCoreApplication.translate("MainWindow", u"Select Device:", None))
        self.sn_easy_lineEdit.setText("")
        self.on_off_easy_label.setText(QCoreApplication.translate("MainWindow", u"On/Off", None))
#if QT_CONFIG(tooltip)
        self.on_off_easy_checkBox.setToolTip(QCoreApplication.translate("MainWindow", u"shortcut: O", None))
#endif // QT_CONFIG(tooltip)
        self.on_off_easy_checkBox.setText(QCoreApplication.translate("MainWindow", u"on/off", None))
#if QT_CONFIG(shortcut)
        self.on_off_easy_checkBox.setShortcut(QCoreApplication.translate("MainWindow", u"O", None))
#endif // QT_CONFIG(shortcut)
        self.status_Label_3.setText(QCoreApplication.translate("MainWindow", u"Status:", None))
        self.cameraStatus_easy_label.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
#if QT_CONFIG(whatsthis)
        self.PASS_easy_label.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.PASS_easy_label.setText(QCoreApplication.translate("MainWindow", u"PASS", None))
        self.FAIL_easy_label.setText(QCoreApplication.translate("MainWindow", u"FAIL", None))
        self.inspect_groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Insepct Result", None))
#if QT_CONFIG(tooltip)
        self.onlyNG_easy_checkBox.setToolTip(QCoreApplication.translate("MainWindow", u"shortcut: N", None))
#endif // QT_CONFIG(tooltip)
        self.onlyNG_easy_checkBox.setText(QCoreApplication.translate("MainWindow", u"Only NG", None))
#if QT_CONFIG(shortcut)
        self.onlyNG_easy_checkBox.setShortcut(QCoreApplication.translate("MainWindow", u"N", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.skip_easy_pushButton.setToolTip(QCoreApplication.translate("MainWindow", u"shortcut: S", None))
#endif // QT_CONFIG(tooltip)
        self.skip_easy_pushButton.setText(QCoreApplication.translate("MainWindow", u"Skip", None))
#if QT_CONFIG(shortcut)
        self.skip_easy_pushButton.setShortcut(QCoreApplication.translate("MainWindow", u"S", None))
#endif // QT_CONFIG(shortcut)
        ___qtablewidgetitem11 = self.inspectResult_easy_tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"NG/OK", None));
        ___qtablewidgetitem12 = self.inspectResult_easy_tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem13 = self.inspectResult_easy_tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Start", None));
        ___qtablewidgetitem14 = self.inspectResult_easy_tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"End", None));
#if QT_CONFIG(tooltip)
        self.back_easy_pushButton.setToolTip(QCoreApplication.translate("MainWindow", u"shortcut: Up", None))
#endif // QT_CONFIG(tooltip)
        self.back_easy_pushButton.setText(QCoreApplication.translate("MainWindow", u"Back", None))
#if QT_CONFIG(shortcut)
        self.back_easy_pushButton.setShortcut(QCoreApplication.translate("MainWindow", u"Up", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.next_easy_pushButton.setToolTip(QCoreApplication.translate("MainWindow", u"shortcut:  Down", None))
#endif // QT_CONFIG(tooltip)
        self.next_easy_pushButton.setText(QCoreApplication.translate("MainWindow", u"Next", None))
#if QT_CONFIG(shortcut)
        self.next_easy_pushButton.setShortcut(QCoreApplication.translate("MainWindow", u"Down", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.submit_easy_pushButton.setToolTip(QCoreApplication.translate("MainWindow", u"shortcut:  space", None))
#endif // QT_CONFIG(tooltip)
        self.submit_easy_pushButton.setText(QCoreApplication.translate("MainWindow", u"Submit", None))
#if QT_CONFIG(shortcut)
        self.submit_easy_pushButton.setShortcut(QCoreApplication.translate("MainWindow", u"Space", None))
#endif // QT_CONFIG(shortcut)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_inspection), QCoreApplication.translate("MainWindow", u"&Inspection Mode", None))
#if QT_CONFIG(tooltip)
        self.showimage_confirm_graphicsView.setToolTip(QCoreApplication.translate("MainWindow", u"focus view", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.fail_confirm_pushButton.setToolTip(QCoreApplication.translate("MainWindow", u"shortcut: F", None))
#endif // QT_CONFIG(tooltip)
        self.fail_confirm_pushButton.setText(QCoreApplication.translate("MainWindow", u"Fail", None))
#if QT_CONFIG(shortcut)
        self.fail_confirm_pushButton.setShortcut(QCoreApplication.translate("MainWindow", u"F", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.repass_confirm_pushButton.setToolTip(QCoreApplication.translate("MainWindow", u"shortcut: R", None))
#endif // QT_CONFIG(tooltip)
        self.repass_confirm_pushButton.setText(QCoreApplication.translate("MainWindow", u"Repass", None))
#if QT_CONFIG(shortcut)
        self.repass_confirm_pushButton.setShortcut(QCoreApplication.translate("MainWindow", u"R", None))
#endif // QT_CONFIG(shortcut)
        self.sn_confirm_lineEdit.setText("")
        self.sn_online_label_3.setText(QCoreApplication.translate("MainWindow", u"Serial Number:", None))
        self.model_online_label_3.setText(QCoreApplication.translate("MainWindow", u"Model:", None))
#if QT_CONFIG(tooltip)
        self.reset_confirm_pushButton.setToolTip(QCoreApplication.translate("MainWindow", u"shortcut: S", None))
#endif // QT_CONFIG(tooltip)
        self.reset_confirm_pushButton.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
#if QT_CONFIG(shortcut)
        self.reset_confirm_pushButton.setShortcut(QCoreApplication.translate("MainWindow", u"S", None))
#endif // QT_CONFIG(shortcut)
        self.inspect_groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"NG List", None))
        ___qtablewidgetitem15 = self.inspectResult_confirm_tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"NG", None));
        ___qtablewidgetitem16 = self.inspectResult_confirm_tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem17 = self.inspectResult_confirm_tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"Start", None));
        ___qtablewidgetitem18 = self.inspectResult_confirm_tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"End", None));
#if QT_CONFIG(tooltip)
        self.back_confirm_pushButton.setToolTip(QCoreApplication.translate("MainWindow", u"shortcut: Up", None))
#endif // QT_CONFIG(tooltip)
        self.back_confirm_pushButton.setText(QCoreApplication.translate("MainWindow", u"Back", None))
#if QT_CONFIG(shortcut)
        self.back_confirm_pushButton.setShortcut(QCoreApplication.translate("MainWindow", u"Up", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.next_confirm_pushButton.setToolTip(QCoreApplication.translate("MainWindow", u"shortcut: Down", None))
#endif // QT_CONFIG(tooltip)
        self.next_confirm_pushButton.setText(QCoreApplication.translate("MainWindow", u"Next", None))
#if QT_CONFIG(shortcut)
        self.next_confirm_pushButton.setShortcut(QCoreApplication.translate("MainWindow", u"Down", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.showOverall_confirm_graphicsView.setToolTip(QCoreApplication.translate("MainWindow", u"overall view", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.submit_confirm_pushButton.setToolTip(QCoreApplication.translate("MainWindow", u"shortcut: Space", None))
#endif // QT_CONFIG(tooltip)
        self.submit_confirm_pushButton.setText(QCoreApplication.translate("MainWindow", u"Submit", None))
#if QT_CONFIG(shortcut)
        self.submit_confirm_pushButton.setShortcut(QCoreApplication.translate("MainWindow", u"Space", None))
#endif // QT_CONFIG(shortcut)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_reconfirm), QCoreApplication.translate("MainWindow", u"&Reconfirm Mode", None))
#if QT_CONFIG(tooltip)
        self.on_off_checkBox.setToolTip(QCoreApplication.translate("MainWindow", u"shortcut: O", None))
#endif // QT_CONFIG(tooltip)
        self.on_off_checkBox.setText(QCoreApplication.translate("MainWindow", u"on/off", None))
#if QT_CONFIG(shortcut)
        self.on_off_checkBox.setShortcut(QCoreApplication.translate("MainWindow", u"O", None))
#endif // QT_CONFIG(shortcut)
        self.on_off_label.setText(QCoreApplication.translate("MainWindow", u"On/Off", None))
        self.sn_online_label.setText(QCoreApplication.translate("MainWindow", u"Serial Number:", None))
        self.device_online_label.setText(QCoreApplication.translate("MainWindow", u"Select Device:", None))
        self.model_online_label.setText(QCoreApplication.translate("MainWindow", u"Model:", None))
        self.sn_online_lineEdit.setText("")
        self.device_online_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Web Camera", None))
        self.device_online_comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Basler Camera", None))

        self.status_Label.setText(QCoreApplication.translate("MainWindow", u"Status:", None))
        self.currentstatus_label.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.inspect_groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Insepct Result", None))
        self.PASS_label.setText(QCoreApplication.translate("MainWindow", u"PASS", None))
        ___qtablewidgetitem19 = self.inspectResult_tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"NG/OK", None));
        ___qtablewidgetitem20 = self.inspectResult_tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem21 = self.inspectResult_tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"Confidence", None));
        ___qtablewidgetitem22 = self.inspectResult_tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"Start", None));
        ___qtablewidgetitem23 = self.inspectResult_tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"End", None));
#if QT_CONFIG(tooltip)
        self.goverify_pushButton.setToolTip(QCoreApplication.translate("MainWindow", u"shortcut: Enter", None))
#endif // QT_CONFIG(tooltip)
        self.goverify_pushButton.setText(QCoreApplication.translate("MainWindow", u"Go verify", None))
#if QT_CONFIG(shortcut)
        self.goverify_pushButton.setShortcut(QCoreApplication.translate("MainWindow", u"Return", None))
#endif // QT_CONFIG(shortcut)
        self.FAIL_label.setText(QCoreApplication.translate("MainWindow", u"FAIL", None))
#if QT_CONFIG(tooltip)
        self.reset_pushButton.setToolTip(QCoreApplication.translate("MainWindow", u"shortcut: S", None))
#endif // QT_CONFIG(tooltip)
        self.reset_pushButton.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
#if QT_CONFIG(shortcut)
        self.reset_pushButton.setShortcut(QCoreApplication.translate("MainWindow", u"S", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.submit_pushButton.setToolTip(QCoreApplication.translate("MainWindow", u"shortcut: Space", None))
#endif // QT_CONFIG(tooltip)
        self.submit_pushButton.setText(QCoreApplication.translate("MainWindow", u"Submit", None))
#if QT_CONFIG(shortcut)
        self.submit_pushButton.setShortcut(QCoreApplication.translate("MainWindow", u"Space", None))
#endif // QT_CONFIG(shortcut)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_online), QCoreApplication.translate("MainWindow", u"&Advanced Operation Mode", None))
        self.play_SOP_pushButton.setText(QCoreApplication.translate("MainWindow", u"Play", None))
        self.pause_SOP_pushButton.setText(QCoreApplication.translate("MainWindow", u"Pause", None))
        self.stop_SOP_pushButton.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.state_SOP_label.setText(QCoreApplication.translate("MainWindow", u"FAIL", None))
        self.sn_SOP_label.setText(QCoreApplication.translate("MainWindow", u"Serial Number:", None))
#if QT_CONFIG(tooltip)
        self.sn_SOP_lineEdit.setToolTip(QCoreApplication.translate("MainWindow", u"Enter Serial Number", None))
#endif // QT_CONFIG(tooltip)
        self.sn_SOP_lineEdit.setText("")
        self.start_SOP_pushButton.setText(QCoreApplication.translate("MainWindow", u"Load", None))
        self.Image_SOP_label.setText("")
        self.note_SOP_textBrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Ubuntu'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.stateInfo_SOP_groupBox.setTitle(QCoreApplication.translate("MainWindow", u"State Information", None))
        self.stateInfo_SOP_textBrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Ubuntu'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.terminate_pushButton.setText(QCoreApplication.translate("MainWindow", u"Terminate Inspection", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_sop), QCoreApplication.translate("MainWindow", u"SO&P Inspection", None))
        self.exit_pushButton.setText(QCoreApplication.translate("MainWindow", u"E&xit", None))
        self.logo_label.setText("")
        self.menuLanguage.setTitle(QCoreApplication.translate("MainWindow", u"Language", None))
    # retranslateUi

