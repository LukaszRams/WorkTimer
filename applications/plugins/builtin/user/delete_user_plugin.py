#!/usr/bin/python
# -*- coding: utf-8 -*-
from .ui_auto_gui import Ui_AutoGui
import logging
from applications.database.connect import database
from PyQt5.QtWidgets import QDialog, QPushButton, QHBoxLayout
from PyQt5.QtGui import QCloseEvent, QKeyEvent
from PyQt5.QtCore import Qt
from applications.settings import settings
from .ask_dialog import Ui_AskDialog


btn_style = """QPushButton {
                    min-width: 400;
                    max-width: 400;
                    min-height: 60;
                    max-height: 60;
                    border: 1px solid gray;
                    border-radius: 30px;
                    font: 18pt 75 \"Segoe Print\";
                    background-color: qlineargradient(x1: 0.5, y1: 0.5, x2: 1, y2: 1, stop: 0 #dadbde, stop: 1 #f6f7fa);
                }
                QPushButton:default {
                    border: 2px solid gray;
                }
                QPushButton:hover {
                    border: 1px solid gray;
                    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #f6f7fa, stop: 1 #dadbde);
                }
                QPushButton:pressed {
                    border: 1px solid gray;
                    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dadbde, stop: 1 #f6f7fa);
                }"""


class Plugin(QDialog):
    DISPLAY_NAME = "Delete account"
    DESCRIPTION = "Deletes account and data"
    INSTRUCTION = "Click delete to delete your account"

    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.ui = Ui_AutoGui()
        self.ui.setupUi(self)
        self.btn_back, self.btn_accept = self.ui.add_header("DELETE ACCOUNT")
        self.btn_back.clicked.connect(self.slot_back)
        self.btn_accept.hide()
        self.label = self.ui.add_info_label()
        self.ui.add_spacer_item()
        # LAYOUT
        layout = QHBoxLayout()
        self.btn_delete = QPushButton()
        self.btn_delete.setText("Delete my account")
        self.btn_delete.setStyleSheet(btn_style)
        layout.addWidget(self.btn_delete)
        self.ui.gridLayout_2.addLayout(layout)
        self.btn_delete.clicked.connect(self.slot_accept)
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

    def keyPressEvent(self, a0: QKeyEvent) -> None:
        if a0.key() == Qt.Key.Key_Return:
            return
        QDialog.keyPressEvent(self, a0)

    def slot_accept(self):
        """
        Checks if the user exists, validates the password and displays an appropriate message
        :return:
        """
        logging.debug("Ask for delete account")
        Ask = QDialog()
        ui = Ui_AskDialog()
        ui.setupUi(Ask, "Account deletion", f"Are you sure you want to delete Your account")
        ui.btn_Ok.clicked.connect(Ask.accept)
        ui.btn_cancel.clicked.connect(lambda: self._hide(Ask))
        if Ask.exec_() == QDialog.Accepted:
            database.update(f"""DELETE FROM DETAILED_WORKING_TIME WHERE user = \'{settings.user["username"]}\'""")
            database.update(f"""DELETE FROM USERS WHERE user = \'{settings.user["username"]}\'""")
            database.update(f"""DELETE FROM WORKING_TIME WHERE user = \'{settings.user["username"]}\'""")
            logging.info(f"User account has been deleted")
            from applications.welcome import welcome
            welcome.show()
            self.hide()
        else:
            status = ("Deletion of a user account has been cancelled", "Negative")
            self.show_status(*status)

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

    def _hide(self, window):
        logging.debug("Logout cenceled")
        window.hide()
