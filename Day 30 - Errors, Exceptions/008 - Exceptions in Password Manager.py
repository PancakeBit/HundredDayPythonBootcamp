# The objective of this exercise is to fix a problem in the Password Manager GUI app
# If a file does not yet exist, create that file
# Luckily I already thought of that before and have an if case for it
# This is the code snippet this activity is looking for
# Converted to a try except format
def do_the_thing():
    print("Pretend the password app is here")

try:
    open('file.txt', 'r')
except FileNotFoundError:
    open('file.txt', 'w')
    do_the_thing()
else:
    do_the_thing()