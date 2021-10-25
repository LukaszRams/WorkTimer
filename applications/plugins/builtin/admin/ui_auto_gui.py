from PyQt5 import QtCore, QtGui, QtWidgets


button_style = """QPushButton {
                    min-width: 100;
                    max-width: 100;
                    min-height: 20;
                    max-height: 20;
                    border: 1px solid gray;
                    border-radius: 10px;
                    font: 10pt 75 \"Segoe Print\";
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


lineedit_style = """QLineEdit{
                        min-width: 200;
                        max-width: 200;
                        min-height: 30;
                        max-height: 30;
                        border: 1px solid gray;
                        border-radius: 13px;
                        padding: 0 10px;
                        selection-background-color: darkgray;
                        font: 10pt \\\"Segoe Print\\\";
                    }
                    QLineEdit:hover{
                        border: 2px solid blue;
                    }
                    QLineEdit:focus{
                        border: 1px solid blue;
                    }"""


combobox_style = """QComboBox {
                        min-width: 200;
                        max-width: 200;
                        min-height: 30;
                        max-height: 30;
                        border: 1px solid gray;
                        border-top-left-radius: 13px;
                        border-bottom-left-radius: 0px;
                        border-top-right-radius: 0px;
                        border-bottom-right-radius: 0px;
                        padding: 0 20px;
                        font: 12pt \\\"Segoe Print\\\";
                    }
                    QComboBox:hover{
                        border: 2px solid blue;
                    }
                    QComboBox:focus{
                        border: 1px solid blue;
                    }
                    QComboBox:on {
                        padding-top: 3px;
                        padding-left: 4px;
                    }"""


label_style = """color: black;
                font: 14pt \"Segoe Print\"; 
                min-width: 100; 
                max-width: 400; 
                min-height: 30; 
                max-height: 30"""


checkbox_radiobutton_label = """color: black; 
                                font: 10pt \"Segoe Print\""""


