class MainEventHandler:
    def __init__(self, app, ui, json_data):
        # Store the application object
        self.app = app
        # Store the UI object
        self.ui = ui
        # Store the JSON data
        self.json_data = json_data

    def initial_load(self):
        try:
            # Load data into the combo boxes
            self.load_cmb_data()
            # Set default text for combo boxes
            self.default_cmb_text()
            # Calculate the main rate
            self.calculate_main_rate()
            # Load exchange rates
            self.load_rates()
            # Load the buying price
            self.load_buy_price()
            # Print a message indicating the initial loading is completed
            print("Initial loading completed")
        except Exception as e:
            # Handle any exceptions that occur during initial loading
            print(f"An error occurred during 'Initial Loading': {e}")

    def load_cmb_data(self):
        try:
            # Iterate through the currencies in the JSON data and add them to the combo boxes
            for currency in self.json_data['rates'].keys():
                self.ui.cmb_currency_01.addItem(currency)
                self.ui.cmb_currency_02.addItem(currency)
        except Exception as e:
            # Handle any exceptions that occur during loading combo box data
            print(f"An error occurred during 'Loading Combobox Data': {e}")

    def default_cmb_text(self):
        try:
            # Set default currencies in the combo boxes
            self.ui.cmb_currency_01.setCurrentText("EUR")
            self.ui.cmb_currency_02.setCurrentText("TRY")
        except Exception as e:
            # Handle any exceptions that occur during setting default combo box text
            print(f"An error occurred during 'Defaulting ComboBox Text': {e}")

    def calculate_main_rate(self):
        try:
            # Get the selected currencies and calculate the main exchange rate
            rate_one = self.ui.cmb_currency_01.currentText()
            rate_two = self.ui.cmb_currency_02.currentText()
            rate = "{:.2f}".format((float(self.json_data['rates'][rate_two]) / float(
                self.json_data['rates'][rate_one]) * float(self.ui.lineEdit_currency_01.text())))
            # Set the calculated rate in the second currency input field
            self.ui.lineEdit_currency_02.setText(str(rate))
        except Exception as e:
            # Handle any exceptions that occur during calculating the main rate
            print(f"An error occurred during 'Calculating Main Rate': {e}")

    def calculate_rate(self, rate):
        try:
            # Calculate the exchange rate for a specific currency
            formatted_rate = float((self.json_data['rates']['TRY'])) / (float(self.json_data['rates'][rate]))
            return "{:.2f}".format(formatted_rate)
        except Exception as e:
            # Handle any exceptions that occur during calculating a specific rate
            print(f"An error occurred during 'Calculating Rate': {e}")

    def load_rates(self):
        try:
            # Set the exchange rates for different currencies in the UI labels
            self.ui.lbl_rate_eur.setText(self.calculate_rate('EUR'))
            self.ui.lbl_rate_usd.setText(self.calculate_rate('USD'))
            self.ui.lbl_rate_gbp.setText(self.calculate_rate('GBP'))
            self.ui.lbl_rate_cad.setText(self.calculate_rate('CAD'))
            self.ui.lbl_rate_chf.setText(self.calculate_rate('CHF'))
            self.ui.lbl_rate_rub.setText(self.calculate_rate('RUB'))
            self.ui.lbl_rate_jpy.setText(self.calculate_rate('JPY'))
        except Exception as e:
            # Handle any exceptions that occur during loading rates
            print(f"An error occurred during 'Loading Rates': {e}")

    def calculate_buy_price(self, currency):
        try:
            # Calculate the buy price for a specific currency
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
        except Exception as e:
            # Handle any exceptions that occur during calculating buy prices
            print(f"An error occurred during 'Calculating Buy Prices': {e}")

    def load_buy_price(self):
        try:
            # Set the buy prices for different currencies in the UI labels
            self.ui.lbl_buy_eur.setText(self.calculate_buy_price("eur"))
            self.ui.lbl_buy_usd.setText(self.calculate_buy_price("usd"))
            self.ui.lbl_buy_gbp.setText(self.calculate_buy_price("gbp"))
            self.ui.lbl_buy_cad.setText(self.calculate_buy_price("cad"))
            self.ui.lbl_buy_chf.setText(self.calculate_buy_price("chf"))
            self.ui.lbl_buy_rub.setText(self.calculate_buy_price("rub"))
            self.ui.lbl_buy_jpy.setText(self.calculate_buy_price("jpy"))
        except Exception as e:
            # Handle any exceptions that occur during loading buy prices
            print(f"An error occurred during 'Loading Buy Prices': {e}")

    def update_buy_price(self, sender):
        try:
            # Update the buy price in the UI based on the sender currency
            if sender == "eur":
                self.ui.lbl_buy_eur.setText(self.calculate_buy_price(sender))
            elif sender == "usd":
                self.ui.lbl_buy_usd.setText(self.calculate_buy_price(sender))
            elif sender == "gbp":
                self.ui.lbl_buy_gbp.setText(self.calculate_buy_price(sender))
            elif sender == "cad":
                self.ui.lbl_buy_cad.setText(self.calculate_buy_price(sender))
            elif sender == "chf":
                self.ui.lbl_buy_chf.setText(self.calculate_buy_price(sender))
            elif sender == "rub":
                self.ui.lbl_buy_rub.setText(self.calculate_buy_price(sender))
            elif sender == "jpy":
                self.ui.lbl_buy_jpy.setText(self.calculate_buy_price(sender))
        except Exception as e:
            # Handle any exceptions that occur during updating buy price
            print(f"An error occurred during 'Updating Buy Price': {e}")

    def clear_text(self):
        try:
            # Clear the input fields and set default values
            self.ui.lineEdit_amount_eur.setText("1")
            self.ui.lineEdit_amount_usd.setText("1")
            self.ui.lineEdit_amount_cad.setText("1")
            self.ui.lineEdit_amount_gbp.setText("1")
            self.ui.lineEdit_amount_rub.setText("1")
            self.ui.lineEdit_amount_chf.setText("1")
            self.ui.lineEdit_amount_jpy.setText("1")
            self.ui.lineEdit_currency_01.setText("1")
            self.ui.lineEdit_currency_02.setText("1")
            self.default_cmb_text()
        except Exception as e:
            # Handle any exceptions that occur during clearing text
            print(f"An error occurred during 'Clear Text': {e}")

    def reset_app(self):
        try:
            # Reset the application by clearing text and reloading initial data
            self.clear_text()
            print("Texts cleared")
            self.initial_load()
            print("Reload Completed")
        except Exception as e:
            # Handle any exceptions that occur during resetting the app
            print(f"An error occurred during 'Reset App': {e}")
