# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
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
from drawshapes import DrawShapes

import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1160, 848)
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
        self.on_off_label = QLabel(self.tab_online)
        self.on_off_label.setObjectName(u"on_off_label")
        self.on_off_label.setStyleSheet(u"font: 13pt \"Ubuntu\";")

        self.gridLayout_6.addWidget(self.on_off_label, 0, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(654, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer, 0, 2, 1, 1)

        self.showimage_online_label = DrawShapes(self.tab_online)
        self.showimage_online_label.setObjectName(u"showimage_online_label")
        self.showimage_online_label.setEnabled(True)
        sizePolicy2 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.showimage_online_label.sizePolicy().hasHeightForWidth())
        self.showimage_online_label.setSizePolicy(sizePolicy2)
        self.showimage_online_label.setMinimumSize(QSize(800, 600))
        self.showimage_online_label.setFrameShape(QFrame.Box)
        self.showimage_online_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.showimage_online_label, 1, 0, 1, 3)

        self.on_off_checkBox = Toggle(self.tab_online)
        self.on_off_checkBox.setObjectName(u"on_off_checkBox")
        self.on_off_checkBox.setEnabled(False)
        self.on_off_checkBox.setMinimumSize(QSize(70, 0))
        self.on_off_checkBox.setLayoutDirection(Qt.LeftToRight)

        self.gridLayout_6.addWidget(self.on_off_checkBox, 0, 1, 1, 1)

        self.widget = QWidget(self.tab_online)
        self.widget.setObjectName(u"widget")
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMaximumSize(QSize(300, 16777215))
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
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.sn_online_lineEdit.sizePolicy().hasHeightForWidth())
        self.sn_online_lineEdit.setSizePolicy(sizePolicy3)

        self.gridLayout.addWidget(self.sn_online_lineEdit, 2, 1, 1, 1)

        self.device_online_comboBox = QComboBox(self.widget)
        self.device_online_comboBox.addItem("")
        self.device_online_comboBox.addItem("")
        self.device_online_comboBox.setObjectName(u"device_online_comboBox")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.device_online_comboBox.sizePolicy().hasHeightForWidth())
        self.device_online_comboBox.setSizePolicy(sizePolicy4)

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
        self.inspect_groupBox.setMaximumSize(QSize(300, 16777215))
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
        self.goverify_pushButton = QPushButton(self.inspect_groupBox)
        self.goverify_pushButton.setObjectName(u"goverify_pushButton")
        self.goverify_pushButton.setEnabled(False)
        self.goverify_pushButton.setMinimumSize(QSize(0, 40))
        self.goverify_pushButton.setStyleSheet(u"background-color: rgb(79, 226, 239);")

        self.gridLayout_2.addWidget(self.goverify_pushButton, 0, 1, 1, 1)

        self.inspectResult_tableWidget = QTableWidget(self.inspect_groupBox)
        if (self.inspectResult_tableWidget.columnCount() < 2):
            self.inspectResult_tableWidget.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.inspectResult_tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.inspectResult_tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        if (self.inspectResult_tableWidget.rowCount() < 3):
            self.inspectResult_tableWidget.setRowCount(3)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.inspectResult_tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.inspectResult_tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.inspectResult_tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.inspectResult_tableWidget.setItem(0, 0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.inspectResult_tableWidget.setItem(0, 1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.inspectResult_tableWidget.setItem(1, 0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.inspectResult_tableWidget.setItem(1, 1, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.inspectResult_tableWidget.setItem(2, 0, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        __qtablewidgetitem10.setText(u"NG");
        self.inspectResult_tableWidget.setItem(2, 1, __qtablewidgetitem10)
        self.inspectResult_tableWidget.setObjectName(u"inspectResult_tableWidget")
        sizePolicy5 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.inspectResult_tableWidget.sizePolicy().hasHeightForWidth())
        self.inspectResult_tableWidget.setSizePolicy(sizePolicy5)
        self.inspectResult_tableWidget.setShowGrid(False)
        self.inspectResult_tableWidget.setSortingEnabled(False)
        self.inspectResult_tableWidget.setWordWrap(True)
        self.inspectResult_tableWidget.setCornerButtonEnabled(True)
        self.inspectResult_tableWidget.horizontalHeader().setVisible(False)
        self.inspectResult_tableWidget.verticalHeader().setVisible(False)

        self.gridLayout_2.addWidget(self.inspectResult_tableWidget, 1, 0, 1, 5)

        self.reset_pushButton = QPushButton(self.inspect_groupBox)
        self.reset_pushButton.setObjectName(u"reset_pushButton")
        self.reset_pushButton.setEnabled(False)
        self.reset_pushButton.setMinimumSize(QSize(0, 40))

        self.gridLayout_2.addWidget(self.reset_pushButton, 0, 3, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_3, 0, 2, 1, 1)


        self.gridLayout_4.addWidget(self.inspect_groupBox, 2, 0, 1, 2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.NG_pushButton = QPushButton(self.widget)
        self.NG_pushButton.setObjectName(u"NG_pushButton")
        self.NG_pushButton.setEnabled(False)
        sizePolicy6 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.NG_pushButton.sizePolicy().hasHeightForWidth())
        self.NG_pushButton.setSizePolicy(sizePolicy6)
        self.NG_pushButton.setMinimumSize(QSize(0, 80))
        self.NG_pushButton.setStyleSheet(u"background-color: rgb(249, 122, 122);")

        self.horizontalLayout.addWidget(self.NG_pushButton)

        self.horizontalSpacer_4 = QSpacerItem(57, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)

        self.PASS_pushButton = QPushButton(self.widget)
        self.PASS_pushButton.setObjectName(u"PASS_pushButton")
        self.PASS_pushButton.setEnabled(False)
        self.PASS_pushButton.setMinimumSize(QSize(0, 80))
        self.PASS_pushButton.setStyleSheet(u"background-color: rgb(205, 249, 161);")

        self.horizontalLayout.addWidget(self.PASS_pushButton)


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

        self.horizontalSpacer_13 = QSpacerItem(100, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_13)

        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.device_offline_label = QLabel(self.tab_offline)
        self.device_offline_label.setObjectName(u"device_offline_label")
        self.device_offline_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_7.addWidget(self.device_offline_label, 0, 0, 1, 1)

        self.device_offline_comboBox = QComboBox(self.tab_offline)
        self.device_offline_comboBox.addItem("")
        self.device_offline_comboBox.addItem("")
        self.device_offline_comboBox.addItem("")
        self.device_offline_comboBox.setObjectName(u"device_offline_comboBox")
        self.device_offline_comboBox.setEnabled(False)

        self.gridLayout_7.addWidget(self.device_offline_comboBox, 0, 1, 1, 1)


        self.horizontalLayout_2.addLayout(self.gridLayout_7)

        self.capture_pushButton = QPushButton(self.tab_offline)
        self.capture_pushButton.setObjectName(u"capture_pushButton")
        self.capture_pushButton.setEnabled(False)
        self.capture_pushButton.setMinimumSize(QSize(0, 40))

        self.horizontalLayout_2.addWidget(self.capture_pushButton)

        self.horizontalSpacer_2 = QSpacerItem(450, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

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

        self.horizontalLayout_2.addWidget(self.train_pushButton)


        self.gridLayout_16.addLayout(self.horizontalLayout_2, 0, 0, 1, 3)

        self.line_3 = QFrame(self.tab_offline)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.gridLayout_16.addWidget(self.line_3, 1, 0, 1, 3)

        self.widget_3 = QWidget(self.tab_offline)
        self.widget_3.setObjectName(u"widget_3")
        sizePolicy5.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy5)
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
        sizePolicy5.setHeightForWidth(self.label_groupBox.sizePolicy().hasHeightForWidth())
        self.label_groupBox.setSizePolicy(sizePolicy5)
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

        self.gridLayout_3.addWidget(self.autoLable_pushButton, 2, 0, 1, 3)


        self.gridLayout_10.addWidget(self.label_groupBox, 2, 0, 1, 1)

        self.line_4 = QFrame(self.widget_3)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.gridLayout_10.addWidget(self.line_4, 1, 0, 1, 1)


        self.gridLayout_16.addWidget(self.widget_3, 2, 0, 2, 1)

        self.showImage_offline_label = DrawShapes(self.tab_offline)
        self.showImage_offline_label.setObjectName(u"showImage_offline_label")
        sizePolicy6.setHeightForWidth(self.showImage_offline_label.sizePolicy().hasHeightForWidth())
        self.showImage_offline_label.setSizePolicy(sizePolicy6)
        self.showImage_offline_label.setMinimumSize(QSize(600, 450))
        self.showImage_offline_label.setStyleSheet(u"border-color: rgb(138, 226, 52);")
        self.showImage_offline_label.setFrameShape(QFrame.Box)
        self.showImage_offline_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_16.addWidget(self.showImage_offline_label, 3, 1, 1, 1)

        self.widget_2 = QWidget(self.tab_offline)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy5.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy5)
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
        self.labelInfo_tableWidget = QTableWidget(self.labelInfo_groupBox)
        if (self.labelInfo_tableWidget.columnCount() < 5):
            self.labelInfo_tableWidget.setColumnCount(5)
        font = QFont()
        font.setPointSize(8)
        __qtablewidgetitem11 = QTableWidgetItem()
        __qtablewidgetitem11.setFont(font);
        self.labelInfo_tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        __qtablewidgetitem12.setFont(font);
        self.labelInfo_tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        __qtablewidgetitem13.setFont(font);
        self.labelInfo_tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        __qtablewidgetitem14.setFont(font);
        self.labelInfo_tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        __qtablewidgetitem15.setFont(font);
        self.labelInfo_tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem15)
        self.labelInfo_tableWidget.setObjectName(u"labelInfo_tableWidget")
        sizePolicy7 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.labelInfo_tableWidget.sizePolicy().hasHeightForWidth())
        self.labelInfo_tableWidget.setSizePolicy(sizePolicy7)
        self.labelInfo_tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.labelInfo_tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.labelInfo_tableWidget.horizontalHeader().setMinimumSectionSize(30)

        self.gridLayout_5.addWidget(self.labelInfo_tableWidget, 0, 0, 1, 2)

        self.delete_pushButton = QPushButton(self.labelInfo_groupBox)
        self.delete_pushButton.setObjectName(u"delete_pushButton")
        self.delete_pushButton.setEnabled(False)
        self.delete_pushButton.setMinimumSize(QSize(0, 40))

        self.gridLayout_5.addWidget(self.delete_pushButton, 1, 0, 1, 2)


        self.gridLayout_9.addWidget(self.labelInfo_groupBox, 0, 0, 1, 1)

        self.saveasgolden_pushButton = QPushButton(self.widget_2)
        self.saveasgolden_pushButton.setObjectName(u"saveasgolden_pushButton")
        self.saveasgolden_pushButton.setEnabled(False)
        self.saveasgolden_pushButton.setMinimumSize(QSize(0, 20))
        self.saveasgolden_pushButton.setStyleSheet(u"background-color: rgb(252, 202, 202);")

        self.gridLayout_9.addWidget(self.saveasgolden_pushButton, 2, 0, 1, 1)

        self.saveLabel_pushButton = QPushButton(self.widget_2)
        self.saveLabel_pushButton.setObjectName(u"saveLabel_pushButton")
        self.saveLabel_pushButton.setEnabled(False)
        self.saveLabel_pushButton.setMinimumSize(QSize(0, 20))
        self.saveLabel_pushButton.setStyleSheet(u"background-color: rgb(252, 202, 202);")

        self.gridLayout_9.addWidget(self.saveLabel_pushButton, 3, 0, 1, 1)


        self.gridLayout_16.addWidget(self.widget_2, 3, 2, 1, 1)

        self.widget_5 = QWidget(self.tab_offline)
        self.widget_5.setObjectName(u"widget_5")
        sizePolicy8 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.widget_5.sizePolicy().hasHeightForWidth())
        self.widget_5.setSizePolicy(sizePolicy8)
        self.widget_5.setMaximumSize(QSize(16777215, 150))
        self.gridLayout_15 = QGridLayout(self.widget_5)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.showImagelist_tableWidget = QTableWidget(self.widget_5)
        if (self.showImagelist_tableWidget.rowCount() < 3):
            self.showImagelist_tableWidget.setRowCount(3)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.showImagelist_tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.showImagelist_tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.showImagelist_tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem18)
        self.showImagelist_tableWidget.setObjectName(u"showImagelist_tableWidget")
        sizePolicy8.setHeightForWidth(self.showImagelist_tableWidget.sizePolicy().hasHeightForWidth())
        self.showImagelist_tableWidget.setSizePolicy(sizePolicy8)
        self.showImagelist_tableWidget.setMaximumSize(QSize(16777215, 150))
        self.showImagelist_tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.showImagelist_tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.showImagelist_tableWidget.setSelectionBehavior(QAbstractItemView.SelectColumns)
        self.showImagelist_tableWidget.setShowGrid(False)
        self.showImagelist_tableWidget.horizontalHeader().setVisible(False)
        self.showImagelist_tableWidget.verticalHeader().setVisible(False)
        self.showImagelist_tableWidget.verticalHeader().setStretchLastSection(True)

        self.gridLayout_15.addWidget(self.showImagelist_tableWidget, 0, 1, 1, 1)

        self.widget_4 = QWidget(self.widget_5)
        self.widget_4.setObjectName(u"widget_4")
        sizePolicy6.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy6)
        self.widget_4.setMinimumSize(QSize(120, 0))
        self.widget_4.setMaximumSize(QSize(16777215, 150))
        self.verticalLayout_2 = QVBoxLayout(self.widget_4)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.next_pushButton = QPushButton(self.widget_4)
        self.next_pushButton.setObjectName(u"next_pushButton")
        self.next_pushButton.setEnabled(False)
        sizePolicy9 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.next_pushButton.sizePolicy().hasHeightForWidth())
        self.next_pushButton.setSizePolicy(sizePolicy9)
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
        sizePolicy9.setHeightForWidth(self.back_pushButton.sizePolicy().hasHeightForWidth())
        self.back_pushButton.setSizePolicy(sizePolicy9)
        self.back_pushButton.setMinimumSize(QSize(0, 30))

        self.verticalLayout_2.addWidget(self.back_pushButton)


        self.gridLayout_15.addWidget(self.widget_4, 0, 2, 1, 1)


        self.gridLayout_16.addWidget(self.widget_5, 4, 0, 1, 3)

        self.tabWidget.addTab(self.tab_offline, "")
        self.tab_setting = QWidget()
        self.tab_setting.setObjectName(u"tab_setting")
        self.gridLayout_19 = QGridLayout(self.tab_setting)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.gridLayout_11 = QGridLayout()
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.sn_setting_label = QLabel(self.tab_setting)
        self.sn_setting_label.setObjectName(u"sn_setting_label")
        self.sn_setting_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_11.addWidget(self.sn_setting_label, 0, 0, 1, 1)

        self.sn_setting_lineEdit = QLineEdit(self.tab_setting)
        self.sn_setting_lineEdit.setObjectName(u"sn_setting_lineEdit")

        self.gridLayout_11.addWidget(self.sn_setting_lineEdit, 0, 1, 1, 1)

        self.model_setting_comboBox = QComboBox(self.tab_setting)
        self.model_setting_comboBox.setObjectName(u"model_setting_comboBox")

        self.gridLayout_11.addWidget(self.model_setting_comboBox, 1, 1, 1, 1)

        self.model_setting_label = QLabel(self.tab_setting)
        self.model_setting_label.setObjectName(u"model_setting_label")
        self.model_setting_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_11.addWidget(self.model_setting_label, 1, 0, 1, 1)


        self.gridLayout_19.addLayout(self.gridLayout_11, 0, 0, 1, 1)

        self.line_2 = QFrame(self.tab_setting)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout_19.addWidget(self.line_2, 0, 1, 4, 1)

        self.storage_groupBox = QGroupBox(self.tab_setting)
        self.storage_groupBox.setObjectName(u"storage_groupBox")
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
        self.storage_ip_label = QLabel(self.storage_groupBox)
        self.storage_ip_label.setObjectName(u"storage_ip_label")
        self.storage_ip_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_12.addWidget(self.storage_ip_label, 0, 0, 1, 1)

        self.storage_account_label = QLabel(self.storage_groupBox)
        self.storage_account_label.setObjectName(u"storage_account_label")
        self.storage_account_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_12.addWidget(self.storage_account_label, 1, 0, 1, 1)

        self.storage_account_lineEdit = QLineEdit(self.storage_groupBox)
        self.storage_account_lineEdit.setObjectName(u"storage_account_lineEdit")

        self.gridLayout_12.addWidget(self.storage_account_lineEdit, 1, 1, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(150, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_12.addItem(self.horizontalSpacer_6, 1, 2, 1, 1)

        self.storage_pw_label = QLabel(self.storage_groupBox)
        self.storage_pw_label.setObjectName(u"storage_pw_label")
        self.storage_pw_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_12.addWidget(self.storage_pw_label, 2, 0, 1, 1)

        self.storage_pw_lineEdit = PasswordEdit(self.storage_groupBox)
        self.storage_pw_lineEdit.setObjectName(u"storage_pw_lineEdit")

        self.gridLayout_12.addWidget(self.storage_pw_lineEdit, 2, 1, 1, 1)

        self.storage_path_label = QLabel(self.storage_groupBox)
        self.storage_path_label.setObjectName(u"storage_path_label")
        self.storage_path_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_12.addWidget(self.storage_path_label, 3, 0, 1, 1)

        self.storage_path_lineEdit = QLineEdit(self.storage_groupBox)
        self.storage_path_lineEdit.setObjectName(u"storage_path_lineEdit")
        self.storage_path_lineEdit.setMinimumSize(QSize(250, 0))

        self.gridLayout_12.addWidget(self.storage_path_lineEdit, 3, 1, 1, 2)

        self.storage_ip_lineEdit = QLineEdit(self.storage_groupBox)
        self.storage_ip_lineEdit.setObjectName(u"storage_ip_lineEdit")

        self.gridLayout_12.addWidget(self.storage_ip_lineEdit, 0, 1, 1, 1)


        self.gridLayout_19.addWidget(self.storage_groupBox, 0, 2, 2, 1)

        self.tabWidget_2 = QTabWidget(self.tab_setting)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_17 = QGridLayout(self.tab)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.label = QLabel(self.tab)
        self.label.setObjectName(u"label")

        self.gridLayout_17.addWidget(self.label, 0, 0, 1, 1)

        self.label_2 = QLabel(self.tab)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_17.addWidget(self.label_2, 1, 0, 1, 2)

        self.label_3 = QLabel(self.tab)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_17.addWidget(self.label_3, 2, 0, 1, 1)

        self.label_4 = QLabel(self.tab)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_17.addWidget(self.label_4, 3, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_17.addItem(self.verticalSpacer_2, 4, 1, 1, 1)

        self.tabWidget_2.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_14 = QGridLayout(self.tab_2)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.verticalSpacer_4 = QSpacerItem(20, 243, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_14.addItem(self.verticalSpacer_4, 3, 0, 1, 1)

        self.label_6 = QLabel(self.tab_2)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_14.addWidget(self.label_6, 1, 0, 1, 1)

        self.label_5 = QLabel(self.tab_2)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_14.addWidget(self.label_5, 0, 0, 1, 1)

        self.label_11 = QLabel(self.tab_2)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_14.addWidget(self.label_11, 2, 0, 1, 1)

        self.tabWidget_2.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayout_18 = QGridLayout(self.tab_3)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.label_7 = QLabel(self.tab_3)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_18.addWidget(self.label_7, 0, 0, 1, 1)

        self.label_8 = QLabel(self.tab_3)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_18.addWidget(self.label_8, 1, 0, 1, 1)

        self.label_9 = QLabel(self.tab_3)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_18.addWidget(self.label_9, 2, 0, 1, 1)

        self.label_10 = QLabel(self.tab_3)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_18.addWidget(self.label_10, 3, 0, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 220, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_18.addItem(self.verticalSpacer_5, 4, 0, 1, 1)

        self.tabWidget_2.addTab(self.tab_3, "")

        self.gridLayout_19.addWidget(self.tabWidget_2, 1, 0, 2, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 161, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_19.addItem(self.verticalSpacer_6, 3, 2, 1, 1)

        self.line_7 = QFrame(self.tab_setting)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.HLine)
        self.line_7.setFrameShadow(QFrame.Sunken)

        self.gridLayout_19.addWidget(self.line_7, 4, 0, 1, 4)

        self.horizontalSpacer_7 = QSpacerItem(921, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_19.addItem(self.horizontalSpacer_7, 5, 0, 1, 3)

        self.SaveSetting_pushButton = QPushButton(self.tab_setting)
        self.SaveSetting_pushButton.setObjectName(u"SaveSetting_pushButton")
        self.SaveSetting_pushButton.setMinimumSize(QSize(150, 40))

        self.gridLayout_19.addWidget(self.SaveSetting_pushButton, 5, 3, 1, 1)

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
        self.gridLayout_13 = QGridLayout(self.training_groupBox)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.training_modelConfig_label = QLabel(self.training_groupBox)
        self.training_modelConfig_label.setObjectName(u"training_modelConfig_label")
        self.training_modelConfig_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_13.addWidget(self.training_modelConfig_label, 5, 0, 1, 1)

        self.training_savePath_label = QLabel(self.training_groupBox)
        self.training_savePath_label.setObjectName(u"training_savePath_label")
        self.training_savePath_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_13.addWidget(self.training_savePath_label, 3, 0, 1, 1)

        self.training_activeTime_label = QLabel(self.training_groupBox)
        self.training_activeTime_label.setObjectName(u"training_activeTime_label")
        self.training_activeTime_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_13.addWidget(self.training_activeTime_label, 6, 0, 1, 1)

        self.training_ip_lineEdit = QLineEdit(self.training_groupBox)
        self.training_ip_lineEdit.setObjectName(u"training_ip_lineEdit")

        self.gridLayout_13.addWidget(self.training_ip_lineEdit, 0, 1, 1, 1)

        self.training_modelConfig_lineEdit = QLineEdit(self.training_groupBox)
        self.training_modelConfig_lineEdit.setObjectName(u"training_modelConfig_lineEdit")
        self.training_modelConfig_lineEdit.setMinimumSize(QSize(250, 0))

        self.gridLayout_13.addWidget(self.training_modelConfig_lineEdit, 5, 1, 1, 2)

        self.training_pw_label = QLabel(self.training_groupBox)
        self.training_pw_label.setObjectName(u"training_pw_label")
        self.training_pw_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_13.addWidget(self.training_pw_label, 2, 0, 1, 1)

        self.training_pw_lineEdit = PasswordEdit(self.training_groupBox)
        self.training_pw_lineEdit.setObjectName(u"training_pw_lineEdit")

        self.gridLayout_13.addWidget(self.training_pw_lineEdit, 2, 1, 1, 1)

        self.training_savePath_lineEdit = QLineEdit(self.training_groupBox)
        self.training_savePath_lineEdit.setObjectName(u"training_savePath_lineEdit")
        self.training_savePath_lineEdit.setMinimumSize(QSize(250, 0))

        self.gridLayout_13.addWidget(self.training_savePath_lineEdit, 3, 1, 1, 2)

        self.training_ip_label = QLabel(self.training_groupBox)
        self.training_ip_label.setObjectName(u"training_ip_label")
        self.training_ip_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_13.addWidget(self.training_ip_label, 0, 0, 1, 1)

        self.training_account_label = QLabel(self.training_groupBox)
        self.training_account_label.setObjectName(u"training_account_label")
        self.training_account_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_13.addWidget(self.training_account_label, 1, 0, 1, 1)

        self.horizontalSpacer_8 = QSpacerItem(139, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_13.addItem(self.horizontalSpacer_8, 1, 2, 1, 1)

        self.training_pretrained_label = QLabel(self.training_groupBox)
        self.training_pretrained_label.setObjectName(u"training_pretrained_label")
        self.training_pretrained_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_13.addWidget(self.training_pretrained_label, 4, 0, 1, 1)

        self.training_account_lineEdit = QLineEdit(self.training_groupBox)
        self.training_account_lineEdit.setObjectName(u"training_account_lineEdit")

        self.gridLayout_13.addWidget(self.training_account_lineEdit, 1, 1, 1, 1)

        self.training_pretrained_lineEdit = QLineEdit(self.training_groupBox)
        self.training_pretrained_lineEdit.setObjectName(u"training_pretrained_lineEdit")
        self.training_pretrained_lineEdit.setMinimumSize(QSize(250, 0))

        self.gridLayout_13.addWidget(self.training_pretrained_lineEdit, 4, 1, 1, 2)

        self.training_activeTime_lineEdit = QLineEdit(self.training_groupBox)
        self.training_activeTime_lineEdit.setObjectName(u"training_activeTime_lineEdit")

        self.gridLayout_13.addWidget(self.training_activeTime_lineEdit, 6, 1, 1, 1)

        self.retrain_label = QLabel(self.training_groupBox)
        self.retrain_label.setObjectName(u"retrain_label")

        self.gridLayout_13.addWidget(self.retrain_label, 7, 0, 1, 1)

        self.retrain_spinBox = QSpinBox(self.training_groupBox)
        self.retrain_spinBox.setObjectName(u"retrain_spinBox")
        self.retrain_spinBox.setValue(20)

        self.gridLayout_13.addWidget(self.retrain_spinBox, 7, 1, 1, 1)


        self.gridLayout_19.addWidget(self.training_groupBox, 2, 2, 1, 1)

        self.tabWidget.addTab(self.tab_setting, "")

        self.gridLayout_8.addWidget(self.tabWidget, 0, 0, 1, 3)

        self.logo_label = QLabel(self.centralwidget)
        self.logo_label.setObjectName(u"logo_label")
        self.logo_label.setMaximumSize(QSize(120, 60))
        self.logo_label.setPixmap(QPixmap(u":/<logo>/resource/EVA_logo"))
        self.logo_label.setScaledContents(True)

        self.gridLayout_8.addWidget(self.logo_label, 1, 0, 1, 1)

        self.exit_pushButton = QPushButton(self.centralwidget)
        self.exit_pushButton.setObjectName(u"exit_pushButton")
        self.exit_pushButton.setMinimumSize(QSize(0, 40))

        self.gridLayout_8.addWidget(self.exit_pushButton, 1, 2, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(909, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_5, 1, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1160, 22))
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
        QWidget.setTabOrder(self.on_off_checkBox, self.NG_pushButton)
        QWidget.setTabOrder(self.NG_pushButton, self.inspectResult_tableWidget)
        QWidget.setTabOrder(self.inspectResult_tableWidget, self.device_online_comboBox)
        QWidget.setTabOrder(self.device_online_comboBox, self.sn_online_lineEdit)
        QWidget.setTabOrder(self.sn_online_lineEdit, self.PASS_pushButton)

        self.menubar.addAction(self.menuLanguage.menuAction())
        self.menuLanguage.addAction(self.actionEnglish)
        self.menuLanguage.addAction(self.actionChinese)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(1)
        self.orderList_listWidget.setCurrentRow(0)
        self.durationList_listWidget.setCurrentRow(0)
        self.tabWidget_2.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"ADLINK AI Automatic Inspection", None))
        self.actionEnglish.setText(QCoreApplication.translate("MainWindow", u"English", None))
        self.actionChinese.setText(QCoreApplication.translate("MainWindow", u"Chinese", None))
        self.on_off_label.setText(QCoreApplication.translate("MainWindow", u"On/Off", None))
        self.showimage_online_label.setText("")
        self.on_off_checkBox.setText(QCoreApplication.translate("MainWindow", u"on/off", None))
        self.sn_online_label.setText(QCoreApplication.translate("MainWindow", u"Serial Number:", None))
        self.device_online_label.setText(QCoreApplication.translate("MainWindow", u"Select Device:", None))
        self.model_online_label.setText(QCoreApplication.translate("MainWindow", u"Model:", None))
        self.sn_online_lineEdit.setText("")
        self.device_online_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Web Camera", None))
        self.device_online_comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Basler Camera", None))

        self.status_Label.setText(QCoreApplication.translate("MainWindow", u"Status:", None))
        self.currentstatus_label.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.inspect_groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Insepct Result", None))
        self.goverify_pushButton.setText(QCoreApplication.translate("MainWindow", u"Go verify", None))
        ___qtablewidgetitem = self.inspectResult_tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtablewidgetitem1 = self.inspectResult_tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtablewidgetitem2 = self.inspectResult_tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem3 = self.inspectResult_tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem4 = self.inspectResult_tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"New Row", None));

        __sortingEnabled = self.inspectResult_tableWidget.isSortingEnabled()
        self.inspectResult_tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem5 = self.inspectResult_tableWidget.item(0, 0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"XXXXXX", None));
        ___qtablewidgetitem6 = self.inspectResult_tableWidget.item(0, 1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"OK", None));
        ___qtablewidgetitem7 = self.inspectResult_tableWidget.item(1, 0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"XXX", None));
        ___qtablewidgetitem8 = self.inspectResult_tableWidget.item(1, 1)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"OK", None));
        ___qtablewidgetitem9 = self.inspectResult_tableWidget.item(2, 0)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"XXXX", None));
        self.inspectResult_tableWidget.setSortingEnabled(__sortingEnabled)

        self.reset_pushButton.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.NG_pushButton.setText(QCoreApplication.translate("MainWindow", u"NG", None))
        self.PASS_pushButton.setText(QCoreApplication.translate("MainWindow", u"PASS", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_online), QCoreApplication.translate("MainWindow", u"Operation Mode", None))
        self.start_pushButton.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.device_offline_label.setText(QCoreApplication.translate("MainWindow", u"Select Source", None))
        self.device_offline_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Static Image", None))
        self.device_offline_comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Web Camera", None))
        self.device_offline_comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Basler Camera", None))

        self.capture_pushButton.setText(QCoreApplication.translate("MainWindow", u"Capture Image", None))
        self.export_pushButton.setText(QCoreApplication.translate("MainWindow", u"Export", None))
        self.train_pushButton.setText(QCoreApplication.translate("MainWindow", u"Train", None))
        self.position_pushButton.setText(QCoreApplication.translate("MainWindow", u"Positioning tool", None))
        self.label_groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Label Tool", None))
        self.orderList_label.setText(QCoreApplication.translate("MainWindow", u"Order", None))

        __sortingEnabled1 = self.orderList_listWidget.isSortingEnabled()
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
        self.orderList_listWidget.setSortingEnabled(__sortingEnabled1)

        self.labelEdit_pushButton.setText(QCoreApplication.translate("MainWindow", u"Edit ", None))
        self.durationList_label.setText(QCoreApplication.translate("MainWindow", u"Duration", None))

        __sortingEnabled2 = self.durationList_listWidget.isSortingEnabled()
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
        self.durationList_listWidget.setSortingEnabled(__sortingEnabled2)

        self.labelList_label.setText(QCoreApplication.translate("MainWindow", u"Label List", None))
        self.autoLable_pushButton.setText(QCoreApplication.translate("MainWindow", u"Auto Label", None))
        self.showImage_offline_label.setText("")
        self.labelInfo_groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Label Information", None))
        ___qtablewidgetitem10 = self.labelInfo_tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem11 = self.labelInfo_tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Start", None));
