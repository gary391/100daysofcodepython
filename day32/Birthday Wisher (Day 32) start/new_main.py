# import smtplib
#
# my_email = "codewithgary@gmail.com"
# to_email = "codewithgary@yahoo.com"
# # way to connect to gmail
# password = "aged qjyq zeii gyxs"
# with smtplib.SMTP("smtp.gmail.com", 587) as connection:
#     connection.starttls() # enable tls connection
#     connection.login(my_email, password=password)
#     connection.sendmail(from_addr=my_email,to_addrs=to_email,
#                         msg="Subject:Hello\n\n This is the body of my email.")
#     # connection.close()
#
# import datetime as dt
# now = dt.datetime.now()
# year = now.year
# month = now.month
# day = now.day
# day_of_week = now.weekday()
# print(day_of_week)
#
# date_of_birth = dt.datetime(year=1980, month=1, day=1, hour=0, minute=0, second=0)
# print(dat
# date_of_birth)
"""
Objective: send a motivational quote via email on the current weekday (you can change it to saturday or sunday.

Hints:
1. Use th dateime module to obtain the current day of the week.
2. Open the quotes.txt file and obtain a list of quotes.
3. Use the random module to pick a random quote from your list of quotes.
4. Use the smtplib to send the email to yourself.
"""

import random
import datetime as dt

import smtplib
def current_weekday():
    now = dt.datetime.now()
    return now.weekday()


def get_quotes(file_location):

    with open(file_location) as quotes_file:
        quotes = quotes_file.readlines()
        return random.choice(quotes)

def sent_email(file_location):
    my_email = "codewithgary@gmail.com"
    to_email = "codewithgary@yahoo.com"
    # way to connect to gmail
    password = "aged qjyq zeii gyxs"
    quotes = get_quotes(file_location)
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls() # enable tls connection
        connection.login(my_email, password=password)
        connection.sendmail(from_addr=my_email,to_addrs=to_email,
                            msg=f"Subject:Quote of the day!\n\n {quotes}")

def main():
    if current_weekday() == 5:
        sent_email("/Users/gauyada/WorkDocs/03_KNOWLEDGE/09_PYTHON/33_100DaysOfCode/100daysofcodepython/day32/Birthday Wisher (Day 32) start/quotes.txt")

if __name__ == '__main__':
   main()
