#!/usr/bin/python
# -*- coding: utf-8 -*-
import logging
import os


def list_plugins(path, tp):
    """
    Returns a list of valid plug-ins
    :param path:
    :param tp:
    :return:
    """
    try:
        rel_path = os.path.join(path[path.index("applications"):], tp)
        names = [file.split(".")[0] for file in os.listdir(os.path.join(path, tp)) if file.split(".")[0].endswith("plugin")]
        import importlib
        return [importlib.import_module(".".join(rel_path.split("\\")) + "." + name) for name in names]
    except WindowsError as error:
        if error.winerror == 3:
            logging.error("Current path not exist \'%s\'" % os.path.join(path, tp))
        else:
            import traceback
            logging.error("Unforeseen function error: \n%s" % traceback.format_exc())


class Settings:
    """
    Managing and storing application settings
    TODO: Better way to save settings e.g.: system registers or configuration file
    """

    def __init__(self):
        self.db_path = os.path.join(os.getenv("LocalAppData"), "WorkTimer\\Worktimer.db")
        self.users_table = "USERS"
        self.log_level = logging.DEBUG


    def initialize_client_settings(self):
        """
        Initializes client settings
        :return:
        """
        self.first_run = False

        # Lists of basic user and administrator plug-ins
        self.user_builtin_plugins = []
        self.admin_builtin_plugins = []

        # Lists of additional user and administrator plug-ins
        self.user_installed_plugins = []
        self.admin_installed_plugins = []

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

    def load_plugins(self, user_type):
        """
        Loads application plug-ins based on user type
        :param user_type: admin or user
        :return:
        """
        logging.info("Loading basic plugins")
        self._load_plugins("builtin", user_type)
        logging.info("Loading additional plugins")
        self._load_plugins("installed", user_type)

    def _load_plugins(self, plugin_type, user_type):
        """
        Loads the selected plugin type for the selected user type
        :param plugin_type: builtin or installed
        :param user_type: admin or user
        :return:
        """
        path = os.path.join(os.getcwd(), "plugins", plugin_type)
        # The name of the plug-in must look like this: name_plugin e.g. screenlock_plugin
        if plugin_type == "builtin":
            if user_type == "user":
                self.user_builtin_plugins = list_plugins(path, "user")
            else:
                self.user_builtin_plugins = list_plugins(path, "user")
                self.admin_builtin_plugins = list_plugins(path, "admin")
        else:
            if user_type == "user":
                self.user_installed_plugins = list_plugins(path, "user")
            else:
                self.user_installed_plugins = list_plugins(path, "user")
                self.admin_installed_plugins = list_plugins(path, "admin")


settings = Settings()
