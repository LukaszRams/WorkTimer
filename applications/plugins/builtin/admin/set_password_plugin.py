#!/usr/bin/python
# -*- coding: utf-8 -*-
from .ui_auto_gui import Ui_AutoGui
import logging
from applications.database.connect import database
from PyQt5.QtWidgets import QDialog, QLineEdit
from PyQt5.QtGui import QCloseEvent
from applications.settings import settings
import re


class Plugin(QDialog):
    DISPLAY_NAME = "Set password"
    DESCRIPTION = "Sets the password for a given user"
    INSTRUCTION = "Select a username and enter a password. \nIf a user with this name exists, \nthe password will be changed."

    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.ui = Ui_AutoGui()
        self.ui.setupUi(self)
        self.btn_back, self.btn_accept = self.ui.add_header("SET PASSWORD")
        self.btn_back.clicked.connect(self.slot_back)
        self.btn_accept.clicked.connect(self.slot_accept)
        self.label = self.ui.add_info_label()
        self.ui.add_spacer_item()
        self.username = self.ui.add_lineedit("Username")
        self.new_password = self.ui.add_lineedit("New password")
        self.new_password.setEchoMode(QLineEdit.Password)
        self.retype_password = self.ui.add_lineedit("Retype password")
        self.retype_password.setEchoMode(QLineEdit.Password)
        self.ui.add_spacer_item()

    def slot_back(self):
        """
        Classic operation of the back button
        :return:
        """
        logging.debug("Back button clicked")
        self.parent.show()
        self.hide()

    def closeEvent(self, a0: QCloseEvent) -> None:
        """
        Close dialog and show parent
        :param a0:
        :return:
        """
        logging.info("Close event")
        self.parent.show()
        self.hide()

    def slot_accept(self):
        """
        Checks if the user exists, validates the password and displays an appropriate message
        :return:
        """
        if self.check_user():
            pwd, status = self.check_password()
            if pwd:
                self.update_password()
                status = "The password has been set up"
                self.label.setText(status)
                self.label.setStyleSheet("""color: green;
                                            font: 14pt \"Segoe Print\"; 
                                            min-width: 100; 
                                            max-width: 400; 
                                            min-height: 30; 
                                            max-height: 30""")
        else:
            status = "The user with the specified name does not exist"
            self.label.setStyleSheet("""color: black;
                                        font: 12pt \"Segoe Print\"; 
                                        min-width: 100; 
                                        max-width: 400; 
                                        min-height: 30; 
                                        max-height: 30""")
            self.label.setText(status)

    def check_password(self):
        """
        The function expects the password to be entered twice and checks whether it contains a lowercase letter,
        an uppercase letter, a symbol (!@#$%^&*?), a number and at least eight characters
        :return:
        """
        pwd, re_pwd = self.new_password.text(), self.retype_password.text()
        if pwd != re_pwd:
            return None, "Passwords are diferent"
        elif len(pwd) < 8:
            return None, "Password is too short"
        elif not re.findall(r"[A-Z]+", pwd):
            return None, "Password should contain upper letter"
        elif not re.findall(r"[a-z]+", pwd):
            return None, "Password should contain lower letter"
        elif not re.findall(r"\d+", pwd):
            return None, "Password should contain number"
        elif not re.findall(r"[!@#$%^&*?]+", pwd):
            return None, "Password should contain special character"
        return pwd, ""

    def check_user(self):
        """
        Checks whether a particular user exists
        :return:
        """
        return len(database.get_record(f'''SELECT * FROM {settings.users_table} WHERE username == "{self.username.text()}"'''))

    def update_password(self):
        """
        Sets a password for the user
        :return:
        """
        database.update(f"""UPDATE {settings.users_table} SET password==\"{self.new_password.text()}\" WHERE username==\"{self.username.text()}\"""")
