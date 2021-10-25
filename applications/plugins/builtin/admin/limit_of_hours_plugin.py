#!/usr/bin/python
# -*- coding: utf-8 -*-
from .ui_auto_gui import Ui_AutoGui
import logging
from applications.database.connect import database
from PyQt5.QtWidgets import QDialog, QSpacerItem, QSizePolicy
from PyQt5.QtGui import QCloseEvent, QIntValidator
import datetime


class Plugin(QDialog):
    DISPLAY_NAME = "Monthly working time"
    DESCRIPTION = "Sets or updates the monthly working time"
    INSTRUCTION = "Enter the year, month and number of hours for the month. \nThis data will be the monthly working hours for the employees."

    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.ui = Ui_AutoGui()
        self.ui.setupUi(self)
        self.btn_back, self.btn_accept = self.ui.add_header("Monthly working time")
        self.btn_back.clicked.connect(self.slot_back)
        self.btn_accept.clicked.connect(self.slot_accept)
        self.label = self.ui.add_info_label()
        self.ui.add_spacer_item()
        self.year = self.ui.add_comboboxes("Year", [str(i) for i in range(datetime.datetime.now().year, 1899, -1)])
        self.month = self.ui.add_comboboxes("Month", ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"])
        self.hours = self.ui.add_lineedit("Hours limit")
        self.onlyInt = QIntValidator()
        self.hours.setValidator(self.onlyInt)
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

    def slot_accept(self):
        """
        Updates or add record to database
        :return:
        """
        if self.hours.text():
            data = database.get_record(f"""SELECT * 
                                            FROM MONTHLY_WORKING_TIME 
                                            WHERE (year = {self.year.currentText()})
                                            AND (month = \"{self.month.currentText()}\")""")
            if data:
                logging.debug("Updating working time")
                database.update(f"""UPDATE MONTHLY_WORKING_TIME 
                                    SET hours = {self.hours.text()}
                                    WHERE (year = {self.year.currentText()})
                                    AND (month = \"{self.month.currentText()}\")""")
                status = f"""Update of working hours from {data[0][3]} hours \nto {self.hours.text()} hours for {self.month.currentText()} {self.year.currentText()} successful"""
            else:
                logging.debug("Set working time")
                database.add_record(["year", "month", "hours"], [self.year.currentText(), self.month.currentText(), self.hours.text()], "MONTHLY_WORKING_TIME")
                status = f"""Setting the working time to {self.hours.text()} hours \nfor {self.month.currentText()} {self.year.currentText()} was successful"""
            self.show_status(status, "Positive")
        else:
            status = "You must enter the number of hours"
            self.show_status(status, "Negative")

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


