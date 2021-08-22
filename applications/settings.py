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
        logging.info("Initialisation of settings")
        self.db_path = os.path.join(os.path.abspath(os.getcwd()), "application\\database\\WorkTimer.db")


settings = Settings()
