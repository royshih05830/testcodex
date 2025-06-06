# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_graphicsview.ui'
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
        MainWindow.resize(1227, 890)
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
        self.exit_pushButton = QPushButton(self.centralwidget)
        self.exit_pushButton.setObjectName(u"exit_pushButton")
        self.exit_pushButton.setMinimumSize(QSize(0, 40))

        self.gridLayout_8.addWidget(self.exit_pushButton, 1, 2, 1, 1)

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy1)
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
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.sn_online_lineEdit.sizePolicy().hasHeightForWidth())
        self.sn_online_lineEdit.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.sn_online_lineEdit, 2, 1, 1, 1)

        self.device_online_comboBox = QComboBox(self.widget)
        self.device_online_comboBox.addItem("")
        self.device_online_comboBox.addItem("")
        self.device_online_comboBox.setObjectName(u"device_online_comboBox")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.device_online_comboBox.sizePolicy().hasHeightForWidth())
        self.device_online_comboBox.setSizePolicy(sizePolicy3)

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
        if (self.inspectResult_tableWidget.columnCount() < 4):
            self.inspectResult_tableWidget.setColumnCount(4)
        font = QFont()
        font.setPointSize(8)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font);
        self.inspectResult_tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font);
        self.inspectResult_tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font);
        self.inspectResult_tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font);
        self.inspectResult_tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.inspectResult_tableWidget.setObjectName(u"inspectResult_tableWidget")
        sizePolicy1.setHeightForWidth(self.inspectResult_tableWidget.sizePolicy().hasHeightForWidth())
        self.inspectResult_tableWidget.setSizePolicy(sizePolicy1)
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
        self.tab_offline = QWidget()
        self.tab_offline.setObjectName(u"tab_offline")
        self.gridLayout_16 = QGridLayout(self.tab_offline)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.start_pushButton = QPushButton(self.tab_offline)
        self.start_pushButton.setObjectName(u"start_pushButton")
        self.start_pushButton.setMinimumSize(QSize(0, 40))
        self.start_pushButton.setStyleSheet(u"background-color: rgb(205, 249, 161);")

        self.horizontalLayout_2.addWidget(self.start_pushButton)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_9)

        self.goldenmode_checkBox = QCheckBox(self.tab_offline)
        self.goldenmode_checkBox.setObjectName(u"goldenmode_checkBox")
        self.goldenmode_checkBox.setEnabled(False)

        self.horizontalLayout_2.addWidget(self.goldenmode_checkBox)

        self.horizontalSpacer_13 = QSpacerItem(100, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_13)

        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.device_offline_comboBox = QComboBox(self.tab_offline)
        self.device_offline_comboBox.addItem("")
        self.device_offline_comboBox.addItem("")
        self.device_offline_comboBox.addItem("")
        self.device_offline_comboBox.setObjectName(u"device_offline_comboBox")
        self.device_offline_comboBox.setEnabled(False)
        self.device_offline_comboBox.setMinimumSize(QSize(0, 30))

        self.gridLayout_7.addWidget(self.device_offline_comboBox, 0, 1, 1, 1)

        self.device_offline_label = QLabel(self.tab_offline)
        self.device_offline_label.setObjectName(u"device_offline_label")
        self.device_offline_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_7.addWidget(self.device_offline_label, 0, 0, 1, 1)

        self.importImage_pushButton = QPushButton(self.tab_offline)
        self.importImage_pushButton.setObjectName(u"importImage_pushButton")
        self.importImage_pushButton.setEnabled(True)
        self.importImage_pushButton.setMinimumSize(QSize(0, 40))

        self.gridLayout_7.addWidget(self.importImage_pushButton, 0, 2, 1, 1)


        self.horizontalLayout_2.addLayout(self.gridLayout_7)

        self.capture_pushButton = QPushButton(self.tab_offline)
        self.capture_pushButton.setObjectName(u"capture_pushButton")
        self.capture_pushButton.setEnabled(False)
        self.capture_pushButton.setMinimumSize(QSize(0, 40))

        self.horizontalLayout_2.addWidget(self.capture_pushButton)

        self.horizontalSpacer_2 = QSpacerItem(200, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.export_pushButton = QPushButton(self.tab_offline)
        self.export_pushButton.setObjectName(u"export_pushButton")
        self.export_pushButton.setEnabled(False)
        self.export_pushButton.setMinimumSize(QSize(0, 40))

        self.horizontalLayout_2.addWidget(self.export_pushButton)

        self.train_pushButton = QPushButton(self.tab_offline)
        self.train_pushButton.setObjectName(u"train_pushButton")
        self.train_pushButton.setEnabled(False)
        self.train_pushButton.setMinimumSize(QSize(0, 40))
        self.train_pushButton.setStyleSheet(u"background-color: rgb(252, 175, 62);")

        self.horizontalLayout_2.addWidget(self.train_pushButton)


        self.gridLayout_16.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)

        self.line_3 = QFrame(self.tab_offline)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.gridLayout_16.addWidget(self.line_3, 1, 0, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.widget_3 = QWidget(self.tab_offline)
        self.widget_3.setObjectName(u"widget_3")
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy4)
        self.widget_3.setMaximumSize(QSize(190, 16777215))
        self.gridLayout_10 = QGridLayout(self.widget_3)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.position_pushButton = QPushButton(self.widget_3)
        self.position_pushButton.setObjectName(u"position_pushButton")
        self.position_pushButton.setEnabled(False)
        self.position_pushButton.setMinimumSize(QSize(0, 40))

        self.gridLayout_10.addWidget(self.position_pushButton, 0, 0, 1, 1)

        self.label_groupBox = QGroupBox(self.widget_3)
        self.label_groupBox.setObjectName(u"label_groupBox")
        sizePolicy4.setHeightForWidth(self.label_groupBox.sizePolicy().hasHeightForWidth())
        self.label_groupBox.setSizePolicy(sizePolicy4)
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
        __qlistwidgetitem20 = QListWidgetItem(self.orderList_listWidget)
        __qlistwidgetitem20.setTextAlignment(Qt.AlignCenter);
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
        __qlistwidgetitem41 = QListWidgetItem(self.durationList_listWidget)
        __qlistwidgetitem41.setTextAlignment(Qt.AlignCenter);
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
        self.autoLable_pushButton.setMinimumSize(QSize(0, 30))

        self.gridLayout_3.addWidget(self.autoLable_pushButton, 2, 0, 1, 3)


        self.gridLayout_10.addWidget(self.label_groupBox, 2, 0, 1, 1)

        self.line_4 = QFrame(self.widget_3)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.gridLayout_10.addWidget(self.line_4, 1, 0, 1, 1)


        self.horizontalLayout_5.addWidget(self.widget_3)

        self.widget_6 = QWidget(self.tab_offline)
        self.widget_6.setObjectName(u"widget_6")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.showImage_offline_graphicsView = DrawShapesGraphics(self.widget_6)
        self.showImage_offline_graphicsView.setObjectName(u"showImage_offline_graphicsView")

        self.horizontalLayout_3.addWidget(self.showImage_offline_graphicsView)


        self.horizontalLayout_5.addWidget(self.widget_6)

        self.widget_2 = QWidget(self.tab_offline)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy4.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy4)
        self.widget_2.setMinimumSize(QSize(300, 0))
        self.gridLayout_9 = QGridLayout(self.widget_2)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
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
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font);
        self.labelInfo_tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setFont(font);
        self.labelInfo_tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setFont(font);
        self.labelInfo_tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setFont(font);
        self.labelInfo_tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setFont(font);
        self.labelInfo_tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem8)
        self.labelInfo_tableWidget.setObjectName(u"labelInfo_tableWidget")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.labelInfo_tableWidget.sizePolicy().hasHeightForWidth())
        self.labelInfo_tableWidget.setSizePolicy(sizePolicy5)
        self.labelInfo_tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.labelInfo_tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.labelInfo_tableWidget.horizontalHeader().setMinimumSectionSize(30)

        self.gridLayout_5.addWidget(self.labelInfo_tableWidget, 0, 0, 1, 2)


        self.gridLayout_9.addWidget(self.labelInfo_groupBox, 0, 0, 1, 1)

        self.saveLabel_pushButton = QPushButton(self.widget_2)
        self.saveLabel_pushButton.setObjectName(u"saveLabel_pushButton")
        self.saveLabel_pushButton.setEnabled(False)
        self.saveLabel_pushButton.setMinimumSize(QSize(0, 40))
        self.saveLabel_pushButton.setStyleSheet(u"background-color: rgb(252, 202, 202);")

        self.gridLayout_9.addWidget(self.saveLabel_pushButton, 1, 0, 1, 1)


        self.horizontalLayout_5.addWidget(self.widget_2)


        self.gridLayout_16.addLayout(self.horizontalLayout_5, 2, 0, 1, 1)

        self.widget_5 = QWidget(self.tab_offline)
        self.widget_5.setObjectName(u"widget_5")
        sizePolicy6 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.widget_5.sizePolicy().hasHeightForWidth())
        self.widget_5.setSizePolicy(sizePolicy6)
        self.widget_5.setMaximumSize(QSize(16777215, 150))
        self.gridLayout_15 = QGridLayout(self.widget_5)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.showImagelist_tableWidget = QTableWidget(self.widget_5)
        if (self.showImagelist_tableWidget.rowCount() < 3):
            self.showImagelist_tableWidget.setRowCount(3)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.showImagelist_tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.showImagelist_tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.showImagelist_tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem11)
        self.showImagelist_tableWidget.setObjectName(u"showImagelist_tableWidget")
        self.showImagelist_tableWidget.setEnabled(True)
        sizePolicy6.setHeightForWidth(self.showImagelist_tableWidget.sizePolicy().hasHeightForWidth())
        self.showImagelist_tableWidget.setSizePolicy(sizePolicy6)
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
        sizePolicy7 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy7)
        self.widget_4.setMinimumSize(QSize(120, 0))
        self.widget_4.setMaximumSize(QSize(16777215, 150))
        self.verticalLayout_2 = QVBoxLayout(self.widget_4)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.next_pushButton = QPushButton(self.widget_4)
        self.next_pushButton.setObjectName(u"next_pushButton")
        self.next_pushButton.setEnabled(False)
        sizePolicy8 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.next_pushButton.sizePolicy().hasHeightForWidth())
        self.next_pushButton.setSizePolicy(sizePolicy8)
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
        sizePolicy8.setHeightForWidth(self.back_pushButton.sizePolicy().hasHeightForWidth())
        self.back_pushButton.setSizePolicy(sizePolicy8)
        self.back_pushButton.setMinimumSize(QSize(0, 30))

        self.verticalLayout_2.addWidget(self.back_pushButton)


        self.gridLayout_15.addWidget(self.widget_4, 0, 2, 1, 1)

        self.golden_tableWidget = QTableWidget(self.widget_5)
        if (self.golden_tableWidget.rowCount() < 3):
            self.golden_tableWidget.setRowCount(3)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.golden_tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.golden_tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.golden_tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem14)
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

        self.tabWidget.addTab(self.tab_offline, "")
        self.tab_setting = QWidget()
        self.tab_setting.setObjectName(u"tab_setting")
        self.gridLayout_19 = QGridLayout(self.tab_setting)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.gridLayout_11 = QGridLayout()
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.model_setting_label = QLabel(self.tab_setting)
        self.model_setting_label.setObjectName(u"model_setting_label")
        self.model_setting_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_11.addWidget(self.model_setting_label, 3, 0, 1, 1)

        self.model_setting_comboBox = QComboBox(self.tab_setting)
        self.model_setting_comboBox.setObjectName(u"model_setting_comboBox")

        self.gridLayout_11.addWidget(self.model_setting_comboBox, 3, 2, 1, 1)

        self.label_4 = QLabel(self.tab_setting)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_11.addWidget(self.label_4, 2, 0, 1, 1)

        self.sn_setting_lineEdit = QLineEdit(self.tab_setting)
        self.sn_setting_lineEdit.setObjectName(u"sn_setting_lineEdit")

        self.gridLayout_11.addWidget(self.sn_setting_lineEdit, 1, 2, 1, 1)

        self.lineEdit_2 = QLineEdit(self.tab_setting)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.gridLayout_11.addWidget(self.lineEdit_2, 0, 2, 1, 1)

        self.label_3 = QLabel(self.tab_setting)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_11.addWidget(self.label_3, 0, 0, 1, 1)

        self.sn_setting_label = QLabel(self.tab_setting)
        self.sn_setting_label.setObjectName(u"sn_setting_label")
        self.sn_setting_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_11.addWidget(self.sn_setting_label, 1, 0, 1, 1)

        self.lineEdit_3 = QLineEdit(self.tab_setting)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.gridLayout_11.addWidget(self.lineEdit_3, 2, 2, 1, 1)


        self.verticalLayout_4.addLayout(self.gridLayout_11)

        self.groupBox = QGroupBox(self.tab_setting)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setEnabled(True)
        self.groupBox.setStyleSheet(u"QGroupBox{\n"
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
        self.groupBox.setCheckable(True)
        self.groupBox.setChecked(True)
        self.gridLayout_18 = QGridLayout(self.groupBox)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.pushButton = QPushButton(self.groupBox)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 35))
        self.pushButton.setStyleSheet(u"background-color: rgb(252, 175, 62);")

        self.gridLayout_18.addWidget(self.pushButton, 2, 0, 1, 1)

        self.treeWidget = QTreeWidget(self.groupBox)
        __qtreewidgetitem = QTreeWidgetItem(self.treeWidget)
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
        self.treeWidget.setObjectName(u"treeWidget")
        self.treeWidget.setMinimumSize(QSize(0, 200))
        self.treeWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.treeWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.treeWidget.header().setVisible(False)

        self.gridLayout_18.addWidget(self.treeWidget, 1, 0, 1, 1)


        self.verticalLayout_4.addWidget(self.groupBox)


        self.verticalLayout_5.addLayout(self.verticalLayout_4)

        self.verticalSpacer_8 = QSpacerItem(17, 285, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_8)


        self.horizontalLayout_11.addLayout(self.verticalLayout_5)

        self.line_2 = QFrame(self.tab_setting)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_11.addWidget(self.line_2)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.training_groupBox = QGroupBox(self.tab_setting)
        self.training_groupBox.setObjectName(u"training_groupBox")
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

        self.horizontalSpacer_8 = QSpacerItem(200, 17, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_17.addItem(self.horizontalSpacer_8, 0, 1, 1, 1)

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
        self.inference_comboBox.setObjectName(u"inference_comboBox")

        self.horizontalLayout_7.addWidget(self.inference_comboBox)


        self.gridLayout_17.addLayout(self.horizontalLayout_7, 4, 0, 1, 2)

        self.gridLayout_13 = QGridLayout()
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.training_ip_label = QLabel(self.training_groupBox)
        self.training_ip_label.setObjectName(u"training_ip_label")
        self.training_ip_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_13.addWidget(self.training_ip_label, 0, 0, 1, 1)

        self.training_ip_lineEdit = QLineEdit(self.training_groupBox)
        self.training_ip_lineEdit.setObjectName(u"training_ip_lineEdit")

        self.gridLayout_13.addWidget(self.training_ip_lineEdit, 0, 1, 1, 1)

        self.label_12 = QLabel(self.training_groupBox)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_13.addWidget(self.label_12, 1, 0, 1, 1)

        self.training_port_lineEdit = QLineEdit(self.training_groupBox)
        self.training_port_lineEdit.setObjectName(u"training_port_lineEdit")

        self.gridLayout_13.addWidget(self.training_port_lineEdit, 1, 1, 1, 1)

        self.training_account_label = QLabel(self.training_groupBox)
        self.training_account_label.setObjectName(u"training_account_label")
        self.training_account_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_13.addWidget(self.training_account_label, 2, 0, 1, 1)

        self.training_account_lineEdit = QLineEdit(self.training_groupBox)
        self.training_account_lineEdit.setObjectName(u"training_account_lineEdit")

        self.gridLayout_13.addWidget(self.training_account_lineEdit, 2, 1, 1, 1)

        self.training_pw_label = QLabel(self.training_groupBox)
        self.training_pw_label.setObjectName(u"training_pw_label")
        self.training_pw_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_13.addWidget(self.training_pw_label, 3, 0, 1, 1)

        self.training_pw_lineEdit = PasswordEdit(self.training_groupBox)
        self.training_pw_lineEdit.setObjectName(u"training_pw_lineEdit")

        self.gridLayout_13.addWidget(self.training_pw_lineEdit, 3, 1, 1, 1)


        self.gridLayout_17.addLayout(self.gridLayout_13, 0, 0, 1, 1)

        self.line_6 = QFrame(self.training_groupBox)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.HLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.gridLayout_17.addWidget(self.line_6, 1, 0, 1, 2)

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
        self.checkBox = QCheckBox(self.dip_groupBox)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setTristate(False)

        self.gridLayout_14.addWidget(self.checkBox, 0, 0, 1, 1)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.training_modelConfig_label = QLabel(self.dip_groupBox)
        self.training_modelConfig_label.setObjectName(u"training_modelConfig_label")
        sizePolicy.setHeightForWidth(self.training_modelConfig_label.sizePolicy().hasHeightForWidth())
        self.training_modelConfig_label.setSizePolicy(sizePolicy)
        self.training_modelConfig_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_8.addWidget(self.training_modelConfig_label)

        self.spinBox = QSpinBox(self.dip_groupBox)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setAlignment(Qt.AlignCenter)
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(16777215)
        self.spinBox.setValue(1)

        self.horizontalLayout_8.addWidget(self.spinBox)


        self.gridLayout_14.addLayout(self.horizontalLayout_8, 1, 0, 1, 1)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_14.addItem(self.horizontalSpacer_10, 1, 1, 1, 1)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label = QLabel(self.dip_groupBox)
        self.label.setObjectName(u"label")
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)

        self.horizontalLayout_9.addWidget(self.label)

        self.lineEdit = QLineEdit(self.dip_groupBox)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout_9.addWidget(self.lineEdit)


        self.gridLayout_14.addLayout(self.horizontalLayout_9, 2, 0, 1, 2)


        self.gridLayout_17.addWidget(self.dip_groupBox, 5, 0, 1, 2)


        self.verticalLayout_6.addWidget(self.training_groupBox)

        self.verticalSpacer_6 = QSpacerItem(17, 285, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_6)


        self.horizontalLayout_11.addLayout(self.verticalLayout_6)

        self.line_8 = QFrame(self.tab_setting)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setFrameShape(QFrame.VLine)
        self.line_8.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_11.addWidget(self.line_8)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.storage_groupBox = QGroupBox(self.tab_setting)
        self.storage_groupBox.setObjectName(u"storage_groupBox")
        self.storage_groupBox.setEnabled(True)
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

        self.verticalSpacer_7 = QSpacerItem(20, 471, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_7)


        self.horizontalLayout_11.addLayout(self.verticalLayout_7)


        self.verticalLayout_8.addLayout(self.horizontalLayout_11)

        self.line_7 = QFrame(self.tab_setting)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.HLine)
        self.line_7.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_8.addWidget(self.line_7)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalSpacer_7 = QSpacerItem(921, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_7)

        self.SaveSetting_pushButton = QPushButton(self.tab_setting)
        self.SaveSetting_pushButton.setObjectName(u"SaveSetting_pushButton")
        self.SaveSetting_pushButton.setMinimumSize(QSize(150, 40))
        self.SaveSetting_pushButton.setStyleSheet(u"background-color: rgb(205, 249, 161);")

        self.horizontalLayout_10.addWidget(self.SaveSetting_pushButton)


        self.verticalLayout_8.addLayout(self.horizontalLayout_10)


        self.gridLayout_19.addLayout(self.verticalLayout_8, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_setting, "")

        self.gridLayout_8.addWidget(self.tabWidget, 0, 0, 1, 3)

        self.horizontalSpacer_5 = QSpacerItem(909, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_5, 1, 1, 1, 1)

        self.logo_label = QLabel(self.centralwidget)
        self.logo_label.setObjectName(u"logo_label")
        self.logo_label.setMaximumSize(QSize(120, 60))
        self.logo_label.setPixmap(QPixmap(u":/<logo>/resource/EVA_logo"))
        self.logo_label.setScaledContents(True)

        self.gridLayout_8.addWidget(self.logo_label, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1227, 22))
        self.menuLanguage = QMenu(self.menubar)
        self.menuLanguage.setObjectName(u"menuLanguage")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.device_offline_comboBox, self.start_pushButton)
        QWidget.setTabOrder(self.start_pushButton, self.capture_pushButton)
        QWidget.setTabOrder(self.capture_pushButton, self.showImagelist_tableWidget)
        QWidget.setTabOrder(self.showImagelist_tableWidget, self.labelList_listWidget)
        QWidget.setTabOrder(self.labelList_listWidget, self.orderList_listWidget)
        QWidget.setTabOrder(self.orderList_listWidget, self.labelEdit_pushButton)
        QWidget.setTabOrder(self.labelEdit_pushButton, self.labelInfo_tableWidget)
        QWidget.setTabOrder(self.labelInfo_tableWidget, self.export_pushButton)
        QWidget.setTabOrder(self.export_pushButton, self.train_pushButton)
        QWidget.setTabOrder(self.train_pushButton, self.exit_pushButton)
        QWidget.setTabOrder(self.exit_pushButton, self.tabWidget)
        QWidget.setTabOrder(self.tabWidget, self.on_off_checkBox)
        QWidget.setTabOrder(self.on_off_checkBox, self.inspectResult_tableWidget)
        QWidget.setTabOrder(self.inspectResult_tableWidget, self.device_online_comboBox)
        QWidget.setTabOrder(self.device_online_comboBox, self.sn_online_lineEdit)
        QWidget.setTabOrder(self.sn_online_lineEdit, self.submit_pushButton)

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
        self.exit_pushButton.setText(QCoreApplication.translate("MainWindow", u"E&xit", None))
        self.on_off_checkBox.setText(QCoreApplication.translate("MainWindow", u"on/off", None))
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
        ___qtablewidgetitem = self.inspectResult_tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"NG/OK", None));
        ___qtablewidgetitem1 = self.inspectResult_tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem2 = self.inspectResult_tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Start", None));
        ___qtablewidgetitem3 = self.inspectResult_tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"End", None));
        self.goverify_pushButton.setText(QCoreApplication.translate("MainWindow", u"Go verify", None))
        self.FAIL_label.setText(QCoreApplication.translate("MainWindow", u"FAIL", None))
        self.reset_pushButton.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.submit_pushButton.setText(QCoreApplication.translate("MainWindow", u"Submit", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_online), QCoreApplication.translate("MainWindow", u"Advanced Operation Mode", None))
        self.start_pushButton.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.goldenmode_checkBox.setText(QCoreApplication.translate("MainWindow", u"Golden Mode", None))
        self.device_offline_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Static Image", None))
        self.device_offline_comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Web Camera", None))
        self.device_offline_comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Basler Camera", None))

        self.device_offline_label.setText(QCoreApplication.translate("MainWindow", u"Select Source", None))
        self.importImage_pushButton.setText(QCoreApplication.translate("MainWindow", u"Import Image", None))
        self.capture_pushButton.setText(QCoreApplication.translate("MainWindow", u"Capture Image", None))
        self.export_pushButton.setText(QCoreApplication.translate("MainWindow", u"Export", None))
        self.train_pushButton.setText(QCoreApplication.translate("MainWindow", u"Train", None))
        self.position_pushButton.setText(QCoreApplication.translate("MainWindow", u"Registration Anchor", None))
        self.label_groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Label Tool", None))
        self.orderList_label.setText(QCoreApplication.translate("MainWindow", u"Order", None))

        __sortingEnabled = self.orderList_listWidget.isSortingEnabled()
        self.orderList_listWidget.setSortingEnabled(False)
        ___qlistwidgetitem = self.orderList_listWidget.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"Ignore", None));
        ___qlistwidgetitem1 = self.orderList_listWidget.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qlistwidgetitem2 = self.orderList_listWidget.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qlistwidgetitem3 = self.orderList_listWidget.item(3)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qlistwidgetitem4 = self.orderList_listWidget.item(4)
        ___qlistwidgetitem4.setText(QCoreApplication.translate("MainWindow", u"4", None));
        ___qlistwidgetitem5 = self.orderList_listWidget.item(5)
        ___qlistwidgetitem5.setText(QCoreApplication.translate("MainWindow", u"5", None));
        ___qlistwidgetitem6 = self.orderList_listWidget.item(6)
        ___qlistwidgetitem6.setText(QCoreApplication.translate("MainWindow", u"6", None));
        ___qlistwidgetitem7 = self.orderList_listWidget.item(7)
        ___qlistwidgetitem7.setText(QCoreApplication.translate("MainWindow", u"7", None));
        ___qlistwidgetitem8 = self.orderList_listWidget.item(8)
        ___qlistwidgetitem8.setText(QCoreApplication.translate("MainWindow", u"8", None));
        ___qlistwidgetitem9 = self.orderList_listWidget.item(9)
        ___qlistwidgetitem9.setText(QCoreApplication.translate("MainWindow", u"9", None));
        ___qlistwidgetitem10 = self.orderList_listWidget.item(10)
        ___qlistwidgetitem10.setText(QCoreApplication.translate("MainWindow", u"10", None));
        ___qlistwidgetitem11 = self.orderList_listWidget.item(11)
        ___qlistwidgetitem11.setText(QCoreApplication.translate("MainWindow", u"11", None));
        ___qlistwidgetitem12 = self.orderList_listWidget.item(12)
        ___qlistwidgetitem12.setText(QCoreApplication.translate("MainWindow", u"12", None));
        ___qlistwidgetitem13 = self.orderList_listWidget.item(13)
        ___qlistwidgetitem13.setText(QCoreApplication.translate("MainWindow", u"13", None));
        ___qlistwidgetitem14 = self.orderList_listWidget.item(14)
        ___qlistwidgetitem14.setText(QCoreApplication.translate("MainWindow", u"14", None));
        ___qlistwidgetitem15 = self.orderList_listWidget.item(15)
        ___qlistwidgetitem15.setText(QCoreApplication.translate("MainWindow", u"15", None));
        ___qlistwidgetitem16 = self.orderList_listWidget.item(16)
        ___qlistwidgetitem16.setText(QCoreApplication.translate("MainWindow", u"16", None));
        ___qlistwidgetitem17 = self.orderList_listWidget.item(17)
        ___qlistwidgetitem17.setText(QCoreApplication.translate("MainWindow", u"17", None));
        ___qlistwidgetitem18 = self.orderList_listWidget.item(18)
        ___qlistwidgetitem18.setText(QCoreApplication.translate("MainWindow", u"18", None));
        ___qlistwidgetitem19 = self.orderList_listWidget.item(19)
        ___qlistwidgetitem19.setText(QCoreApplication.translate("MainWindow", u"19", None));
        ___qlistwidgetitem20 = self.orderList_listWidget.item(20)
        ___qlistwidgetitem20.setText(QCoreApplication.translate("MainWindow", u"20", None));
        self.orderList_listWidget.setSortingEnabled(__sortingEnabled)

        self.labelEdit_pushButton.setText(QCoreApplication.translate("MainWindow", u"Edit ", None))
        self.durationList_label.setText(QCoreApplication.translate("MainWindow", u"Duration", None))

        __sortingEnabled1 = self.durationList_listWidget.isSortingEnabled()
        self.durationList_listWidget.setSortingEnabled(False)
        ___qlistwidgetitem21 = self.durationList_listWidget.item(0)
        ___qlistwidgetitem21.setText(QCoreApplication.translate("MainWindow", u"Ignore", None));
        ___qlistwidgetitem22 = self.durationList_listWidget.item(1)
        ___qlistwidgetitem22.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qlistwidgetitem23 = self.durationList_listWidget.item(2)
        ___qlistwidgetitem23.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qlistwidgetitem24 = self.durationList_listWidget.item(3)
        ___qlistwidgetitem24.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qlistwidgetitem25 = self.durationList_listWidget.item(4)
        ___qlistwidgetitem25.setText(QCoreApplication.translate("MainWindow", u"4", None));
        ___qlistwidgetitem26 = self.durationList_listWidget.item(5)
        ___qlistwidgetitem26.setText(QCoreApplication.translate("MainWindow", u"5", None));
        ___qlistwidgetitem27 = self.durationList_listWidget.item(6)
        ___qlistwidgetitem27.setText(QCoreApplication.translate("MainWindow", u"6", None));
        ___qlistwidgetitem28 = self.durationList_listWidget.item(7)
        ___qlistwidgetitem28.setText(QCoreApplication.translate("MainWindow", u"7", None));
        ___qlistwidgetitem29 = self.durationList_listWidget.item(8)
        ___qlistwidgetitem29.setText(QCoreApplication.translate("MainWindow", u"8", None));
        ___qlistwidgetitem30 = self.durationList_listWidget.item(9)
        ___qlistwidgetitem30.setText(QCoreApplication.translate("MainWindow", u"9", None));
        ___qlistwidgetitem31 = self.durationList_listWidget.item(10)
        ___qlistwidgetitem31.setText(QCoreApplication.translate("MainWindow", u"10", None));
        ___qlistwidgetitem32 = self.durationList_listWidget.item(11)
        ___qlistwidgetitem32.setText(QCoreApplication.translate("MainWindow", u"11", None));
        ___qlistwidgetitem33 = self.durationList_listWidget.item(12)
        ___qlistwidgetitem33.setText(QCoreApplication.translate("MainWindow", u"12", None));
        ___qlistwidgetitem34 = self.durationList_listWidget.item(13)
        ___qlistwidgetitem34.setText(QCoreApplication.translate("MainWindow", u"13", None));
        ___qlistwidgetitem35 = self.durationList_listWidget.item(14)
        ___qlistwidgetitem35.setText(QCoreApplication.translate("MainWindow", u"14", None));
        ___qlistwidgetitem36 = self.durationList_listWidget.item(15)
        ___qlistwidgetitem36.setText(QCoreApplication.translate("MainWindow", u"15", None));
        ___qlistwidgetitem37 = self.durationList_listWidget.item(16)
        ___qlistwidgetitem37.setText(QCoreApplication.translate("MainWindow", u"16", None));
        ___qlistwidgetitem38 = self.durationList_listWidget.item(17)
        ___qlistwidgetitem38.setText(QCoreApplication.translate("MainWindow", u"17", None));
        ___qlistwidgetitem39 = self.durationList_listWidget.item(18)
        ___qlistwidgetitem39.setText(QCoreApplication.translate("MainWindow", u"18", None));
        ___qlistwidgetitem40 = self.durationList_listWidget.item(19)
        ___qlistwidgetitem40.setText(QCoreApplication.translate("MainWindow", u"19", None));
        ___qlistwidgetitem41 = self.durationList_listWidget.item(20)
        ___qlistwidgetitem41.setText(QCoreApplication.translate("MainWindow", u"20", None));
        self.durationList_listWidget.setSortingEnabled(__sortingEnabled1)

        self.labelList_label.setText(QCoreApplication.translate("MainWindow", u"Label List", None))
        self.autoLable_pushButton.setText(QCoreApplication.translate("MainWindow", u"Pattern Label", None))
        self.labelInfo_groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Label Information", None))
        self.delete_pushButton.setText(QCoreApplication.translate("MainWindow", u"Delete Selected Item", None))
        ___qtablewidgetitem4 = self.labelInfo_tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem5 = self.labelInfo_tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Start", None));
