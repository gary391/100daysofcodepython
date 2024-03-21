from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1#25
SHORT_BREAK_MIN = 1#5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    # reset the check marks
    window.after_cancel(timer)
    # reset the timer to "00:00"
    canvas.itemconfig(timer_text, text='00:00')
    # change the title back to timer
    timer_label.config(text="Timer", fg=GREEN)
    # reset the marks
    check_label.config(text="", bg=YELLOW)
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    print("Starting the timer")
    global reps
    work_sec = WORK_MIN * 60 # 25 mins cycles
    short_break_sec = SHORT_BREAK_MIN * 60 # 5 mins
    long_break_sec = LONG_BREAK_MIN * 60 # 20 mins
    reps = reps + 1

    #If it's the 8th rep: (This comes after 4 work sessions)
    if reps % 8 == 0:
        print(type(long_break_sec))
        print(f'long_break_sec: {long_break_sec}')
        # timer_label = Label()
        timer_label.config(text="Break", fg=RED)
        # timer_label.grid(column=2, row=1)  # This is relative to
        # update_label(long_break_sec)
        count_down(long_break_sec)
    # If it's the 2nd/4th/6th rep:
    elif reps % 2 == 0:
        print(type(short_break_sec))
        print(f'long_break_sec: {short_break_sec}')
        # timer_label = Label()
        timer_label.config(text="Break", fg=PINK)
        # timer_label.grid(column=2, row=1)  # This is relative to
        # update_label(short_break_sec)
        count_down(short_break_sec)
        # If it's the 1st/3rd/5th/7th/ rep:
    else:
        print(type(work_sec))
        print(f'work_sec: {work_sec}')
        timer_label.config(text="Work", fg=GREEN)

        # update_label(work_sec)
        count_down(work_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
# Event driven
def count_down(count):
    print(f'count: {count}')
    print(type(count))

    "For counting using time denominations i.e. 00:00"
    count_min = math.floor(count / 60) # Returns the largest whole number.
    count_sec = count % 60  # Returns the remaining number of seconds
    # Python dynamic typing, which allow variables to change the type depending on the value
    # being assigned to the variable.
    if count_sec == 0:
        count_sec = "00"
    elif count_sec < 10:
        count_sec = f'0{count_sec}'
    canvas.itemconfig(timer_text, text=f'{count_min}:{count_sec}')
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        # Every two sessions we get one check mark
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
        check_label.config(text=marks)

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
# specify the layout using either the pack or some other method.
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=2, row=2)
# canvas.pack()


# Add the image to the Canvas
# Make sure the image is at the center of the canvas
#
# button = Button(text="Start", command=button_clicked)
button_start = Button(text="Start",  highlightthickness=0, bg=YELLOW,  command=start_timer)
button_start.grid(column=1, row=3)

# button = Button(text="Start", command=button_clicked)
button_reset = Button(text="Reset",  highlightthickness=0, bg=YELLOW, command=reset_timer)
button_reset.grid(column=3, row=3)


# Label

timer_label = Label(text="Timer", fg=GREEN,  bg=YELLOW, font=(FONT_NAME, 50, "bold"))
timer_label.grid(column=2, row=1) # This is relative to
# Button

check_label = Label(fg=GREEN,  bg=YELLOW, font=(FONT_NAME, 40, "bold"))
check_label.grid(column=2, row=4) # This is relative to

# For window to show up we have to use windowmainloop
# Did something happen or did something happen?
window.mainloop()