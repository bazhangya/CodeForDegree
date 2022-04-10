# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'remote_sign_ui.ui'
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
        Form.resize(1280, 720)
        Form.setStyleSheet(u"#QWidget{\n"
"	background:url(./images/sign2.jpg);\n"
"}\n"
"QWidget{\n"
"border-image:url(./images/sign2.jpg);\n"
"}\n"
"QTextEdit{\n"
"	color:rgb(255,255,255);\n"
"	font: 12pt \"\u5e7c\u5706\";\n"
"\n"
"}\n"
"QPushButton{\n"
"	background:transparent;\n"
"	border-image:transparent;\n"
"    color:white;\n"
"	font: 15pt \"\u5e7c\u5706\";\n"
"	border-color:(255,255,255);\n"
"	border-width:1px;\n"
"	border-style:outset;\n"
"	border-radius:5px;\n"
"}\n"
"QPushButton:pressed{\n"
"	background:transparent;\n"
"	border-image:transparent;\n"
"    color:white;\n"
"	font: 17pt \"\u5e7c\u5706\";	\n"
"	border-style:inset;\n"
"	border-width:2px;\n"
"	border-radius:5px;\n"
"}\n"
"QLabel {\n"
"	color:rgb(255,255,255);\n"
"	font: 22pt \"\u5e7c\u5706\";\n"
"}\n"
"QLineEdit{\n"
"	background:transparent;\n"
"	border-image:transparent;\n"
"	color:rgb(255,255,255);\n"
"	font: 18pt \"\u5e7c\u5706\";\n"
"\n"
"\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.lineEdit_id = QLineEdit(Form)
        self.lineEdit_id.setObjectName(u"lineEdit_id")
        self.lineEdit_id.setMinimumSize(QSize(50, 30))

        self.horizontalLayout_3.addWidget(self.lineEdit_id)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lineEdit_passwd = QLineEdit(Form)
        self.lineEdit_passwd.setObjectName(u"lineEdit_passwd")
        self.lineEdit_passwd.setMinimumSize(QSize(50, 30))
        self.lineEdit_passwd.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_2.addWidget(self.lineEdit_passwd)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.pushButton_sign = QPushButton(Form)
        self.pushButton_sign.setObjectName(u"pushButton_sign")
        self.pushButton_sign.setEnabled(True)
        self.pushButton_sign.setMinimumSize(QSize(50, 30))

        self.horizontalLayout_4.addWidget(self.pushButton_sign)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)

        self.pushButton_quit = QPushButton(Form)
        self.pushButton_quit.setObjectName(u"pushButton_quit")
        self.pushButton_quit.setMinimumSize(QSize(50, 30))

        self.horizontalLayout_4.addWidget(self.pushButton_quit)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.verticalLayout.setStretch(0, 108)
        self.verticalLayout.setStretch(1, 5)
        self.verticalLayout.setStretch(2, 5)
        self.verticalLayout.setStretch(3, 1)
        self.verticalLayout.setStretch(4, 15)
        self.verticalLayout.setStretch(5, 110)

        self.horizontalLayout.addLayout(self.verticalLayout)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)

        self.horizontalLayout.setStretch(0, 32)
        self.horizontalLayout.setStretch(1, 10)
        self.horizontalLayout.setStretch(2, 30)

        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.verticalLayout_2.setStretch(0, 10)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u767b\u5f55", None))
        self.lineEdit_id.setText(QCoreApplication.translate("Form", u"admin", None))
        self.pushButton_sign.setText(QCoreApplication.translate("Form", u"\u767b\u5f55", None))
        self.pushButton_quit.setText(QCoreApplication.translate("Form", u"\u9000\u51fa", None))
    # retranslateUi

