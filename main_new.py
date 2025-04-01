# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_new.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(377, 447)
        MainWindow.setMinimumSize(QSize(377, 447))
        MainWindow.setMaximumSize(QSize(377, 447))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(-1, -1, 381, 451))
        self.frame.setStyleSheet(u"background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgb(162, 139, 233), stop:1 rgb(120, 145, 221));")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.progressBar = QProgressBar(self.frame)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(37, 24, 321, 50))
        self.progressBar.setStyleSheet(u"QProgressBar {\n"
"    border: 1px solid rgb(81, 81, 228);\n"
"    border-radius: 22px;\n"
"    text-align: center;\n"
"    background: rgb(150, 183, 224);\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    border-radius: 21px; \n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgb(75, 143, 228), stop:1 rgb(13, 76, 153));\n"
"}")
        self.progressBar.setValue(55)
        self.progressBar.setTextVisible(False)
        self.DB_button = QPushButton(self.frame)
        self.DB_button.setObjectName(u"DB_button")
        self.DB_button.setGeometry(QRect(19, 113, 168, 41))
        self.DB_button.setMaximumSize(QSize(80124, 16777215))
        self.DB_button.setStyleSheet(u"QPushButton {\n"
"    border-radius: 10px;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgb(229, 236, 242), stop:1 rgb(212, 233, 252));\n"
"    color: rgb(0, 0, 0); /* \u0426\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"    font-family: \"Inter\"; /* \u0428\u0440\u0438\u0444\u0442 */\n"
"    font-size: 14px; /* \u0420\u0430\u0437\u043c\u0435\u0440 \u0448\u0440\u0438\u0444\u0442\u0430 */\n"
"    font-weight: 400; /* \u0422\u043e\u043b\u0449\u0438\u043d\u0430 \u0448\u0440\u0438\u0444\u0442\u0430 */\n"
"    line-height: 17px; /* \u0412\u044b\u0441\u043e\u0442\u0430 \u0441\u0442\u0440\u043e\u043a\u0438 */\n"
"    letter-spacing: 0px; /* \u0420\u0430\u0441\u0441\u0442\u043e\u044f\u043d\u0438\u0435 \u043c\u0435\u0436\u0434\u0443 \u0431\u0443\u043a\u0432\u0430\u043c\u0438 */\n"
"    text-align: center; /* \u0412\u044b\u0440\u0430\u0432\u043d\u0438\u0432\u0430\u043d\u0438\u0435 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"    padding: 8px 16px; /* \u0414\u043e\u0431\u0430"
                        "\u0432\u043b\u044f\u0435\u043c \u043e\u0442\u0441\u0442\u0443\u043f\u044b \u0432\u043d\u0443\u0442\u0440\u0438 \u043a\u043d\u043e\u043f\u043a\u0438 */\n"
"    border: none; /* \u0423\u0431\u0438\u0440\u0430\u0435\u043c \u0433\u0440\u0430\u043d\u0438\u0446\u0443 */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: none; /* \u0423\u0431\u0438\u0440\u0430\u0435\u043c \u0433\u0440\u0430\u043d\u0438\u0446\u0443 */\n"
"    border-radius: 10px; /* \u0417\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u0435 \u0443\u0433\u043b\u043e\u0432 */\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(151, 236, 242, 255), stop:1 rgba(212, 233, 252, 255)); /* \u0413\u0440\u0430\u0434\u0438\u0435\u043d\u0442 */\n"
"    padding: 8px 16px; /* \u0412\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0438\u0435 \u043e\u0442\u0441\u0442\u0443\u043f\u044b */\n"
"    min-width: 100px; /* \u041c\u0438\u043d\u0438\u043c\u0430\u043b\u044c\u043d\u0430\u044f \u0448\u0438\u0440\u0438\u043d\u0430 */\n"
"    min"
                        "-height: 40px; /* \u041c\u0438\u043d\u0438\u043c\u0430\u043b\u044c\u043d\u0430\u044f \u0432\u044b\u0441\u043e\u0442\u0430 */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border: none; /* \u0423\u0431\u0438\u0440\u0430\u0435\u043c \u0433\u0440\u0430\u043d\u0438\u0446\u0443 */\n"
"    border-radius: 10px; /* \u0417\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u0435 \u0443\u0433\u043b\u043e\u0432 */\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(116, 212, 219, 255), stop:1 rgba(131, 167, 198, 255)); /* \u0413\u0440\u0430\u0434\u0438\u0435\u043d\u0442 */\n"
"    padding: 8px 16px; /* \u0412\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0438\u0435 \u043e\u0442\u0441\u0442\u0443\u043f\u044b */\n"
"    min-width: 100px; /* \u041c\u0438\u043d\u0438\u043c\u0430\u043b\u044c\u043d\u0430\u044f \u0448\u0438\u0440\u0438\u043d\u0430 */\n"
"    min-height: 40px; /* \u041c\u0438\u043d\u0438\u043c\u0430\u043b\u044c\u043d\u0430\u044f \u0432\u044b\u0441\u043e\u0442\u0430 */\n"
"}")
        self.email_button_stop = QPushButton(self.frame)
        self.email_button_stop.setObjectName(u"email_button_stop")
        self.email_button_stop.setGeometry(QRect(203, 274, 168, 41))
        self.email_button_stop.setMaximumSize(QSize(80124, 16777215))
        self.email_button_stop.setStyleSheet(u"QPushButton {\n"
"    border-radius: 10px;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgb(229, 236, 242), stop:1 rgb(212, 233, 252));\n"
"    color: rgb(0, 0, 0); /* \u0426\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"    font-family: \"Inter\"; /* \u0428\u0440\u0438\u0444\u0442 */\n"
"    font-size: 14px; /* \u0420\u0430\u0437\u043c\u0435\u0440 \u0448\u0440\u0438\u0444\u0442\u0430 */\n"
"    font-weight: 400; /* \u0422\u043e\u043b\u0449\u0438\u043d\u0430 \u0448\u0440\u0438\u0444\u0442\u0430 */\n"
"    line-height: 17px; /* \u0412\u044b\u0441\u043e\u0442\u0430 \u0441\u0442\u0440\u043e\u043a\u0438 */\n"
"    letter-spacing: 0px; /* \u0420\u0430\u0441\u0441\u0442\u043e\u044f\u043d\u0438\u0435 \u043c\u0435\u0436\u0434\u0443 \u0431\u0443\u043a\u0432\u0430\u043c\u0438 */\n"
"    text-align: center; /* \u0412\u044b\u0440\u0430\u0432\u043d\u0438\u0432\u0430\u043d\u0438\u0435 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"    padding: 8px 16px; /* \u0414\u043e\u0431\u0430"
                        "\u0432\u043b\u044f\u0435\u043c \u043e\u0442\u0441\u0442\u0443\u043f\u044b \u0432\u043d\u0443\u0442\u0440\u0438 \u043a\u043d\u043e\u043f\u043a\u0438 */\n"
"    border: none; /* \u0423\u0431\u0438\u0440\u0430\u0435\u043c \u0433\u0440\u0430\u043d\u0438\u0446\u0443 */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: none; /* \u0423\u0431\u0438\u0440\u0430\u0435\u043c \u0433\u0440\u0430\u043d\u0438\u0446\u0443 */\n"
"    border-radius: 10px; /* \u0417\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u0435 \u0443\u0433\u043b\u043e\u0432 */\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(151, 236, 242, 255), stop:1 rgba(212, 233, 252, 255)); /* \u0413\u0440\u0430\u0434\u0438\u0435\u043d\u0442 */\n"
"    padding: 8px 16px; /* \u0412\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0438\u0435 \u043e\u0442\u0441\u0442\u0443\u043f\u044b */\n"
"    min-width: 100px; /* \u041c\u0438\u043d\u0438\u043c\u0430\u043b\u044c\u043d\u0430\u044f \u0448\u0438\u0440\u0438\u043d\u0430 */\n"
"    min"
                        "-height: 40px; /* \u041c\u0438\u043d\u0438\u043c\u0430\u043b\u044c\u043d\u0430\u044f \u0432\u044b\u0441\u043e\u0442\u0430 */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border: none; /* \u0423\u0431\u0438\u0440\u0430\u0435\u043c \u0433\u0440\u0430\u043d\u0438\u0446\u0443 */\n"
"    border-radius: 10px; /* \u0417\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u0435 \u0443\u0433\u043b\u043e\u0432 */\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(116, 212, 219, 255), stop:1 rgba(131, 167, 198, 255)); /* \u0413\u0440\u0430\u0434\u0438\u0435\u043d\u0442 */\n"
"    padding: 8px 16px; /* \u0412\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0438\u0435 \u043e\u0442\u0441\u0442\u0443\u043f\u044b */\n"
"    min-width: 100px; /* \u041c\u0438\u043d\u0438\u043c\u0430\u043b\u044c\u043d\u0430\u044f \u0448\u0438\u0440\u0438\u043d\u0430 */\n"
"    min-height: 40px; /* \u041c\u0438\u043d\u0438\u043c\u0430\u043b\u044c\u043d\u0430\u044f \u0432\u044b\u0441\u043e\u0442\u0430 */\n"
"}")
        self.email_button = QPushButton(self.frame)
        self.email_button.setObjectName(u"email_button")
        self.email_button.setGeometry(QRect(19, 275, 168, 41))
        self.email_button.setMaximumSize(QSize(80124, 16777215))
        self.email_button.setStyleSheet(u"QPushButton {\n"
"    border-radius: 10px;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgb(229, 236, 242), stop:1 rgb(212, 233, 252));\n"
"    color: rgb(0, 0, 0); /* \u0426\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"    font-family: \"Inter\"; /* \u0428\u0440\u0438\u0444\u0442 */\n"
"    font-size: 14px; /* \u0420\u0430\u0437\u043c\u0435\u0440 \u0448\u0440\u0438\u0444\u0442\u0430 */\n"
"    font-weight: 400; /* \u0422\u043e\u043b\u0449\u0438\u043d\u0430 \u0448\u0440\u0438\u0444\u0442\u0430 */\n"
"    line-height: 17px; /* \u0412\u044b\u0441\u043e\u0442\u0430 \u0441\u0442\u0440\u043e\u043a\u0438 */\n"
"    letter-spacing: 0px; /* \u0420\u0430\u0441\u0441\u0442\u043e\u044f\u043d\u0438\u0435 \u043c\u0435\u0436\u0434\u0443 \u0431\u0443\u043a\u0432\u0430\u043c\u0438 */\n"
"    text-align: center; /* \u0412\u044b\u0440\u0430\u0432\u043d\u0438\u0432\u0430\u043d\u0438\u0435 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"    padding: 8px 16px; /* \u0414\u043e\u0431\u0430"
                        "\u0432\u043b\u044f\u0435\u043c \u043e\u0442\u0441\u0442\u0443\u043f\u044b \u0432\u043d\u0443\u0442\u0440\u0438 \u043a\u043d\u043e\u043f\u043a\u0438 */\n"
"    border: none; /* \u0423\u0431\u0438\u0440\u0430\u0435\u043c \u0433\u0440\u0430\u043d\u0438\u0446\u0443 */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: none; /* \u0423\u0431\u0438\u0440\u0430\u0435\u043c \u0433\u0440\u0430\u043d\u0438\u0446\u0443 */\n"
"    border-radius: 10px; /* \u0417\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u0435 \u0443\u0433\u043b\u043e\u0432 */\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(151, 236, 242, 255), stop:1 rgba(212, 233, 252, 255)); /* \u0413\u0440\u0430\u0434\u0438\u0435\u043d\u0442 */\n"
"    padding: 8px 16px; /* \u0412\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0438\u0435 \u043e\u0442\u0441\u0442\u0443\u043f\u044b */\n"
"    min-width: 100px; /* \u041c\u0438\u043d\u0438\u043c\u0430\u043b\u044c\u043d\u0430\u044f \u0448\u0438\u0440\u0438\u043d\u0430 */\n"
"    min"
                        "-height: 40px; /* \u041c\u0438\u043d\u0438\u043c\u0430\u043b\u044c\u043d\u0430\u044f \u0432\u044b\u0441\u043e\u0442\u0430 */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border: none; /* \u0423\u0431\u0438\u0440\u0430\u0435\u043c \u0433\u0440\u0430\u043d\u0438\u0446\u0443 */\n"
"    border-radius: 10px; /* \u0417\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u0435 \u0443\u0433\u043b\u043e\u0432 */\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(116, 212, 219, 255), stop:1 rgba(131, 167, 198, 255)); /* \u0413\u0440\u0430\u0434\u0438\u0435\u043d\u0442 */\n"
"    padding: 8px 16px; /* \u0412\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0438\u0435 \u043e\u0442\u0441\u0442\u0443\u043f\u044b */\n"
"    min-width: 100px; /* \u041c\u0438\u043d\u0438\u043c\u0430\u043b\u044c\u043d\u0430\u044f \u0448\u0438\u0440\u0438\u043d\u0430 */\n"
"    min-height: 40px; /* \u041c\u0438\u043d\u0438\u043c\u0430\u043b\u044c\u043d\u0430\u044f \u0432\u044b\u0441\u043e\u0442\u0430 */\n"
"}")
        self.File_name = QLabel(self.frame)
        self.File_name.setObjectName(u"File_name")
        self.File_name.setGeometry(QRect(242, 156, 125, 85))
        self.File_name.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font-family: Inter;\n"
