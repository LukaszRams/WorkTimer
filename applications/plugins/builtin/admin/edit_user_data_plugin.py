#!/usr/bin/python
# -*- coding: utf-8 -*-
from .ui_auto_gui import Ui_AutoGui
import logging
from applications.database.connect import database
from PyQt5.QtWidgets import QDialog
from PyQt5.QtGui import QCloseEvent
from applications.settings import settings
import re


class Plugin(QDialog):
    DISPLAY_NAME = "Edit user data"
    DESCRIPTION = "Changes user data such as first name, last name, priority"
    INSTRUCTION = "Enter your username and the data you want to change"

    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.ui = Ui_AutoGui()
        self.ui.setupUi(self)
        self.btn_back, self.btn_accept = self.ui.add_header("EDIT USER DATA")
        self.btn_back.clicked.connect(self.slot_back)
        self.btn_accept.clicked.connect(self.slot_accept)
        self.label = self.ui.add_info_label()
        self.ui.add_spacer_item()
        self.username = self.ui.add_lineedit("Username")
        self.ui.add_spacer_item()
        self.first_name = self.ui.add_lineedit("First name")
        self.surname = self.ui.add_lineedit("Surname")
        self.priority = self.ui.add_comboboxes("Priority", ["user", "admin"])
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
            columns, data, result = self.get_data()
            if result:
                status = result
            else:
                if columns:
                    self.update_user(columns, data)
                    status = "User has been updated"
                    self.label.setText(status)
                    self.label.setStyleSheet("""color: green;
                                                font: 14pt \"Segoe Print\"; 
                                                min-width: 100; 
                                                max-width: 400; 
                                                min-height: 30; 
                                                max-height: 30""")
                else:
                    status = "You must enter the data for the update"
        else:
            status = "The user with the specified name does not exist"
        self.label.setStyleSheet("""color: black;
                                                font: 12pt \"Segoe Print\"; 
                                                min-width: 100; 
                                                max-width: 400; 
                                                min-height: 30; 
                                                max-height: 30""")
        self.label.setText(status)

    def get_data(self):
        """
        Retrieves the data entered and returns the list of
        columns to be updated and the data to be updated with
        :return:
        """
        columns, data = [], []
        result = ""
        if self.first_name.text():
            result += self.check_first_name(self.first_name.text())
            columns.append("first_name")
            data.append(self.first_name.text())
        if self.surname.text():
            result += self.check_surname(self.surname.text())
            columns.append("surname")
            data.append(self.surname.text())
        if self.priority.currentText():
            columns.append("priority")
            data.append(self.priority.currentText())
        return columns, data, result

    def check_user(self):
        """
        Checks whether a particular user exists
        :return:
        """
        return len(database.get_record(f'''SELECT * FROM {settings.users_table} WHERE username == "{self.username.text()}"'''))

    def update_user(self, cols, vals):
        """
        Updates user data
        :param cols: columns to update
        :param vals: values for columns
        :return:
        """
        database.update(f"""UPDATE {settings.users_table} SET {" = '%s', ".join([col for col in cols])}= \'%s\' WHERE username == \'{self.username.text()}\'""" % tuple(vals))

    def check_first_name(self, first_name):
        """
        First name may be given as first name only or first and second name
        :param first_name
        :return:
        """
        parts = first_name.split(" ")
        result = self._check_parts(parts)
        if result:
            return f"First name is incorrect, {result}"
        return ""

    def check_surname(self, surname):
        """
        The surname must consist of letters only or letters and a hyphen followed by a capital letter,
        the minimum length of the last name is two characters e.g. "Ul"
        :param surname:
        :return:
        """
        parts = surname.split("-")
        result = self._check_parts(parts)
        if result:
            return f"Surname is incorrect, {result}"
        return ""

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