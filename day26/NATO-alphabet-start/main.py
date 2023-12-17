student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
#{"A": "Alfa", "B": "Bravo"}

nato_data = pandas.read_csv("nato_phonetic_alphabet.csv")
# print(nato_data)
# for index, row in nato_data.iterrows():
#     print(row.code)
nato_dict = {row.letter:row.code for index, row in nato_data.iterrows()}
print(nato_dict)
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

user_name = input("Enter your name: ")
# split_name = [letter.upper() for letter in user_name]
# print(split_name)
# nato_name = [v for i in split_name for k,v in nato_dict.items() if k == i]
# print(nato_name)
output_name = [nato_dict[letter.upper()] for letter in user_name]
print(output_name)

