# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'remote_applicantion_set_ui.ui'
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
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet(u"QPushButton{\n"
"	color:rgb(17,17,17);\n"
"	border-width: 1px;\n"
"	border-radius: 6px;\n"
"	border-bottom-color: rgb(150,150,150);\n"
"	border-right-color: rgb(165,165,165);\n"
"	border-left-color: rgb(165,165,165);\n"
"	border-top-color: rgb(180,180,180);\n"
"	border-style: solid;\n"
"	padding: 4px;\n"
"	background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(155, 187, 89, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"QPushButton:default{\n"
"	color:rgb(17,17,17);\n"
"	border-width: 1px;\n"
"	border-radius: 6px;\n"
"	border-bottom-color: rgb(150,150,150);\n"
"	border-right-color: rgb(165,165,165);\n"
"	border-left-color: rgb(165,165,165);\n"
"	border-top-color: rgb(180,180,180);\n"
"	border-style: solid;\n"
"	padding: 4px;\n"
"	background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(155, 187, 89, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"QPushButton:pressed{\n"
"	color:rgb(17,17,17);\n"
"	border-width: 1px;\n"
"	border-radius: 6px;\n"
"	"
                        "border-width: 1px;\n"
"	border-top-color: rgba(255,150,60,200);\n"
"	border-right-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(200, 70, 20, 255), stop:1 rgba(255,150,60, 200));\n"
"	border-left-color:  qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:0, stop:0 rgba(200, 70, 20, 255), stop:1 rgba(255,150,60, 200));\n"
"	border-bottom-color: rgba(200,70,20,200);\n"
"	border-style: solid;\n"
"	padding: 2px;\n"
"	background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(155, 187, 89, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"QPushButton:disabled{\n"
"	color:rgb(174,167,159);\n"
"	border-width: 1px;\n"
"	border-radius: 6px;\n"
"	background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(155, 187, 89, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"QRadioButton {\n"
"	padding: 1px;\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"	height: 10px;\n"
"	width: 10px;\n"
"	border-style:solid;\n"
"	border-radius:5px;\n"
"	border-width"
                        ": 1px;\n"
"	border-color: rgba(246, 134, 86, 255);\n"
"	color: #a9b7c6;\n"
"	background-color:rgba(246, 134, 86, 255);\n"
"}\n"
"QRadioButton::indicator:!checked {\n"
"	height: 10px;\n"
"	width: 10px;\n"
"	border-style:solid;\n"
"	border-radius:5px;\n"
"	border-width: 1px;\n"
"	border-color: rgb(246, 134, 86);\n"
"	color: #a9b7c6;\n"
"	background-color: transparent;\n"
"}\n"
"QWidget {\n"
"	background-color:#f0f0f0;\n"
"}\n"
"QLabel {\n"
"	color:rgb(17,17,17);\n"
"}\n"
"QWidget {\n"
"	color:rgb(0,0,0);\n"
"	background-color:rgb(76,93,99);\n"
"}\n"
"font: 22pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_set_title = QLabel(self.centralwidget)
        self.label_set_title.setObjectName(u"label_set_title")
        font = QFont()
        font.setFamily(u"\u5fae\u8f6f\u96c5\u9ed1")
        font.setPointSize(24)
        self.label_set_title.setFont(font)
        self.label_set_title.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_set_title)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_6)

        self.label_set_y_uplimit = QLabel(self.centralwidget)
        self.label_set_y_uplimit.setObjectName(u"label_set_y_uplimit")

        self.horizontalLayout_2.addWidget(self.label_set_y_uplimit)

        self.lineEdit_set_graph_y_up = QLineEdit(self.centralwidget)
        self.lineEdit_set_graph_y_up.setObjectName(u"lineEdit_set_graph_y_up")

        self.horizontalLayout_2.addWidget(self.lineEdit_set_graph_y_up)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_7)

        self.label_set_alarm_uplimit = QLabel(self.centralwidget)
        self.label_set_alarm_uplimit.setObjectName(u"label_set_alarm_uplimit")

        self.horizontalLayout_2.addWidget(self.label_set_alarm_uplimit)

        self.lineEdit_set_alarm_uplimit = QLineEdit(self.centralwidget)
        self.lineEdit_set_alarm_uplimit.setObjectName(u"lineEdit_set_alarm_uplimit")

        self.horizontalLayout_2.addWidget(self.lineEdit_set_alarm_uplimit)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_5)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_10)

        self.label_set_y_downlimit = QLabel(self.centralwidget)
        self.label_set_y_downlimit.setObjectName(u"label_set_y_downlimit")

        self.horizontalLayout_3.addWidget(self.label_set_y_downlimit)

        self.lineEdit_set_graph_y_down = QLineEdit(self.centralwidget)
        self.lineEdit_set_graph_y_down.setObjectName(u"lineEdit_set_graph_y_down")

        self.horizontalLayout_3.addWidget(self.lineEdit_set_graph_y_down)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_9)

        self.label_set_alarm_downlimit = QLabel(self.centralwidget)
        self.label_set_alarm_downlimit.setObjectName(u"label_set_alarm_downlimit")

        self.horizontalLayout_3.addWidget(self.label_set_alarm_downlimit)

        self.lineEdit_set_alarm_down_limit = QLineEdit(self.centralwidget)
        self.lineEdit_set_alarm_down_limit.setObjectName(u"lineEdit_set_alarm_down_limit")

        self.horizontalLayout_3.addWidget(self.lineEdit_set_alarm_down_limit)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_8)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_12)

        self.label_set_servechose = QLabel(self.centralwidget)
        self.label_set_servechose.setObjectName(u"label_set_servechose")
        self.label_set_servechose.setMinimumSize(QSize(130, 0))

        self.horizontalLayout_5.addWidget(self.label_set_servechose)

        self.comboBox_set_servechose = QComboBox(self.centralwidget)
        self.comboBox_set_servechose.addItem("")
        self.comboBox_set_servechose.addItem("")
        self.comboBox_set_servechose.addItem("")
        self.comboBox_set_servechose.addItem("")
        self.comboBox_set_servechose.addItem("")
        self.comboBox_set_servechose.addItem("")
        self.comboBox_set_servechose.addItem("")
        self.comboBox_set_servechose.addItem("")
        self.comboBox_set_servechose.setObjectName(u"comboBox_set_servechose")
        self.comboBox_set_servechose.setMinimumSize(QSize(130, 0))

        self.horizontalLayout_5.addWidget(self.comboBox_set_servechose)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_13)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_14)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_11)

        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_15)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pushButton_set_save = QPushButton(self.centralwidget)
        self.pushButton_set_save.setObjectName(u"pushButton_set_save")

        self.horizontalLayout.addWidget(self.pushButton_set_save)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)

        self.pushButton_set_signin = QPushButton(self.centralwidget)
        self.pushButton_set_signin.setObjectName(u"pushButton_set_signin")

        self.horizontalLayout.addWidget(self.pushButton_set_signin)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.pushButton_set_cancel = QPushButton(self.centralwidget)
        self.pushButton_set_cancel.setObjectName(u"pushButton_set_cancel")

        self.horizontalLayout.addWidget(self.pushButton_set_cancel)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_5)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 23))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e", None))
        self.label_set_title.setText(QCoreApplication.translate("MainWindow", u"\u94a2\u4e1d\u7ef3\u8fdc\u7a0b\u667a\u80fd\u76d1\u63a7\u7cfb\u7edf\u8f6f\u4ef6\u8bbe\u7f6e", None))
        self.label_set_y_uplimit.setText(QCoreApplication.translate("MainWindow", u"Y\u8f74\u663e\u793a\u4e0a\u9650\uff1a", None))
        self.label_set_alarm_uplimit.setText(QCoreApplication.translate("MainWindow", u"\u7f3a\u9677\u62a5\u8b66\u4e0a\u9650\uff1a", None))
        self.label_set_y_downlimit.setText(QCoreApplication.translate("MainWindow", u"Y\u8f74\u663e\u793a\u4e0b\u9650\uff1a", None))
        self.label_set_alarm_downlimit.setText(QCoreApplication.translate("MainWindow", u"\u7f3a\u9677\u62a5\u8b66\u4e0b\u9650\uff1a", None))
        self.label_set_servechose.setText(QCoreApplication.translate("MainWindow", u"\u6570\u636e\u4e0b\u8f7d\u670d\u52a1\u5668\u9009\u62e9\uff1a", None))
        self.comboBox_set_servechose.setItemText(0, QCoreApplication.translate("MainWindow", u"get1", None))
        self.comboBox_set_servechose.setItemText(1, QCoreApplication.translate("MainWindow", u"get2", None))
        self.comboBox_set_servechose.setItemText(2, QCoreApplication.translate("MainWindow", u"get3", None))
        self.comboBox_set_servechose.setItemText(3, QCoreApplication.translate("MainWindow", u"get4", None))
        self.comboBox_set_servechose.setItemText(4, QCoreApplication.translate("MainWindow", u"get5", None))
        self.comboBox_set_servechose.setItemText(5, QCoreApplication.translate("MainWindow", u"get6", None))
        self.comboBox_set_servechose.setItemText(6, QCoreApplication.translate("MainWindow", u"get7", None))
        self.comboBox_set_servechose.setItemText(7, QCoreApplication.translate("MainWindow", u"get8", None))

        self.pushButton_set_save.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58", None))
        self.pushButton_set_signin.setText(QCoreApplication.translate("MainWindow", u"\u8fde\u63a5\u670d\u52a1\u5668", None))
        self.pushButton_set_cancel.setText(QCoreApplication.translate("MainWindow", u"\u53d6\u6d88", None))
    # retranslateUi

