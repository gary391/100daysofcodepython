from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


# ---------------------------- UI SETUP ------------------------------- #
# This is the first part - 1
# Window
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
# We need canvas to layer text on top on a image
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
# Getting the image using the tkinter's PhotoImage class that take the location of the image as an input.
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
canvas.grid(column=2, row=3)
# specify the layout using either the pack or someother method.
canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=2, row=2)
# canvas.pack()


# Add the image to the Canvas
# Make sure the image is at the center of the canvas
#
# button = Button(text="Start", command=button_clicked)
button_start = Button(text="Start",  highlightthickness=0, bg=YELLOW)
button_start.grid(column=1, row=3)

# button = Button(text="Start", command=button_clicked)
button_stop = Button(text="Reset",  highlightthickness=0, bg=YELLOW)
button_stop.grid(column=3, row=3)


# Label

timer_label = Label()
timer_label.config(text="Timer", fg=GREEN,  bg=YELLOW, font=(FONT_NAME, 50, "bold"))
timer_label.grid(column=2, row=1) # This is relative to
# Button

check_label = Label()
check_label.config(text="✔", fg=GREEN,  bg=YELLOW, font=(FONT_NAME, 40, "bold"))
check_label.grid(column=2, row=4) # This is relative to


# For window to show up we have to use windowmainloop
window.mainloop()