"""
file = open ("my_file.txt")
contents = file.read()
print(contents)
file.close() # why do we need to close the file? As python an close any time.

"""

with open("../../desktop/my_file.txt", mode="a") as file:
    # contents = file.read()
    # print(contents)

    file.write("\nNew Text.")