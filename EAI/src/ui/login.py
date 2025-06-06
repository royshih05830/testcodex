# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from qtwidgets import PasswordEdit


class Ui_login_Dialog(object):
    def setupUi(self, login_Dialog):
        if not login_Dialog.objectName():
            login_Dialog.setObjectName(u"login_Dialog")
        login_Dialog.resize(303, 346)
        self.verticalLayout_2 = QVBoxLayout(login_Dialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widget = QWidget(login_Dialog)
        self.widget.setObjectName(u"widget")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.radioButton_operator = QRadioButton(self.widget)
        self.radioButton_operator.setObjectName(u"radioButton_operator")
        self.radioButton_operator.setChecked(True)

        self.verticalLayout.addWidget(self.radioButton_operator)

        self.radioButton_corrector = QRadioButton(self.widget)
        self.radioButton_corrector.setObjectName(u"radioButton_corrector")

        self.verticalLayout.addWidget(self.radioButton_corrector)

        self.radioButton_admin = QRadioButton(self.widget)
        self.radioButton_admin.setObjectName(u"radioButton_admin")

        self.verticalLayout.addWidget(self.radioButton_admin)


        self.verticalLayout_2.addWidget(self.widget)

        self.line = QFrame(login_Dialog)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line)

        self.fullscreen_checkBox = QCheckBox(login_Dialog)
        self.fullscreen_checkBox.setObjectName(u"fullscreen_checkBox")

        self.verticalLayout_2.addWidget(self.fullscreen_checkBox)

        self.line_3 = QFrame(login_Dialog)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line_3)

        self.create_checkBox = QCheckBox(login_Dialog)
        self.create_checkBox.setObjectName(u"create_checkBox")
        self.create_checkBox.setEnabled(False)

        self.verticalLayout_2.addWidget(self.create_checkBox)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.projectName_lineEdit = QLineEdit(login_Dialog)
        self.projectName_lineEdit.setObjectName(u"projectName_lineEdit")

        self.gridLayout_2.addWidget(self.projectName_lineEdit, 0, 1, 1, 1)

        self.label = QLabel(login_Dialog)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout_2)

        self.line_2 = QFrame(login_Dialog)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line_2)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.username_label = QLabel(login_Dialog)
        self.username_label.setObjectName(u"username_label")
        self.username_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.username_label, 0, 0, 1, 1)

        self.username_edit = QLineEdit(login_Dialog)
        self.username_edit.setObjectName(u"username_edit")

        self.gridLayout.addWidget(self.username_edit, 0, 1, 1, 1)

        self.password_label = QLabel(login_Dialog)
        self.password_label.setObjectName(u"password_label")
        self.password_label.setEnabled(False)
        self.password_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.password_label, 1, 0, 1, 1)

        self.password_edit = PasswordEdit(login_Dialog)
        self.password_edit.setObjectName(u"password_edit")
        self.password_edit.setEnabled(False)
        self.password_edit.setEchoMode(QLineEdit.Password)

        self.gridLayout.addWidget(self.password_edit, 1, 1, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout)

        self.line_4 = QFrame(login_Dialog)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.login_horizontalSpacer = QSpacerItem(84, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.login_horizontalSpacer)

        self.login_pushButton = QPushButton(login_Dialog)
        self.login_pushButton.setObjectName(u"login_pushButton")
        self.login_pushButton.setMinimumSize(QSize(100, 30))
        self.login_pushButton.setStyleSheet(u"QPushButton{ \n"
"color: white;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.857143, y2:0.857955, stop:0 rgba(10, 242, 251, 255), stop:1 rgba(224, 6, 159, 255));\n"
"border-radius: 15px; \n"
"}\n"
"QPushButton:hover{ color: white;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.857143, y2:0.857955, stop:0 rgba(224, 6, 159, 255), stop:1 rgba(224, 6, 159, 255));\n"
"border-radius: 15px; }\n"
"")

        self.horizontalLayout_3.addWidget(self.login_pushButton)

        self.login_horizontalSpacer_2 = QSpacerItem(84, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.login_horizontalSpacer_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)


        self.retranslateUi(login_Dialog)

        QMetaObject.connectSlotsByName(login_Dialog)
    # setupUi

    def retranslateUi(self, login_Dialog):
        login_Dialog.setWindowTitle(QCoreApplication.translate("login_Dialog", u"Login", None))
        self.radioButton_operator.setText(QCoreApplication.translate("login_Dialog", u"Operator", None))
        self.radioButton_corrector.setText(QCoreApplication.translate("login_Dialog", u"Corrector/Trainer", None))
        self.radioButton_admin.setText(QCoreApplication.translate("login_Dialog", u"Administrator", None))
        self.fullscreen_checkBox.setText(QCoreApplication.translate("login_Dialog", u"Full screen", None))
        self.create_checkBox.setText(QCoreApplication.translate("login_Dialog", u"Create a new project", None))
        self.label.setText(QCoreApplication.translate("login_Dialog", u"Project  Name*", None))
        self.username_label.setText(QCoreApplication.translate("login_Dialog", u"User", None))
        self.password_label.setText(QCoreApplication.translate("login_Dialog", u"Password", None))
        self.login_pushButton.setText(QCoreApplication.translate("login_Dialog", u"Login", None))
    # retranslateUi

