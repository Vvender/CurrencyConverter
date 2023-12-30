import sys
from PyQt5.QtWidgets import QApplication, QWidget
from Gui.ui_currency_converter import Ui_Currency
from EventHandler.utility_event_handler import UtilityEventHandler
from EventHandler.main_event_handler import MainEventHandler
import CurrencyData.currency_data as data


class MainWindow:

    def __init__(self):
        # Setting Currency Data (json)
        self.json_data = data.Currency("968cf488b856f206db08b0ed1de12d0a").get_exchange_rate()
        self.app = QApplication(sys.argv)
        self.ui_window = QWidget()
        self.ui = Ui_Currency()
        self.ui.setupUi(self.ui_window)
        self.ui_window.show()

        # Create an instance of EventHandler and pass the app and ui objects
        self.utility_events = UtilityEventHandler(self.app, self.ui)
        self.main_events = MainEventHandler(self.app, self.ui, self.json_data)

        # UTILITY EVENTS #
        self.ui.btn_github.clicked.connect(self.utility_events.utility_event_handler)
        self.ui.btn_linkedin.clicked.connect(self.utility_events.utility_event_handler)
        self.ui.btn_cv.clicked.connect(self.utility_events.utility_event_handler)
        self.ui.btn_email.clicked.connect(self.utility_events.utility_event_handler)
        self.ui.btn_minimize.clicked.connect(self.ui_window.showMinimized)
        self.ui.btn_close.clicked.connect(self.app.quit)

        # MAIN EVENTS #

        # Loading Initial Data
        self.main_events.initial_load()

        # Currency Text Change Event
        self.ui.lineEdit_currency_01.textChanged.connect(self.main_events.calculate_main_rate)

        # Combo Box Text Change Event
        self.ui.cmb_currency_01.currentTextChanged.connect(self.main_events.calculate_main_rate)
        self.ui.cmb_currency_02.currentTextChanged.connect(self.main_events.calculate_main_rate)

        # Amount Text Change Events
        self.ui.lineEdit_amount_eur.textChanged.connect(lambda: self.main_events.update_buy_price("eur"))
        self.ui.lineEdit_amount_usd.textChanged.connect(lambda: self.main_events.update_buy_price("usd"))
        self.ui.lineEdit_amount_gbp.textChanged.connect(lambda: self.main_events.update_buy_price("gbp"))
        self.ui.lineEdit_amount_cad.textChanged.connect(lambda: self.main_events.update_buy_price("cad"))
        self.ui.lineEdit_amount_chf.textChanged.connect(lambda: self.main_events.update_buy_price("chf"))
        self.ui.lineEdit_amount_rub.textChanged.connect(lambda: self.main_events.update_buy_price("rub"))
        self.ui.lineEdit_amount_jpy.textChanged.connect(lambda: self.main_events.update_buy_price("jpy"))

        # Button Events
        self.ui.btn_clear.clicked.connect(self.main_events.clear_text)
        self.ui.btn_reset.clicked.connect(self.main_events.reset_app)


if __name__ == "__main__":
    main_app = MainWindow()
    sys.exit(main_app.app.exec_())
