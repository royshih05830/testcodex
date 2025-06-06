# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'selectproduct.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_SelectProduct(object):
    def setupUi(self, SelectProduct):
        if not SelectProduct.objectName():
            SelectProduct.setObjectName(u"SelectProduct")
        SelectProduct.resize(350, 191)
        self.gridLayout = QGridLayout(SelectProduct)
        self.gridLayout.setObjectName(u"gridLayout")
        self.sn_label = QLabel(SelectProduct)
        self.sn_label.setObjectName(u"sn_label")

        self.gridLayout.addWidget(self.sn_label, 0, 0, 1, 1)

        self.sn_lineEdit = QLineEdit(SelectProduct)
        self.sn_lineEdit.setObjectName(u"sn_lineEdit")

        self.gridLayout.addWidget(self.sn_lineEdit, 0, 2, 1, 2)

        self.line = QFrame(SelectProduct)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line, 1, 0, 1, 4)

        self.pn_label = QLabel(SelectProduct)
        self.pn_label.setObjectName(u"pn_label")

        self.gridLayout.addWidget(self.pn_label, 2, 0, 1, 1)

        self.pn_lineEdit = QLineEdit(SelectProduct)
        self.pn_lineEdit.setObjectName(u"pn_lineEdit")

        self.gridLayout.addWidget(self.pn_lineEdit, 2, 2, 1, 2)

        self.useImage_checkBox = QCheckBox(SelectProduct)
        self.useImage_checkBox.setObjectName(u"useImage_checkBox")
        self.useImage_checkBox.setEnabled(False)

        self.gridLayout.addWidget(self.useImage_checkBox, 3, 0, 1, 2)

        self.imageLocation_lineEdit = QLineEdit(SelectProduct)
        self.imageLocation_lineEdit.setObjectName(u"imageLocation_lineEdit")
        self.imageLocation_lineEdit.setEnabled(False)

        self.gridLayout.addWidget(self.imageLocation_lineEdit, 4, 0, 1, 3)

        self.imageLocation_toolButton = QToolButton(SelectProduct)
        self.imageLocation_toolButton.setObjectName(u"imageLocation_toolButton")
        self.imageLocation_toolButton.setEnabled(False)

        self.gridLayout.addWidget(self.imageLocation_toolButton, 4, 3, 1, 1)

        self.buttonBox = QDialogButtonBox(SelectProduct)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 5, 1, 1, 3)


        self.retranslateUi(SelectProduct)
        self.buttonBox.rejected.connect(SelectProduct.reject)

        QMetaObject.connectSlotsByName(SelectProduct)
    # setupUi

    def retranslateUi(self, SelectProduct):
        SelectProduct.setWindowTitle(QCoreApplication.translate("SelectProduct", u"Select Product", None))
        self.sn_label.setText(QCoreApplication.translate("SelectProduct", u"Serial Number", None))
        self.pn_label.setText(QCoreApplication.translate("SelectProduct", u"Product Number", None))
        self.useImage_checkBox.setText(QCoreApplication.translate("SelectProduct", u"Use existing images", None))
        self.imageLocation_toolButton.setText(QCoreApplication.translate("SelectProduct", u"...", None))
    # retranslateUi

