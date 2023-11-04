import config  # THIS CONFIG PY IS WHERE THE API KEY IS STORED, USE YOUR OWN API KEY
import requests
import datetime
import json
import smtplib
from os import remove

EMAIL = config.EMAIL # tuple (email, app_password)
API_KEY = config.API_KEY
NEWS_KEY = config.NEWS_KEY

# CHANGE STOCK NAME HERE
# Originally Tesla, change these two variables if you want to search for other stocks
# Also works with crypto? Alphavantage API is cool
STOCK = "DOGE"
COMPANY_NAME = "Dogecoin"

today = datetime.datetime.today().date()
yesterday = today - datetime.timedelta(days=1)
todayfilename = f"{today}.txt"

# NOTE: Should add exceptions for API fetch failures

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").


# First, get stock data
# I'm going to write this to a json file so i can test it out
def getData():
    """Return json data from Alphavantage
    If a today's file exists, read from today's file, if it doesn't make a new file
    if yesterday's file exists, delete it"""
    try:
        with open(todayfilename, mode="r") as datafile:
            data = json.load(datafile)

            dat = data['Time Series (Daily)']
            return data
    except FileNotFoundError:
        print("FILE NOT FOUND, REQUESTING FROM API")
        # If today's file is not found, print out data from Alphavantage
        request_url = 'https://www.alphavantage.co/query?'
        parameters = {"function": "TIME_SERIES_DAILY",
                      "symbol": STOCK,
                      "apikey": API_KEY}
        request = requests.get(url=request_url, params=parameters)
        request.raise_for_status()
        data = request.json()

        # Write to file
        with open(todayfilename, mode="w") as datafile:
            json.dump(data, datafile, indent=4)
        # Try to delete yesterday's file if it exists
        try:
            remove(f"{yesterday}.txt")
        except FileNotFoundError:
            pass

        return data


## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
def getNews(percentage):
    api_url = "https://newsapi.org/v2/everything?"
    parameters = {"apiKey": NEWS_KEY,
                  "q": COMPANY_NAME,
                  "pageSize": 3}
    news_req = requests.get(url=api_url, params=parameters)
    news_req.raise_for_status()
    news = news_req.json()

    if percentage >= 0:
        sign = "🔺"
    else:
        sign = "🔻"
        percentage = abs(percentage)

    # Send Email starts here
    message = f"Subject: {STOCK}{sign}{percentage}%\n\n"
    for item in news['articles']:
        message += (f"Headline: {item['title']}\n"
                    f"Brief: {item['description']}\n\n")

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(EMAIL[0], EMAIL[1])
        connection.sendmail(
            from_addr=EMAIL[0],
            to_addrs=EMAIL[0],
            msg=message.encode("utf8"))
        connection.close()

# STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 
# I AM NOT GOING TO USE TWILIO ITS TOO MUCH OF A HASSLE TO FIT INTO THIS CODE



# Main code starts here
stock_data = getData()['Time Series (Daily)']
# remove the meta data from JSON, we don need that

# You can't just use datetime to get the keys for today and yesterday because of timezones and mid-day code execs
# convert the keys to a list and use that to get the close value of 2 most recent dates
dates_list = list(stock_data.keys())
today_value = float(stock_data[dates_list[0]]['4. close'])
yesterday_value = float(stock_data[dates_list[1]]['4. close'])

# calculate the percentage by which the value of the stock changed
percentage = round((today_value - yesterday_value) / yesterday_value * 100.0)

# if today's value is greater than yesterday's value + 5%, else if lower by 5%
if percentage >=5 or percentage <= -5:
    getNews(percentage)
