# THIS WILL BE THE UI FOR THE PROGRAM
import google_sheet
import flight_finder
import config
import smtplib

# CHEAPEST FLIGHT IN THE NEXT 6 MONTHS

# For some reason the Kiwi search code generator recognizes Philippines as Philadelphia
# and so gives a Philadelphian flight schedule
# Something that Kiwi/Tequila will have to fix but will circumvent by asking user's City instead

# TODO 1: This file needs to be isolated so it can be automated to run
#          SPECIFICALLY sending an email if flights are cheaper.\n
#          Transfer this code to

# TODO 2: Format date and time for email flight_finder->getCheaperFlights->flightDepart and flightReturn

# TODO 3: Make actual "Add Row" functionality, adding a row is functional in google_sheet it just needs implementation here

# TODO 4: Specify CITY name for "From"

# TODO 5: Account Creation
#         User Table
#         User column in flight table

def refreshDatabase():
    sheet = google_sheet.googleSheet()
    database = sheet.getData()
    return database

def add():
    print("ADD NEW ROW")
    sheet.addRow('Philippines', 'PHL', 'Malaysia', '0')


def search(database:list):
    for rownum in range(0, len(database)):
        origin = flightFinder.get_IATA(database[rownum]['from'])
        destinCode = flightFinder.get_IATA(database[rownum]['destination'])
        budget = database[rownum]['budget']
        flights = flightFinder.getCheaperFlights(origin, destinCode)

        print(origin)
        if flights is not None and int(flights['price']) <= int(budget):
            send_email(flights)

def edit():
    print("EDIT SOMETHING WITHIN THE GOOGLE SHEET")


def send_email(f_dict):
    head = f"Subject: Found Cheap Flight from {f_dict['city']} to {f_dict['destination']}\n\n"
    body = f"""Low Price Alert! Only P{f_dict['price']} to fly from {f_dict['city']}-{f_dict['cityCode']} to {f_dict['destination']}-{f_dict['destinationCode']} from {f_dict['departure']} to {f_dict['return']}\n"""
    lower = f'Click below to start booking now!\n{f_dict["link"]}'
    message = head + body + lower

    EMAIL = config.EMAIL  # tuple (email, app_password)

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(EMAIL[0], EMAIL[1])
        connection.sendmail(
            from_addr=EMAIL[0],
            to_addrs=EMAIL[0],
            msg=message.encode("utf8"))
        connection.close()


# This is what the program will do every time it runs
sheet = google_sheet.googleSheet()
flightFinder = flight_finder.FlightFinder()
sheet_data = refreshDatabase()
search(sheet_data)





