
for i in range (1,101):
    display = ""
    if i % 3 == 0:
        display += "Fizz"
    if i % 5 == 0:
        display += "Buzz"
#    Also very easy to add more conditions on
#    if i % 6 == 0:
#        display += "Hoof"
    # IF the display variable is blank
    if display == "":
        display = str(i)
    print(display)


