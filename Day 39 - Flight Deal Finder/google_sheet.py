
# example code structure

# FROM   DESTINATION  USER_BUDGET  HISTORIAL_LOW_PRICE   CURRENT_PRICE
import requests
import config

SHEETY_URL = config.SHEETY_API
BEARER = config.BEARER_TOKEN
HEADER = {
    "Authorization": BEARER,
    "Connection": "close",
    "Content-Type": "application/json"
}

class googleSheet:
    def __init__(self):
        pass

    def getData(self):
        sheety_req = requests.get(url=SHEETY_URL, headers=HEADER)
        return sheety_req.json()['flights']

    def addRow(self, origin, code, destination, budget):
        insert = {
                "flight": {
                    "from": origin,
                    "code": code,
                    "destination": destination,
                    "budget": budget
                }
            }
        requests.post(url=SHEETY_URL, json=insert, headers=HEADER)

