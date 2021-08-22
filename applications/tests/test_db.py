#!/usr/bin/python
# -*- coding: utf-8 -*-

from applications.database.connect import database
import os




def test_create_db():
    database.create_table(table_name="test", firstname=("text", "PRIMARY KEY"),
                          lastname=("text", "NOT NULL"), password=("text",),
                          priority=("integer", "NOT NULL"))
    # checking whether a database has been created
    path = os.path.join(os.getcwd(), "WorkTimer.db")
    assert os.path.isfile(path)
    query = """SELECT name FROM sqlite_master WHERE type='table'
            AND name='test';"""

    # check whether a table has been created
    table = database.cursor.execute(query).fetchall()
    assert not 0 == len(table)


def test_add_record_and_get_record():
    database.create_table(table_name="test", firstname=("text", "PRIMARY KEY"),
                          lastname=("text", "NOT NULL"), password=("text",),
                          priority=("integer", "NOT NULL"))
    count_query = """SELECT count(*) FROM test"""
    assert 0 == database.get_record(count_query)[0][0]
    database.add_record("FN_1", "LN_1", "", "High", table_name="test")
    database.add_record("FN_2", "LN_1", "", "High", table_name="test")
    assert 2 == database.get_record(count_query)[0][0]
    rows = database.get_record("""SELECT * FROM test""")
    assert rows[0] == ("FN_1", "LN_1", "", "High")
    assert rows[1] == ("FN_2", "LN_1", "", "High")
    del_database()


def del_database():
    """
    deleting the database (the connection has to be terminated first)
    :return:
    """
    path = os.path.join(os.getcwd(), "WorkTimer.db")
    database.connection.close()
    os.system(f"del /f {path}")