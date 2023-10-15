def checkifleapyear(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 ==0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
def daysinmonth(month, year):
    '''Get the days in the month and if it's a leap year for feruary make it 29'''
    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = months[month-1]
    if checkifleapyear(year) and month == 2:
        days += 1
    return days

month = int(input("What month would you like to check? (1,2,3,...): "))
year = int(input("What year would you like to check?: "))

print(f"There are {daysinmonth(month,year)} days on the {month} month of {year}")
