# Don't change this code
year = int(input("which year do you want to check?: "))
#Don't change this code

leap = f"{year} is a leap year!"
noleap = f"{year} is not a leap year"

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 ==0:
            print(leap)
        else:
            print(noleap)
    else:
        print(leap)
else:
    print(noleap)