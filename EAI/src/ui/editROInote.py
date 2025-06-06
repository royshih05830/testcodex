# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'editROInote.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_EditROINote_Dialog(object):
    def setupUi(self, EditROINote_Dialog):
        if not EditROINote_Dialog.objectName():
            EditROINote_Dialog.setObjectName(u"EditROINote_Dialog")
        EditROINote_Dialog.resize(968, 644)
        self.gridLayout_2 = QGridLayout(EditROINote_Dialog)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.widget = QWidget(EditROINote_Dialog)
        self.widget.setObjectName(u"widget")
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tableWidget = QTableWidget(self.widget)
        if (self.tableWidget.columnCount() < 5):
            self.tableWidget.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.horizontalHeader().setStretchLastSection(False)

        self.gridLayout.addWidget(self.tableWidget, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.widget, 0, 0, 1, 4)

        self.reset_threshold_pushButton = QPushButton(EditROINote_Dialog)
        self.reset_threshold_pushButton.setObjectName(u"reset_threshold_pushButton")

        self.gridLayout_2.addWidget(self.reset_threshold_pushButton, 1, 0, 1, 1)

        self.buttonBox = QDialogButtonBox(EditROINote_Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout_2.addWidget(self.buttonBox, 1, 3, 1, 1)

        self.reset_passframe_pushButton = QPushButton(EditROINote_Dialog)
        self.reset_passframe_pushButton.setObjectName(u"reset_passframe_pushButton")

        self.gridLayout_2.addWidget(self.reset_passframe_pushButton, 1, 1, 1, 1)

        self.clean_pushButton = QPushButton(EditROINote_Dialog)
        self.clean_pushButton.setObjectName(u"clean_pushButton")

        self.gridLayout_2.addWidget(self.clean_pushButton, 1, 2, 1, 1)


        self.retranslateUi(EditROINote_Dialog)
        self.buttonBox.rejected.connect(EditROINote_Dialog.reject)

        QMetaObject.connectSlotsByName(EditROINote_Dialog)
    # setupUi

    def retranslateUi(self, EditROINote_Dialog):
        EditROINote_Dialog.setWindowTitle(QCoreApplication.translate("EditROINote_Dialog", u"Edit Note/Threshold ", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("EditROINote_Dialog", u"Order", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("EditROINote_Dialog", u"Image", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("EditROINote_Dialog", u"Note", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("EditROINote_Dialog", u"Threshold", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("EditROINote_Dialog", u"PASS frame", None));
#if QT_CONFIG(tooltip)
        self.reset_threshold_pushButton.setToolTip(QCoreApplication.translate("EditROINote_Dialog", u"reset all threshold/offset to default value.", None))
#endif // QT_CONFIG(tooltip)
        self.reset_threshold_pushButton.setText(QCoreApplication.translate("EditROINote_Dialog", u"Reset Threshold", None))
#if QT_CONFIG(tooltip)
        self.reset_passframe_pushButton.setToolTip(QCoreApplication.translate("EditROINote_Dialog", u"Reset all roi PASS frame to default value", None))
#endif // QT_CONFIG(tooltip)
        self.reset_passframe_pushButton.setText(QCoreApplication.translate("EditROINote_Dialog", u"Reset PASS frame", None))
#if QT_CONFIG(tooltip)
        self.clean_pushButton.setToolTip(QCoreApplication.translate("EditROINote_Dialog", u"clean all roi data from train mode and reset to default value.", None))
#endif // QT_CONFIG(tooltip)
        self.clean_pushButton.setText(QCoreApplication.translate("EditROINote_Dialog", u"Clean Threshold", None))
    # retranslateUi

