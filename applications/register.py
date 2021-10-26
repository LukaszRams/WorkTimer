#!/usr/bin/python
# -*- coding: utf-8 -*-
from applications.frames.ui_register import Ui_Register
from PyQt5.QtWidgets import QWidget
from PyQt5 import QtCore, QtGui
from applications.database.connect import database
from applications.settings import settings
import re
import logging


class Register(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.ui = Ui_Register()
        self.ui.setupUi(self)
        self.parent = parent
        if settings.first_run:
            self.ui.l_priority.removeItem(0)
        else:
            if settings.user and settings.user["priority"] != "admin":
                self.ui.l_priority.removeItem(1)
        self.detect_changes()
        self.ui.Register.setDisabled(True)
        self.ui.Back.clicked.connect(self.slot_back)
        self.ui.Register.clicked.connect(self.slot_register_user)

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        """
        Closing the app
        :param a0:
        :return:
        """
        import sys
        sys.exit()

    def detect_changes(self):
        """
        Detects if the data in the form fields have been changed and, if so, activates the registration button
        :return:
        """
        logging.info("Changes have been made to the form fields")
        self.ui.l_username.textChanged.connect(self.slot_activate_register_btn)
        self.ui.l_first_name.textChanged.connect(self.slot_activate_register_btn)
        self.ui.l_surname.textChanged.connect(self.slot_activate_register_btn)
        self.ui.l_password.textChanged.connect(self.slot_activate_register_btn)
        self.ui.l_re_password.textChanged.connect(self.slot_activate_register_btn)
        self.ui.l_priority.currentTextChanged.connect(self.slot_activate_register_btn)

    def slot_activate_register_btn(self):
        """
        Enables the registration button
        :return:
        """
        self.ui.Register.setEnabled(True)

    def slot_back(self):
        """
        Classic operation of the back button
        :return:
        """
        logging.info("Back button clicked")
        if self.parent.first_run():
            self.parent.ui.login_btn.setVisible(False)
        else:
            self.parent.ui.login_btn.setVisible(True)
        self.parent.show()
        self.hide()

    def slot_register_user(self) -> bool:
        """
        Function to create a user account, if there are currently no users an administrator user is created
        """
        status, status_string, data = self.try_register()
        if not status:
            self.ui.show_info.setText(status_string)
            self.ui.show_info.setStyleSheet("color: red;")
            self.ui.show_info.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
            logging.info("Error during user registration: %s" % status_string)
        else:
            self.ui.show_info.setText(status_string)
            self.ui.show_info.setStyleSheet("color: green; font: bold 16pt")
            self.ui.show_info.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
            if settings.first_run:
                database.create_table(table_name=settings.users_table,
                                      data={"user": ("text", "PRIMARY KEY", "NOT NULL"),
                                            "first_name": ("text", "NOT NULL"),
                                            "surname": ("text", "NOT NULL"),
                                            "password": ("text", "NOT NULL"),
                                            "priority": ("integer", "NOT NULL")})

            database.add_record(["user", "first_name", "surname", "password", "priority"], data,
                                table_name=settings.users_table)
            logging.info("New user registered")
        self.ui.Register.setDisabled(True)

    def try_register(self):
        """
        Checks that the data entered is correct. If not it returns "status" False and a message indicating which data
        are incorrect. If the data is correct, returns the "status" True, a message with information about the correct
        registration and the data entered
        :return:
        """
        status_string = ""
        first_name, status = self.check_first_name(self.ui.l_first_name.text())
        status_string += status
        surname, status = self.check_surname(self.ui.l_surname.text())
        status_string += status
        username, status = self.check_username(self.ui.l_username.text())
        status_string += status
        password, status = self.check_password(self.ui.l_password.text(), self.ui.l_re_password.text())
        status_string += status
        priority = self.ui.l_priority.currentText()
        if status_string != "":
            return False, status_string, None
        else:
            return True, "Registration successfully completed", [username, first_name, surname, password, priority]

    def check_username(self, username):
        """
        The user name must start with a letter and may only consist of letters, numbers and an underscore character.
        Letters are case-sensitive. The minimum length is four characters. Also checks if the username is already taken
        :param username:
        :return:
        """
        match = re.findall(r"^[a-zA-Z]+\w+$", username)
        if match and username == match[0] and len(username) >= 4:
            if not settings.first_run:
                query = f"SELECT user FROM {settings.users_table}"
                users = database.get_record(query)
                if username in users[0]:
                    return None, "Your username is taken\n"
            return username, ""
        else:
            return None, "Username is incorrect, check the tip in the input field\n"

    def check_first_name(self, first_name):
        """
        First name may be given as first name only or first and second name
        :param first_name:
        :return:
        """
        parts = first_name.split(" ")
        if parts[0] == "":
            return None, f"First name is required\n"
        result = self._check_parts(parts)
        if result:
            return None, f"First name is incorrect, {result}"
        return first_name, ""

    def check_surname(self, surname):
        """
        The surname must consist of letters only or letters and a hyphen followed by a capital letter,
        the minimum length of the last name is two characters e.g. "Ul"
        :param surname:
        :return:
        """
        parts = surname.split("-")
        if parts[0] == "":
            return None, f"Surname is required\n"
        result = self._check_parts(parts)
        if result:
            return None, f"Surname is incorrect, {result}"
        return surname, ""

    def _check_parts(self, parts):
        """
        Checks whether the parts can be first or last name
        :param parts:
        :return:
        """
        for elem in parts:
            if not elem[0].isupper():
                return f"\"{elem}\" must begin with a capital letter\n"
            elif re.findall(r"\d+", elem):
                return f"\"{elem}\" contains a digit\n"
            elif len(elem) < 2:
                return f"\"{elem}\" is too short\n"
        return None

    def check_password(self, pwd, re_pwd):
        """
        The function expects the password to be entered twice and checks whether it contains a lowercase letter,
        an uppercase letter, a symbol (!@#$%^&*?), a number and at least eight characters
        :param pwd:
        :param re_pwd:
        :return:
        """
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
