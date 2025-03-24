# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'second_main_new.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(554, 548)
        Form.setMinimumSize(QSize(554, 548))
        Form.setMaximumSize(QSize(554, 548))
        Form.setStyleSheet(u"background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgb(162, 139, 233), stop:1 rgb(120, 145, 221));")
        self.mail_adress = QLabel(Form)
        self.mail_adress.setObjectName(u"mail_adress")
        self.mail_adress.setGeometry(QRect(32, 28, 97, 17))
        self.mail_adress.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font-family: Inter;\n"
"font-size: 14px;\n"
"font-weight: 800;\n"
"line-height: 44px;\n"
"letter-spacing: 0px;\n"
"text-align: left;\n"
"\n"
"background: linear-gradient(180.00deg, rgb(0, 0, 0),rgba(20, 19, 20, 0));")
        self.mail_password = QLabel(Form)
        self.mail_password.setObjectName(u"mail_password")
        self.mail_password.setGeometry(QRect(33, 93, 110, 17))
        self.mail_password.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font-family: Inter;\n"
"font-size: 14px;\n"
"font-weight: 800;\n"
"line-height: 44px;\n"
"letter-spacing: 0px;\n"
"text-align: left;\n"
"\n"
"background: linear-gradient(180.00deg, rgb(0, 0, 0),rgba(20, 19, 20, 0));")
        self.mail_topic = QLabel(Form)
        self.mail_topic.setObjectName(u"mail_topic")
        self.mail_topic.setGeometry(QRect(33, 158, 98, 17))
        self.mail_topic.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font-family: Inter;\n"
"font-size: 14px;\n"
"font-weight: 800;\n"
"line-height: 44px;\n"
"letter-spacing: 0px;\n"
"text-align: left;\n"
"\n"
"background: linear-gradient(180.00deg, rgb(0, 0, 0),rgba(20, 19, 20, 0));")
        self.mail_body = QLabel(Form)
        self.mail_body.setObjectName(u"mail_body")
        self.mail_body.setGeometry(QRect(231, 211, 101, 17))
        self.mail_body.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font-family: Inter;\n"
"font-size: 14px;\n"
"font-weight: 800;\n"
"line-height: 44px;\n"
"letter-spacing: 0px;\n"
"text-align: left;\n"
"\n"
"background: linear-gradient(180.00deg, rgb(0, 0, 0),rgba(20, 19, 20, 0));")
        self.mail_signature = QLabel(Form)
        self.mail_signature.setObjectName(u"mail_signature")
        self.mail_signature.setGeometry(QRect(228, 373, 112, 17))
        self.mail_signature.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font-family: Inter;\n"
