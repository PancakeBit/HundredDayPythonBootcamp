total = input("What was the total bill?: ")
tip = input("How much would you like to tip in percentage?(2,5,10): ")
people = input("How many people will be splitting the bill?: ")

total = float(total)
tip = float(tip)
people = int(people)

# This is code for if tip is flat amount: perPerson = (total+tip) / people
perPerson = (((tip * 0.01) * total)+total) / people

print(f"Each person should pay: {perPerson:.2f}")
