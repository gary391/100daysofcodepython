from tkinter import *

# new window
# Initializing an instance of a class we get a window.
window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=100, height=80)
window.config(padx=20, pady=20)



# Entry
input = Entry(width=10)

# If you want to capture the value from the input.
# you can use input.get()
print(input.get())
# If you want something on the screen you will need a layout.
# We can use a pack()
# input.pack()

# Using the grid layout manager
input.grid(column=1, row=0)


# Label
#
my_label = Label()
# my_label.pack()

# This will allow the window to remain on the screen after the initialization.
# listen for the user input.

# This has to be at the end of the program.
# my_label["text"] = "New Text"
my_label.config(text="is equal to")
my_label.grid(column=0, row=1) # This is relative to
# my_label.config(padx=50, pady=50)

my_label1 = Label()
my_label1.config(text="Miles")
my_label1.grid(column=2, row=0) # This is relative to

my_label2 = Label()
my_label2.config(text="Km")
my_label2.grid(column=2, row=1) # This is relative to
# Button

my_label3 = Label()
my_label3.config(text="0")
my_label3.grid(column=1, row=1) # This is relative to



# Event listener
# def button_clicked():
#     print("I got clicked")
def button_clicked():
    # my_label.config(text="Button Got Clicked")
    # miles_value = int((input.get() * 1.6))
    new_value = int(input.get())

    miles = new_value * 1.6
    my_label3.config(text=miles)


# Here the command is click which is executing a method.
# This in turn is returning "I got clicked"
button = Button(text="Calculate", command=button_clicked)
# This packs it to the screen, this is the layout on the screen.
# button.pack()
# Using the grid layout manager
button.grid(column=1, row=2)



window.mainloop()
