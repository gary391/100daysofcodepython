# list comprehension
"""
new_list = [new_item for item in list]
"""
numbers = [1,2,3]

new_list = [n+1 for n in numbers]
print(new_list)

name = "Angela"
'''
new_list = [new_item for item in list]

_'''
letter_list = [letter for letter in name]
print(letter_list)

# Double the value in a list

# range(1,5) [2, 4, 6, 8]

double_list = [2 * i for i in range(1,5)]
print(double_list)

# Conditional list comprehension

'''
new_list = [new_item for item in list if test]
'''

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie", "Rohan", "Rohit"]

# Get name of the list that are less or equal to 4 letters or less
# new_list = [new_list for item in list if test]
new_list = [name for name in names if len(name)<= 4]
print(new_list)

long_name = [name.capitalize() for name in names if len(name)> 4]
print(long_name)


numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
square_numbers = [number*number for number in numbers]
print(square_numbers)