"font-size: 14px;\n"
"font-weight: 800;\n"
"line-height: 44px;\n"
"letter-spacing: 0px;\n"
"text-align: left;\n"
"\n"
"background: linear-gradient(180.00deg, rgb(0, 0, 0),rgba(20, 19, 20, 0));")
        self.DB_name = QLabel(self.frame)
        self.DB_name.setObjectName(u"DB_name")
        self.DB_name.setGeometry(QRect(242, 125, 125, 17))
        self.DB_name.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font-family: Inter;\n"
"font-size: 14px;\n"
"font-weight: 800;\n"
"line-height: 44px;\n"
"letter-spacing: 0px;\n"
"text-align: left;\n"
"\n"
"background: linear-gradient(180.00deg, rgb(0, 0, 0),rgba(20, 19, 20, 0));")
        self.settings_button = QPushButton(self.frame)
        self.settings_button.setObjectName(u"settings_button")
        self.settings_button.setGeometry(QRect(136, 382, 122, 41))
        self.settings_button.setMaximumSize(QSize(80124, 16777215))
        self.settings_button.setStyleSheet(u"QPushButton {\n"
"    border-radius: 10px;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgb(229, 236, 242), stop:1 rgb(212, 233, 252));\n"
"    color: rgb(0, 0, 0); /* \u0426\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"    font-family: \"Inter\"; /* \u0428\u0440\u0438\u0444\u0442 */\n"
"    font-size: 14px; /* \u0420\u0430\u0437\u043c\u0435\u0440 \u0448\u0440\u0438\u0444\u0442\u0430 */\n"
"    font-weight: 400; /* \u0422\u043e\u043b\u0449\u0438\u043d\u0430 \u0448\u0440\u0438\u0444\u0442\u0430 */\n"
"    line-height: 17px; /* \u0412\u044b\u0441\u043e\u0442\u0430 \u0441\u0442\u0440\u043e\u043a\u0438 */\n"
"    letter-spacing: 0px; /* \u0420\u0430\u0441\u0441\u0442\u043e\u044f\u043d\u0438\u0435 \u043c\u0435\u0436\u0434\u0443 \u0431\u0443\u043a\u0432\u0430\u043c\u0438 */\n"
"    text-align: center; /* \u0412\u044b\u0440\u0430\u0432\u043d\u0438\u0432\u0430\u043d\u0438\u0435 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"    padding: 8px 16px; /* \u0414\u043e\u0431\u0430"
                        "\u0432\u043b\u044f\u0435\u043c \u043e\u0442\u0441\u0442\u0443\u043f\u044b \u0432\u043d\u0443\u0442\u0440\u0438 \u043a\u043d\u043e\u043f\u043a\u0438 */\n"
"    border: none; /* \u0423\u0431\u0438\u0440\u0430\u0435\u043c \u0433\u0440\u0430\u043d\u0438\u0446\u0443 */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: none; /* \u0423\u0431\u0438\u0440\u0430\u0435\u043c \u0433\u0440\u0430\u043d\u0438\u0446\u0443 */\n"
"    border-radius: 10px; /* \u0417\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u0435 \u0443\u0433\u043b\u043e\u0432 */\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(151, 236, 242, 255), stop:1 rgba(212, 233, 252, 255)); /* \u0413\u0440\u0430\u0434\u0438\u0435\u043d\u0442 */\n"
"    padding: 8px 16px; /* \u0412\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0438\u0435 \u043e\u0442\u0441\u0442\u0443\u043f\u044b */\n"
"    min-width: 100px; /* \u041c\u0438\u043d\u0438\u043c\u0430\u043b\u044c\u043d\u0430\u044f \u0448\u0438\u0440\u0438\u043d\u0430 */\n"
"    min"
                        "-height: 40px; /* \u041c\u0438\u043d\u0438\u043c\u0430\u043b\u044c\u043d\u0430\u044f \u0432\u044b\u0441\u043e\u0442\u0430 */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border: none; /* \u0423\u0431\u0438\u0440\u0430\u0435\u043c \u0433\u0440\u0430\u043d\u0438\u0446\u0443 */\n"
"    border-radius: 10px; /* \u0417\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u0435 \u0443\u0433\u043b\u043e\u0432 */\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(116, 212, 219, 255), stop:1 rgba(131, 167, 198, 255)); /* \u0413\u0440\u0430\u0434\u0438\u0435\u043d\u0442 */\n"
"    padding: 8px 16px; /* \u0412\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0438\u0435 \u043e\u0442\u0441\u0442\u0443\u043f\u044b */\n"
"    min-width: 100px; /* \u041c\u0438\u043d\u0438\u043c\u0430\u043b\u044c\u043d\u0430\u044f \u0448\u0438\u0440\u0438\u043d\u0430 */\n"
"    min-height: 40px; /* \u041c\u0438\u043d\u0438\u043c\u0430\u043b\u044c\u043d\u0430\u044f \u0432\u044b\u0441\u043e\u0442\u0430 */\n"
"}")
        self.File_button = QPushButton(self.frame)
        self.File_button.setObjectName(u"File_button")
        self.File_button.setGeometry(QRect(19, 178, 168, 41))
        self.File_button.setMaximumSize(QSize(80124, 16777215))
        self.File_button.setStyleSheet(u"QPushButton {\n"
"    border-radius: 10px;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgb(229, 236, 242), stop:1 rgb(212, 233, 252));\n"
"    color: rgb(0, 0, 0); /* \u0426\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"    font-family: \"Inter\"; /* \u0428\u0440\u0438\u0444\u0442 */\n"
"    font-size: 14px; /* \u0420\u0430\u0437\u043c\u0435\u0440 \u0448\u0440\u0438\u0444\u0442\u0430 */\n"
"    font-weight: 400; /* \u0422\u043e\u043b\u0449\u0438\u043d\u0430 \u0448\u0440\u0438\u0444\u0442\u0430 */\n"
"    line-height: 17px; /* \u0412\u044b\u0441\u043e\u0442\u0430 \u0441\u0442\u0440\u043e\u043a\u0438 */\n"
"    letter-spacing: 0px; /* \u0420\u0430\u0441\u0441\u0442\u043e\u044f\u043d\u0438\u0435 \u043c\u0435\u0436\u0434\u0443 \u0431\u0443\u043a\u0432\u0430\u043c\u0438 */\n"
"    text-align: center; /* \u0412\u044b\u0440\u0430\u0432\u043d\u0438\u0432\u0430\u043d\u0438\u0435 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"    padding: 8px 16px; /* \u0414\u043e\u0431\u0430"
                        "\u0432\u043b\u044f\u0435\u043c \u043e\u0442\u0441\u0442\u0443\u043f\u044b \u0432\u043d\u0443\u0442\u0440\u0438 \u043a\u043d\u043e\u043f\u043a\u0438 */\n"
"    border: none; /* \u0423\u0431\u0438\u0440\u0430\u0435\u043c \u0433\u0440\u0430\u043d\u0438\u0446\u0443 */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: none; /* \u0423\u0431\u0438\u0440\u0430\u0435\u043c \u0433\u0440\u0430\u043d\u0438\u0446\u0443 */\n"
"    border-radius: 10px; /* \u0417\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u0435 \u0443\u0433\u043b\u043e\u0432 */\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(151, 236, 242, 255), stop:1 rgba(212, 233, 252, 255)); /* \u0413\u0440\u0430\u0434\u0438\u0435\u043d\u0442 */\n"
"    padding: 8px 16px; /* \u0412\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0438\u0435 \u043e\u0442\u0441\u0442\u0443\u043f\u044b */\n"
"    min-width: 100px; /* \u041c\u0438\u043d\u0438\u043c\u0430\u043b\u044c\u043d\u0430\u044f \u0448\u0438\u0440\u0438\u043d\u0430 */\n"
"    min"
                        "-height: 40px; /* \u041c\u0438\u043d\u0438\u043c\u0430\u043b\u044c\u043d\u0430\u044f \u0432\u044b\u0441\u043e\u0442\u0430 */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border: none; /* \u0423\u0431\u0438\u0440\u0430\u0435\u043c \u0433\u0440\u0430\u043d\u0438\u0446\u0443 */\n"
"    border-radius: 10px; /* \u0417\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u0435 \u0443\u0433\u043b\u043e\u0432 */\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(116, 212, 219, 255), stop:1 rgba(131, 167, 198, 255)); /* \u0413\u0440\u0430\u0434\u0438\u0435\u043d\u0442 */\n"
"    padding: 8px 16px; /* \u0412\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0438\u0435 \u043e\u0442\u0441\u0442\u0443\u043f\u044b */\n"
"    min-width: 100px; /* \u041c\u0438\u043d\u0438\u043c\u0430\u043b\u044c\u043d\u0430\u044f \u0448\u0438\u0440\u0438\u043d\u0430 */\n"
"    min-height: 40px; /* \u041c\u0438\u043d\u0438\u043c\u0430\u043b\u044c\u043d\u0430\u044f \u0432\u044b\u0441\u043e\u0442\u0430 */\n"
"}")
        self.sending_confirm = QLabel(self.frame)
        self.sending_confirm.setObjectName(u"sending_confirm")
        self.sending_confirm.setGeometry(QRect(120, 340, 151, 20))
        self.sending_confirm.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font-family: Inter;\n"
