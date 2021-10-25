#!/usr/bin/python
# -*- coding: utf-8 -*-
from applications.frames.ui_menu import Ui_Menu
from applications.frames.ui_logout_prompt import Ui_LogoutPrompt
from PyQt5.QtWidgets import QWidget, QDialog, QHBoxLayout, QPushButton
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QCloseEvent
from applications.settings import settings
import logging


class Menu(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Menu()
        self.ui.setupUi(self)
        self.ui.logout_btn.clicked.connect(self.slot_logout)
        self.ui.back_btn.clicked.connect(self.slot_back)
        self.show_categories()

    def closeEvent(self, a0: QCloseEvent) -> None:
        """
        Logout and close the app
        :return:
        """
        settings.initialize_client_settings()
        import sys
        sys.exit()

    def slot_logout(self):
        """
        Displays a logout request window
        :return:
        """
        logging.debug("Ask for logout")
        LogoutPrompt = QDialog()
        ui = Ui_LogoutPrompt()
        ui.setupUi(LogoutPrompt)
        ui.btn_Ok.clicked.connect(LogoutPrompt.accept)
        ui.btn_cancel.clicked.connect(lambda: self._hide(LogoutPrompt))
        if LogoutPrompt.exec_() == QDialog.Accepted:
            from applications.welcome import welcome
            settings.initialize_client_settings()
            logging.debug("A welcome window has been created")
            welcome.show()
            self.hide()

    def _hide(self, window):
        logging.debug("Logout cenceled")
        window.hide()

    def slot_back(self):
        self.ui.back_btn.hide()
        self.clear()
        self.show_categories()

    def show_categories(self):
        """
        Displays plug-in category selection
        "Basic options" - plug-in from builtin\\client
        "Added options" - plug-in from installed\\client
        "Basic admin options" - plug-in from builtin\\admin
        "Added admin options" - plug-in from installed\\admin
        A category is only visible if there are plug-ins assigned to it !!!
        :return:
        """
        logging.info("Creating a category window")
        self.ui.back_btn.hide()  # Hide the back button
        if self.ui.verticalLayout_2.count():  # Checking whether there is anything to remove
            self.clear()

        if settings.user_builtin_plugins:
            btn = self.add_btn("Basic options")
            btn.clicked.connect(self.slot_basic_user)

        if settings.user_installed_plugins:
            btn = self.add_btn("Added options")
            btn.clicked.connect(self.slot_added_user)
        if settings.user["priority"] == "admin":
            if settings.admin_builtin_plugins:
                btn = self.add_btn("Basic admin options")
                btn.clicked.connect(self.slot_basic_admin)

            if settings.admin_installed_plugins:
                btn = self.add_btn("Added admin options")
                btn.clicked.connect(self.slot_added_admin)

    def clear(self):
        """
        Clears current options
        :return:
        """
        while self.ui.verticalLayout_2.count():
            child = self.ui.verticalLayout_2.takeAt(0)
            if child.layout():
                while child.count():
                    grandchild = child.takeAt(0)
                    if grandchild.widget():
                        grandchild.widget().deleteLater()
                child.layout().deleteLater()

    def add_btn(self, name):
        """
        Adds a button with the given name and returns it
        :param name:
        :return:
        """
        btn70_style = """QPushButton {
                            border: 1px solid gray;
                            border-radius: 35px;
                            padding: 20px;
                            font: bold 15pt "Segoe Print";
                            background-color: qlineargradient(x1: 0.5, y1: 0.5, x2: 1, y2: 1,
                                                              stop: 0 #dadbde, stop: 1 #f6f7fa);
                        }
                        QPushButton:hover {
                            border: 1px solid gray;
                            background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                                              stop: 0 #f6f7fa, stop: 1 #dadbde);
                        }
                        QPushButton:pressed {
                            border: 1px solid gray;
                            background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                                              stop: 0 #dadbde, stop: 1 #f6f7fa);
                        }
                        QToolTip { background-color: qlineargradient(x1: 0.5, y1: 0.5, x2: 1, y2: 1,
                                                              stop: 0 #dadbde, stop: 1 #f6f7fa);
                                   color: black; 
                                   border: 1px solid gray;
                                   border-radius: 4px;
                                   }"""

        self.ui.horizontalLayout = QHBoxLayout()
        self.ui.horizontalLayout.setObjectName("horizontalLayout")
        self.ui.horizontalLayout.setContentsMargins(50, 0, 50, 20)
        self.ui.btn = QPushButton(self.ui.scrollAreaWidgetContents)
        self.ui.btn.setMinimumSize(QSize(300, 70))
        self.ui.btn.setMaximumSize(QSize(1000, 70))
        self.ui.btn.setText(name)
        self.ui.btn.setStyleSheet(btn70_style)
        self.ui.horizontalLayout.addWidget(self.ui.btn)
        self.ui.verticalLayout_2.addLayout(self.ui.horizontalLayout)
        return self.ui.btn

    def slot_basic_user(self):
        logging.info("Show basic user options")
        self.show_plugins(settings.user_builtin_plugins)

    def slot_added_user(self):
        logging.info("Show installed user options")
        self.show_plugins(settings.user_installed_plugins)

    def slot_basic_admin(self):
        logging.info("Show basic admin options")
        self.show_plugins(settings.admin_builtin_plugins)

    def slot_added_admin(self):
        logging.info("Show installed admin options")
        self.show_plugins(settings.admin_installed_plugins)

    def show_plugins(self, plugins_list):
        """
        Displays plug-ins from a given category and sets slots for activation
        :param plugins_list:
        :return:
        """
        self.ui.back_btn.show()
        self.clear()
        for plugin in plugins_list:
            btn = self.add_btn(plugin.Plugin.DISPLAY_NAME)
            btn.setToolTip(plugin.Plugin.DESCRIPTION)
            btn.clicked.connect(lambda ch, plugin=plugin: self.plugin_selected(plugin))


    def plugin_selected(self, plugin):
        """
        Display the plug-in window and minimise the menu window
        :param plugin:
        :return:
        """
        self.active_plugin = plugin.Plugin(parent=self)
        self.active_plugin.setWhatsThis(self.active_plugin.INSTRUCTION)
        self.hide()
        logging.debug("Plugin %s has been activated" % self.active_plugin.DISPLAY_NAME)
        self.active_plugin.exec_()
