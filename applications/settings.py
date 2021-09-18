#!/usr/bin/python
# -*- coding: utf-8 -*-
import logging
import os


class Settings:
    """
    Managing and storing application settings
    TODO: Better way to save settings e.g.: system registers or configuration file
    """

    def __init__(self):
        self.db_path = os.path.join(os.getenv("LocalAppData"), "WorkTimer\\Worktimer.db")
        self.users_table = "USERS"
        self.log_level = logging.DEBUG
        self.user = None
        self.first_run = False

    def initialize_client_settings(self):
        """
        Initializes client settings
        :return:
        """
        logging.basicConfig(level=self.log_level,
                            format='%(asctime)s %(levelname)s  ||file:%(filename)s \tfunc:%(funcName)s \tline:%(lineno)s|| \t%(message)s')
        self.user = {
            "username": None,
            "first_name": None,
            "surname": None,
            "priority": None,
        }

    def update_user_setting(self, setting, value):
        """
        Updates the user setting
        :param setting: setting name
        :param value: setting value
        :return:
        """
        if isinstance(setting, type(value)):
            if isinstance(setting, str):
                self.user[setting] = value
            else:
                for key, val in list(zip(setting, value)):
                    self.user[key] = val
        else:
            logging.error("Incorrect arguments for the function update_user_setting")





settings = Settings()
