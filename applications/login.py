#!/usr/bin/python
# -*- coding: utf-8 -*-
from applications.frames.ui_login import Ui_Login
from PyQt5.QtWidgets import QDialog, QErrorMessage, QMessageBox
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
                settings.update_user_setting(["username", "first_name", "surname", "priority"], [*data[:3], data[4]])
                self.accept()
                logging.info("The user has been logged in")
            else:
                logging.debug("Incorrect password")
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText("Password is incorect")
                msg.setInformativeText("Verify the correct password")
                msg.setWindowTitle("Error")
                msg.exec_()
        else:
            logging.debug("Incorrect login")
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("User name is incorect")
            msg.setInformativeText("Verify the correct user name")
            msg.setWindowTitle("Error")
            msg.exec_()

    def check_user(self):
        """
        Checks if the user exists and returns his data
        :return:
        """
        user = self.ui.l_login.text()
        query = f'SELECT * from {settings.users_table} where username == \"{user}\"'
        data = database.get_record(query)
        return data[0] if data else None