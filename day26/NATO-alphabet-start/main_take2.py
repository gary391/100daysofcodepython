# combining the data frame and dictionary comprehension
# {new_value:new_key for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B", "Bravo'}

# TODO 2. Create a list of the phonetic code words from a word that the
# user inputs.

import pandas
output = []
# reading a csv using pandas library
data = pandas.read_csv("nato_phonetic_alphabet.csv")
# print(type(data))
# print(data)

# Using dictionary comprehension create a dictionary
nato_dict = {row.letter:row.code for (index, row) in data.iterrows()}
print(nato_dict)
# print(type(nato_dict))

user_input = input("Enter a word: ").upper()
# format_user_input = user_input.upper()

# Using the regular for loop
# for letter in user_input:
#     for k,v in nato_dict.items():
#         if letter == k:
#             output.append(v)

# Using list comprehesion
# [new_list for item in list]

# How to create a list from a dictionary using a list which has elements as the key of the dictionary
print([nato_dict[letter] for letter in user_input])

# print(output)