class Ui_AutoGui:
    def setupUi(self, AutoGui):
        AutoGui.setObjectName("WorkTimer")
        AutoGui.setEnabled(True)
        AutoGui.setFixedSize(653, 478)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(AutoGui.sizePolicy().hasHeightForWidth())
        AutoGui.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        AutoGui.setFont(font)
        self.gridLayout = QtWidgets.QGridLayout(AutoGui)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        # creating header layout
        self.layout = QtWidgets.QHBoxLayout()
        self.layout.setSpacing(20)
        self.layout.setContentsMargins(20, 0, 20, 0)
        self.layout.setObjectName("horizontalLayout")

        # creating SCROLLAREA
        self.scrollArea = QtWidgets.QScrollArea(AutoGui)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 694, 481))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")

        # add VERTICALLAYOUT to SCROLLAREA
        self.gridLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setContentsMargins(0, 10, 0, 20)
        self.gridLayout_2.setSpacing(30)
        self.gridLayout_2.setObjectName("gridLayout_2")

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addLayout(self.layout)
        self.verticalLayout.addWidget(self.scrollArea)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(AutoGui)
        QtCore.QMetaObject.connectSlotsByName(AutoGui)


    def add_header(self, text):
        """
        Adds a header containing a back button, setting name and accept button to the window header
        :param text: setting name
        :return: btn_back, btn_accept - buttons
        """
        # BTN_BACK
        btn_back = QtWidgets.QPushButton()
        btn_back.setStyleSheet(button_style)
        btn_back.setText("Back")
        self.layout.addWidget(btn_back)

        # spacerItem between BTN_BACK and SETTING_NAME
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.layout.addItem(spacerItem)

        # SETTING_NAME
        label = QtWidgets.QLabel()
        label.setStyleSheet("color: black; font: 16pt \"Segoe Print\"")
        label.setText(text)
        self.layout.addWidget(label)

        # spacerItem between SETTING_NAME and BTN_ACCEPT
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.layout.addItem(spacerItem)

        # BTN_ACCEPT
        btn_accept = QtWidgets.QPushButton()
        btn_accept.setStyleSheet(button_style)
        btn_accept.setText("Accept")
        self.layout.addWidget(btn_accept)

        return btn_back, btn_accept

    def add_info_label(self):
        """
        Adds a label to the body. The text of the label can be freely modified
        :return: label
        """
        # LAYOUT
        layout = QtWidgets.QHBoxLayout()
        label = QtWidgets.QLabel()

        # LABEL
        label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        label.setStyleSheet("color: black; font: 12pt \"Segoe Print\"; max-width: 600; max-height: 300")
        label.setText("")
        layout.addWidget(label)
        self.gridLayout_2.addLayout(layout)
        return label

    def add_spacer_item(self):
        """
        Adds a spacer to the dialog body.
        :return:
        """
        # SPACERITEM
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem)

    def add_comboboxes(self, label_name, options_list):
        """
        Adds a combo box, to the body of the dialog.
        :param label_name: Name of the form field e.g. user
        :param options_list: List of available options
        :return: combo box
        """
        # COMBOBOX
        # LAYOUT
        layout = QtWidgets.QHBoxLayout()
        layout.setContentsMargins(50, 0, 50, 0)

        # LABEL
        label = QtWidgets.QLabel()
        label.setStyleSheet(label_style)
        label.setText(label_name)
        layout.addWidget(label)

        # SPACERITEM
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        layout.addItem(spacerItem)

        # COMBOBOX
        comboBox = QtWidgets.QComboBox()
        comboBox.setStyleSheet(combobox_style)
        comboBox.setObjectName("comboBox")
        for option in options_list:
            comboBox.addItem(option)
        layout.addWidget(comboBox)
        self.gridLayout_2.addLayout(layout)

        return comboBox

    def add_lineedit(self, label_name):
        """
        Adds a line edit field to the body of the dialog.
        :param label_name: Form field name e.g. new_password
        :return: line edit
        """

        # LINEEDIT
        # LAYOUT
        layout = QtWidgets.QHBoxLayout()
        layout.setContentsMargins(50, 0, 50, 0)

        # LABEL
        label = QtWidgets.QLabel()
        label.setStyleSheet(label_style)
        label.setText(label_name)
        layout.addWidget(label)

        # SPACERITEM
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        layout.addItem(spacerItem)

        # LINEEDIT
        lineedit = QtWidgets.QLineEdit()
        lineedit.setStyleSheet(lineedit_style)
        lineedit.setObjectName("setting_lineedit_41")
        layout.addWidget(lineedit)

        self.gridLayout_2.addLayout(layout)
        return lineedit

    def add_radiobuttons(self, label_name, options_list):
        """
        Adds a radiobuttons, to the body of the dialog.
        :param label_name: Name of the form field e.g. priority
        :param options_list: List of available options
        :return: list of radiobuttons
        """
        # RADIOBUTTONS
        # LAYOUT
        layout = QtWidgets.QHBoxLayout()
        layout.setContentsMargins(50, 0, 50, 0)
        layout.setSpacing(30)

        # LABEL
        label = QtWidgets.QLabel()
        label.setStyleSheet(label_style)
        label.setText(label_name)
        layout.addWidget(label)

        # SPACERITEM
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        layout.addItem(spacerItem)

        # RADIOBUTTON
        options = []
        for option in options_list:
            radiobutton = QtWidgets.QRadioButton()
            radiobutton.setStyleSheet(checkbox_radiobutton_label)
            radiobutton.setText(option)
            layout.addWidget(radiobutton)
            options.append(radiobutton)

        self.gridLayout_2.addLayout(layout)
        return options

    def add_checkboxes(self, label_name, options_list):
        """
        Adds a checkboxes, to the body of the dialog.
        :param label_name: Name of the form field e.g. chose
        :param options_list: List of available options
        :return: list of checkboxes
        """
        # CHECKBOXES
        # LAYOUT
        layout = QtWidgets.QHBoxLayout()
        layout.setContentsMargins(50, 0, 50, 0)
        layout.setSpacing(30)

        # LABEL
        label = QtWidgets.QLabel()
        label.setStyleSheet(label_style)
        label.setText(label_name)
        layout.addWidget(label)

        # SPACERITEM
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        layout.addItem(spacerItem)

        # CHECKBOX
        options = []
        for option in options_list:
            checkBox = QtWidgets.QCheckBox()
            checkBox.setStyleSheet(checkbox_radiobutton_label)
            checkBox.setText(option)
            layout.addWidget(checkBox)
            options.append(checkBox)


        self.gridLayout_2.addLayout(layout)
        return options

    def retranslateUi(self, AutoGui):
        _translate = QtCore.QCoreApplication.translate
        AutoGui.setWindowTitle(_translate("AutoGui", "WorkTimer"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AutoGui = QtWidgets.QDialog()
    ui = Ui_AutoGui()
    ui.setupUi(AutoGui)
    ui.add_header("Test ustawień")
    ui.add_info_label()
    ui.add_spacer_item()
    ui.add_radiobuttons("radiobuttons", ["option A", "option B", "option C"])
    ui.add_checkboxes("checkboxes", ["option A", "option B", "option C"])
    ui.add_lineedit("Lineedit")
    ui.add_comboboxes("comboboxes", ["option A", "option B", "option C"])
    ui.add_spacer_item()
    AutoGui.show()
    sys.exit(app.exec_())