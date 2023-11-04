import requests

request = requests.get('http://api.open-notify.org/iss-now.json')
request.raise_for_status()

location = request.json()

print(location)