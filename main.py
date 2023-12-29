import sys
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QWidget
from Gui.ui_currency_converter import Ui_Currency
from EventHandler.event_handler import EventHandler


class MainWindow:

    def __init__(self):
        self.app = QApplication(sys.argv)
        self.ui_window = QWidget()
        self.ui = Ui_Currency()
        self.ui.setupUi(self.ui_window)
        self.ui_window.show()

        # Create an instance of EventHandler and pass the app and ui objects
        self.event_handler = EventHandler(self.app, self.ui)

        # Main Button Events
        self.ui.btn_github.clicked.connect(self.event_handler.main_event_handler)
        self.ui.btn_linkedin.clicked.connect(self.event_handler.main_event_handler)
        self.ui.btn_cv.clicked.connect(self.event_handler.main_event_handler)
        self.ui.btn_email.clicked.connect(self.event_handler.main_event_handler)
        self.ui.btn_minimize.clicked.connect(self.ui_window.showMinimized)
        self.ui.btn_close.clicked.connect(self.app.quit)


if __name__ == "__main__":
    main_app = MainWindow()
    sys.exit(main_app.app.exec_())
