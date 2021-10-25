#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
This file will store the data for the database queries that will be called to create the database
"""


#  Table of how many hours an employee should work per month
class Monthly_working_time:
    table_name = "MONTHLY_WORKING_TIME"
    data = {
        "id": ("integer", "PRIMARY KEY"),
        "year": ("integer", "NOT NULL"),
        "month": ("text", "NOT NULL"),
        "hours": ("integer", "NOT NULL")
    }


#  A table that will contain data on the time worked by the employee during the month
class Working_time:
    table_name = "WORKING_TIME"
    data = {
        "id": ("integer", "PRIMARY KEY"),
        "user": ("text", "NOT NULL"),
        "year": ("YEAR", "NOT NULL"),
        "month": ("text", "NOT NULL"),
        "total_hours": ("integer", "NOT NULL"),  # number of hours worked by the employee
        "base_hours": ("integer", "NOT NULL"),  # the number of hours the employee was to work
        "overtime_hours": ("integer", "NOT NULL"),  # number of overtime hours
    }


#  Detailed data from employees' work, the amount of data grows very quickly so it needs to be cleaned
class Detailed_working_time:
    table_name = "DETAILED_WORKING_TIME"
    data = {
        "id": ("integer", "PRIMARY KEY"),
        "user": ("text", "NOT NULL"),
        "date": ("DATE", "NOT NULL"),  # detailed_working_time
        "start_at": ("TIME", "NOT NULL"),  # start time
        "end_at": ("TIME", "NOT NULL"),  # end time
    }



tables = [Monthly_working_time, Working_time, Detailed_working_time]
