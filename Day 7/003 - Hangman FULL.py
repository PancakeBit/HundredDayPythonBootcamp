import random
import words
import time
import os

# list of words to choose from
# word_list = ["aaaaaa"]
word_list = words.words

# initialize needed variables
chosenword = word_list[random.randint(0, len(word_list) - 1)]
answer = []
lives = 0
wrongletters = ""

# make underlines for the chosen word in a new list
for i in chosenword:
    answer.append("_")

# Print Hangman ascii art once before entering loop
print(words.art[lives])

# While answer is incorrect AND mistakes are below limit, loop
while answer != list(chosenword) and lives != 6:
    print(answer)
    print(f"Wrong letters: {wrongletters.upper()}")
    # Ask for user input
    guess = input("Guess a letter: ").lower()
    # Reasign False to correct answer
    correctans = False

    # if guessed letter is in chosenword, mark answer as correct
    for i in range(len(chosenword)):
        if guess == chosenword[i]:
            answer[i] = chosenword[i]
            correctans = True

    # if correctans was UNCHANGED in previous check, add 1 mistake

    # clear() NOTE: apparently clear command does not work in the Pycharm console which is what I'm using
    # just imagine this is where the console clears before printing the status of man again

    if correctans == False:
        # Before marking input as incorrect, check first if the input was valid
        # There's definitely a better way of doing this but this is what I'm going with for now
        if len(guess) == 0:
            print("You didn't type anything, did you press enter by mistake?")
            time.sleep(0.5)
        elif len(guess) > 1:
            print("Only one letter at a time please!")
            time.sleep(0.5)
        # ---------------end input checking-------------
        elif guess not in wrongletters:
            print("That's not in the word, too bad, he hangs")
            wrongletters += guess
            lives += 1
        else:
            print(f"You've already guessed '{guess}'")
            time.sleep(0.5)
    # print current status of man
    print(words.art[lives])

print(f"The Correct Answer is {chosenword.upper()}")

if answer == list(chosenword):
    print(words.winner)
    print("Congratulations! You win the game and guessed the word!")
elif lives == 6:
    print("OOF, you made too many mistakes and this guy is dead now, tough luck, try again?")
print("GAMEOVER")
