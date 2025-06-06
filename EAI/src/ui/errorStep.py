# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'errorStep.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_ErrorStep_Dialog(object):
    def setupUi(self, ErrorStep_Dialog):
        if not ErrorStep_Dialog.objectName():
            ErrorStep_Dialog.setObjectName(u"ErrorStep_Dialog")
        ErrorStep_Dialog.resize(471, 133)
        self.gridLayout = QGridLayout(ErrorStep_Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(ErrorStep_Dialog)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(16)
        self.label.setFont(font)

        self.verticalLayout.addWidget(self.label)

        self.label_2 = QLabel(ErrorStep_Dialog)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.label_3 = QLabel(ErrorStep_Dialog)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.enterCode_lineEdit = QLineEdit(ErrorStep_Dialog)
        self.enterCode_lineEdit.setObjectName(u"enterCode_lineEdit")

        self.verticalLayout.addWidget(self.enterCode_lineEdit)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.retranslateUi(ErrorStep_Dialog)

        QMetaObject.connectSlotsByName(ErrorStep_Dialog)
    # setupUi

    def retranslateUi(self, ErrorStep_Dialog):
        ErrorStep_Dialog.setWindowTitle(QCoreApplication.translate("ErrorStep_Dialog", u"Error Correction?", None))
        self.label.setText(QCoreApplication.translate("ErrorStep_Dialog", u"Failure occurs!!", None))
        self.label_2.setText(QCoreApplication.translate("ErrorStep_Dialog", u"<html><head/><body><p>* After removing the incorrect step, enter <span style=\" font-weight:600; color:#ef2929;\">RESTART</span> to continue inspecting.</p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("ErrorStep_Dialog", u"<html><head/><body><p>* To stop this inspection, enter <span style=\" font-weight:600; color:#3465a4;\">END</span>.</p></body></html>", None))
        self.enterCode_lineEdit.setPlaceholderText("")
    # retranslateUi

