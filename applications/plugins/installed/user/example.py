from PyQt5.QtWidgets import QDialog
import logging
from PyQt5.QtGui import QCloseEvent

from path_to_ui import ui_name  # import plugin window


class Plugin(QDialog):
    DISPLAY_NAME = "This text is displayed as the name of the setting"
    DESCRIPTION = "This text is displayed as a label when hovering over a setting name in the menu"
    INSTRUCTION = "Text to be displayed after using the dialog's help button"

    def __init__(self, parent):
        """
        In this function, initialise the dialog and connect the necessary slots
        """
        super().__init__()
        self.parent = parent
        self.ui = ui_name()  # use plugin window name
        self.ui.setupUi(self)


    def slot_back(self):  # You should have button back connected to this slot
        """
        Classic operation of the back button
        :return:
        """
        logging.debug("Back button clicked")
        self.parent.show()
        self.hide()

    def closeEvent(self, a0: QCloseEvent) -> None:  # If you try to close the dialog, you goes to parent window
        """
        Close dialog and show parent
        :param a0:
        :return:
        """
        logging.info("Close event")
        self.parent.show()
        self.hide()

    # Here should be the logic behind the plug-in