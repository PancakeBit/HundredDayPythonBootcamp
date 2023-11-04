import config
import requests
import datetime

# This program gets input from the user and runs it through Nutritionix API -> Open AI is cool
# Once it has retrieved data from Nutritionix it will call the Sheety API to write
# Into a google sheet that it has been given access to.
# I will not include this google sheet link in this file so if you want to test this program out
# set up API keys for Nutrix and Sheety then make a google sheet
# put all of that into variables in a config.py as is used in this code

# I don't want to learn about bearer authentication
# It's the exact same as the user made key from pixela
# you set a custom auth key and then pass that as an "Authorization" header
# anyone who has that auth key can access your project API

def get_data():
    '''Return JSON data from API'''
    NUTRIX_ID = config.NUTRIX_ID
    NUTRIX_KEY = config.NUTRIX_KEY

    # Set header API keys
    header = {
        "x-app-id": NUTRIX_ID,
        "x-app-key": NUTRIX_KEY,
        "Content-Type": "application/json"
    }

    # These parameters based on me, but the only required argument is the query
    parameters = {
        "gender": "male",
        "weight_kg": 87,
        "height_cm": 170,
        "age": 24
    }
    nutrix_url = "https://trackapi.nutritionix.com/v2/natural/exercise"

    # Ask for input from the user
    parameters['query'] = input("What did you do today?: ")

    # Process input into API thanks Nutitionix
    nutrix_req = requests.post(url=nutrix_url, json=parameters, headers=header)
    nutrix_req.raise_for_status()

    # This post request will return a JSON, get only needed data from that JSON
    result = nutrix_req.json()['exercises'][0]

    return result

def addRowToSheet(result:dict):
    sheety_url = config.SHEETY_API  # this is the API URL that has no auth key because I haven't set it up
    now = datetime.datetime.now()
    date = now.strftime("%d/%m/%Y")
    time = now.strftime("%H:%M:%S")

    insert = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": str(result['name']).title(),
            "duration": result['duration_min'],
            "calories": result['nf_calories']
        }
    }
    sheety_req = requests.post(url=sheety_url, json=insert)
    sheety_req.raise_for_status()

if __name__ == '__main__':
    result = get_data()
    addRowToSheet(result)
