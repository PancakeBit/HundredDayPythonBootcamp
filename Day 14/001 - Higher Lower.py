import art
from random import randint, shuffle
from time import sleep

# Needs more data
testdata = [
    {
        "name" : "Uberhaxornova",
        "followers" : 12380,
        "description" : "A gaming youtuber from 2013"
    },
    {
        "name": "Pewdiepie",
        "followers": 901239,
        "description": "A Sugondese PUBG professional"
    },
    {
        "name": "Prof Lando",
        "followers": 12390,
        "description": "A fembologist with a phD in waifuism"
    }
]

print(art.title)
print("Try and guess who has more Followers between the two Online Personalities\n")

def calculateanswer(answer="", p1=0, p2=0):
    if answer.lower() == 'a':
        return p1 >= p2
    elif answer.lower() == 'b':
        return p2 >= p1

def askforinput(p1, p2, score):
    print(f"A: {p1['name']}, {p1['description']}")
    print(art.vs)
    print(f"B: {p2['name']}, {p2['description']}")
    print(f"Current Score: {score}")
    while True:
        ans = input(f"Who has more followers? A or B? : ")
        if ans.lower() == 'a' or ans.lower() == 'b':
            return ans
        elif ans.lower() == 'quit':
            return ans
        else:
            print("Please type 'A' or 'B'")

def game():
    # How do I make sure that the data set does not repeat?
    # Thinking 1: if player1==player2 then player2.pop?
    #             error if player2 is last element of list
    # Very minor problem either way, if both items are equal it is automatically correct
    deck = []
    score = 0
    deck = resetdata(deck)
    #assign choice A outside of loop
    player1 = deck.pop()
    while True:
        #if deck is empty repopulate it, still has problem of repeating data
        if len(deck) == 0:
            deck = resetdata(deck)
        #assign 2nd choice
        player2 = deck.pop()

        ans = askforinput(player1, player2, score)
        if ans == 'quit':
            print("GAME HAS ENDED")
            return

        result = calculateanswer(ans, player1['followers'], player2['followers'])
        # if result is false (wrong) end game
        if not result:
            print(art.wrong)
            print(f"Your Final Score is: {score}")
            return True
        # otherwise result is correct so add 1 to score
        score +=1
        print(art.correct)
        sleep(0.5)
        # make choice B into choice A
        player1 = player2

def resetdata(deck):
    deck.extend(testdata)
    shuffle(deck)
    return deck

gameover = False
while gameover == False:
    game()

    while True:
        choice = input("Do you want to play again?: ").lower()
        if choice == 'y' or choice == 'yes':
            gameover = False
            break
        else:
            gameover = True
            print("Thank you for playing!")
            break

