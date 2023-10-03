# Don't change this code
print("Welcome to Python Pizza Deliveries!")
size = input("What size Pizza do you want? (S, M, or L): ")
pepperoni =  input("Do you want pepperoni? (Y or N): ")
extra_cheese = input("do you want extra cheese? (Y or N): ")
# Don't change this code

total = 0

if size == 'S':
    total += 15
elif size == 'M':
    total += 20
elif size == 'L':
    total += 25

if pepperoni == 'Y':
    if size == 'S':
        total += 2
    else:
        total += 3

if extra_cheese == 'Y':
    total += 1

print(f"Your final bill is ${total}")