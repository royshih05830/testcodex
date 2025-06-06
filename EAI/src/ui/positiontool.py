# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'positiontool.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from drawshapes import DrawShapes


class Ui_PositionDialog(object):
    def setupUi(self, PositionDialog):
        if not PositionDialog.objectName():
            PositionDialog.setObjectName(u"PositionDialog")
        PositionDialog.resize(892, 564)
        self.gridLayout_4 = QGridLayout(PositionDialog)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.widget = QWidget(PositionDialog)
        self.widget.setObjectName(u"widget")
        self.gridLayout_3 = QGridLayout(self.widget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.source_groupBox = QGroupBox(self.widget)
        self.source_groupBox.setObjectName(u"source_groupBox")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.source_groupBox.sizePolicy().hasHeightForWidth())
        self.source_groupBox.setSizePolicy(sizePolicy)
        self.source_groupBox.setMinimumSize(QSize(250, 0))
        self.source_groupBox.setMaximumSize(QSize(250, 16777215))
        self.source_groupBox.setStyleSheet(u"QGroupBox{\n"
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
        self.gridLayout = QGridLayout(self.source_groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.static_radioButton = QRadioButton(self.source_groupBox)
        self.static_radioButton.setObjectName(u"static_radioButton")
        self.static_radioButton.setChecked(True)

        self.gridLayout.addWidget(self.static_radioButton, 0, 0, 1, 2)

        self.horizontalSpacer = QSpacerItem(18, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.import_pushButton = QPushButton(self.source_groupBox)
        self.import_pushButton.setObjectName(u"import_pushButton")
        self.import_pushButton.setMinimumSize(QSize(0, 30))

        self.gridLayout.addWidget(self.import_pushButton, 1, 1, 1, 1)

        self.live_radioButton = QRadioButton(self.source_groupBox)
        self.live_radioButton.setObjectName(u"live_radioButton")

        self.gridLayout.addWidget(self.live_radioButton, 2, 0, 1, 2)

        self.horizontalSpacer_2 = QSpacerItem(18, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 3, 0, 1, 1)

        self.camera_comboBox = QComboBox(self.source_groupBox)
        self.camera_comboBox.addItem("")
        self.camera_comboBox.addItem("")
        self.camera_comboBox.addItem("")
        self.camera_comboBox.setObjectName(u"camera_comboBox")
        self.camera_comboBox.setEnabled(False)
        self.camera_comboBox.setMinimumSize(QSize(0, 30))

        self.gridLayout.addWidget(self.camera_comboBox, 3, 1, 1, 1)

        self.capture_pushButton = QPushButton(self.source_groupBox)
        self.capture_pushButton.setObjectName(u"capture_pushButton")
        self.capture_pushButton.setEnabled(False)
        self.capture_pushButton.setMinimumSize(QSize(0, 30))

        self.gridLayout.addWidget(self.capture_pushButton, 4, 1, 1, 1)


        self.gridLayout_3.addWidget(self.source_groupBox, 0, 0, 1, 1)

        self.showImage_label = DrawShapes(self.widget)
        self.showImage_label.setObjectName(u"showImage_label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.showImage_label.sizePolicy().hasHeightForWidth())
        self.showImage_label.setSizePolicy(sizePolicy1)
        self.showImage_label.setMinimumSize(QSize(600, 450))
        self.showImage_label.setStyleSheet(u"border-color: rgb(138, 226, 52);")
        self.showImage_label.setFrameShape(QFrame.Box)

        self.gridLayout_3.addWidget(self.showImage_label, 0, 1, 3, 1)

        self.groupBox = QGroupBox(self.widget)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QSize(250, 0))
        self.groupBox.setMaximumSize(QSize(250, 16777215))
        self.groupBox.setStyleSheet(u"QGroupBox{\n"
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
        self.gridLayout_5 = QGridLayout(self.groupBox)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.point3_lineEdit = QLineEdit(self.groupBox)
        self.point3_lineEdit.setObjectName(u"point3_lineEdit")
        self.point3_lineEdit.setMinimumSize(QSize(0, 30))
        self.point3_lineEdit.setReadOnly(True)

        self.gridLayout_5.addWidget(self.point3_lineEdit, 8, 0, 1, 1)

        self.line_3 = QFrame(self.groupBox)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.gridLayout_5.addWidget(self.line_3, 6, 0, 1, 1)

        self.point1_lineEdit = QLineEdit(self.groupBox)
        self.point1_lineEdit.setObjectName(u"point1_lineEdit")
        self.point1_lineEdit.setMinimumSize(QSize(0, 30))
        self.point1_lineEdit.setReadOnly(True)

        self.gridLayout_5.addWidget(self.point1_lineEdit, 1, 0, 1, 1)

        self.addpoint2_pushButton = QPushButton(self.groupBox)
        self.addpoint2_pushButton.setObjectName(u"addpoint2_pushButton")
        self.addpoint2_pushButton.setMinimumSize(QSize(0, 30))
        self.addpoint2_pushButton.setStyleSheet(u"background-color: rgb(138, 226, 52);")

        self.gridLayout_5.addWidget(self.addpoint2_pushButton, 4, 0, 1, 1)

        self.point2_lineEdit = QLineEdit(self.groupBox)
        self.point2_lineEdit.setObjectName(u"point2_lineEdit")
        self.point2_lineEdit.setMinimumSize(QSize(0, 30))
        self.point2_lineEdit.setReadOnly(True)

        self.gridLayout_5.addWidget(self.point2_lineEdit, 5, 0, 1, 1)

        self.addpoint3_pushButton = QPushButton(self.groupBox)
        self.addpoint3_pushButton.setObjectName(u"addpoint3_pushButton")
        self.addpoint3_pushButton.setMinimumSize(QSize(0, 30))
        self.addpoint3_pushButton.setStyleSheet(u"background-color: rgb(79, 226, 239);")

        self.gridLayout_5.addWidget(self.addpoint3_pushButton, 7, 0, 1, 1)

        self.addpoint1_pushButton = QPushButton(self.groupBox)
        self.addpoint1_pushButton.setObjectName(u"addpoint1_pushButton")
        self.addpoint1_pushButton.setMinimumSize(QSize(0, 30))
        self.addpoint1_pushButton.setStyleSheet(u"background-color: rgb(249, 122, 122);")

        self.gridLayout_5.addWidget(self.addpoint1_pushButton, 0, 0, 1, 1)

        self.line_2 = QFrame(self.groupBox)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout_5.addWidget(self.line_2, 2, 0, 1, 1)


        self.gridLayout_3.addWidget(self.groupBox, 1, 0, 1, 1)


        self.gridLayout_4.addWidget(self.widget, 0, 0, 1, 1)

        self.line = QFrame(PositionDialog)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout_4.addWidget(self.line, 1, 0, 1, 1)

        self.buttonBox = QDialogButtonBox(PositionDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(False)

        self.gridLayout_4.addWidget(self.buttonBox, 2, 0, 1, 1)


        self.retranslateUi(PositionDialog)
        self.buttonBox.rejected.connect(PositionDialog.reject)

        QMetaObject.connectSlotsByName(PositionDialog)
    # setupUi

    def retranslateUi(self, PositionDialog):
        PositionDialog.setWindowTitle(QCoreApplication.translate("PositionDialog", u"Positioning Tool", None))
        self.source_groupBox.setTitle(QCoreApplication.translate("PositionDialog", u"Image", None))
        self.static_radioButton.setText(QCoreApplication.translate("PositionDialog", u"Static Image", None))
        self.import_pushButton.setText(QCoreApplication.translate("PositionDialog", u"Import Image", None))
        self.live_radioButton.setText(QCoreApplication.translate("PositionDialog", u"Live Camera", None))
        self.camera_comboBox.setItemText(0, QCoreApplication.translate("PositionDialog", u"Select a Camaera", None))
        self.camera_comboBox.setItemText(1, QCoreApplication.translate("PositionDialog", u"Web Camera", None))
        self.camera_comboBox.setItemText(2, QCoreApplication.translate("PositionDialog", u"Basler Camera", None))

        self.capture_pushButton.setText(QCoreApplication.translate("PositionDialog", u"Capture Image", None))
        self.showImage_label.setText("")
        self.groupBox.setTitle(QCoreApplication.translate("PositionDialog", u"Anchor Point", None))
        self.addpoint2_pushButton.setText(QCoreApplication.translate("PositionDialog", u"+", None))
        self.addpoint3_pushButton.setText(QCoreApplication.translate("PositionDialog", u"+", None))
        self.addpoint1_pushButton.setText(QCoreApplication.translate("PositionDialog", u"+", None))
    # retranslateUi

