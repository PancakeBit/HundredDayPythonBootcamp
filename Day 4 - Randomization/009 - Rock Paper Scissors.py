import random

# Rock
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

player = 0
cpu = 0

janken = [rock, paper, scissors]

try:
    userinput = int(input("Janken! Choose 0 for Rock, 1 for Paper, 2 for Scissors: "))
except ValueError:
    print("You typed something that's not a number, you lose")
    exit()

if userinput < 0 or userinput > 2:
    print("You typed an invalid number, you lose")
    exit()

cpuInput = random.randint(0, 2)

print("You chose: ")
print(janken[userinput])

print("The computer chose: ")
print(janken[cpuInput])

if userinput == cpuInput:
    print("It's a tie!")
elif (userinput == 0 and cpuInput == 2) \
        or (userinput == 1 and cpuInput == 0) \
        or (userinput == 2 and cpuInput == 1):
    print(" You win! Congratulations!")
else:
    print("You lose! Try again next time")
