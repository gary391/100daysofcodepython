# dictionary comprehension
# new_dict = {new_key: new_value for item in list}
# Where list can be any iterable list, range
# We can also create a new dictionary as well, using a value of an existing dictionay
# new_dict = {new_key: new_value for (key,value) in dict.items()}
# new_dict = {new_key: new_value for (key,value) in dict.items() if test}

student_dict = {
    "student": ["Sonu", "Minku", "Veer"],
    "score": [56, 76, 98]
}
import pandas

student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)

# loop through a data frame
# for (key, value) in student_data_frame.items():
#     print(key,value)

# Loop through rows of a data frame instead of the columns
for (index, row) in student_data_frame.iterrows():
    # print(row) # panda series object
    # print(row.student)
    # print(row.score)

    if row.student == 'Veer':
        print(row.score)