"font-size: 14px;\n"
"font-weight: 800;\n"
"line-height: 44px;\n"
"letter-spacing: 0px;\n"
"text-align: left;\n"
"\n"
"background: linear-gradient(180.00deg, rgb(0, 0, 0),rgba(20, 19, 20, 0));")
        self.mail_adress_edit = QLineEdit(Form)
        self.mail_adress_edit.setObjectName(u"mail_adress_edit")
        self.mail_adress_edit.setGeometry(QRect(164, 23, 367, 23))
        self.mail_adress_edit.setStyleSheet(u"QLineEdit {\n"
"border: 1px solid rgb(53, 81, 87);\n"
"border-radius: 7px;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgb(229, 236, 242), stop:1 rgb(212, 233, 252));\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"border: 2px solid rgb(80, 48, 205);\n"
"border-radius: 7px;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgb(229, 236, 242), stop:1 rgb(212, 233, 252));\n"
"}")
        self.mail_password_edit = QLineEdit(Form)
        self.mail_password_edit.setObjectName(u"mail_password_edit")
        self.mail_password_edit.setGeometry(QRect(164, 88, 367, 28))
        self.mail_password_edit.setStyleSheet(u"QLineEdit {\n"
"border: 1px solid rgb(53, 81, 87);\n"
"border-radius: 7px;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgb(229, 236, 242), stop:1 rgb(212, 233, 252));\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"border: 2px solid rgb(80, 48, 205);\n"
"border-radius: 7px;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgb(229, 236, 242), stop:1 rgb(212, 233, 252));\n"
"}")
        self.mail_topic_edit = QLineEdit(Form)
        self.mail_topic_edit.setObjectName(u"mail_topic_edit")
        self.mail_topic_edit.setGeometry(QRect(164, 153, 367, 28))
        self.mail_topic_edit.setStyleSheet(u"QLineEdit {\n"
"border: 1px solid rgb(53, 81, 87);\n"
"border-radius: 7px;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgb(229, 236, 242), stop:1 rgb(212, 233, 252));\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"border: 2px solid rgb(80, 48, 205);\n"
"border-radius: 7px;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgb(229, 236, 242), stop:1 rgb(212, 233, 252));\n"
"}")
        self.mail_body_edit = QTextEdit(Form)
        self.mail_body_edit.setObjectName(u"mail_body_edit")
        self.mail_body_edit.setGeometry(QRect(33, 246, 491, 75))
        self.mail_body_edit.setStyleSheet(u"QTextEdit {\n"
"border: 1px solid rgb(53, 81, 87);\n"
"border-radius: 7px;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgb(229, 236, 242), stop:1 rgb(212, 233, 252));\n"
"}\n"
"\n"
"QTextEdit:focus {\n"
"border: 2px solid rgb(80, 48, 205);\n"
"border-radius: 7px;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgb(229, 236, 242), stop:1 rgb(212, 233, 252));\n"
"}")
        self.mail_signature_edit = QTextEdit(Form)
        self.mail_signature_edit.setObjectName(u"mail_signature_edit")
        self.mail_signature_edit.setGeometry(QRect(33, 408, 491, 75))
        self.mail_signature_edit.setStyleSheet(u"QTextEdit {\n"
"border: 1px solid rgb(53, 81, 87);\n"
"border-radius: 7px;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgb(229, 236, 242), stop:1 rgb(212, 233, 252));\n"
"}\n"
"\n"
"QTextEdit:focus {\n"
"border: 2px solid rgb(80, 48, 205);\n"
"border-radius: 7px;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgb(229, 236, 242), stop:1 rgb(212, 233, 252));\n"
"}")
        self.open_config_button = QPushButton(Form)
        self.open_config_button.setObjectName(u"open_config_button")
        self.open_config_button.setGeometry(QRect(16, 503, 226, 31))
        self.open_config_button.setStyleSheet(u"QPushButton {\n"
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
        self.save_config_button = QPushButton(Form)
        self.save_config_button.setObjectName(u"save_config_button")
        self.save_config_button.setGeometry(QRect(286, 503, 237, 31))
        self.save_config_button.setStyleSheet(u"QPushButton {\n"
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
        self.add_name_button = QPushButton(Form)
        self.add_name_button.setObjectName(u"add_name_button")
        self.add_name_button.setGeometry(QRect(33, 333, 179, 31))
        self.add_name_button.setStyleSheet(u"QPushButton {\n"
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
        self.mail_password_visible = QPushButton(Form)
        self.mail_password_visible.setObjectName(u"mail_password_visible")
        self.mail_password_visible.setEnabled(True)
        self.mail_password_visible.setGeometry(QRect(503, 88, 28, 28))
        self.mail_password_visible.setStyleSheet(u"QPushButton {\n"
"border: 1px solid rgb(53, 81, 87);\n"
"border-radius: 7px;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgb(229, 236, 242), stop:1 rgb(212, 233, 252));\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"border: 2px solid rgb(80, 48, 205);\n"
"border-radius: 7px;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgb(229, 236, 242), stop:1 rgb(212, 233, 252));\n"
"}")
        icon = QIcon()
        icon.addFile(u"../../../Downloads/show.png", QSize(), QIcon.Normal, QIcon.Off)
        self.mail_password_visible.setIcon(icon)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.mail_adress.setText(QCoreApplication.translate("Form", u"\u0410\u0434\u0440\u0435\u0441 \u043f\u043e\u0447\u0442\u044b", None))
        self.mail_password.setText(QCoreApplication.translate("Form", u"\u041f\u0430\u0440\u043e\u043b\u044c \u043f\u043e\u0447\u0442\u044b", None))
        self.mail_topic.setText(QCoreApplication.translate("Form", u"\u0422\u0435\u043c\u0430 \u043f\u0438\u0441\u044c\u043c\u0430", None))
        self.mail_body.setText(QCoreApplication.translate("Form", u"\u0422\u0435\u043a\u0441\u0442 \u043f\u0438\u0441\u044c\u043c\u0430", None))
        self.mail_signature.setText(QCoreApplication.translate("Form", u"\u0422\u0435\u043a\u0441\u0442 \u043f\u043e\u0434\u043f\u0438\u0441\u0438", None))
        self.open_config_button.setText(QCoreApplication.translate("Form", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c \u0444\u0430\u0439\u043b \u043a\u043e\u043d\u0444\u0438\u0433\u0443\u0440\u0430\u0446\u0438\u0438", None))
        self.save_config_button.setText(QCoreApplication.translate("Form", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0444\u0430\u0439\u043b \u043a\u043e\u043d\u0444\u0438\u0433\u0443\u0440\u0430\u0446\u0438\u0438", None))
        self.add_name_button.setText(QCoreApplication.translate("Form", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043e\u0431\u0440\u0430\u0449\u0435\u043d\u0438\u0435", None))
        self.mail_password_visible.setText("")
    # retranslateUi

