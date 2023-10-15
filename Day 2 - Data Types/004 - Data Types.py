# Write a program that adds the digits in a 2 digit number. if the input was 35 then the output should be 3 + 5 = 8
# WARNING. Do not change the code in lines 1-3. Your program should work for different inputs e.g. any two digit number.
two_digit_number = input("Type a two digit number: ")
# -----------------------
if not two_digit_number.isnumeric():
    print("That's not a number!")
    exit()

if len(two_digit_number) != 2:
    print("That's not 2 digits!")
    exit()

num1 = two_digit_number[0]
num2 = two_digit_number[1]

num1 = int(num1)
num2 = int(num2)

num1and2 = num1 + num2

print(num1, " + ", num2, " = ", num1and2)
