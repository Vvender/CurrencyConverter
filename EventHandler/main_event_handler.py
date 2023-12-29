from PyQt5.QtWidgets import QApplication, QWidget


class MainEventHandler:
    def __init__(self, app, ui, json_data):
        self.app = app
        self.ui = ui
        self.json_data = json_data

    def combo_box_data(self):
        print(self.json_data)  # Add this line to check if json_data is accessible
        for currency in self.json_data['rates'].keys():
            self.ui.cmb_currency_01.addItem(currency)
            self.ui.cmb_currency_02.addItem(currency)
