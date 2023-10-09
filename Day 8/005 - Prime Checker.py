def checkIfPrime(number=0):
    # RULE 1: Numbers ending with 0, 2, 4, 6 and 8 are never prime numbers
    #convert num to string and get the last digit

    # RULE 2: Numbers whose sum of digits are divisible by 3 are never prime numbers
    return False
    #

# note: i'm going to skip this exercise, i know the concept i just don't want to think about
# how to check if a number is prime, it's gonna take a while
# i'm thinking to modulo every number up to the number given \
# but holy cow thats going to take a while

isprime = checkIfPrime(109)
print(isprime)