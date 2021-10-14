#!/usr/bin/python
# -*- coding: utf-8 -*-


def main():
    from applications.settings import settings
    settings.initialize_client_settings()
    from PyQt5.QtWidgets import QApplication
    import sys
    from PyQt5.QtGui import QIcon
    import logging
    import os
    logging.info("User settings initialised")
    app = QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)
    import ctypes
    app_id = u'WorkTimer.1.0.0'
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(app_id)
    app.setWindowIcon(QIcon(os.path.join(os.getcwd(), "res", "icons", "WT.ico")))
    logging.debug("A welcome window has been created")
    from applications.welcome import welcome
    welcome.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
