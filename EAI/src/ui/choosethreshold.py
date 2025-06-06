# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'choosethreshold.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_ChooseThreshold_Dialog(object):
    def setupUi(self, ChooseThreshold_Dialog):
        if not ChooseThreshold_Dialog.objectName():
            ChooseThreshold_Dialog.setObjectName(u"ChooseThreshold_Dialog")
        ChooseThreshold_Dialog.resize(1101, 827)
        self.gridLayout = QGridLayout(ChooseThreshold_Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.widget = QWidget(ChooseThreshold_Dialog)
        self.widget.setObjectName(u"widget")
        self.gridLayout_2 = QGridLayout(self.widget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.allOK_radioButton = QRadioButton(self.widget)
        self.allOK_radioButton.setObjectName(u"allOK_radioButton")
        self.allOK_radioButton.setCheckable(True)

        self.horizontalLayout.addWidget(self.allOK_radioButton)

        self.allNG_radioButton = QRadioButton(self.widget)
        self.allNG_radioButton.setObjectName(u"allNG_radioButton")

        self.horizontalLayout.addWidget(self.allNG_radioButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.tableWidget = QTableWidget(self.widget)
        if (self.tableWidget.columnCount() < 3):
            self.tableWidget.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(100)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(400)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout.addWidget(self.tableWidget)


        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)

        self.buttonBox = QDialogButtonBox(ChooseThreshold_Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)


        self.retranslateUi(ChooseThreshold_Dialog)
        self.buttonBox.rejected.connect(ChooseThreshold_Dialog.reject)

        QMetaObject.connectSlotsByName(ChooseThreshold_Dialog)
    # setupUi

    def retranslateUi(self, ChooseThreshold_Dialog):
        ChooseThreshold_Dialog.setWindowTitle(QCoreApplication.translate("ChooseThreshold_Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("ChooseThreshold_Dialog", u"Match Result", None))
        self.allOK_radioButton.setText(QCoreApplication.translate("ChooseThreshold_Dialog", u"All OK", None))
        self.allNG_radioButton.setText(QCoreApplication.translate("ChooseThreshold_Dialog", u"All NG", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("ChooseThreshold_Dialog", u"Image Information", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("ChooseThreshold_Dialog", u"Match Status", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("ChooseThreshold_Dialog", u"Recommended Threshold", None));
    # retranslateUi

