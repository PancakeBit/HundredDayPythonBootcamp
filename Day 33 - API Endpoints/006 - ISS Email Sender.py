import requests
from datetime import datetime
from time import sleep


def sendEmail():
    print("Pretend this is sending an email")
    print("I don't want to put my app password in here")
    print("So just pretend")

    # import smtplib
    #
    # email = "email"
    # password = "app password "
    #
    # with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    #     connection.starttls()
    #     connection.login(email, password)
    #     connection.sendmail(
    #         from_addr=email,
    #         to_addrs=ENTER_RECEIPENT,
    #         msg="Hello")
    #     connection.close()

# I'm not going to put my actual coords in here
MY_LAT = 3 # Your latitude
MY_LONG = 1 # Your longitude
parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

def checkISS():
    # COMMENTING THESE FOR TESTING PURPOSES
    #response = requests.get(url="http://api.open-notify.org/iss-now.json")
    #response.raise_for_status()
    #data = response.json()

    #iss_latitude = float(data["iss_position"]["latitude"])
    #iss_longitude = float(data["iss_position"]["longitude"])
    iss_latitude = 5.0
    iss_longitude = 5.0

    #Your position is within +5 or -5 degrees of the ISS position.

    # needs absolute function to ensure both numbers are positive to find
    # if they are within 5 units of each other
    if (abs(iss_latitude) - abs(MY_LAT)) <= 5 and (abs(iss_longitude) - abs(MY_LONG)) <= 5:
        return checkTime()
        # if between 5 and -5

def checkTime():
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()
    # If it is after sunset OR before sunrise
    if time_now.hour > sunset or time_now.hour < sunrise:
        return True
    else:
        return False


while checkISS():
    sendEmail()
    sleep(60)




#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.



