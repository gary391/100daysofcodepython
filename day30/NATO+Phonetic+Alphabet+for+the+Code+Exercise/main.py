# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
#TODO 1. Create a dictionary in this format:
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

"""
Catch the KeyError when a user enters a character that is not in the dictionary 
Provide feedback to the user when an illegal word was entered.
Continue prompting the user to enter another word until they enter a valid word.
"""
# word = input("Enter a word: ").upper()
# is_true = True
# while is_true:
#     try:
#         output_list = [phonetic_dict[letter] for letter in word]
#         print(output_list)
#         is_true = False
#     except KeyError:
#         print("Sorry, only letters in the alphabet please.")
#         word = input("Enter a word: ").upper()

# Using function
def generator_phonetic():
    word = input("Enter a word: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generator_phonetic()
    else:
        print(output_list)

generator_phonetic()
