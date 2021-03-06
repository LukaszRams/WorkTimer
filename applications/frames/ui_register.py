# -*- coding: utf-8 -*-

# Register implementation generated from reading ui file 'register.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


lineedit_style = """QLineEdit{
                        border: 1px solid gray;
                        border-radius: 13px;
                        padding: 0 10px;
                        selection-background-color: darkgray;
                        font: 10pt \"Segoe Print\";
                    }
                    QLineEdit:hover{
                        border: 2px solid blue;
                    }
                    QLineEdit:focus{
                        border: 1px solid blue;
                    }
                    QToolTip { background-color: qlineargradient(x1: 0.5, y1: 0.5, x2: 1, y2: 1, stop: 0 #dadbde, stop: 1 #f6f7fa);
                        color: black; 
                        border: 1px solid gray;
                        border-radius: 4px;
                    }"""

btn_style = """QPushButton {
                    border: 1px solid gray;
                    border-radius: 15px;
                    font: 10pt \"Segoe Print\";
                    background-color: qlineargradient(x1: 0.5, y1: 0.5, x2: 1, y2: 1, stop: 0 #dadbde, stop: 1 #f6f7fa);
                }
                QPushButton:hover {
                    border: 1px solid gray;
                    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #f6f7fa, stop: 1 #dadbde);
                }
                QPushButton:pressed {
                    border: 1px solid gray;
                    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dadbde, stop: 1 #f6f7fa);
                }"""

ComboBox_style = """QComboBox {
                        border: 1px solid gray;
                        border-top-left-radius: 13px;
                        border-bottom-left-radius: 0px;
                        border-top-right-radius: 0px;
                        border-bottom-right-radius: 0px;
                        padding: 0 20px;
                        font: 10pt \"Segoe Print\";
                    }
                    QComboBox:hover{
                        border: 2px solid blue;
                    }
                    QComboBox:focus{
                        border: 1px solid blue;
                    }
                    QComboBox:on {
                        padding-top: 3px;
                        padding-left: 4px;
                    }"""


