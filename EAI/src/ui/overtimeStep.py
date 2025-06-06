# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'overtimeStep.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from drawshapesgraphics import DrawShapesGraphics


class Ui_OvertimeStep_Dialog(object):
    def setupUi(self, OvertimeStep_Dialog):
        if not OvertimeStep_Dialog.objectName():
            OvertimeStep_Dialog.setObjectName(u"OvertimeStep_Dialog")
        OvertimeStep_Dialog.resize(1000, 600)
        self.gridLayout_2 = QGridLayout(OvertimeStep_Dialog)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_5 = QLabel(OvertimeStep_Dialog)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout.addWidget(self.label_5)

        self.layer_step_label = QLabel(OvertimeStep_Dialog)
        self.layer_step_label.setObjectName(u"layer_step_label")

        self.horizontalLayout.addWidget(self.layer_step_label)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.user_label = QLabel(OvertimeStep_Dialog)
        self.user_label.setObjectName(u"user_label")

        self.horizontalLayout.addWidget(self.user_label)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(OvertimeStep_Dialog)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.overtime_label = QLabel(OvertimeStep_Dialog)
        self.overtime_label.setObjectName(u"overtime_label")
        self.overtime_label.setStyleSheet(u"color: rgb(239, 41, 41);")

        self.horizontalLayout_3.addWidget(self.overtime_label)

        self.label = QLabel(OvertimeStep_Dialog)
        self.label.setObjectName(u"label")

        self.horizontalLayout_3.addWidget(self.label)

        self.label_4 = QLabel(OvertimeStep_Dialog)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_3.addWidget(self.label_4)

        self.duration_label = QLabel(OvertimeStep_Dialog)
        self.duration_label.setObjectName(u"duration_label")

        self.horizontalLayout_3.addWidget(self.duration_label)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.currentNumber_label = QLabel(OvertimeStep_Dialog)
        self.currentNumber_label.setObjectName(u"currentNumber_label")

        self.horizontalLayout_2.addWidget(self.currentNumber_label)

        self.label_3 = QLabel(OvertimeStep_Dialog)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_2.addWidget(self.label_3)

        self.totalNumber_label = QLabel(OvertimeStep_Dialog)
        self.totalNumber_label.setObjectName(u"totalNumber_label")

        self.horizontalLayout_2.addWidget(self.totalNumber_label)


        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.showImage_SOP_graphicsView = DrawShapesGraphics(OvertimeStep_Dialog)
        self.showImage_SOP_graphicsView.setObjectName(u"showImage_SOP_graphicsView")

        self.gridLayout.addWidget(self.showImage_SOP_graphicsView, 0, 0, 2, 1)

        self.enterCode_lineEdit = QLineEdit(OvertimeStep_Dialog)
        self.enterCode_lineEdit.setObjectName(u"enterCode_lineEdit")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.enterCode_lineEdit.sizePolicy().hasHeightForWidth())
        self.enterCode_lineEdit.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.enterCode_lineEdit, 0, 1, 1, 1)

        self.errorCodeList_textEdit = QTextEdit(OvertimeStep_Dialog)
        self.errorCodeList_textEdit.setObjectName(u"errorCodeList_textEdit")
        self.errorCodeList_textEdit.setMinimumSize(QSize(250, 0))
        self.errorCodeList_textEdit.setMaximumSize(QSize(300, 16777215))
        self.errorCodeList_textEdit.setReadOnly(True)

        self.gridLayout.addWidget(self.errorCodeList_textEdit, 1, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)


        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.retranslateUi(OvertimeStep_Dialog)

        QMetaObject.connectSlotsByName(OvertimeStep_Dialog)
    # setupUi

    def retranslateUi(self, OvertimeStep_Dialog):
        OvertimeStep_Dialog.setWindowTitle(QCoreApplication.translate("OvertimeStep_Dialog", u"Overtime Step/Terminate Step", None))
        self.label_5.setText(QCoreApplication.translate("OvertimeStep_Dialog", u"Layer - Step:", None))
        self.layer_step_label.setText(QCoreApplication.translate("OvertimeStep_Dialog", u"Layer - Step", None))
        self.user_label.setText(QCoreApplication.translate("OvertimeStep_Dialog", u"Employee Number", None))
        self.label_2.setText(QCoreApplication.translate("OvertimeStep_Dialog", u"Overtime:", None))
        self.overtime_label.setText(QCoreApplication.translate("OvertimeStep_Dialog", u"Overtime", None))
        self.label.setText(QCoreApplication.translate("OvertimeStep_Dialog", u"/", None))
        self.label_4.setText(QCoreApplication.translate("OvertimeStep_Dialog", u"Setup time:", None))
        self.duration_label.setText(QCoreApplication.translate("OvertimeStep_Dialog", u"Duration_Time", None))
        self.currentNumber_label.setText(QCoreApplication.translate("OvertimeStep_Dialog", u"2", None))
        self.label_3.setText(QCoreApplication.translate("OvertimeStep_Dialog", u"/", None))
        self.totalNumber_label.setText(QCoreApplication.translate("OvertimeStep_Dialog", u"3", None))
        self.errorCodeList_textEdit.setHtml(QCoreApplication.translate("OvertimeStep_Dialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Ubuntu'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
    # retranslateUi

