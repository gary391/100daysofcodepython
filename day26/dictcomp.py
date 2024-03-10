# Dictionary comprehension
# new_dict = {new_key: new_value for item in list}

# new_dict = {new_key:new_value for (key, value) in dict.items()}

# new_dict = {new_key:new_value for (key, value) in dict.items() if test}
import random
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie", "Rohan", "Rohit"]

student_score = {student: random.randint(1,100) for student in names}
print(student_score)

student_data = {'Alex': 38, 'Beth': 100, 'Caroline': 87, 'Dave': 93, 'Eleanor': 13, 'Freddie': 55, 'Rohan': 30, 'Rohit': 87}
passed_student = {student:value for (student, value) in student_data.items() if value > 60}
print(passed_student)


import pandas


student_dict1 = {
    "student" : ["Rohan", "Ham", "Jack"],
    "score": [56, 58, 87]
}
# # looping through dictionaries:
# for (key, value) in student_dict1.items():
#     print(key,value)

# Using Data frames
student_data_frame = pandas.DataFrame(student_dict1)
# print(student_data_frame)

# Loop through a data frame
# for (key, value) in student_data_frame.items():
#     print(value)

# Pandas data frame that allows to loop through the rows
for (index, row) in student_data_frame.iterrows():
    print(row.student)
    # if row.student == 'Rohan':
    #     print(f"Rohan: {row.score}")

# combining the data frame and dictionary comprehension
# {new_key:new_value for (key, value) in dict.items()}
# {new_value:new_key for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B", "Bravo'}

# TODO2. Create a list of the phen
