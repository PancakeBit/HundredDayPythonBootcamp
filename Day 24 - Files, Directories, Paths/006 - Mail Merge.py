# Get contents of input
with open("Input/Letters/starting_letter.txt", 'r') as letter:
    base_letter = letter.read()
with open("Input/Names/invited_names.txt", 'r') as letter:
    names = letter.read()

# Split names into list for ease of use
names = names.split()

# loop through the names and output each updated letter into Output folder
for name in names:
    with open(f'Output/ReadyToSend/{name}Letter.txt', 'w') as file:
        new_letter = base_letter.replace('[name]', name)
        file.write(new_letter)
