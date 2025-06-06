# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ThresholdImage.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Threshold_Image_Widget(object):
    def setupUi(self, Threshold_Image_Widget):
        if not Threshold_Image_Widget.objectName():
            Threshold_Image_Widget.setObjectName(u"Threshold_Image_Widget")
        Threshold_Image_Widget.resize(468, 455)
        self.horizontalLayout_3 = QHBoxLayout(Threshold_Image_Widget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.Widget = QWidget(Threshold_Image_Widget)
        self.Widget.setObjectName(u"Widget")
        self.Widget.setMinimumSize(QSize(450, 0))
        self.gridLayout = QGridLayout(self.Widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.Golden_Image_label = QLabel(self.Widget)
        self.Golden_Image_label.setObjectName(u"Golden_Image_label")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Golden_Image_label.sizePolicy().hasHeightForWidth())
        self.Golden_Image_label.setSizePolicy(sizePolicy)
        self.Golden_Image_label.setMinimumSize(QSize(300, 200))
        self.Golden_Image_label.setFrameShape(QFrame.Box)
        self.Golden_Image_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.Golden_Image_label)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.Golden_label = QLabel(self.Widget)
        self.Golden_label.setObjectName(u"Golden_label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.Golden_label.sizePolicy().hasHeightForWidth())
        self.Golden_label.setSizePolicy(sizePolicy1)
        self.Golden_label.setMinimumSize(QSize(80, 0))
        self.Golden_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.Golden_label)

        self.Golden_Threshold_label = QLabel(self.Widget)
        self.Golden_Threshold_label.setObjectName(u"Golden_Threshold_label")
        sizePolicy1.setHeightForWidth(self.Golden_Threshold_label.sizePolicy().hasHeightForWidth())
        self.Golden_Threshold_label.setSizePolicy(sizePolicy1)
        self.Golden_Threshold_label.setMinimumSize(QSize(80, 0))
        self.Golden_Threshold_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.Golden_Threshold_label)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.Train_Image_label = QLabel(self.Widget)
        self.Train_Image_label.setObjectName(u"Train_Image_label")
        sizePolicy.setHeightForWidth(self.Train_Image_label.sizePolicy().hasHeightForWidth())
        self.Train_Image_label.setSizePolicy(sizePolicy)
        self.Train_Image_label.setMinimumSize(QSize(300, 200))
        self.Train_Image_label.setFrameShape(QFrame.Box)
        self.Train_Image_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.Train_Image_label)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_4)

        self.Train_ROI_label = QLabel(self.Widget)
        self.Train_ROI_label.setObjectName(u"Train_ROI_label")
        sizePolicy1.setHeightForWidth(self.Train_ROI_label.sizePolicy().hasHeightForWidth())
        self.Train_ROI_label.setSizePolicy(sizePolicy1)
        self.Train_ROI_label.setMinimumSize(QSize(80, 0))
        self.Train_ROI_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.Train_ROI_label)

        self.Train_Threshold_label = QLabel(self.Widget)
        self.Train_Threshold_label.setObjectName(u"Train_Threshold_label")
        sizePolicy1.setHeightForWidth(self.Train_Threshold_label.sizePolicy().hasHeightForWidth())
        self.Train_Threshold_label.setSizePolicy(sizePolicy1)
        self.Train_Threshold_label.setMinimumSize(QSize(80, 0))
        self.Train_Threshold_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.Train_Threshold_label)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)


        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)

        self.line = QFrame(self.Widget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line, 1, 0, 1, 1)


        self.horizontalLayout_3.addWidget(self.Widget)


        self.retranslateUi(Threshold_Image_Widget)

        QMetaObject.connectSlotsByName(Threshold_Image_Widget)
    # setupUi

    def retranslateUi(self, Threshold_Image_Widget):
        Threshold_Image_Widget.setWindowTitle(QCoreApplication.translate("Threshold_Image_Widget", u"Form", None))
        self.Golden_Image_label.setText("")
        self.Golden_label.setText(QCoreApplication.translate("Threshold_Image_Widget", u"Golden", None))
        self.Golden_Threshold_label.setText("")
        self.Train_Image_label.setText("")
        self.Train_ROI_label.setText(QCoreApplication.translate("Threshold_Image_Widget", u"Train", None))
        self.Train_Threshold_label.setText("")
    # retranslateUi

