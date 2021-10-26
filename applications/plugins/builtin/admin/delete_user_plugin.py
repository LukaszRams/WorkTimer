#!/usr/bin/python
# -*- coding: utf-8 -*-
from .ui_auto_gui import Ui_AutoGui
import logging
from applications.database.connect import database
from PyQt5.QtWidgets import QDialog
from PyQt5.QtGui import QCloseEvent, QKeyEvent
from PyQt5.QtCore import Qt
from applications.settings import settings
from .ask_dialog import Ui_AskDialog
import re


class Plugin(QDialog):
    DISPLAY_NAME = "Delete user"
    DESCRIPTION = "Deletes the user and his data"
    INSTRUCTION = "Enter the name of the user you want to delete. \nNOTE You cannot delete yourself"

    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.ui = Ui_AutoGui()
        self.ui.setupUi(self)
        self.btn_back, self.btn_accept = self.ui.add_header("DELETE USER")
        self.btn_back.clicked.connect(self.slot_back)
        self.btn_accept.clicked.connect(self.slot_accept)
        self.label = self.ui.add_info_label()
        self.ui.add_spacer_item()
        self.username = self.ui.add_lineedit("Username")
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

    def keyPressEvent(self, a0: QKeyEvent) -> None:
        if a0.key() == Qt.Key.Key_Return:
            return
        QDialog.keyPressEvent(self, a0)

    def slot_accept(self):
        """
        Checks if the user exists, validates the password and displays an appropriate message
        :return:
        """
        if self.username.text() == settings.user["username"]:
            status = ("You cannot remove yourself", "Negative")
        elif not self.username.text():
            status = ("You must enter a username", "Negative")
        elif self.check_user():
            logging.debug("Ask for logout")
            Ask = QDialog()
            ui = Ui_AskDialog()
            ui.setupUi(Ask, "User deletion", f"Are you sure you want to delete the user \"{self.username.text()}\"")
            ui.btn_Ok.clicked.connect(Ask.accept)
            ui.btn_cancel.clicked.connect(lambda: self._hide(Ask))
            if Ask.exec_() == QDialog.Accepted:
                database.update(f"""DELETE FROM DETAILED_WORKING_TIME WHERE user = \'{self.username.text()}\'""")
                database.update(f"""DELETE FROM USERS WHERE user = \'{self.username.text()}\'""")
                database.update(f"""DELETE FROM WORKING_TIME WHERE user = \'{self.username.text()}\'""")

                status = (f"User \"{self.username.text()}\" has been deleted", "Positive")
                logging.info(f"User \"{self.username.text()}\" has been deleted")
            else:
                status = ("Deletion of a user has been cancelled", "Negative")
        else:
            status = ("This user does not exist", "Negative")
        self.show_status(*status)

    def show_status(self, status, type):
        """
        Show status in label
        :param status:
        :param type:
        :return:
        """
        if type == "Positive":
            self.label.setStyleSheet("""color: green;
                                        font: 12pt \"Segoe Print\"; """)
        else:
            self.label.setStyleSheet("""color: black;
                                        font: 12pt \"Segoe Print\"; """)
        self.label.setText(status)


    def _hide(self, window):
        logging.debug("Logout cenceled")
        window.hide()

    def check_user(self):
        """
        Checks whether a particular user exists
        :return:
        """
        return len(database.get_record(f'''SELECT * FROM {settings.users_table} WHERE user == "{self.username.text()}"'''))
