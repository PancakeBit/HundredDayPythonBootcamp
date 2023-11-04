import requests
import config
import datetime

# not a very interesting project day

today = datetime.date.today()

pixela_url = "https://pixe.la/v1/users"
PIXELA_KEY = config.PIXELA_KEY
USERNAME = "welly"

parameters = {
    "token": PIXELA_KEY,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

graphs_url = f"{pixela_url}/{USERNAME}/graphs"
graph_config = {
    "id": "graph123",
    "name": "100 Days of Code Tracker",
    "unit": "days",
    "type": "int",
    "color": "sora"
}

# ----------------- THIS CODE FOR CREATING USER, NOT NEEDED ANYMORE PAST 1st RUNTHROUGH------------
#
# request = requests.post(url=pixela_url, json=parameters)
# print(request.text)
# ------------------------------------------------------------------------
graph_id = "graph123"
postpixel_url = f"{graphs_url}/{graph_id}"
today_formatted = f"{today.year}{today.month}{today.day}"
postpixel_config = {
    "date": today_formatted,
    "quantity": "1"
}

header = {
    "X-USER-TOKEN": PIXELA_KEY
}

# MAKE NEW GRAPH
# request = requests.post(url=graphs_url, json=graph_config, headers=header)
# print(request.text)

# MAKE NEW PIXEL
request = requests.post(url=postpixel_url, json=postpixel_config, headers=header)
print(request.text)

# UPDATE PIXEL
# request = requests.post(url=postpixel_url, json=postpixel_config, headers=header)
# print(request.text)