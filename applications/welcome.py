#!/usr/bin/python
# -*- coding: utf-8 -*-
from .database.connect import database
from .settings import settings
from .frames.ui_welcome import Ui_WelcomeFrame
from PyQt5.QtWidgets import QMainWindow, QDialog
from PyQt5 import QtGui
import logging


class Welcome(QMainWindow):
    """
    User authentication class
    """
    def __init__(self):
        """
        Initialisation of basic data, such as:
        * username
        * first_name
        * surname
        * priority
        """
        super().__init__()
        self.ui = Ui_WelcomeFrame()
        self.ui.setupUi(self)
        if self.first_run():  # if we have no user
            logging.debug("First run")
            settings.first_run = True
            self.ui.login_btn.setVisible(False)
        self.ui.login_btn.clicked.connect(self.slot_login)
        self.ui.signup_btn.clicked.connect(self.slot_sign_up)

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        """
        Closing the app
        :param a0: event
        :return:
        """
        import sys
        sys.exit()

    def slot_login(self):
        """
        Opens the login window and closing the welcome window.
        If you manage to log in, it displays the menu window
        :return:
        """
        logging.info("Login selected")
        from applications.login import Login
        settings.first_run = False
        self.login = Login(parent=self)
        self.hide()
        if self.login.exec_() == QDialog.Accepted:  # If log in
            from applications.menu import Menu
            self.menu = Menu()
            self.menu.show()
            self.login.hide()
            logging.debug("The menu window is displayed")

    def slot_sign_up(self):
        """
        Opens the registration window by closing the welcome window
        :return:
        """
        logging.info("Sign up selected")
        from applications.register import Register
        self.register = Register(parent=self)
        self.hide()
        self.register.show()

    @staticmethod
    def first_run() -> bool:
        """
        Checks whether there are already any users in the database
        :return:
        """
        query = f"SELECT name FROM sqlite_master WHERE type='table' AND name=\'{settings.users_table}\';"
        # check whether a table has been created
        table = database.cursor.execute(query).fetchall()
        if len(table) == 0:
            return True
        # check if table has records
        return len(database.get_record(f"SELECT * FROM {settings.users_table}")) == 0

welcome = Welcome()

