import random

deck = {
    "A": 11,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 10,
    "Q": 10,
    "K": 10,
}

#### IMPORTANT also add check if HOUSE gets blackjack
def calculatewinner(player, house):
    housedraws = True
    while housedraws == True:
        totalplayer =0
        totalhouse =0
        numaces =0
        # get accurate total
        for card in player:
            totalplayer += deck[card]
            if card == 'A':
                numaces += 1
        #check number of aces for both
        while totalplayer > 21 and numaces > 0:
            totalplayer -= 10
            numaces -= 1

        # get accurate total
        for card in house:
            totalhouse += deck[card]
            if card == 'A':
                numaces += 1
        while totalhouse > 21 and numaces > 0:
            totalhouse -= 10
            numaces -= 1

        print(f"Your cards are: {player} = {totalplayer}")
        print(f"The house has: {house} = {totalhouse}")
        # house AI
        # if total of house is greater than 21, house loses player wins
        if totalplayer == 21 and totalhouse != 21:
            win()
            return
        if totalhouse > 21:
            win()
            housedraws = False
        # if total of house is greater than total of player without going over 21, house wins player loses
        elif totalhouse > totalplayer:
            lose()
            housedraws = False
        # if total of player is greater than 16 and both are equal, call draw
        # House is not risky
        elif totalplayer > 16 and totalplayer == totalhouse:
            print("It's a draw")
            housedraws = False
        # IF neither player or house has won, number is less than 16, and house will lose
        # draw another card and loop again
        elif totalplayer > totalhouse:
            print("The computer draws a card")
            house.append(hit())
        else:
            house.append(hit())

def win():
    print("You win!")

def lose():
    print("You lost, sorry")

def hit():
    cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    draw = cards[random.randint(0, len(cards) - 1)]
    #draw = cards[0]
    return draw

def play():
    print("BLACKJACK")
    print("\n\n\n\n\n\n")
    #input("Do you want to play Blackjack?: ")

    # Initialize playern hand and hous  e hand then add 2 cards to both
    currenthand = [hit(), hit()]
    househand = [hit(), hit()]

    while True:
        total = 0
        numaces =0
        # Get total of current hand
        for card in currenthand:
            total += deck[card]
            if card == 'A':
                numaces += 1
        while total > 21 and numaces > 0:
            total -= 10
            numaces -= 1

        # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! IN PROGRESS !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        # Currently, House CANNOT win if a blackjack is drawn first hand
        # Which means they also cannot 'draw' should both player and house get blackjack on the first hand
        # ALSO IN PROGRESS - a proper scoring system or a money tracker, should be easy enough to add
        print(f"Your cards are: {currenthand} = {total}")
        print(f"The house has: ['{househand[0]}', '▒▒']")

        # Calculate total, if it goes over 21 while you have an Ace in your hand, it becomes a 1
        if total > 21:
            print("You went over 21")
            lose()
            return
        elif total == 21:
            calculatewinner(currenthand, househand)
            return
        # Ask for hit or stand, if player wants to hit then add another card and calculate if it is over 21
        # if user wants to stand then go to calculate winner and end the play function
        # if input unrecognized, repeat loop
        while True:
            choice = input("(Hit) or (Stand)?: ").lower()

            if choice == 'hit':
                currenthand.append(hit())
                break
            elif choice == 'stand':
                calculatewinner(currenthand, househand)
                return
            else:
                print("could not quite get that, gomen")
                continue

while True:
    play()

    choice = input("Play again?: ").lower()
    if not choice == 'y' and not choice == 'yes':
        break

