# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'matplotlibTest.ui'
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
        Form.resize(400, 300)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.graphicsView_mat = QGraphicsView(Form)
        self.graphicsView_mat.setObjectName(u"graphicsView_mat")

        self.verticalLayout.addWidget(self.graphicsView_mat)

        self.pushButton_gen = QPushButton(Form)
        self.pushButton_gen.setObjectName(u"pushButton_gen")

        self.verticalLayout.addWidget(self.pushButton_gen)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButton_gen.setText(QCoreApplication.translate("Form", u"PushButton", None))
    # retranslateUi

