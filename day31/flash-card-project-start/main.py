from tkinter import *
from tkinter import messagebox
BACKGROUND_COLOR = "#B1DDC6"

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
my_img = PhotoImage(file="/Users/gauyada/WorkDocs/03_KNOWLEDGE/09_PYTHON/33_100DaysOfCode/100daysofcodepython/day31/flash-card-project-start/images/card_front.png")
canvas.create_image(100, 112, image=my_img)
canvas.grid(row=2, column=2)

# Labels
# website_label = Label(text="Website:")
# website_label.grid(row=1, column=0)
# email_label = Label(text="Email/Username:")
# email_label.grid(row=2, column=0)
# password_label = Label(text="Password:")
# password_label.grid(row=3, column=0)
#
# # Entries
# website_entry = Entry(width=21)
# website_entry.grid(row=1, column=1)
# website_entry.focus()
# email_entry = Entry(width=35)
# email_entry.grid(row=2, column=1, columnspan=2)
# email_entry.insert(0, "angela@gmail.com")
# password_entry = Entry(width=21)
# password_entry.grid(row=3, column=1)
#
# # Buttons
# search_button = Button(text="          Search         ", command=find_password)
# # search_button = Button(text="Generate Password")#,command=search_password)
# search_button.grid(row=1, column=2)
# generate_password_button = Button(text="Generate Password", command=generate_password)
# generate_password_button.grid(row=3, column=2)
# add_button = Button(text="Add", width=36, command=save)
# add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()