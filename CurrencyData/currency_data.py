import requests
import sys


class Currency:
    def __init__(self, access_key):
        # Initialize the Currency class with the API access key
        # The URL and access key are obtained from "https://fixer.io/documentation"
        self.url = f"http://data.fixer.io/api/latest?access_key={access_key}"

    def get_exchange_rate(self):
        # Get the latest exchange rate data from the API
        response = requests.get(self.url)
        json_data = response.json()
        return json_data
