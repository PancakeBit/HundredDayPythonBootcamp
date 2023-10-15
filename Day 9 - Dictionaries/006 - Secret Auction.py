
# This "Secret" auction really only works for console based compilers
# clear screen does not work in Pycharm which makes it difficult to keep inputs secret
# in substitute of that, i'm just going to write like 50 new lines to bury the text

# This program still has a few holes like input checking, but let's not focus on that
import art
print(art.art)
print("Welcome to the Secret Auction")

allbids = {}

def calculateWinner():
    highestbid = 0
    winners = []
    for name in allbids:
        if allbids[name] > highestbid:
            highestbid = allbids[name]
            winners = [name]
        elif allbids[name] == highestbid:
            #print("two have the highest")
            winners.append(name)
    print("Congratulations to", winners, "with a bid of", highestbid)

cont = True
biddernumber = 1
while cont == True:
    print(f"Bidder #{biddernumber}")
    invalidinput = True

    name = input("What is your name?: ")
    bid = int(input("How much do you bid?: "))

    allbids[name] = bid

    contChoice = input("Are there any other Bidders?(Yes or No): ").lower()
    # if it's not Y or Yes
    if contChoice.lower() == 'y' or contChoice.lower() == 'yes':
        biddernumber += 1
        for i in range(50):
            print("\n")
    elif contChoice.lower() == 'n' or contChoice.lower() == 'no':
        cont = False
    else:
        print("Sorry couldn't quite understand that, can you try again?")

calculateWinner()