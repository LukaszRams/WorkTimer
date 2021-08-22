#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3
from sqlite3 import Error
import logging
from applications.settings import settings


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

    def create_table(self, table_name, **kwargs) -> None:
        """
        Creates a table in the database (if the table with the specified name does not exist).
        Primary key must be add to kwargs
            example:
                create_table(table_name="accounts", id=("integer", "PRIMARY KEY"), firstname=("text", "NOT NULL"),
                            lastname=("text", "NOT NULL"), password=("text", "NOT NULL"), priority=("integer", "NOT NULL"),
                            position=("text",), comments=("text",))
        :param table_name: name of the table to be created
        :param kwargs: column names and Tuple(type, other flags)
        :return: None
        """
        sql_string = f"""CREATE TABLE IF NOT EXISTS {table_name} 
                    ({", ".join([f'{key} {" ".join([elem for elem in val])}' for key, val in kwargs.items()])})"""
        logging.debug("sql string: \n%s" % sql_string)
        try:
            self.cursor.execute(sql_string)
            self.connection.commit()
            logging.info("A table has been created ")
            return True
        except:
            import traceback
            logging.error(traceback.format_exc())

    def add_record(self, *args, table_name) -> None:
        """
        Adds a record to the table and returns an error in case of failure
        :param args: values to be set for specific columns, missing values are marked as "", it is important
                     that the order of values corresponds to the order of columns
        :param table_name: Name of the table
        :return: None
        """
        try:
            self.cursor.execute(f"""INSERT INTO {table_name} VALUES ({", ".join(["?" for _ in args])})""", args)
            self.connection.commit()
            logging.info("Record added ")
            return True
        except:
            import traceback
            logging.error(traceback.format_exc())

    def get_record(self, sql_query):
        """
        Performs a database query and returns the result
        :param sql_query: string representing a database query
        :return: result of the query
        """
        return self.cursor.execute(sql_query).fetchall()


database = Database()

