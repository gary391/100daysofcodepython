from tkinter import *
import requests

def get_quote():
    # pass
    #Write your code here.
    """
    1. Make a get() request to the kanye-quotes endpoint or API https://api.kanye.rest
    2. Raise an exception if the request returned an unsuccessful status code.
    3. Parse the JSON to obtain the quote text.
    4. Display the quote in the canvas 'quote_text' widget.
    
    """
    response = requests.get(url='https://api.kanye.rest')
    # Raises an exception if the response in not 200 OK
    response.raise_for_status()
    data = response.json()
    quote =  data['quote']
    # In order to pass the quote to the canvas is by using itemconfig
    # and passing in the value where we have the text in the quote_text field.
    canvas.itemconfig(quote_text, text=quote)




window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 30, "bold"), fill="white")
# quote_text = canvas.create_text(150, 207, text=quote, width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)



window.mainloop()