# Don't change this code
namesString = input("Give me everybody's names, separated by a comma. ")
names = namesString.split(",")
# Don't change this code
import random

buyer = names[random.randint(0, len(names)-1)]

print(f"The buyer for tonight will be {buyer}")