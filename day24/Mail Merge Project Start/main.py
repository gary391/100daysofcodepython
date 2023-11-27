# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
'''
f = open("demofile.txt", "r")
print(f.readlines())
'''
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
'''
txt = "I like bananas"
x = txt.replace("bananas", "apples")
print(x)
'''
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
'''
txt = "     banana     "
x = txt.strip()
print("of all fruits", x, "is my favorite")
'''


INVITES = './Input/Names/invited_names.txt'
STARTING_LETTER = './Input/Letters/starting_letter.txt'
OUTPUT = './Output/ReadyToSend'


def read_names_file(file_path):
    with open(file_path, mode="r") as file:
        return (file.readlines())


def replace_name_in_letter(file_path, invitee):
    with open(file_path, mode='r') as file:
        text = file.read()
        x = text.replace("[name]", invitee)
        return x


def write_letter(OUTPUT, content, invitee):
    with open(OUTPUT+f'/letter_for_{invitee}.txt', mode='w') as file:
        file.write(content)


for name in read_names_file(INVITES):
    letter = replace_name_in_letter(STARTING_LETTER, name.strip())
    write_letter(OUTPUT, letter, name.strip())
