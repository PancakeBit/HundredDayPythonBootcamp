import requests
import datetime
import config
# REMEMBER TO ENCLOSE THIS TO A CLASS AFTER TESTING
# CHEAPEST FLIGHT IN THE NEXT 6 MONTHS
import config


ENDPOINT = "https://api.tequila.kiwi.com"
HEADER = {
    "apikey": "4_pNba5iyYvUXzbf9Qddyd8md49Yy2Tb",
    "Connection": "close",
}

class FlightFinder:
    def __init__(self):
        self.NOW = datetime.date.today()
        self.fromtoday = self.NOW.strftime("%d/%m/%Y")
        self.tosixmonths = (self.NOW + datetime.timedelta(days=183)).strftime("%d/%m/%Y")

    def getCheaperFlights(self, originCode, destinCode):
        '''Return a list[dictionary] of flights cheaper than budget'''
        searchParams = {
            "curr": "PHP",
            "fly_from": originCode,
            "fly_to": destinCode,
            "date_from": self.fromtoday,
            "date_to": self.tosixmonths,
            "one_for_city": "1",
            "nights_in_dst_from": "1",
            "nights_in_dst_to": "10",
        }
        search_endpoint = ENDPOINT + "/v2/search?"
        req = requests.get(url=search_endpoint, params=searchParams, headers=HEADER)

        try:
            results = req.json()['data'][0]
        except IndexError:
            return None
        except KeyError:
            return None

        # Price, Origin, Destination, Flight Departure, Flight Return
        price = results['price']
        city = results['cityFrom']
        cityCode = results['cityCodeFrom']
        destination = results['cityTo']
        destinationCode = results['cityCodeTo']
        flightDepart = results['local_departure']
        flightReturn = results['route'][-1]['local_departure']
        link = results['deep_link']

        results = {
            "price": price,
            "city": city,
            "cityCode": cityCode,
            "destination": destination,
            "destinationCode": destinationCode,
            "departure": flightDepart,
            "return": flightReturn,
            "link": link,
        }
        return results

    def get_IATA(self, city):
        search_endpoint = ENDPOINT + "/locations/query"
        searchCity = {
            "term": city,
        }
        req = requests.get(url=search_endpoint, params=searchCity, headers=HEADER)
        city = req.json()

        try:
            return city['locations'][0]['code_alpha_3']
        except KeyError:
            return city['locations'][0]['code']
        except IndexError:
            return 'NULL'

# testing code, don't mind this
# flight = FlightFinder()
#
# print(flight.getCheaperFlights("MNL", "DOH"))