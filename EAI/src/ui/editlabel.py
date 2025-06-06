# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'editlabel.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_EditLabel_Dialog(object):
    def setupUi(self, EditLabel_Dialog):
        if not EditLabel_Dialog.objectName():
            EditLabel_Dialog.setObjectName(u"EditLabel_Dialog")
        EditLabel_Dialog.resize(326, 323)
        self.gridLayout_2 = QGridLayout(EditLabel_Dialog)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.widget = QWidget(EditLabel_Dialog)
        self.widget.setObjectName(u"widget")
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.edit_listWidget = QListWidget(self.widget)
        self.edit_listWidget.setObjectName(u"edit_listWidget")

        self.gridLayout.addWidget(self.edit_listWidget, 0, 0, 4, 1)

        self.new_pushButton = QPushButton(self.widget)
        self.new_pushButton.setObjectName(u"new_pushButton")

        self.gridLayout.addWidget(self.new_pushButton, 0, 1, 1, 1)

        self.edit_pushButton = QPushButton(self.widget)
        self.edit_pushButton.setObjectName(u"edit_pushButton")

        self.gridLayout.addWidget(self.edit_pushButton, 1, 1, 1, 1)

        self.delete_pushButton = QPushButton(self.widget)
        self.delete_pushButton.setObjectName(u"delete_pushButton")

        self.gridLayout.addWidget(self.delete_pushButton, 2, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 58, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 3, 1, 1, 1)


        self.gridLayout_2.addWidget(self.widget, 0, 0, 1, 1)

        self.buttonBox = QDialogButtonBox(EditLabel_Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout_2.addWidget(self.buttonBox, 1, 0, 1, 1)


        self.retranslateUi(EditLabel_Dialog)
        self.buttonBox.accepted.connect(EditLabel_Dialog.accept)
        self.buttonBox.rejected.connect(EditLabel_Dialog.reject)

        QMetaObject.connectSlotsByName(EditLabel_Dialog)
    # setupUi

    def retranslateUi(self, EditLabel_Dialog):
        EditLabel_Dialog.setWindowTitle(QCoreApplication.translate("EditLabel_Dialog", u"Edit Label List", None))
        self.new_pushButton.setText(QCoreApplication.translate("EditLabel_Dialog", u"&New", None))
        self.edit_pushButton.setText(QCoreApplication.translate("EditLabel_Dialog", u"&Edit", None))
        self.delete_pushButton.setText(QCoreApplication.translate("EditLabel_Dialog", u"&Delete", None))
    # retranslateUi

