# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_detaildialog.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DetailDialog(object):
    def setupUi(self, DetailDialog):
        DetailDialog.setObjectName("DetailDialog")
        DetailDialog.resize(670, 476)
        self.verticalLayout = QtWidgets.QVBoxLayout(DetailDialog)
        self.verticalLayout.setContentsMargins(-1, 0, -1, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.formLayout.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.formLayout.setContentsMargins(-1, 0, 9, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(DetailDialog)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.textName = QtWidgets.QLineEdit(DetailDialog)
        self.textName.setObjectName("textName")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.textName)
        self.label_2 = QtWidgets.QLabel(DetailDialog)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.textState = QtWidgets.QLineEdit(DetailDialog)
        self.textState.setObjectName("textState")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.textState)
        self.label_3 = QtWidgets.QLabel(DetailDialog)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.textChamber = QtWidgets.QLineEdit(DetailDialog)
        self.textChamber.setObjectName("textChamber")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.textChamber)
        self.label_4 = QtWidgets.QLabel(DetailDialog)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.textParty = QtWidgets.QLineEdit(DetailDialog)
        self.textParty.setObjectName("textParty")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.textParty)
        self.label_5 = QtWidgets.QLabel(DetailDialog)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.textBirthday = QtWidgets.QLineEdit(DetailDialog)
        self.textBirthday.setObjectName("textBirthday")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.textBirthday)
        self.label_6 = QtWidgets.QLabel(DetailDialog)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.textPhone = QtWidgets.QLineEdit(DetailDialog)
        self.textPhone.setObjectName("textPhone")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.textPhone)
        self.label_7 = QtWidgets.QLabel(DetailDialog)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.textAddress = QtWidgets.QLineEdit(DetailDialog)
        self.textAddress.setObjectName("textAddress")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.textAddress)
        self.label_8 = QtWidgets.QLabel(DetailDialog)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.textWeb = QtWidgets.QLineEdit(DetailDialog)
        self.textWeb.setObjectName("textWeb")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.textWeb)
        self.label_9 = QtWidgets.QLabel(DetailDialog)
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.textCrp = QtWidgets.QLineEdit(DetailDialog)
        self.textCrp.setObjectName("textCrp")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.textCrp)
        self.label12 = QtWidgets.QLabel(DetailDialog)
        self.label12.setObjectName("label12")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.label12)
        self.textGovTrack = QtWidgets.QLineEdit(DetailDialog)
        self.textGovTrack.setObjectName("textGovTrack")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.textGovTrack)
        self.label_10 = QtWidgets.QLabel(DetailDialog)
        self.label_10.setObjectName("label_10")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.textVoteSmart = QtWidgets.QLineEdit(DetailDialog)
        self.textVoteSmart.setObjectName("textVoteSmart")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.FieldRole, self.textVoteSmart)
        self.label_11 = QtWidgets.QLabel(DetailDialog)
        self.label_11.setObjectName("label_11")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.textContact = QtWidgets.QLineEdit(DetailDialog)
        self.textContact.setObjectName("textContact")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.textContact)
        self.verticalLayout.addLayout(self.formLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(DetailDialog)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)
        spacerItem = QtWidgets.QSpacerItem(20, 15, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.verticalLayout.setStretch(0, 1)

        self.retranslateUi(DetailDialog)
        QtCore.QMetaObject.connectSlotsByName(DetailDialog)

    def retranslateUi(self, DetailDialog):
        _translate = QtCore.QCoreApplication.translate
        DetailDialog.setWindowTitle(_translate("DetailDialog", "Open Congress"))
        self.label.setText(_translate("DetailDialog", "Name"))
        self.label_2.setText(_translate("DetailDialog", "State"))
        self.label_3.setText(_translate("DetailDialog", "Chamber"))
        self.label_4.setText(_translate("DetailDialog", "Party"))
        self.label_5.setText(_translate("DetailDialog", "Birthday"))
        self.label_6.setText(_translate("DetailDialog", "Phone"))
        self.label_7.setText(_translate("DetailDialog", "Address"))
        self.label_8.setText(_translate("DetailDialog", "Web"))
        self.label_9.setText(_translate("DetailDialog", "CRP"))
        self.label12.setText(_translate("DetailDialog", "GovTrack"))
        self.label_10.setText(_translate("DetailDialog", "VoteSmart"))
        self.label_11.setText(_translate("DetailDialog", "Contact"))

