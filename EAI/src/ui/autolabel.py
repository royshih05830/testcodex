# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'autolabel.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from myview import myview


class Ui_AutoLabel_Widget(object):
    def setupUi(self, AutoLabel_Widget):
        if not AutoLabel_Widget.objectName():
            AutoLabel_Widget.setObjectName(u"AutoLabel_Widget")
        AutoLabel_Widget.resize(800, 600)
        self.gridLayout = QGridLayout(AutoLabel_Widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.buttonBox = QDialogButtonBox(AutoLabel_Widget)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 2, 0, 1, 1)

        self.line_2 = QFrame(AutoLabel_Widget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_2, 1, 0, 1, 1)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.graphicsView = myview(AutoLabel_Widget)
        self.graphicsView.setObjectName(u"graphicsView")

        self.horizontalLayout_6.addWidget(self.graphicsView)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.area_pushButton = QPushButton(AutoLabel_Widget)
        self.area_pushButton.setObjectName(u"area_pushButton")
        self.area_pushButton.setMinimumSize(QSize(85, 0))

        self.horizontalLayout.addWidget(self.area_pushButton)

        self.search_lineEdit = QLineEdit(AutoLabel_Widget)
        self.search_lineEdit.setObjectName(u"search_lineEdit")
        self.search_lineEdit.setReadOnly(True)

        self.horizontalLayout.addWidget(self.search_lineEdit)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pattern_pushButton = QPushButton(AutoLabel_Widget)
        self.pattern_pushButton.setObjectName(u"pattern_pushButton")
        self.pattern_pushButton.setMinimumSize(QSize(85, 0))

        self.horizontalLayout_2.addWidget(self.pattern_pushButton)

        self.obj_lineEdit = QLineEdit(AutoLabel_Widget)
        self.obj_lineEdit.setObjectName(u"obj_lineEdit")
        self.obj_lineEdit.setReadOnly(True)

        self.horizontalLayout_2.addWidget(self.obj_lineEdit)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label = QLabel(AutoLabel_Widget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(94, 0))

        self.horizontalLayout_5.addWidget(self.label)

        self.doubleSpinBox = QDoubleSpinBox(AutoLabel_Widget)
        self.doubleSpinBox.setObjectName(u"doubleSpinBox")
        self.doubleSpinBox.setMinimumSize(QSize(0, 0))
        self.doubleSpinBox.setMinimum(0.650000000000000)
        self.doubleSpinBox.setMaximum(0.990000000000000)
        self.doubleSpinBox.setSingleStep(0.010000000000000)
        self.doubleSpinBox.setValue(0.900000000000000)

        self.horizontalLayout_5.addWidget(self.doubleSpinBox)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(AutoLabel_Widget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.spinBox = QSpinBox(AutoLabel_Widget)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setMinimumSize(QSize(85, 0))
        self.spinBox.setMinimum(-10)
        self.spinBox.setMaximum(10)
        self.spinBox.setSingleStep(1)
        self.spinBox.setValue(0)

        self.horizontalLayout_3.addWidget(self.spinBox)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.aotuLabel_pushButton = QPushButton(AutoLabel_Widget)
        self.aotuLabel_pushButton.setObjectName(u"aotuLabel_pushButton")
        self.aotuLabel_pushButton.setEnabled(False)
        self.aotuLabel_pushButton.setMinimumSize(QSize(0, 30))
        self.aotuLabel_pushButton.setStyleSheet(u"background-color: rgb(205, 249, 161);")

        self.verticalLayout.addWidget(self.aotuLabel_pushButton)

        self.line = QFrame(AutoLabel_Widget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.label_3 = QLabel(AutoLabel_Widget)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.labellist_listWidget = QListWidget(AutoLabel_Widget)
        self.labellist_listWidget.setObjectName(u"labellist_listWidget")

        self.verticalLayout.addWidget(self.labellist_listWidget)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout_6.addLayout(self.verticalLayout)

        self.horizontalLayout_6.setStretch(0, 3)
        self.horizontalLayout_6.setStretch(1, 1)

        self.gridLayout.addLayout(self.horizontalLayout_6, 0, 0, 1, 1)


        self.retranslateUi(AutoLabel_Widget)

        QMetaObject.connectSlotsByName(AutoLabel_Widget)
    # setupUi

    def retranslateUi(self, AutoLabel_Widget):
        AutoLabel_Widget.setWindowTitle(QCoreApplication.translate("AutoLabel_Widget", u"Pattern Label", None))
        self.area_pushButton.setText(QCoreApplication.translate("AutoLabel_Widget", u"Select area", None))
        self.pattern_pushButton.setText(QCoreApplication.translate("AutoLabel_Widget", u"Pattern", None))
        self.label.setText(QCoreApplication.translate("AutoLabel_Widget", u"Score Adjust", None))
#if QT_CONFIG(tooltip)
        self.doubleSpinBox.setToolTip(QCoreApplication.translate("AutoLabel_Widget", u"range: 0.65~0.99", None))
#endif // QT_CONFIG(tooltip)
        self.label_2.setText(QCoreApplication.translate("AutoLabel_Widget", u"Overlap Level", None))
        self.aotuLabel_pushButton.setText(QCoreApplication.translate("AutoLabel_Widget", u"Match", None))
        self.label_3.setText(QCoreApplication.translate("AutoLabel_Widget", u"Choose a Label ", None))
    # retranslateUi

