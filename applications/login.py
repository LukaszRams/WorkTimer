#!/usr/bin/python
# -*- coding: utf-8 -*-
from applications.frames.ui_login import Ui_Login
from applications.frames.ui_login_error import Ui_LoginError
from PyQt5.QtWidgets import QDialog, QLineEdit
from PyQt5.QtGui import QCloseEvent
from applications.database.connect import database
from applications.settings import settings
import logging


class Login(QDialog):
    def __init__(self, parent):
        super().__init__()
        self.ui = Ui_Login()
        self.ui.setupUi(self)
        self.parent = parent
        self.ui.Login_btn.clicked.connect(self.slot_try_login)
        self.ui.Back_btn.clicked.connect(self.slot_back)
        self.ui.check_password.pressed.connect(self.slot_show_password)
        self.ui.check_password.released.connect(self.slot_hide_password)

    def closeEvent(self, a0: QCloseEvent) -> None:
        """
        Close dialog and show parent window
        :param a0:
        :return:
        """
        logging.debug("Close event")
        self.parent.show()
        self.hide()


    def slot_show_password(self):
        """
        Shows the password when pressed
        :return:
        """
        self.ui.l_password.setEchoMode(QLineEdit.Normal)

    def slot_hide_password(self):
        """
        Hide the password when released
        :return:
        """
        self.ui.l_password.setEchoMode(QLineEdit.Password)

    def slot_back(self):
        """
        Classic operation of the back button
        :return:
        """
        logging.debug("Back button clicked")
        self.parent.show()
        self.hide()

    def slot_try_login(self):
        """
        Checks that the login and password are correct. If yes, the user data is saved to the
        settings. Otherwise it displays an error message
        :return:
        """
        data = self.check_user()
        if data:
            if self.ui.l_password.text() == data[3]:
                settings.update_user_setting(["username", "first_name", "surname", "priority"], [*data[0:3], data[4]])
                settings.load_plugins(settings.user["priority"])
                self.accept()
                logging.info("The user has been logged in")
                database.create_other_databases()
            else:
                logging.debug("Incorrect password")
                LoginError = QDialog()
                ui = Ui_LoginError()
                ui.setupUi(LoginError)
                ui.btn_Ok.clicked.connect(LoginError.accept)
                ui.label.setText("Verify correctness of password")
                LoginError.exec_()
        else:
            logging.debug("Incorrect login")
            LoginError = QDialog()
            ui = Ui_LoginError()
            ui.setupUi(LoginError)
            ui.btn_Ok.clicked.connect(LoginError.accept)
            ui.label.setText("Verify correctness of user name")
            LoginError.exec_()

    def check_user(self):
        """
        Checks if the user exists and returns his data
        :return:
        """
        user = self.ui.l_login.text()
        query = f'SELECT * from {settings.users_table} where user == \"{user}\"'
        data = database.get_record(query)
        return data[0] if data else None