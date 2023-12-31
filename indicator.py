# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\indicators.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(488, 355)
        self.emergency = QtWidgets.QFrame(Form)
        self.emergency.setGeometry(QtCore.QRect(40, 90, 161, 161))
        self.emergency.setStyleSheet("QFrame{\n"
"    border-color: rgb(0, 255, 0);\n"
"    border-radius:80px;\n"
"    background-color: rgb(255, 00, 00);border: 2px solid black\n"
"}")
        self.emergency.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.emergency.setFrameShadow(QtWidgets.QFrame.Raised)
        self.emergency.setObjectName("emergency")
        self.setup_status_2 = QtWidgets.QFrame(Form)
        self.setup_status_2.setGeometry(QtCore.QRect(260, 90, 161, 161))
        self.setup_status_2.setStyleSheet("QFrame{\n"
"    border-radius:80px;\n"
"    border: 2px solid black;background-color: rgb(0, 209, 0);\n"
"}")
        self.setup_status_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.setup_status_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.setup_status_2.setObjectName("setup_status_2")
        self.emergency = QtWidgets.QLabel(Form)
        self.emergency.setGeometry(QtCore.QRect(46, 270, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.emergency.setFont(font)
        self.emergency.setAlignment(QtCore.Qt.AlignCenter)
        self.emergency.setObjectName("emergency")
        self.setup = QtWidgets.QLabel(Form)
        self.setup.setGeometry(QtCore.QRect(260, 270, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.setup.setFont(font)
        self.setup.setAlignment(QtCore.Qt.AlignCenter)
        self.setup.setObjectName("setup")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.emergency.setText(_translate("Form", "EMERGENCY STATUS"))
        self.setup.setText(_translate("Form", "SETUP STATUS"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
