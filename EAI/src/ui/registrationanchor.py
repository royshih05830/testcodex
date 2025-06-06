# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'registrationanchor.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from drawshapesgraphics import DrawShapesGraphics


class Ui_RegistrationDialog(object):
    def setupUi(self, RegistrationDialog):
        if not RegistrationDialog.objectName():
            RegistrationDialog.setObjectName(u"RegistrationDialog")
        RegistrationDialog.resize(892, 550)
        self.gridLayout_4 = QGridLayout(RegistrationDialog)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.widget = QWidget(RegistrationDialog)
        self.widget.setObjectName(u"widget")
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox = QGroupBox(self.widget)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
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
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.label_2, 4, 0, 1, 1)

        self.point1_lineEdit = QLineEdit(self.groupBox)
        self.point1_lineEdit.setObjectName(u"point1_lineEdit")
        self.point1_lineEdit.setMinimumSize(QSize(0, 30))
        self.point1_lineEdit.setReadOnly(True)

        self.gridLayout_5.addWidget(self.point1_lineEdit, 2, 0, 1, 1)

        self.addpoint3_pushButton = QPushButton(self.groupBox)
        self.addpoint3_pushButton.setObjectName(u"addpoint3_pushButton")
        self.addpoint3_pushButton.setMinimumSize(QSize(0, 30))
        self.addpoint3_pushButton.setStyleSheet(u"background-color: rgb(79, 226, 239);")

        self.gridLayout_5.addWidget(self.addpoint3_pushButton, 9, 0, 1, 1)

        self.point3_lineEdit = QLineEdit(self.groupBox)
        self.point3_lineEdit.setObjectName(u"point3_lineEdit")
        self.point3_lineEdit.setMinimumSize(QSize(0, 30))
        self.point3_lineEdit.setReadOnly(True)

        self.gridLayout_5.addWidget(self.point3_lineEdit, 10, 0, 1, 1)

        self.line_2 = QFrame(self.groupBox)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout_5.addWidget(self.line_2, 3, 0, 1, 1)

        self.line_3 = QFrame(self.groupBox)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.gridLayout_5.addWidget(self.line_3, 7, 0, 1, 1)

        self.point2_lineEdit = QLineEdit(self.groupBox)
        self.point2_lineEdit.setObjectName(u"point2_lineEdit")
        self.point2_lineEdit.setMinimumSize(QSize(0, 30))
        self.point2_lineEdit.setReadOnly(True)

        self.gridLayout_5.addWidget(self.point2_lineEdit, 6, 0, 1, 1)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.label, 0, 0, 1, 1)

        self.addpoint2_pushButton = QPushButton(self.groupBox)
        self.addpoint2_pushButton.setObjectName(u"addpoint2_pushButton")
        self.addpoint2_pushButton.setMinimumSize(QSize(0, 30))
        self.addpoint2_pushButton.setStyleSheet(u"background-color: rgb(138, 226, 52);")

        self.gridLayout_5.addWidget(self.addpoint2_pushButton, 5, 0, 1, 1)

        self.addpoint1_pushButton = QPushButton(self.groupBox)
        self.addpoint1_pushButton.setObjectName(u"addpoint1_pushButton")
        self.addpoint1_pushButton.setMinimumSize(QSize(0, 30))
        self.addpoint1_pushButton.setStyleSheet(u"background-color: rgb(249, 122, 122);")

        self.gridLayout_5.addWidget(self.addpoint1_pushButton, 1, 0, 1, 1)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.label_3, 8, 0, 1, 1)


        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)

        self.showImage_graphicsView = DrawShapesGraphics(self.widget)
        self.showImage_graphicsView.setObjectName(u"showImage_graphicsView")

        self.gridLayout.addWidget(self.showImage_graphicsView, 0, 1, 2, 1)

        self.verticalSpacer = QSpacerItem(20, 128, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 1, 0, 1, 1)


        self.gridLayout_4.addWidget(self.widget, 0, 0, 1, 1)

        self.line = QFrame(RegistrationDialog)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout_4.addWidget(self.line, 1, 0, 1, 1)

        self.buttonBox = QDialogButtonBox(RegistrationDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(False)

        self.gridLayout_4.addWidget(self.buttonBox, 2, 0, 1, 1)


        self.retranslateUi(RegistrationDialog)
        self.buttonBox.rejected.connect(RegistrationDialog.reject)

        QMetaObject.connectSlotsByName(RegistrationDialog)
    # setupUi

    def retranslateUi(self, RegistrationDialog):
        RegistrationDialog.setWindowTitle(QCoreApplication.translate("RegistrationDialog", u"Registration", None))
        self.groupBox.setTitle(QCoreApplication.translate("RegistrationDialog", u"Anchor Point", None))
        self.label_2.setText(QCoreApplication.translate("RegistrationDialog", u"Point2", None))
        self.addpoint3_pushButton.setText(QCoreApplication.translate("RegistrationDialog", u"+", None))
        self.label.setText(QCoreApplication.translate("RegistrationDialog", u"Point1", None))
        self.addpoint2_pushButton.setText(QCoreApplication.translate("RegistrationDialog", u"+", None))
        self.addpoint1_pushButton.setText(QCoreApplication.translate("RegistrationDialog", u"+", None))
        self.label_3.setText(QCoreApplication.translate("RegistrationDialog", u"Point3", None))
    # retranslateUi

