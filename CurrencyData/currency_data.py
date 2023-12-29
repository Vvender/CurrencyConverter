import requests
import sys


class Currency:
    def __init__(self, access_key):
        # url and access key is from "https://fixer.io/documentation"
        self.url = f"http://data.fixer.io/api/latest?access_key={access_key}"

    def get_exchange_rate(self):
        response = requests.get(self.url)
        json_data = response.json()
        return json_data
