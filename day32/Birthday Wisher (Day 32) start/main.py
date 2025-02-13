import smtplib
import pprint as pp
import random
import datetime as dt

my_email = "codewithgary@gmail.com"
password = "#############"

#
# # Using context manager we can avoid explicitly closing the connection.
#
# with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
#     # Create a tls connection
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email, to_addrs="codewithgary@yahoo.com",
#                         msg="Subject: Second Email! \n\nThis is the body of my 2nd email.")


# import datetime as dt
#
now = dt.datetime.now() # Current date time.
print(type(now))
print(f"Year: {now.year}")
if now.year == 2025:
# print("Prioritize health")
# print(f"Month: {now.month}")
# print(f"Day: {now.day}")
    print(f"Day of the week: {now.weekday()}")
#
date_of_birth = dt.datetime(year=1995, month=12, day=15)
print(date_of_birth)


"""
Objective: Send a motivational quote via email on the current weekday (You can change it to Monday afterwords)
Hints:
1. Use the datetime module to obtain the current day of the week.
2. Open the quotes.txt file and obtain a list of quotes.
3. Use the random module to pick a random quotes from your list of quotes.
4. Us the smtplib  to send the eamil to yourself.

"""


# Check which day of the week it is?
#  If the date of the week is monday
# open the text file and select a random string
# seend that random string to the email address


def random_quote():
    #TODO pass in the location of the file here instead of hardcoding the text filename.
    with open('quotes.txt') as quotes:
        quotes_list = quotes.read().splitlines()
        return random.choice(quotes_list)


def email_quote():
    # Using context manager we can avoid explicitly closing the connection.
    quote = random_quote()
    msg = f"Subject: Quote of the day! \n\n {quote}"
    with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
        # Create a tls connection
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="codewithgary@gmail.com",
                            msg=msg)


now = dt.datetime.now()

if now.weekday() == 5:
    email_quote()
