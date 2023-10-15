import random

art = '''
 ██████╗ ██╗   ██╗███████╗███████╗███████╗███████╗██████╗ 
██╔════╝ ██║   ██║██╔════╝██╔════╝██╔════╝██╔════╝██╔══██╗
██║  ███╗██║   ██║█████╗  ███████╗███████╗█████╗  ██████╔╝
██║   ██║██║   ██║██╔══╝  ╚════██║╚════██║██╔══╝  ██╔══██╗
╚██████╔╝╚██████╔╝███████╗███████║███████║███████╗██║  ██║
 ╚═════╝  ╚═════╝ ╚══════╝╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝
'''

def difficulty():
    while True:
        diff = input("Choose a difficulty (Easy, Hard, Psychic): ").lower()

        if diff == 'easy':
            return 10
        elif diff == 'hard':
            return 5
        elif diff == 'psychic':
            return 1
        else:
            print("\n\nDid you mistype? Try again")

def guessingGame():
    print("I'm thinking of a number between 1 and 100")

    lives = difficulty()
    gameover = False
    number = random.randint(1, 100)

    while not gameover:
        print(f"You have {lives} guesses remaining to guess the number")

        # simple input checker try catch value error for accepting int
        while True:
            try:
                guess = int(input("What's your guess?: "))
                break
            except ValueError:
                print("\n\nThat wasn't a number, try again")
                continue
        #spacing
        print("\n")
        # comparison between guess and randomly generated number
        if number == guess:
            print(f"Congratulations! You got it right, it was {number}")
            gameover = True
        elif number > guess:
            print("Too Low")
            lives -= 1
        elif number < guess:
            print("Too High")
            lives -= 1

        if lives < 1:
            print("You ran out of guesses")
            print(f"You lose, sorry, the number I was thinking was '{number}'")
            return

if __name__ == '__main__':
    print(art)
    print("Welcome to the Number Guessing Game!!!\n")
    while True:
        guessingGame()

        choice = input("\n\nWanna play again?(Y or N): ")

        if not choice == 'y' and not choice == 'yes':
            print("Thank you for playing!")
            break

