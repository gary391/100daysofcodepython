# File Not found
# with open("a_file.txt") as file:
#     file.read()

# KeyError
# a_dictionary = {"key": "value"}
# value = a_dictionary["non_existent_key"]


# IndexError
# fruit_list = ["apple", "banana", "pear"]
# fruit = fruit_list[3]


# TypeError
# text = "abc"
# print(text + 5)

"""
try: ---> Something that might cause an exception
except: --> Do this if there was an exception
else: --> Do this if there were no exceptions
finally: Do this no matter what happens - cleaning it up.
raise:

"""
# FileNotFound
# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["key"])
# except FileNotFoundError:
#     # print("The file doesn't exist")
#     file = open("a_file.txt", 'w')
#     file.write("something!")
# except KeyError as error_message:
#     print(f"The {error_message} does not exist.")
# else:
#     content = file.read()
#     print(content)
# finally:
#     # file.close()
#     # print("File was closed.")
#     raise TypeError("This is an error that I made up")

height = float(input("Height: ")) # Can't go above 3 meters
weight = float(input("Weight: "))

if height > 3:
    raise ValueError("Human Height should not be over 3 meters.")

bmi = weight / height ** 2
print(bmi)