"font-size: 14px;\n"
"font-weight: 800;\n"
"line-height: 44px;\n"
"letter-spacing: 0px;\n"
"text-align: left;\n"
"\n"
"background: linear-gradient(180.00deg, rgb(0, 0, 0),rgba(20, 19, 20, 0));")
        self.sending_progress_stat = QLabel(self.frame)
        self.sending_progress_stat.setObjectName(u"sending_progress_stat")
        self.sending_progress_stat.setGeometry(QRect(83, 34, 229, 29))
        self.sending_progress_stat.setStyleSheet(u"background: linear-gradient(180.00deg, rgb(0, 0, 0),rgba(20, 19, 20, 0));\n"
"background-clip: text;\n"
"font-family: Inter;\n"
"font-size: 24px;\n"
"font-weight: 400;\n"
"line-height: 29px;\n"
"letter-spacing: 0px;\n"
"text-align: center;")
        self.sending_progress_stat.setAlignment(Qt.AlignCenter)
        self.help_button = QPushButton(self.frame)
        self.help_button.setObjectName(u"help_button")
        self.help_button.setGeometry(QRect(310, 382, 41, 41))
        self.help_button.setMaximumSize(QSize(80124, 16777215))
        self.help_button.setStyleSheet(u"QPushButton {\n"
"    border-radius: 10px;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgb(229, 236, 242), stop:1 rgb(212, 233, 252));\n"
"    color: rgb(0, 0, 0); /* \u0426\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"    font-family: \"Inter\"; /* \u0428\u0440\u0438\u0444\u0442 */\n"
"    font-size: 14px; /* \u0420\u0430\u0437\u043c\u0435\u0440 \u0448\u0440\u0438\u0444\u0442\u0430 */\n"
"    font-weight: 400; /* \u0422\u043e\u043b\u0449\u0438\u043d\u0430 \u0448\u0440\u0438\u0444\u0442\u0430 */\n"
"    line-height: 17px; /* \u0412\u044b\u0441\u043e\u0442\u0430 \u0441\u0442\u0440\u043e\u043a\u0438 */\n"
"    letter-spacing: 0px; /* \u0420\u0430\u0441\u0441\u0442\u043e\u044f\u043d\u0438\u0435 \u043c\u0435\u0436\u0434\u0443 \u0431\u0443\u043a\u0432\u0430\u043c\u0438 */\n"
"    text-align: center; /* \u0412\u044b\u0440\u0430\u0432\u043d\u0438\u0432\u0430\u043d\u0438\u0435 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"    padding: 8px 16px; /* \u0414\u043e\u0431\u0430"
                        "\u0432\u043b\u044f\u0435\u043c \u043e\u0442\u0441\u0442\u0443\u043f\u044b \u0432\u043d\u0443\u0442\u0440\u0438 \u043a\u043d\u043e\u043f\u043a\u0438 */\n"
"    border: none; /* \u0423\u0431\u0438\u0440\u0430\u0435\u043c \u0433\u0440\u0430\u043d\u0438\u0446\u0443 */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: none; /* \u0423\u0431\u0438\u0440\u0430\u0435\u043c \u0433\u0440\u0430\u043d\u0438\u0446\u0443 */\n"
"    border-radius: 10px; /* \u0417\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u0435 \u0443\u0433\u043b\u043e\u0432 */\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(151, 236, 242, 255), stop:1 rgba(212, 233, 252, 255)); /* \u0413\u0440\u0430\u0434\u0438\u0435\u043d\u0442 */\n"
"    padding: 8px 16px; /* \u0412\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0438\u0435 \u043e\u0442\u0441\u0442\u0443\u043f\u044b */\n"
"    min-width: 100px; /* \u041c\u0438\u043d\u0438\u043c\u0430\u043b\u044c\u043d\u0430\u044f \u0448\u0438\u0440\u0438\u043d\u0430 */\n"
"    min"
                        "-height: 40px; /* \u041c\u0438\u043d\u0438\u043c\u0430\u043b\u044c\u043d\u0430\u044f \u0432\u044b\u0441\u043e\u0442\u0430 */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border: none; /* \u0423\u0431\u0438\u0440\u0430\u0435\u043c \u0433\u0440\u0430\u043d\u0438\u0446\u0443 */\n"
"    border-radius: 10px; /* \u0417\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u0435 \u0443\u0433\u043b\u043e\u0432 */\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(116, 212, 219, 255), stop:1 rgba(131, 167, 198, 255)); /* \u0413\u0440\u0430\u0434\u0438\u0435\u043d\u0442 */\n"
"    padding: 8px 16px; /* \u0412\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0438\u0435 \u043e\u0442\u0441\u0442\u0443\u043f\u044b */\n"
"    min-width: 100px; /* \u041c\u0438\u043d\u0438\u043c\u0430\u043b\u044c\u043d\u0430\u044f \u0448\u0438\u0440\u0438\u043d\u0430 */\n"
"    min-height: 40px; /* \u041c\u0438\u043d\u0438\u043c\u0430\u043b\u044c\u043d\u0430\u044f \u0432\u044b\u0441\u043e\u0442\u0430 */\n"
"}")
        icon = QIcon()
        icon.addFile(u"../../../Downloads/free-icon-question-3106703.png", QSize(), QIcon.Normal, QIcon.Off)
        self.help_button.setIcon(icon)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 400, 61, 31))
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font-family: Inter;\n"
"font-size: 12px;\n"
"font-weight: 800;\n"
"line-height: 44px;\n"
"letter-spacing: 0px;\n"
"text-align: left;\n"
"\n"
"background: linear-gradient(180.00deg, rgb(0, 0, 0),rgba(20, 19, 20, 0));")
        self.label.setWordWrap(True)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.DB_button.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c \u0444\u0430\u0439\u043b \u0411\u0414", None))
        self.email_button_stop.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0435\u0440\u0432\u0430\u0442\u044c \u043e\u0442\u043f\u0440\u0430\u0432\u043a\u0443", None))
        self.email_button.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0447\u0430\u0442\u044c \u043e\u0442\u043f\u0440\u0430\u0432\u043a\u0443", None))
        self.File_name.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0444\u0430\u0439\u043b\u0430", None))
        self.DB_name.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0444\u0430\u0439\u043b\u0430", None))
        self.settings_button.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.File_button.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u043a\u0440\u0435\u043f\u0438\u0442\u044c \u0444\u0430\u0439\u043b", None))
        self.sending_confirm.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0430\u0442\u0443\u0441 \u043e\u0442\u043f\u0440\u0430\u0432\u043a\u0438", None))
        self.sending_progress_stat.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0433\u0440\u0435\u0441\u0441 \u043e\u0442\u043f\u0440\u0430\u0432\u043a\u0438", None))
        self.help_button.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Created by TaCeiN", None))
    # retranslateUi

