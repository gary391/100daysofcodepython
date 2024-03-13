from tkinter import *

# new window
# Initializing an instance of a class we get a window.
window = Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)

# Label
#
my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
# my_label.pack()

# This will allow the window to remain on the screen after the initialization.
# listen for the user input.

# This has to be at the end of the program.
my_label["text"] = "New Text"
my_label.config(text="New text")
my_label.grid(column=0, row=0) # This is relative to
my_label.config(padx=50, pady=50)

# Button

# Event listener
# def button_clicked():
#     print("I got clicked")
def button_clicked():
    # my_label.config(text="Button Got Clicked")
    my_label.config(text=input.get())


# Here the command is click which is executing a method.
# This in turn is returning "I got clicked"
button = Button(text="Click Me", command=button_clicked)
# This packs it to the screen, this is the layout on the screen.
# button.pack()
# Using the grid layout manager
button.grid(column=1, row=1)

def button_clicked_1():
    # my_label.config(text="Button Got Clicked")
    my_label.config(text=input.get())


# Here the command is click which is executing a method.
# This in turn is returning "I got clicked"
button1 = Button(text="Click Me", command=button_clicked_1)
# This packs it to the screen, this is the layout on the screen.
# button.pack()
# Using the grid layout manager
button1.grid(column=2, row=0)


# Entry
input = Entry(width=10)



# If you want to capture the value from the input.
# you can use input.get()
print(input.get())
# If you want something on the screen you will need a layout.
# We can use a pack()
# input.pack()

# Using the grid layout manager
input.grid(column=3, row=3)

window.mainloop()
