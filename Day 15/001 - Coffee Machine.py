from time import sleep

# ---------------------------------------------
# This program is mostly done, not the most efficient or readable but it works pretty well
# Can make this code more efficient by making several processes into functions
# This code is also leaning HARD into dictionary references and is not easy to modify

# menu and resources provided by AppBrewery from the exercise at Replit
menu = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    },
}

resources = {
    "water": 500,
    "milk": 400,
    "coffee": 500,
}

def report(currResources):
    #print the current resources
    currResources = (f"Water: {currResources['water']}\n"
                     f"Milk: {currResources['milk']}\n"
                     f"Coffee: {currResources['coffee']}\n"
                     f"Money: ${currResources['money']}")
    print(currResources)

def insertcoins(order):
    '''Ask for constant input until user has inserted enough coins'''
    # Quarter, Dime, Nickel, Penny
    acceptedcoins = {
        'Q' : 0.25,
        'D' : 0.10,
        'N' : 0.05,
        'P' : 0.01,
    }
    cost = order['cost']
    inserted = 0.0
    change = 0.0
    # While user has not inserted enough coins, keep asking for coins
    while inserted < cost:
        print(f"You need: ${cost:.2f}")
        print(f"You have: ${inserted:.2f}")
        print("(Q) for Quarter, (D) for Dime, (N) for Nickel, (P) for Penny. (Cancel) to cancel transaction")
        choice = input("Please insert coins: ").upper()
        # If user's input is within accepted coins,
        # add the value of that coin to the inserted amount
        if choice in acceptedcoins:
            inserted += acceptedcoins[choice]
        # User can also type 'cancel' at any time to cancel the order
        elif choice.lower() == 'cancel' or choice.lower() == 'exit':
            print("\nOrder Cancelled\n")
            return False
        print("\n")
    # If user has inserted enough but is over the cost, dispense change
    # Otherwise, change will remain at 0
    if inserted > cost:
        change = inserted - cost
    print(f"You need: ${cost:.2f}")
    print(f"You have: ${inserted:.2f}")
    print(f"Your change is ${change:.2f}")
    # subtract the change from the amount inserted before returning value
    inserted -= change
        #if there's ever a functionality to dispense change this is where it would go
    # Return the amount inserted which is just the cost of the drink
    return inserted

def makeorder():
    '''Process the order here in this function'''
    # If this was a real coffee machine this would be where the process would initiate
    print("ORDER IN PROGRESS")
    sleep(1)

def checkReso(order, currResources):
    '''Check if order can be made with current resources, prints lacking ingredients and returns false if not enough
    returns True if order can be made'''
    check = {}
    check.update(order['ingredients'])
    for ingredients in check:
        check[ingredients] = currResources[ingredients] > check[ingredients]

    # if the checking variable contains any "False" values, print all keys with False values
    # Then return False
    if False in check.values():
        lacking = ''
        for ingredient in check:
            if check[ingredient] == False:
                lacking += f"{ingredient} "
        print(f"Not enough: {lacking}")
        print("Please contact staff, or choose a different drink")
        return False
    else:
        return True

def On():
    # First things to always initialize when turning on
    reso = {}
    reso.update(resources)
    reso['money'] = 0.0
    power = True
    print("Hello, welcome to the coffee machine :3")
    # -------------------------------------------------
    while power: # while power is True -> THis is the main loop of the program
        choice = input("What would you like? (Espresso/Latte/Cappuccino): ").lower()
        print("\n")
        if choice in menu: # ----------------if order input is valid ------------------
            order = menu[choice]
            canmake = checkReso(order, reso)
            if canmake == False:
                continue
            # if the input is valid and the order can be made, ask for deposit
            paid = insertcoins(order)

            # if paid returns false meaning user has cancelled order, restart loop
            if paid == False:
                continue

            # Deduct the needed resources to make the order from the current resources
            for ingredients in order['ingredients']:
                reso[ingredients] -= order['ingredients'][ingredients]
            paid = reso['money'] + float("{:.2f}".format(paid))
            reso['money'] = paid
            makeorder()

            print("Order finished! Hope you enjoy your drink")
            sleep(1)
            print("\n\n")
        # -----------------------------------------------------------------------------
        elif choice == 'report':
            report(reso)
        elif choice == 'off':
            exit()
        else:
            print("Sorry, I couldn't quite understand that, try again?")

#run main function
On()
