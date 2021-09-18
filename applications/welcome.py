#!/usr/bin/python
# -*- coding: utf-8 -*-
from .database.connect import database
from .settings import settings
from .frames.ui_welcome import Ui_WelcomeFrame
from PyQt5.QtWidgets import QMainWindow, QDialog
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
        self.ui.signin_btn.clicked.connect(self.slot_sign_in)

    def slot_login(self):
        """
        Opens the login window closing the welcome window
        :return:
        """
        logging.info("Login selected")
        from applications.login import Login
        settings.first_run = False
        self.login = Login(parent=self)
        self.hide()
        if self.login.exec_() == QDialog.Accepted:
            # TODO: Menu window
            print("accepted")
            # self.menu = Menu()
            # self.menu.show()

    def slot_sign_in(self):
        """
        Opens the registration window by closing the welcome window
        :return:
        """
        logging.info("Sign in selected")
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

