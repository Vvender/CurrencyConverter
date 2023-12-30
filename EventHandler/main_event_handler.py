from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import QUrl


class MainEventHandler:
    def __init__(self, app, ui, json_data):
        self.app = app
        self.ui = ui
        self.json_data = json_data

    def calculate_rate(self, rate):
        formatted_rate = float((self.json_data['rates']['TRY'])) / (float(self.json_data['rates'][rate]))
        return "{:.2f}".format(formatted_rate)

    def calculate_buy_price(self, currency):
        currency_widgets = {
            "eur": (self.ui.lbl_rate_eur, self.ui.lineEdit_amount_eur),
            "usd": (self.ui.lbl_rate_usd, self.ui.lineEdit_amount_usd),
            "gbp": (self.ui.lbl_rate_gbp, self.ui.lineEdit_amount_gbp),
            "cad": (self.ui.lbl_rate_cad, self.ui.lineEdit_amount_cad),
            "chf": (self.ui.lbl_rate_chf, self.ui.lineEdit_amount_chf),
            "rub": (self.ui.lbl_rate_rub, self.ui.lineEdit_amount_rub),
            "jpy": (self.ui.lbl_rate_jpy, self.ui.lineEdit_amount_jpy),
        }
        rate_widget, amount_widget = currency_widgets.get(currency)
        rate = rate_widget.text()
        amount = amount_widget.text()
        buy_price = float(rate) * float(amount)
        return "{:.2f}".format(buy_price)

    def load_cmb_data(self):
        for currency in self.json_data['rates'].keys():
            self.ui.cmb_currency_01.addItem(currency)
            self.ui.cmb_currency_02.addItem(currency)

    def load_rates(self):
        self.ui.lbl_rate_eur.setText(self.calculate_rate('EUR'))
        self.ui.lbl_rate_usd.setText(self.calculate_rate('USD'))
        self.ui.lbl_rate_gbp.setText(self.calculate_rate('GBP'))
        self.ui.lbl_rate_cad.setText(self.calculate_rate('CAD'))
        self.ui.lbl_rate_chf.setText(self.calculate_rate('CHF'))
        self.ui.lbl_rate_rub.setText(self.calculate_rate('RUB'))
        self.ui.lbl_rate_jpy.setText(self.calculate_rate('JPY'))

    def load_buy_price(self):
        self.ui.lbl_buy_eur.setText(self.calculate_buy_price("eur"))
        self.ui.lbl_buy_usd.setText(self.calculate_buy_price("usd"))
        self.ui.lbl_buy_gbp.setText(self.calculate_buy_price("gbp"))
        self.ui.lbl_buy_cad.setText(self.calculate_buy_price("cad"))
        self.ui.lbl_buy_chf.setText(self.calculate_buy_price("chf"))
        self.ui.lbl_buy_rub.setText(self.calculate_buy_price("rub"))
        self.ui.lbl_buy_jpy.setText(self.calculate_buy_price("jpy"))
