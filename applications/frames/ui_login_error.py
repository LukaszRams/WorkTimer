# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login_error.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


btn_style = """QPushButton {
                   border: 1px solid gray;
                   border-radius: 13px;
                   font: 10pt \\\"Segoe Print\\\";
                   background-color: qlineargradient(x1: 0.5, y1: 0.5, x2: 1, y2: 1, stop: 0 #dadbde, stop: 1 #f6f7fa);
               }
               QPushButton:default {
                   border: 2px solid gray;
               }
                   QPushButton:hover {
                   border: 1px solid gray;
                   background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #f6f7fa, stop: 1 #dadbde);
               }
               QPushButton:pressed {
                   border: 1px solid gray;
                   background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dadbde, stop: 1 #f6f7fa);
               }"""


class Ui_LoginError:
    def setupUi(self, LoginError):
        LoginError.setObjectName("LoginError")
        LoginError.setFixedSize(500, 200)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(LoginError.sizePolicy().hasHeightForWidth())
        LoginError.setSizePolicy(sizePolicy)
        self.gridLayout = QtWidgets.QGridLayout(LoginError)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(LoginError)
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label = QtWidgets.QLabel(LoginError)
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btn_Ok = QtWidgets.QPushButton(LoginError)
        self.btn_Ok.setMinimumSize(QtCore.QSize(100, 26))
        self.btn_Ok.setMaximumSize(QtCore.QSize(100, 26))
        self.btn_Ok.setStyleSheet(btn_style)
        self.btn_Ok.setDefault(True)
        self.btn_Ok.setObjectName("btnOk")
        self.horizontalLayout.addWidget(self.btn_Ok)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(LoginError)
        QtCore.QMetaObject.connectSlotsByName(LoginError)

    def retranslateUi(self, LoginError):
        _translate = QtCore.QCoreApplication.translate
        LoginError.setWindowTitle(_translate("LoginError", "WorkTimer"))
        self.label_2.setText(_translate("LoginError", "Error while logging in !!!"))
        self.label.setText(_translate("LoginError", "Message"))
        self.btn_Ok.setText(_translate("LoginError", "Ok"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LoginError = QtWidgets.QDialog()
    ui = Ui_LoginError()
    ui.setupUi(LoginError)
    LoginError.show()
    sys.exit(app.exec_())