#if QT_CONFIG(tooltip)
        ___qtablewidgetitem11.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Upper left conrner</p><p>(x1,y1)</p></body></html>", None));
#endif // QT_CONFIG(tooltip)
        ___qtablewidgetitem12 = self.labelInfo_tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"End", None));
#if QT_CONFIG(tooltip)
        ___qtablewidgetitem12.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Lower right conrner</p><p>(x2,y2)</p></body></html>", None));
#endif // QT_CONFIG(tooltip)
        ___qtablewidgetitem13 = self.labelInfo_tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Order", None));
        ___qtablewidgetitem14 = self.labelInfo_tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Duration(s)", None));
        self.delete_pushButton.setText(QCoreApplication.translate("MainWindow", u"Delete Selected Item", None))
        self.saveasgolden_pushButton.setText(QCoreApplication.translate("MainWindow", u"save as Golden", None))
        self.saveLabel_pushButton.setText(QCoreApplication.translate("MainWindow", u"save image/label result", None))
        ___qtablewidgetitem15 = self.showImagelist_tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Labeled/Unlabeled", None));
        ___qtablewidgetitem16 = self.showImagelist_tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"Filename", None));
        ___qtablewidgetitem17 = self.showImagelist_tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"Image", None));
        self.next_pushButton.setText(QCoreApplication.translate("MainWindow", u"&Next", None))
        self.page_label.setText(QCoreApplication.translate("MainWindow", u"Page", None))
        self.pageOf_label.setText(QCoreApplication.translate("MainWindow", u"of 1", None))
        self.back_pushButton.setText(QCoreApplication.translate("MainWindow", u"&Back", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_offline), QCoreApplication.translate("MainWindow", u"Training Mode", None))
        self.sn_setting_label.setText(QCoreApplication.translate("MainWindow", u"Serial Number:", None))
        self.sn_setting_lineEdit.setText("")
        self.model_setting_label.setText(QCoreApplication.translate("MainWindow", u"Model:", None))
        self.storage_groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Storage Server", None))
        self.storage_ip_label.setText(QCoreApplication.translate("MainWindow", u"ip Address", None))
        self.storage_account_label.setText(QCoreApplication.translate("MainWindow", u"Account", None))
        self.storage_pw_label.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.storage_path_label.setText(QCoreApplication.translate("MainWindow", u"Path", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"name", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"related model number", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"accuracy", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"....", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Basic", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"related product", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"trained data", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"....", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Data", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"trained image number", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"trained class number", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"portion of the training data", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Report", None))
        self.SaveSetting_pushButton.setText(QCoreApplication.translate("MainWindow", u"Save for this Serial number", None))
        self.training_groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Training Server", None))
        self.training_modelConfig_label.setText(QCoreApplication.translate("MainWindow", u"Model Config", None))
        self.training_savePath_label.setText(QCoreApplication.translate("MainWindow", u"Save path", None))
        self.training_activeTime_label.setText(QCoreApplication.translate("MainWindow", u"Active Time", None))
        self.training_pw_label.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.training_ip_label.setText(QCoreApplication.translate("MainWindow", u"ip address", None))
        self.training_account_label.setText(QCoreApplication.translate("MainWindow", u"Account", None))
        self.training_pretrained_label.setText(QCoreApplication.translate("MainWindow", u"Pretrained", None))
        self.retrain_label.setText(QCoreApplication.translate("MainWindow", u"Retrain in online", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_setting), QCoreApplication.translate("MainWindow", u"System Setting", None))
        self.logo_label.setText("")
        self.exit_pushButton.setText(QCoreApplication.translate("MainWindow", u"E&xit", None))
        self.menuLanguage.setTitle(QCoreApplication.translate("MainWindow", u"Language", None))
    # retranslateUi

