import sys
from PyQt5.QtWidgets import QApplication, QWidget
from Gui.ui_currency_converter import Ui_Currency
from EventHandler.utility_event_handler import UtilityEventHandler
from EventHandler.main_event_handler import MainEventHandler
import CurrencyData.currency_data as data



class MainWindow:

    def __init__(self):
        self.app = QApplication(sys.argv)
        self.ui_window = QWidget()
        self.ui = Ui_Currency()
        self.ui.setupUi(self.ui_window)
        self.ui_window.show()

        # Main Button Events
        self.ui.btn_github.clicked.connect(self.utility_events.utility_event_handler)
        self.ui.btn_linkedin.clicked.connect(self.utility_events.utility_event_handler)
        self.ui.btn_cv.clicked.connect(self.utility_events.utility_event_handler)
        self.ui.btn_email.clicked.connect(self.utility_events.utility_event_handler)
        self.ui.btn_minimize.clicked.connect(self.ui_window.showMinimized)
        self.ui.btn_close.clicked.connect(self.app.quit)

        # Setting Currency Data (json)
        self.json_data = data.Currency("968cf488b856f206db08b0ed1de12d0a").get_exchange_rate()
        # Create an instance of EventHandler and pass the app and ui objects
        self.utility_events = UtilityEventHandler(self.app, self.ui)
        self.main_events = MainEventHandler(self.app, self.ui, self.json_data)

        # Loading Data
        self.main_events.load_cmb_data()
        self.main_events.load_rates()
        self.main_events.load_buy_price()

        # Amount Text Change Events

        # Currency Text Change Events

        # Button Events



if __name__ == "__main__":
    main_app = MainWindow()
    sys.exit(main_app.app.exec_())
