from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def On():
    power = True
    menu = Menu()
    coffeemaker = CoffeeMaker()
    money = MoneyMachine()
    # Note: wth is up with that MenuItem function, i can't figure out how to print the menu
    # menu.getitems only outputs the name not the required materials which SUCKKS
    # note to self, delete this when i figure out how to print all properties
    # ALSO NOTE: found out how, find_drink returns an object that has
    # everything as properties (name, ingredients, cost, etc)
    while power == True:
        # initialize currently making as none, reinitialize every loop
        making = None

        print(f"Menu Items: {menu.get_items()}")
        order = input("What would you like to order?: ").lower()
        if order == 'off':
            power = False
        elif order == 'report':
            coffeemaker.report()
            money.report()
        else:
            making = menu.find_drink(order)
        if making is not None:
            if coffeemaker.is_resource_sufficient(making): #if canmake
                if money.make_payment(making.cost): #if user input enough money
                    coffeemaker.make_coffee(making)

On()
