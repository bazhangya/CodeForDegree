# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'remote_all_ui.ui'
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
        MainWindow.resize(1280, 711)
        MainWindow.setStyleSheet(u"#QWidget{\n"
"	background:url(./images/all.jpg);\n"
"	color:rgb(255,255,255);\n"
"\n"
"}\n"
"QWidget{\n"
"	background: transparent; \n"
"	border-image:url(./images/all.jpg);\n"
"	color:rgb(255,255,255);\n"
"\n"
"}\n"
"\n"
"QTextEdit{\n"
"	background: transparent; \n"
"	border-image:transparent;\n"
"	color:rgb(255,255,255);\n"
"	font: 12pt \"\u5e7c\u5706\";\n"
"\n"
"}\n"
"QPushButton{\n"
"	background: transparent; \n"
"	border-image:transparent;\n"
"	background: transparent; \n"
"    color:white;\n"
"	font: 15pt \"\u5e7c\u5706\";\n"
"	border-color:(255,255,255);\n"
"	border-width:1px;\n"
"	border-style:outset;\n"
"	border-radius:5px;\n"
"}\n"
"QPushButton:pressed{\n"
"	background: transparent; \n"
"	border-image:transparent;\n"
"	background: transparent; \n"
"    color:white;\n"
"	font: 17pt \"\u5e7c\u5706\";	\n"
"	border-style:inset;\n"
"	border-width:2px;\n"
"	border-radius:5px;\n"
"}\n"
"QLabel {\n"
"	background: transparent; \n"
"	border-image:transparent;\n"
"	color:rgb(255,255,255);\n"
"	font: 30pt \"\u96b6"
                        "\u4e66\";\n"
"}\n"
"\n"
"QListWidget::item{\n"
"	background: transparent; \n"
"	border-image:transparent;\n"
"	color:rgb(255,255,255);\n"
"	font: 4pt \"\u5e7c\u5706\";\n"
"}\n"
"\n"
"\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_5)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_5)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_8)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_online = QLabel(self.centralwidget)
        self.label_online.setObjectName(u"label_online")
        self.label_online.setLayoutDirection(Qt.LeftToRight)
        self.label_online.setStyleSheet(u"QLabel {\n"
"\n"
"	background: transparent;\n"
"	border-image:transparent;\n"
"	color:rgb(245,195,40);\n"
"	font: 30pt \"\u96b6\u4e66\";\n"
"}")
        self.label_online.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.label_online)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_12)

        self.horizontalLayout_5.setStretch(0, 114)
        self.horizontalLayout_5.setStretch(1, 100)

        self.verticalLayout_4.addLayout(self.horizontalLayout_5)

        self.verticalSpacer_12 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_12)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_damage = QLabel(self.centralwidget)
        self.label_damage.setObjectName(u"label_damage")
        self.label_damage.setStyleSheet(u"QLabel {\n"
"	background: transparent; \n"
"	border-image:transparent;\n"
"	color:rgb(255,43,75);\n"
"	font: 30pt \"\u96b6\u4e66\";\n"
"}")
        self.label_damage.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_6.addWidget(self.label_damage)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_10)

        self.horizontalLayout_6.setStretch(0, 114)
        self.horizontalLayout_6.setStretch(1, 100)

        self.verticalLayout_4.addLayout(self.horizontalLayout_6)

        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_11)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_workingtime = QLabel(self.centralwidget)
        self.label_workingtime.setObjectName(u"label_workingtime")
        self.label_workingtime.setStyleSheet(u"QLabel {\n"
"	background: transparent;\n"
"	border-image:transparent; \n"
"	color:rgb(11,255,133);\n"
"	font: 30pt \"\u96b6\u4e66\";\n"
"}")
        self.label_workingtime.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.label_workingtime)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_8)

        self.horizontalLayout_7.setStretch(0, 114)
        self.horizontalLayout_7.setStretch(1, 100)

        self.verticalLayout_4.addLayout(self.horizontalLayout_7)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_10)

        self.verticalLayout_graph = QVBoxLayout()
        self.verticalLayout_graph.setObjectName(u"verticalLayout_graph")

        self.verticalLayout_4.addLayout(self.verticalLayout_graph)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_4)

        self.verticalLayout_4.setStretch(0, 5)
        self.verticalLayout_4.setStretch(1, 80)
        self.verticalLayout_4.setStretch(2, 50)
        self.verticalLayout_4.setStretch(3, 80)
        self.verticalLayout_4.setStretch(4, 50)
        self.verticalLayout_4.setStretch(5, 80)
        self.verticalLayout_4.setStretch(6, 120)
        self.verticalLayout_4.setStretch(7, 330)
        self.verticalLayout_4.setStretch(8, 1)

        self.horizontalLayout_2.addLayout(self.verticalLayout_4)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_6)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_7)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.pushButton_update = QPushButton(self.centralwidget)
        self.pushButton_update.setObjectName(u"pushButton_update")
        self.pushButton_update.setMinimumSize(QSize(80, 50))
        font = QFont()
        font.setFamily(u"\u5e7c\u5706")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_update.setFont(font)
        self.pushButton_update.setStyleSheet(u"QPushButton{\n"
"	border-image:transparent;\n"
"}")

        self.horizontalLayout_4.addWidget(self.pushButton_update)

        self.pushButton_cancel = QPushButton(self.centralwidget)
        self.pushButton_cancel.setObjectName(u"pushButton_cancel")
        self.pushButton_cancel.setMinimumSize(QSize(80, 50))
        self.pushButton_cancel.setFont(font)
        self.pushButton_cancel.setStyleSheet(u"QPushButton{\n"
"	border-image:transparent;\n"
"}")

        self.horizontalLayout_4.addWidget(self.pushButton_cancel)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_9)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_cake = QVBoxLayout()
        self.verticalLayout_cake.setObjectName(u"verticalLayout_cake")

        self.horizontalLayout_3.addLayout(self.verticalLayout_cake)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalSpacer_14 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_14)

        self.label_onworking = QLabel(self.centralwidget)
        self.label_onworking.setObjectName(u"label_onworking")
        self.label_onworking.setStyleSheet(u"QLabel {\n"
"	background: transparent; \n"
"	border-image:transparent;\n"
"	color:rgb(11,255,133);\n"
"	font: 20pt \"\u96b6\u4e66\";\n"
"}\n"
"")
        self.label_onworking.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_6.addWidget(self.label_onworking)

        self.verticalSpacer_15 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_15)

        self.label_notworking = QLabel(self.centralwidget)
        self.label_notworking.setObjectName(u"label_notworking")
        self.label_notworking.setStyleSheet(u"QLabel {\n"
"	background: transparent; \n"
"	border-image:transparent;\n"
"	color:rgb(248,214,2);\n"
"	font: 20pt \"\u96b6\u4e66\";\n"
"}\n"
"")
        self.label_notworking.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_6.addWidget(self.label_notworking)

        self.verticalSpacer_16 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_16)

        self.label_offline = QLabel(self.centralwidget)
        self.label_offline.setObjectName(u"label_offline")
        self.label_offline.setStyleSheet(u"QLabel {\n"
"	background: transparent;\n"
"	border-image:transparent; \n"
"	color:rgb(218,81,0);\n"
"	font: 20pt \"\u96b6\u4e66\";\n"
"}\n"
"")
        self.label_offline.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_6.addWidget(self.label_offline)

        self.verticalSpacer_13 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_13)

        self.verticalLayout_6.setStretch(0, 8)
        self.verticalLayout_6.setStretch(1, 10)
        self.verticalLayout_6.setStretch(2, 8)
        self.verticalLayout_6.setStretch(3, 10)
        self.verticalLayout_6.setStretch(4, 8)
        self.verticalLayout_6.setStretch(5, 10)
        self.verticalLayout_6.setStretch(6, 15)

        self.verticalLayout_5.addLayout(self.verticalLayout_6)


        self.horizontalLayout_3.addLayout(self.verticalLayout_5)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_6)

        self.horizontalLayout_3.setStretch(0, 10)
        self.horizontalLayout_3.setStretch(1, 4)
        self.horizontalLayout_3.setStretch(2, 6)

        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_7)

        self.listWidget_base = QListWidget(self.centralwidget)
        self.listWidget_base.setObjectName(u"listWidget_base")
        self.listWidget_base.setStyleSheet(u"QWidget{\n"
"	border-image:transparent;\n"
"	color:rgb(255, 255, 255);\n"
"	background: rgba(5, 22, 52,50%); \n"
"	font: 14pt \"\u5e7c\u5706\";\n"
"}")

        self.horizontalLayout.addWidget(self.listWidget_base)

        self.listWidget_summary = QListWidget(self.centralwidget)
        self.listWidget_summary.setObjectName(u"listWidget_summary")
        self.listWidget_summary.setMinimumSize(QSize(50, 100))
        self.listWidget_summary.setStyleSheet(u"QWidget{\n"
"	border-image:transparent;\n"
"	color:rgb(255, 255, 255);\n"
"	background: rgba(5, 22, 52,50%); \n"
"	font: 14pt \"\u5e7c\u5706\";\n"
"}")

        self.horizontalLayout.addWidget(self.listWidget_summary)

        self.listWidget_num = QListWidget(self.centralwidget)
        self.listWidget_num.setObjectName(u"listWidget_num")
        self.listWidget_num.setStyleSheet(u"QWidget{\n"
"	border-image:transparent;\n"
"	color:rgb(255, 255, 255);\n"
"	background: rgba(5, 22, 52,50%); \n"
"	font: 14pt \"\u5e7c\u5706\";\n"
"}")

        self.horizontalLayout.addWidget(self.listWidget_num)

        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 10)
        self.horizontalLayout.setStretch(2, 10)
        self.horizontalLayout.setStretch(3, 10)

        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.verticalLayout_3.setStretch(0, 10)
        self.verticalLayout_3.setStretch(1, 60)
        self.verticalLayout_3.setStretch(2, 15)
        self.verticalLayout_3.setStretch(3, 100)
        self.verticalLayout_3.setStretch(4, 10)

        self.horizontalLayout_2.addLayout(self.verticalLayout_3)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.horizontalLayout_2.setStretch(0, 5)
        self.horizontalLayout_2.setStretch(1, 75)
        self.horizontalLayout_2.setStretch(2, 40)
        self.horizontalLayout_2.setStretch(3, 10)
        self.horizontalLayout_2.setStretch(4, 35)
        self.horizontalLayout_2.setStretch(5, 70)
        self.horizontalLayout_2.setStretch(6, 5)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.verticalLayout.setStretch(0, 10)
        self.verticalLayout.setStretch(1, 20)
        self.verticalLayout.setStretch(2, 200)
        MainWindow.setCentralWidget(self.centralwidget)
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
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u94a2\u4e1d\u7ef3\u8fdc\u7a0b\u76d1\u63a7\u7cfb\u7edf", None))
        self.label_online.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label_damage.setText(QCoreApplication.translate("MainWindow", u"75", None))
        self.label_workingtime.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.pushButton_update.setText(QCoreApplication.translate("MainWindow", u"\u66f4\u65b0", None))
        self.pushButton_cancel.setText(QCoreApplication.translate("MainWindow", u"\u9000\u51fa", None))
        self.label_onworking.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label_notworking.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_offline.setText(QCoreApplication.translate("MainWindow", u"4", None))
    # retranslateUi

