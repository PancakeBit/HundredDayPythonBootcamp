def greet(name = "", location = ""):
    print(f"Hello {name}")
    print(f"What's it like over there in {location}?")

# these can actually just be named "name" and "location" since
# they're outside the function, no naming shenanigans will happen
# but let's be professional
inputname = input("What is your name?: ")
inputlocation = input("What country do you live in?: ")

#greet(inputname, inputlocation) -> This code for normal people
greet(name = inputname, location = inputlocation) # -> this code for testing

# because the parameters are initialized, function 'greet' needs no arguments
# in order to run and can be called only giving specific parameters arguments
greet(location = "Sweden")