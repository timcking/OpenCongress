# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_mainapp.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(766, 566)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.leSearchSenate = QtWidgets.QLineEdit(self.centralwidget)
        self.leSearchSenate.setToolTip("")
        self.leSearchSenate.setObjectName("leSearchSenate")
        self.horizontalLayout_2.addWidget(self.leSearchSenate)
        self.leSearchHouse = QtWidgets.QLineEdit(self.centralwidget)
        self.leSearchHouse.setObjectName("leSearchHouse")
        self.horizontalLayout_2.addWidget(self.leSearchHouse)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.listSenate = QtWidgets.QListWidget(self.centralwidget)
        self.listSenate.setObjectName("listSenate")
        self.horizontalLayout.addWidget(self.listSenate)
        self.listHouse = QtWidgets.QListWidget(self.centralwidget)
        self.listHouse.setObjectName("listHouse")
        self.horizontalLayout.addWidget(self.listHouse)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.centralwidget)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)
        self.verticalLayout.setStretch(1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "OpenCongress"))
        self.leSearchSenate.setPlaceholderText(_translate("MainWindow", "Search Senate"))
        self.leSearchHouse.setPlaceholderText(_translate("MainWindow", "Search House"))

