# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'remote_main_ui.ui'
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
        MainWindow.resize(1280, 720)
        MainWindow.setStyleSheet(u"QWidget{\n"
"	background:rgb(0,9,40);\n"
"}\n"
"QTextEdit{\n"
"	color:rgb(255,255,255);\n"
"	font: 12pt \"\u5e7c\u5706\";\n"
"\n"
"}\n"
"QPushButton{\n"
"    color:white;\n"
"	font: 15pt \"\u5e7c\u5706\";\n"
"	border-color:(255,255,255);\n"
"	border-width:1px;\n"
"	border-style:outset;\n"
"	border-radius:5px;\n"
"}\n"
"QPushButton:pressed{\n"
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
"")
        self.top_layer = QWidget(MainWindow)
        self.top_layer.setObjectName(u"top_layer")
        self.verticalLayout_3 = QVBoxLayout(self.top_layer)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_title = QLabel(self.top_layer)
        self.label_title.setObjectName(u"label_title")
        font = QFont()
        font.setFamily(u"\u5e7c\u5706")
        font.setPointSize(22)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_title.setFont(font)
        self.label_title.setTextFormat(Qt.PlainText)
        self.label_title.setAlignment(Qt.AlignCenter)
        self.label_title.setMargin(4)

        self.verticalLayout_3.addWidget(self.label_title)

        self.second_layer = QHBoxLayout()
        self.second_layer.setObjectName(u"second_layer")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.second_layer.addItem(self.horizontalSpacer_2)

        self.third_layer1 = QVBoxLayout()
        self.third_layer1.setObjectName(u"third_layer1")
        self.third_layer1.setContentsMargins(0, 0, 0, 0)
        self.bn_start = QPushButton(self.top_layer)
        self.bn_start.setObjectName(u"bn_start")
        self.bn_start.setMinimumSize(QSize(80, 40))
        font1 = QFont()
        font1.setFamily(u"\u5e7c\u5706")
        font1.setPointSize(15)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setWeight(50)
        self.bn_start.setFont(font1)

        self.third_layer1.addWidget(self.bn_start)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.third_layer1.addItem(self.verticalSpacer_4)

        self.bn_stop = QPushButton(self.top_layer)
        self.bn_stop.setObjectName(u"bn_stop")
        self.bn_stop.setMinimumSize(QSize(80, 40))
        self.bn_stop.setFont(font1)

        self.third_layer1.addWidget(self.bn_stop)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.third_layer1.addItem(self.verticalSpacer_5)

        self.bn_report = QPushButton(self.top_layer)
        self.bn_report.setObjectName(u"bn_report")
        self.bn_report.setMinimumSize(QSize(80, 40))
        self.bn_report.setFont(font1)

        self.third_layer1.addWidget(self.bn_report)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.third_layer1.addItem(self.verticalSpacer_6)

        self.bn_back = QPushButton(self.top_layer)
        self.bn_back.setObjectName(u"bn_back")
        self.bn_back.setMinimumSize(QSize(80, 40))
        self.bn_back.setFont(font1)

        self.third_layer1.addWidget(self.bn_back)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.third_layer1.addItem(self.verticalSpacer_7)

        self.bn_set = QPushButton(self.top_layer)
        self.bn_set.setObjectName(u"bn_set")
        self.bn_set.setMinimumSize(QSize(80, 40))
        self.bn_set.setFont(font1)

        self.third_layer1.addWidget(self.bn_set)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.third_layer1.addItem(self.verticalSpacer_8)

        self.bn_quit = QPushButton(self.top_layer)
        self.bn_quit.setObjectName(u"bn_quit")
        self.bn_quit.setMinimumSize(QSize(80, 40))
        self.bn_quit.setFont(font1)

        self.third_layer1.addWidget(self.bn_quit)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.third_layer1.addItem(self.verticalSpacer)

        self.label_2 = QLabel(self.top_layer)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(80, 40))
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.third_layer1.addWidget(self.label_2)

        self.label_distance = QLabel(self.top_layer)
        self.label_distance.setObjectName(u"label_distance")
        self.label_distance.setMinimumSize(QSize(80, 40))
        self.label_distance.setFont(font)
        self.label_distance.setAlignment(Qt.AlignCenter)
        self.label_distance.setMargin(-6)

        self.third_layer1.addWidget(self.label_distance)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.third_layer1.addItem(self.verticalSpacer_3)

        self.label_4 = QLabel(self.top_layer)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(80, 40))
        self.label_4.setSizeIncrement(QSize(0, 0))
        self.label_4.setFont(font)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.third_layer1.addWidget(self.label_4)

        self.label_damage = QLabel(self.top_layer)
        self.label_damage.setObjectName(u"label_damage")
        self.label_damage.setMinimumSize(QSize(80, 40))
        self.label_damage.setFont(font)
        self.label_damage.setAlignment(Qt.AlignCenter)

        self.third_layer1.addWidget(self.label_damage)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.third_layer1.addItem(self.verticalSpacer_2)

        self.third_layer1.setStretch(0, 1)
        self.third_layer1.setStretch(2, 1)
        self.third_layer1.setStretch(4, 1)
        self.third_layer1.setStretch(6, 1)
        self.third_layer1.setStretch(10, 1)

        self.second_layer.addLayout(self.third_layer1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.second_layer.addItem(self.horizontalSpacer_3)

        self.third_layer2 = QVBoxLayout()
        self.third_layer2.setObjectName(u"third_layer2")

        self.second_layer.addLayout(self.third_layer2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.second_layer.addItem(self.horizontalSpacer)

        self.second_layer.setStretch(0, 1)
        self.second_layer.setStretch(1, 2)
        self.second_layer.setStretch(2, 1)
        self.second_layer.setStretch(3, 20)
        self.second_layer.setStretch(4, 1)

        self.verticalLayout_3.addLayout(self.second_layer)

        self.verticalLayout_3.setStretch(0, 1)
        self.verticalLayout_3.setStretch(1, 9)
        MainWindow.setCentralWidget(self.top_layer)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1280, 23))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u94a2\u4e1d\u7ef3\u8fdc\u7a0b\u667a\u80fd\u76d1\u63a7\u7cfb\u7edf", None))
        self.label_title.setText(QCoreApplication.translate("MainWindow", u"\u68c0\u6d4b\u70b9\u5b9e\u65f6\u6570\u636e\u6ce2\u5f62", None))
        self.bn_start.setText(QCoreApplication.translate("MainWindow", u"\u68c0\u6d4b", None))
        self.bn_stop.setText(QCoreApplication.translate("MainWindow", u"\u6682\u505c", None))
        self.bn_report.setText(QCoreApplication.translate("MainWindow", u"\u62a5\u8868", None))
        self.bn_back.setText(QCoreApplication.translate("MainWindow", u"\u56de\u653e", None))
        self.bn_set.setText(QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e", None))
        self.bn_quit.setText(QCoreApplication.translate("MainWindow", u"\u9000\u51fa", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u8ddd\u79bb", None))
        self.label_distance.setText(QCoreApplication.translate("MainWindow", u"0m", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u635f\u4f24", None))
        self.label_damage.setText(QCoreApplication.translate("MainWindow", u"0", None))
    # retranslateUi

