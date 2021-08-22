#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3
from sqlite3 import Error
import logging
from settings import settings


class Database:
    """
    Class responsible for creating a connection to the database
    """
    def __init__(self):
        try:
            self.connection = sqlite3.connect(settings.db_path)
            logging.info("Connection to database created")
        except Error as e:
            logging.error(e)
        self.cursor = self.connection.cursor()

    def __del__(self):
        self.connection.close()
        logging.debug("Connection to database end")

    def create_table(self, table_name, *args, **kwargs):
        pass