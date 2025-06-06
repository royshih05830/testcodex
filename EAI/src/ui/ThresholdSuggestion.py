# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ThresholdSuggestion.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Suggestion_Threshold_widget(object):
    def setupUi(self, Suggestion_Threshold_widget):
        if not Suggestion_Threshold_widget.objectName():
            Suggestion_Threshold_widget.setObjectName(u"Suggestion_Threshold_widget")
        Suggestion_Threshold_widget.resize(403, 176)
        self.verticalLayout_2 = QVBoxLayout(Suggestion_Threshold_widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(Suggestion_Threshold_widget)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.verticalLayout.addWidget(self.label)

        self.suggestion_label = QLabel(Suggestion_Threshold_widget)
        self.suggestion_label.setObjectName(u"suggestion_label")
        self.suggestion_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.suggestion_label.setMargin(2)
        self.suggestion_label.setIndent(40)

        self.verticalLayout.addWidget(self.suggestion_label)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.line = QFrame(Suggestion_Threshold_widget)
        self.line.setObjectName(u"line")
        self.line.setMidLineWidth(0)
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.golden_radioButton = QRadioButton(Suggestion_Threshold_widget)
        self.golden_radioButton.setObjectName(u"golden_radioButton")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.golden_radioButton)

        self.Golden_Threshold_label = QLabel(Suggestion_Threshold_widget)
        self.Golden_Threshold_label.setObjectName(u"Golden_Threshold_label")
        self.Golden_Threshold_label.setFrameShape(QFrame.StyledPanel)
        self.Golden_Threshold_label.setIndent(4)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.Golden_Threshold_label)

        self.train_radioButton = QRadioButton(Suggestion_Threshold_widget)
        self.train_radioButton.setObjectName(u"train_radioButton")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.train_radioButton)

        self.Train_Threshold_label = QLabel(Suggestion_Threshold_widget)
        self.Train_Threshold_label.setObjectName(u"Train_Threshold_label")
        self.Train_Threshold_label.setFrameShape(QFrame.StyledPanel)
        self.Train_Threshold_label.setIndent(4)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.Train_Threshold_label)

        self.other_radioButton = QRadioButton(Suggestion_Threshold_widget)
        self.other_radioButton.setObjectName(u"other_radioButton")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.other_radioButton)

        self.other_Threshold_doubleSpinBox = QDoubleSpinBox(Suggestion_Threshold_widget)
        self.other_Threshold_doubleSpinBox.setObjectName(u"other_Threshold_doubleSpinBox")
        self.other_Threshold_doubleSpinBox.setDecimals(3)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.other_Threshold_doubleSpinBox)


        self.verticalLayout_2.addLayout(self.formLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.retranslateUi(Suggestion_Threshold_widget)

        QMetaObject.connectSlotsByName(Suggestion_Threshold_widget)
    # setupUi

    def retranslateUi(self, Suggestion_Threshold_widget):
        Suggestion_Threshold_widget.setWindowTitle(QCoreApplication.translate("Suggestion_Threshold_widget", u"Form", None))
        self.label.setText(QCoreApplication.translate("Suggestion_Threshold_widget", u"Suggestion:", None))
        self.suggestion_label.setText(QCoreApplication.translate("Suggestion_Threshold_widget", u"Increase the threshold", None))
        self.golden_radioButton.setText(QCoreApplication.translate("Suggestion_Threshold_widget", u"Use Golden Threshold", None))
        self.Golden_Threshold_label.setText("")
        self.train_radioButton.setText(QCoreApplication.translate("Suggestion_Threshold_widget", u"Base on Training Threshold", None))
        self.Train_Threshold_label.setText("")
        self.other_radioButton.setText(QCoreApplication.translate("Suggestion_Threshold_widget", u"Other", None))
    # retranslateUi

