# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'splash_screen.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Splash_Screen(object):
    def setupUi(self, Splash_Screen):
        if not Splash_Screen.objectName():
            Splash_Screen.setObjectName(u"Splash_Screen")
        Splash_Screen.resize(416, 140)
        Splash_Screen.setStyleSheet(u"background: qlineargradient(x1: 1, y1: 0, x2: 0, y2: 1,\n"
"    stop: 0.13667 rgb(80, 48, 205),\n"
"    stop: 0.64886 rgba(105, 74, 227, 0.82),\n"
"    stop: 1 rgba(154, 135, 227, 0.74));\n"
"")
        self.label = QLabel(Splash_Screen)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 20, 331, 91))
        font = QFont()
        font.setFamily(u"Inter")
        font.setBold(True)
        font.setWeight(99)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font-family: Inter;\n"
"font-size: 36px;\n"
"font-weight: 800;\n"
"line-height: 44px;\n"
"letter-spacing: 0px;\n"
"text-align: left;\n"
"\n"
"background: linear-gradient(180.00deg, rgb(0, 0, 0),rgba(20, 19, 20, 0));")

        self.retranslateUi(Splash_Screen)

        QMetaObject.connectSlotsByName(Splash_Screen)
    # setupUi

    def retranslateUi(self, Splash_Screen):
        Splash_Screen.setWindowTitle(QCoreApplication.translate("Splash_Screen", u"Form", None))
        self.label.setText(QCoreApplication.translate("Splash_Screen", u"\u0417\u0430\u0433\u0440\u0443\u0437\u043a\u0430 \u0434\u0430\u043d\u043d\u044b\u0445", None))
    # retranslateUi

