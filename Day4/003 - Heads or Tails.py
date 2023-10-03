import random

class coingame:
    def __init__(self):
        answer = input("Heads or Tails?: ").lower()
        coin = random.randint(0,1)

        if answer != 'heads' or answer != 'tails':
            print("Please type only \"Heads\" or \"Tails\"")
            exit()

        if coin == 0:
            coin = "heads"
        elif coin == 1:
            coin = "tails"

        if answer == coin:
            print(f"It's {coin}, you win! Try again?(Y or N): ")
        elif answer != coin:
            print(f"Too bad, it's {coin}, Try again?(Y or N): ")

        answer = input().lower()

        if answer == 'y':
            coingame()

if __name__ == '__main__':
    coingame()

    print("Thank you for playing!")