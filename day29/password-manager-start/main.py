from tkinter import *
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def pass_gen():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    # for char in range(nr_letters):
    #   password_list.append(random.choice(letters))
    [password_list.append(random.choice(letters)) for _ in range(nr_letters)]

    # for char in range(nr_symbols):
    #   password_list += random.choice(symbols)
    [password_list.append(random.choice(symbols)) for _ in range(nr_symbols)]

    # for char in range(nr_numbers):
    #   password_list += random.choice(numbers)
    [password_list.append(random.choice(numbers)) for _ in range(nr_numbers)]


    random.shuffle(password_list)

    # password = ""
    # for char in password_list:
    #   password += char
    password = "".join(password_list)
    password_input.delete(0, END)
    password_input.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
"""
When the user click on the 'ADD' button, the information from the 
website, email and password are saved in the csv file. 
1. Create a function named save()
2. Write to the data inside the entries to a data.txt file when the Add button is
   clicked
3. Each website, email, and password combination should be on a new line inside 
   the file.
4. All fields need to cleared after Add button is pressed.
"""

def save():
    # Note if you open a file in an append mode and that file doesn't
    # Python will automatically create the file.
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    # messagebox.showinfo(title="Title", message="Message")
    # This returns boolean value.

    # Validation step
    print(len(website))
    print(len(password))
    if (len(website) != 0) and (len(password) != 0):
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} " 
                           f"\nPassword: {password} \nIs it ok to save?")
        # Based on the output above method we can proceed further.
        if is_ok:
            with open("data.txt", 'a') as file:
                content = f'{website} | {email} | {password}\n'
                file.write(content)
            # This will clean up the entries by deleting the entries from a specific index
            # to another specific index
            website_input.delete(0, END)
            email_input.delete(0, END)
            password_input.delete(0, END)
    else:
        messagebox.showinfo(title="Warning!", message="Please don't leave any fields empty!")



# ---------------------------- UI SETUP ------------------------------- #

# Window
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
# We need canvas to layer text on top on a image
canvas = Canvas(width=200, height=200)
# Getting the image using the tkinter's PhotoImage class that take the location of the image as an input.
lock_img = PhotoImage(file="logo.png")
# This is telling canvas to create an image inside the canvas
# It takes three arguments of which first and second are the location of the image
# and the third is the image itself.
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

# Label
website = Label(text="Website: ")
website.grid(column=0, row=1)
email_usr = Label(text="Email/Username: ")
email_usr.grid(column=0, row=2)
password = Label(text="Password: ")
password.grid(column=0, row=3)

# Entry
website_input = Entry(width=35)
# If you want to capture the value from the input.
# you can use input.get()

print(website)
# Using the grid layout manager
website_input.grid(column=1, row=1, columnspan=2)
# This will allow to start a cursor in the input box.
website_input.focus()

email_input = Entry(width=35)
email = email_input.get()
print(email)
email_input.grid(column=1, row=2, columnspan=2)
# This will add the text at the zeroth position.
# There is another constant called "END".
# END will allow you to enter any text after the email.
email_input.insert(0, 'abc@xyz.com')
password_input = Entry(width=21)
# password = pass_gen()
# print(password)

password_input.grid(column=1, row=3)

# Button

button_gp = Button(text="Generate Password",  command=pass_gen)

button_gp.grid(column=2, row=3)

button_add = Button(text="Add", width=36, command=save)
button_add.grid(column=1, row=4, columnspan=2)

# For window to show up we have to use windowmainloop
# Did something happen or did something happen?
window.mainloop()
