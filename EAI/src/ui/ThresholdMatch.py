# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ThresholdMatch.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Threshold_Match_Widget(object):
    def setupUi(self, Threshold_Match_Widget):
        if not Threshold_Match_Widget.objectName():
            Threshold_Match_Widget.setObjectName(u"Threshold_Match_Widget")
        Threshold_Match_Widget.resize(198, 146)
        self.verticalLayout = QVBoxLayout(Threshold_Match_Widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer = QSpacerItem(20, 29, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.ok_radioButton = QRadioButton(Threshold_Match_Widget)
        self.ok_radioButton.setObjectName(u"ok_radioButton")

        self.verticalLayout.addWidget(self.ok_radioButton)

        self.ng_radioButton = QRadioButton(Threshold_Match_Widget)
        self.ng_radioButton.setObjectName(u"ng_radioButton")

        self.verticalLayout.addWidget(self.ng_radioButton)

        self.verticalSpacer_2 = QSpacerItem(20, 29, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)


        self.retranslateUi(Threshold_Match_Widget)

        QMetaObject.connectSlotsByName(Threshold_Match_Widget)
    # setupUi

    def retranslateUi(self, Threshold_Match_Widget):
        Threshold_Match_Widget.setWindowTitle(QCoreApplication.translate("Threshold_Match_Widget", u"Form", None))
        self.ok_radioButton.setText(QCoreApplication.translate("Threshold_Match_Widget", u"OK (Match)", None))
        self.ng_radioButton.setText(QCoreApplication.translate("Threshold_Match_Widget", u"NG (Mismatch)", None))
    # retranslateUi