#if QT_CONFIG(tooltip)
        ___qtablewidgetitem5.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Upper left conrner</p><p>(x1,y1)</p></body></html>", None));
#endif // QT_CONFIG(tooltip)
        ___qtablewidgetitem6 = self.labelInfo_tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"End", None));
#if QT_CONFIG(tooltip)
        ___qtablewidgetitem6.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Lower right conrner</p><p>(x2,y2)</p></body></html>", None));
#endif // QT_CONFIG(tooltip)
        ___qtablewidgetitem7 = self.labelInfo_tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Order", None));
        ___qtablewidgetitem8 = self.labelInfo_tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Duration(s)", None));
        self.saveLabel_pushButton.setText(QCoreApplication.translate("MainWindow", u"Save Label Result", None))
        ___qtablewidgetitem9 = self.showImagelist_tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Labeled/Unlabeled", None));
        ___qtablewidgetitem10 = self.showImagelist_tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Filename", None));
        ___qtablewidgetitem11 = self.showImagelist_tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Image", None));
        self.next_pushButton.setText(QCoreApplication.translate("MainWindow", u"&Next", None))
        self.page_label.setText(QCoreApplication.translate("MainWindow", u"Page", None))
        self.pageOf_label.setText(QCoreApplication.translate("MainWindow", u"of 1", None))
        self.back_pushButton.setText(QCoreApplication.translate("MainWindow", u"&Back", None))
        ___qtablewidgetitem12 = self.golden_tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Labeled/Unlabeled", None));
        ___qtablewidgetitem13 = self.golden_tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Filename", None));
        ___qtablewidgetitem14 = self.golden_tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Image", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_offline), QCoreApplication.translate("MainWindow", u"Training Mode", None))
        self.model_setting_label.setText(QCoreApplication.translate("MainWindow", u"Model:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Product Number*", None))
        self.sn_setting_lineEdit.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Project Name*", None))
        self.sn_setting_label.setText(QCoreApplication.translate("MainWindow", u"Serial Number:", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Re-Train", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Re-Train", None))
        ___qtreewidgetitem = self.treeWidget.headerItem()
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"Inspection data", None));

        __sortingEnabled2 = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        ___qtreewidgetitem1 = self.treeWidget.topLevelItem(0)
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
        self.treeWidget.setSortingEnabled(__sortingEnabled2)

        self.training_groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Training Setting", None))
        self.training_savePath_label_2.setText(QCoreApplication.translate("MainWindow", u"Number of image column", None))
        self.training_savePath_label.setText(QCoreApplication.translate("MainWindow", u"Inference Type", None))
        self.inference_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Dual In Line Package Inspection", None))

        self.training_ip_label.setText(QCoreApplication.translate("MainWindow", u"IP Address*", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Port", None))
        self.training_account_label.setText(QCoreApplication.translate("MainWindow", u"Account", None))
        self.training_pw_label.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.dip_groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Inference Parameter", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"Export NVIDAI Engine", None))
        self.training_modelConfig_label.setText(QCoreApplication.translate("MainWindow", u"epoch", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Training Data Path*", None))
        self.storage_groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Storage Server", None))
        self.storage_ip_label.setText(QCoreApplication.translate("MainWindow", u"IP Address", None))
        self.storage_account_label.setText(QCoreApplication.translate("MainWindow", u"Account", None))
        self.storage_pw_label.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.storage_path_label.setText(QCoreApplication.translate("MainWindow", u"Path", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Protocal", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Samba", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"FTP", None))

        self.SaveSetting_pushButton.setText(QCoreApplication.translate("MainWindow", u"Save for this Serial Number", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_setting), QCoreApplication.translate("MainWindow", u"System Setting", None))
        self.logo_label.setText("")
        self.menuLanguage.setTitle(QCoreApplication.translate("MainWindow", u"Language", None))
    # retranslateUi

