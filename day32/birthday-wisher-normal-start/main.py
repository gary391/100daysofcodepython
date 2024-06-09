##################### Normal Starting Project ######################

# 1. Update the birthdays.csv with your friends & family's details. 
# HINT: Make sure one of the entries matches today's date for testing purposes. e.g.
#name,email,year,month,day
#YourName,your_own@email.com,today_year,today_month,today_day

# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Create a tuple from today's month and day using datetime. e.g.
# today = (today_month, today_day)
import datetime as dt
import smtplib
my_email = "codewithgary@gmail.com"
password = "#############"
now = dt.datetime.now()
today_month = now.month
today_day = now.day
today = (today_month, today_day)
print(today)

# HINT 2: Use pandas to read the birthdays.csv
import pandas
import random
data = pandas.read_csv("birthdays.csv")
print(data)
# print(data['month'][0])
# print(data['day'][0])

# HINT 3: Use dictionary comprehension to create a dictionary from birthday.csv that is formated like this:
# birthdays_dict = {
#     (birthday_month, birthday_day): data_row
# }
#Dictionary comprehension template for pandas DataFrame looks like this:
# new_dict = {new_key: new_value for (index, data_row) in data.iterrows()}
#e.g. if the birthdays.csv looked like this:
# name,email,year,month,day
# Angela,angela@email.com,1995,12,24
#Then the birthdays_dict should look like this:
# birthdays_dict = {
#     (12, 24): Angela,angela@email.com,1995,12,24
# }

birthdays_dict = {((data['month']),(data['day'])): ((data['name']), (data['email']), (data['year']), (data['month']), (data['day'])) for (index, data) in data.iterrows()}
print(birthdays_dict)



#HINT 4: Then you could compare and see if today's month/day tuple matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:

# 3. If there is a match, pick a random letter (letter_1.txt/letter_2.txt/letter_3.txt) from letter_templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT 1: Think about the relative file path to open each letter. 
# HINT 2: Use the random module to get a number between 1-3 to pick a randome letter.
# HINT 3: Use the replace() method to replace [NAME] with the actual name. https://www.w3schools.com/python/ref_string_replace.asp


"""
1. Open a random letter out of the three letters
2. replace the name with the name of the birthday from the if condition above. 
"""



# with open(LETTER, mode="r") as file:
#     print(file.read())

# def read_names_file(file_path):
#     '''
#     Opens the file, returns a list containing each line in the file as a list items
#     which is the list of names.
#     '''
#     with open(file_path, mode="r") as file:
#         return (file.readlines())

def replace_name_in_letter(file_path, invitee):
    with open(file_path, mode='r') as file:
        text = file.read()
        # The text replacement needs to be saved to a variable.
        x = text.replace("[NAME]", invitee)
        return x

# print(replace_name_in_letter(LETTER, name))
# def write_letter(file_path, content, invitee):
#     with open(file_path+f'/letter_for_{invitee}.txt', mode='w') as file:
#         file.write(content)


# 4. Send the letter generated in step 3 to that person's email address.
# HINT 1: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)
# HINT 2: Remember to call .starttls()
# HINT 3: Remember to login to your email service with email/password. Make sure your security setting is set to allow less secure apps.
# HINT 4: The message should have the Subject: Happy Birthday then after \n\n The Message Body.

def email_quote(file_path, invitee):
    # Using context manager we     quote = random_quote()
    letter = replace_name_in_letter(file_path, invitee)
    msg = f"Subject: Happy Birthday! \n\n {letter}"
    with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
        # Create a tls connection
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="mayank646@gmail.com",
                            msg=msg)
this_letter = random.randint(1,3)
LETTER = f'./letter_templates/letter_{this_letter}.txt'

if (today_month, today_day) in birthdays_dict:
    print(birthdays_dict[((today_month, today_day))]) # value of the specific person
    name = (birthdays_dict[((today_month, today_day))][0])
    email_quote(LETTER, name)