class Ui_Register:
    def setupUi(self, Register):
        Register.setObjectName("Register")
        Register.setFixedSize(653, 478)
        self.RegisterLayout = QtWidgets.QFormLayout(Register)
        self.RegisterLayout.setObjectName("RegisterLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(-1, 20, -1, -1)
        self.verticalLayout_3.setSpacing(15)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Back = QtWidgets.QPushButton(Register)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Back.sizePolicy().hasHeightForWidth())
        self.Back.setSizePolicy(sizePolicy)
        self.Back.setMinimumSize(QtCore.QSize(100, 30))
        self.Back.setMaximumSize(QtCore.QSize(100, 30))
        self.Back.setStyleSheet(btn_style)
        self.Back.setObjectName("Back")
        self.horizontalLayout.addWidget(self.Back)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label = QtWidgets.QLabel(Register)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.Register = QtWidgets.QPushButton(Register)
        self.Register.setMinimumSize(QtCore.QSize(150, 30))
        self.Register.setMaximumSize(QtCore.QSize(150, 30))
        self.Register.setStyleSheet(btn_style)
        self.Register.setObjectName("Register")
        self.horizontalLayout.addWidget(self.Register)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(50, 0, 50, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.show_info = QtWidgets.QLabel(Register)
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(10)
        self.show_info.setFont(font)
        self.show_info.setText("")
        self.show_info.setObjectName("show_info")
        self.show_info.setMinimumSize(500, 100)
        self.show_info.setMaximumSize(500, 100)
        self.horizontalLayout_2.addWidget(self.show_info)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(50, 0, 100, -1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.first_name = QtWidgets.QLabel(Register)
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.first_name.setFont(font)
        self.first_name.setObjectName("first_name")
        self.horizontalLayout_3.addWidget(self.first_name)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.l_first_name = QtWidgets.QLineEdit(Register)
        self.l_first_name.setMinimumSize(QtCore.QSize(200, 26))
        self.l_first_name.setMaximumSize(QtCore.QSize(200, 26))
        self.l_first_name.setStyleSheet(lineedit_style)
        self.l_first_name.setObjectName("l_first_name")
        self.horizontalLayout_3.addWidget(self.l_first_name)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(50, -1, 100, -1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.surname = QtWidgets.QLabel(Register)
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.surname.setFont(font)
        self.surname.setObjectName("surname")
        self.horizontalLayout_4.addWidget(self.surname)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.l_surname = QtWidgets.QLineEdit(Register)
        self.l_surname.setMinimumSize(QtCore.QSize(200, 26))
        self.l_surname.setMaximumSize(QtCore.QSize(200, 26))
        self.l_surname.setStyleSheet(lineedit_style)
        self.l_surname.setObjectName("l_surname")
        self.horizontalLayout_4.addWidget(self.l_surname)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(50, -1, 100, -1)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.username = QtWidgets.QLabel(Register)
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.username.setFont(font)
        self.username.setObjectName("username")
        self.horizontalLayout_5.addWidget(self.username)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem4)
        self.l_username = QtWidgets.QLineEdit(Register)
        self.l_username.setMinimumSize(QtCore.QSize(200, 26))
        self.l_username.setMaximumSize(QtCore.QSize(200, 26))
        self.l_username.setStyleSheet(lineedit_style)
        self.l_username.setObjectName("l_username")
        self.horizontalLayout_5.addWidget(self.l_username)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setContentsMargins(50, 0, 100, -1)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.pwd = QtWidgets.QLabel(Register)
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pwd.setFont(font)
        self.pwd.setObjectName("pwd")
        self.horizontalLayout_6.addWidget(self.pwd)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem5)
        self.l_password = QtWidgets.QLineEdit(Register)
        self.l_password.setMinimumSize(QtCore.QSize(200, 26))
        self.l_password.setMaximumSize(QtCore.QSize(200, 26))
        self.l_password.setStyleSheet(lineedit_style)
        self.l_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.l_password.setObjectName("l_password")
        self.horizontalLayout_6.addWidget(self.l_password)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setContentsMargins(50, -1, 100, -1)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.re_pwd = QtWidgets.QLabel(Register)
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.re_pwd.setFont(font)
        self.re_pwd.setObjectName("re_pwd")
        self.horizontalLayout_7.addWidget(self.re_pwd)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem6)
        self.l_re_password = QtWidgets.QLineEdit(Register)
        self.l_re_password.setMinimumSize(QtCore.QSize(200, 26))
        self.l_re_password.setMaximumSize(QtCore.QSize(200, 26))
        self.l_re_password.setStyleSheet(lineedit_style)
        self.l_re_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.l_re_password.setObjectName("l_re_password")
        self.horizontalLayout_7.addWidget(self.l_re_password)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setContentsMargins(50, -1, 100, -1)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.priority = QtWidgets.QLabel(Register)
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.priority.setFont(font)
        self.priority.setObjectName("priority")
        self.horizontalLayout_8.addWidget(self.priority)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem7)
        self.l_priority = QtWidgets.QComboBox(Register)
        self.l_priority.setMinimumSize(QtCore.QSize(150, 26))
        self.l_priority.setMaximumSize(QtCore.QSize(150, 26))
        self.l_priority.setStyleSheet(ComboBox_style)
        self.l_priority.setObjectName("l_priority")
        self.l_priority.addItem("")
        self.l_priority.addItem("")
        self.horizontalLayout_8.addWidget(self.l_priority)
        self.verticalLayout_3.addLayout(self.horizontalLayout_8)
        self.RegisterLayout.setLayout(0, QtWidgets.QFormLayout.SpanningRole, self.verticalLayout_3)

        self.retranslateUi(Register)
        QtCore.QMetaObject.connectSlotsByName(Register)

    def retranslateUi(self, Register):
        _translate = QtCore.QCoreApplication.translate
        Register.setWindowTitle(_translate("Register", "WorkTimer"))
        self.Back.setText(_translate("Register", "Back"))
        self.label.setText(_translate("Register", "REGISTER USER"))
        self.Register.setText(_translate("Register", "Register"))
        self.first_name.setText(_translate("Register", "FIRST NAME"))
        self.l_first_name.setPlaceholderText(_translate("Register", "Enter your firstname"))
        self.surname.setText(_translate("Register", "SURNAME"))
        self.l_surname.setPlaceholderText(_translate("Register", "Enter your surname"))
        self.username.setText(_translate("Register", "USERNAME"))
        self.l_username.setToolTip(_translate("Register", "The user name must start with a letter \n"
                                                          "and may only consist of letters,\n"
                                                          "numbers and an underscore character.\n"
                                                          "Letters are case-sensitive\n"
                                                          "The minimum length is four characters"))
        self.l_username.setPlaceholderText(_translate("Register", "Enter your username"))
        self.pwd.setText(_translate("Register", "PASSWORD"))
        self.l_password.setToolTip(_translate("Register", "The password must contain at least one lowercase letter,\n"
                                                          "a capital letter, a number, a special character (!@#$%^&*?)\n"
                                                          "and must have at least 8 characters"))
        self.l_password.setPlaceholderText(_translate("Register", "Enter your password"))
        self.re_pwd.setText(_translate("Register", "RETYPE PASSWORD"))
        self.l_re_password.setToolTip(
            _translate("Register", "The password must contain at least one lowercase letter,\n"
                                   "a capital letter, a number, a special character (!@#$%^&*?)\n"
                                   "and must have at least 8 characters"))
        self.l_re_password.setPlaceholderText(_translate("Register", "Retype your password"))
        self.priority.setText(_translate("Register", "PRIORITY"))
        self.l_priority.setCurrentText(_translate("Register", "user"))
        self.l_priority.setItemText(0, _translate("Register", "user"))
        self.l_priority.setItemText(1, _translate("Register", "admin"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Register = QtWidgets.QWidget()
    ui = Ui_Register()
    ui.setupUi(Register)
    Register.show()
    sys.exit(app.exec_())
