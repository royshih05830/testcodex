# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'fileconflict.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_FileConflict(object):
    def setupUi(self, FileConflict):
        if not FileConflict.objectName():
            FileConflict.setObjectName(u"FileConflict")
        FileConflict.resize(522, 262)
        self.gridLayout_2 = QGridLayout(FileConflict)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.widget = QWidget(FileConflict)
        self.widget.setObjectName(u"widget")
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.title_label = QLabel(self.widget)
        self.title_label.setObjectName(u"title_label")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.title_label.sizePolicy().hasHeightForWidth())
        self.title_label.setSizePolicy(sizePolicy)
        self.title_label.setStyleSheet(u"font: 16pt \"Ubuntu\";")

        self.gridLayout.addWidget(self.title_label, 0, 0, 1, 2)

        self.description_label = QLabel(self.widget)
        self.description_label.setObjectName(u"description_label")

        self.gridLayout.addWidget(self.description_label, 1, 0, 1, 2)

        self.rename_checkBox = QCheckBox(self.widget)
        self.rename_checkBox.setObjectName(u"rename_checkBox")

        self.gridLayout.addWidget(self.rename_checkBox, 2, 0, 1, 2)

        self.horizontalSpacer_2 = QSpacerItem(13, 18, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 3, 0, 1, 1)

        self.rename_lineEdit = QLineEdit(self.widget)
        self.rename_lineEdit.setObjectName(u"rename_lineEdit")
        self.rename_lineEdit.setEnabled(False)

        self.gridLayout.addWidget(self.rename_lineEdit, 3, 1, 1, 1)

        self.removeLabelInfo_checkBox = QCheckBox(self.widget)
        self.removeLabelInfo_checkBox.setObjectName(u"removeLabelInfo_checkBox")

        self.gridLayout.addWidget(self.removeLabelInfo_checkBox, 4, 0, 1, 2)

        self.applyAll_checkBox = QCheckBox(self.widget)
        self.applyAll_checkBox.setObjectName(u"applyAll_checkBox")

        self.gridLayout.addWidget(self.applyAll_checkBox, 5, 0, 1, 2)


        self.gridLayout_2.addWidget(self.widget, 0, 0, 1, 4)

        self.line = QFrame(FileConflict)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line, 1, 0, 1, 4)

        self.buttonBox = QDialogButtonBox(FileConflict)
        self.buttonBox.setObjectName(u"buttonBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.buttonBox.sizePolicy().hasHeightForWidth())
        self.buttonBox.setSizePolicy(sizePolicy1)
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel)
        self.buttonBox.setCenterButtons(True)

        self.gridLayout_2.addWidget(self.buttonBox, 2, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(228, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 2, 1, 1, 1)

        self.replace_pushButton = QPushButton(FileConflict)
        self.replace_pushButton.setObjectName(u"replace_pushButton")
        self.replace_pushButton.setStyleSheet(u"background-color: rgb(138, 226, 52);")

        self.gridLayout_2.addWidget(self.replace_pushButton, 2, 2, 1, 1)

        self.skip_pushButton = QPushButton(FileConflict)
        self.skip_pushButton.setObjectName(u"skip_pushButton")
        self.skip_pushButton.setStyleSheet(u"background-color: rgb(252, 175, 62);")

        self.gridLayout_2.addWidget(self.skip_pushButton, 2, 3, 1, 1)


        self.retranslateUi(FileConflict)

        QMetaObject.connectSlotsByName(FileConflict)
    # setupUi

    def retranslateUi(self, FileConflict):
        FileConflict.setWindowTitle(QCoreApplication.translate("FileConflict", u"File conflict !!", None))
        self.title_label.setText(QCoreApplication.translate("FileConflict", u"Replace file \"{}\" ?", None))
        self.description_label.setText(QCoreApplication.translate("FileConflict", u"<html><head/><body><p>Another file with the same name already exists.<br/>Replacing it will overwrite its content.</p></body></html>", None))
        self.rename_checkBox.setText(QCoreApplication.translate("FileConflict", u"Select a new name for the file.", None))
        self.removeLabelInfo_checkBox.setText(QCoreApplication.translate("FileConflict", u"Remove the image file's label information when replacing.", None))
        self.applyAll_checkBox.setText(QCoreApplication.translate("FileConflict", u"Apply this action to all files.", None))
        self.replace_pushButton.setText(QCoreApplication.translate("FileConflict", u"&Replace", None))
        self.skip_pushButton.setText(QCoreApplication.translate("FileConflict", u"&Skip", None))
    # retranslateUi

