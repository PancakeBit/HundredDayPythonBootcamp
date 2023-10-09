travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", 'Lille', "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    }
    ]
# Don't change code above

def addNewCountry(place, timesVisited, cities):
    newDict = { place: place, "visits": timesVisited, "cities": cities}
    travel_log.append(newDict)

# Don't change code below
addNewCountry("Russia", 2, ["Moscow", "Saint Petersburg", "Something probably"])
print(travel_log)