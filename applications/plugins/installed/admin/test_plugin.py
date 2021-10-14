#!/usr/bin/python
# -*- coding: utf-8 -*-
from .ui_plugin_test import Ui_TestPlugin
from PyQt5.QtWidgets import QDialog
import logging


class Plugin(QDialog):
    DISPLAY_NAME = "Test Plug-in for added admin"
    DESCRIPTION = "This is plug-in description"
    INSTRUCTION = "These are the basic instructions for using the plug-in"

    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.ui = Ui_TestPlugin()
        self.ui.setupUi(self)
        self.ui.btn_Back.clicked.connect(self.slot_back)

    def slot_back(self):
        """
        Classic operation of the back button
        :return:
        """
        logging.debug("Back button clicked")
        self.parent.show()
        self.hide()



