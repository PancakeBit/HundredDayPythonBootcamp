# User Console Input to NATO Phonetic Alphabet Translator
import pandas

list = pandas.read_csv('nato_phonetic_alphabet.csv')

nato_dict = {value.letter:value.code for (key, value) in list.iterrows()}

userinput = input("What do you want to translate?: ")
translated= [nato_dict[letter] for letter in userinput.upper()]
print(translated)