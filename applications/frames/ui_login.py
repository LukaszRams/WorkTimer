# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
from PyQt5 import QtCore, QtWidgets, QtGui
import os


btn_style = """QPushButton {
                    border: 1px solid gray;
                    border-radius: 13px;
                    font: 10pt \"Segoe Print\";
                    background-color: qlineargradient(x1: 0.5, y1: 0.5, x2: 1, y2: 1,
                                                      stop: 0 #dadbde, stop: 1 #f6f7fa);
                }
                QPushButton:default {
                    border: 2px solid gray;
                }
                QPushButton:hover {
                    border: 1px solid gray;
                    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                                      stop: 0 #f6f7fa, stop: 1 #dadbde);
                }
                QPushButton:pressed {
                    border: 1px solid gray;
                    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                                      stop: 0 #dadbde, stop: 1 #f6f7fa);
                }"""

le_style = """QLineEdit{
                    border: 1px solid gray;
                    border-radius: 15px;
                    padding: 0 15px;
                    font: 12pt \"Segoe Print\";
                    selection-background-color: darkgray;
              }
              QLineEdit:hover{
                    border: 2px solid blue;
              }
              QLineEdit:focus{
                    border: 1px solid blue;
              }"""

show_password_style = """QPushButton {
                            border: none;
                            border-radius: 15px;
                        }
                        QPushButton:hover {
                            background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                                              stop: 0 #f6f7fa, stop: 1 #dadbde);
                        }
                        QPushButton:pressed {
                            background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                                              stop: 0 #dadbde, stop: 1 #f6f7fa);
                        }"""


class Ui_Login:
    def setupUi(self, Login):
        Login.setObjectName("Login")
        Login.setFixedSize(653, 478)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Login.sizePolicy().hasHeightForWidth())
        Login.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(40)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.NoAntialias)
        self.worktimer_label = QtWidgets.QLabel(Login)
        self.worktimer_label.setFont(font)
        self.worktimer_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter | QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.worktimer_label.setObjectName("worktimer_label")
        self.worktimer_label.setMaximumSize(300, 100)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.horizontalLayout_2.setContentsMargins(100, -1, 100, -1)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_2.addWidget(self.worktimer_label)
        self.gridLayout_2 = QtWidgets.QGridLayout(Login)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(20, 0, 20, 100)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.horizontalLayout_3.setContentsMargins(100, -1, 100, -1)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.l_login = QtWidgets.QLineEdit(Login)
        self.l_login.setMinimumSize(QtCore.QSize(300, 30))
        self.l_login.setMaximumSize(QtCore.QSize(300, 30))
        self.l_login.setObjectName("l_login")
        self.l_login.setStyleSheet(le_style)
        self.l_login.setPlaceholderText("Enter your login")
        self.horizontalLayout_3.addWidget(self.l_login)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.gridLayout.addLayout(self.horizontalLayout_3, 1, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(100, -1, 70, -1)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.l_password = QtWidgets.QLineEdit(Login)
        self.l_password.setMinimumSize(QtCore.QSize(300, 30))
        self.l_password.setMaximumSize(QtCore.QSize(300, 30))
        self.l_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.l_password.setObjectName("l_password")
        self.l_password.setStyleSheet(le_style)
        self.l_password.setPlaceholderText("Enter your password")
        self.check_password = QtWidgets.QPushButton(Login)
        self.check_password.setMaximumSize(30, 30)
        self.check_password.setMinimumSize(30, 30)
        self.check_password.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.check_password.setIcon(QtGui.QIcon(os.path.join(os.getcwd(), "res", "icons", "show_password.ico")))
        self.check_password.setStyleSheet(show_password_style)
        self.horizontalLayout_4.addWidget(self.l_password)
        self.horizontalLayout_4.addWidget(self.check_password)
        self.check_password.setToolTip("Show password")
        self.gridLayout.addLayout(self.horizontalLayout_4, 2, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(200, 0, 100, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Back_btn = QtWidgets.QPushButton(Login)
        self.Back_btn.setObjectName("Back_btn")
        self.Back_btn.setMinimumSize(100, 26)
        self.Back_btn.setMaximumSize(100, 26)
        self.Back_btn.setStyleSheet(btn_style)
        self.horizontalLayout.addWidget(self.Back_btn)
        self.Login_btn = QtWidgets.QPushButton(Login)
        self.Login_btn.setDefault(True)
        self.Login_btn.setFlat(False)
        self.Login_btn.setObjectName("Login_btn")
        self.Login_btn.setMinimumSize(100, 26)
        self.Login_btn.setMaximumSize(100, 26)
        self.Login_btn.setStyleSheet(btn_style)
        self.horizontalLayout.addWidget(self.Login_btn)
        self.gridLayout.addLayout(self.horizontalLayout, 3, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "WorkTimer"))
        self.worktimer_label.setText(_translate("Login", "WorkTimer"))
        self.Back_btn.setText(_translate("Login", "Back"))
        self.Login_btn.setText(_translate("Login", "Login"))
        self.check_password.setText((_translate("Login", "")))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Login = QtWidgets.QDialog()
    ui = Ui_Login()
    ui.setupUi(Login)
    Login.show()
    sys.exit(app.exec_())
