# Simple Calculator program
# Does NOT have input checking for some inputs (for the numbers in particular)
# but just like, only type numbers, adding a checker and a while loop for each would be
# way too much work on a simple command line calculator
# use your phone or something

# Define operations
def add(number1,number2):
    return number1 + number2

def subtract(number1,number2):
    return number1 - number2

def multiply(number1,number2):
    return number1 * number2

def divide(number1,number2):
    return number1/number2

def calculator():
    shouldcont = True
    secondinput = False

    # While the program should continue, do this
    while shouldcont == True:
        # If it's the FIRST time the user is inputting, ask for the first number
        if secondinput == False:
            num1 = float(input("Input the First Number: "))
        # Otherwise, get the result from the previous operation
        else:
            num1 = result
        op = input("Input the operation (+, -, *, /): ").lower()
        num2 = float(input("Input the Second number: "))

        # If user input something weird for the operator, restart the current loop
        # Not the most efficient way to do this since it's AFTER asking for another input
        # but it works
        if op not in operations:
            print("Sorry that wasn't a valid input, can you try again?")
            continue

        # Get key from dictionary 'operations' and assign it
        func = operations[op]
        # Run func and assign it to result
        result = func(num1, num2)
        print(f"{num1} {op} {num2} = {result}")

        # IF user wants to start again type 'new' which sets secondinput to
        # False which makes them input the first number again
        userchoice = input(
            f"Do you want to continue using '{result}' as the First Number?(Y or N, or type 'new' for a new calculation): ")
        if userchoice.lower() == 'y' or userchoice.lower() == 'yes':
            secondinput = True
        elif userchoice.lower() == 'new':
            secondinput = False
        else:
            shouldcont = False
            break

# Store operations in a dictionary
# Python allows keywords to be stored in a dictionary which can be called when needed
operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide,
}

calculator()
print("Thank you for using the Calculator Program!")
