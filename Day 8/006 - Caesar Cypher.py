alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(text="", shift=1):
    shiftText = list(text.lower())
    afterShift = []

    #Encrypt text
    # For every letter in given text
    # The for lettercounter loop can also be done with the index function but i prefer my own way
    for textcounter in range(len(shiftText)):
        # Find what index that letter is in the alphabet
        #if the current letter is not in the alphabet, just append it
        if shiftText[textcounter] not in alphabet:
            afterShift.append(shiftText[textcounter])
        else:
            for lettercounter in range(len(alphabet)):
                # When index of letter is found, add shift variable to get shifted letter
                if shiftText[textcounter] == alphabet[lettercounter]:
                    lettershift = lettercounter + shift
                    # While the shifted letter is beyond the alphabet, go back to beginning of alphabet
                    while lettershift > 25:
                        lettershift -= 26
                    # Append the index of the shifted letter to a new list
                    afterShift.append(alphabet[lettershift])
    return ''.join(afterShift)

#do decrypt but backwards
# I'll use the index function way for this function
def decrypt(text="", shift=1):
    shiftText = list(text.lower())
    afterShift = []

    # For every letter in given text
    for letter in shiftText:
        # if it's not in the alphabet, just add it
        if letter not in alphabet:
            afterShift.append(letter)
        # If it IS in the alphabet, get the index of that letter
        else:
            number = alphabet.index(letter)
            # Remove the shift or deshift because it's decoding time
            lettershift = number - shift
            # while it is negative, go back to the beginning
            #while lettershift > 25:
            #    lettershift += 26
            # I'll try to use the modulo operator for this function
            # Modulo works for negative numbers and will provide the remainder of it when it gets positive
            # example: -30 % 26 = 22 because it goes from -30(+26) = -4(+26)= 22
            # If the shifted letters are less than 26, divide it by 26 and get the remainder
            if lettershift < 26:
                lettershift = lettershift % 26
            #append the shifted position to a list
            afterShift.append(alphabet[lettershift])
    return ''.join(afterShift)

runagain = 'y'
while runagain == 'y' or runagain == 'yes':
    try:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
    except:
        print("Something went wrong with your inputs...")
        break

    if direction.lower() == "encode":
        print(f"Your encoded message is: {encrypt(text, shift)}")
    elif direction.lower() == "decode":
        print(f"Your encoded message is: {decrypt(text, shift)}")
    else:
        print("Sorry could not understand that, try again")

    runagain = input("Do you want to run the program again?: ").lower()

print("Thank you for using the Caesar Cypher program. See ya boi")