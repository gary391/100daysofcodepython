"""
on every year that is evenly divisible by 4 

**except** every year that is evenly divisible by 100 

**unless** the year is also evenly divisible by 400

1. Check if YEAR is divisible by 4 
    2. Check if YEAR is NOT divisible by 100 
        3. Check if YEAR is divisible by 400 
else:
    YEAR IS NOT A LEAP YEAR

"""

# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

""" 
If a year is divisible by 4, it's a potential leap year.
If a year is divisible by 100, it's not a leap year, unless...
If a year is divisible by 400, it is a leap year.
"""
if (year % 4 == 0 ):
    if (year % 100 == 0):
        if (year % 400 == 0):
            print("Leap year.")
        else: 
            print("Not leap year.")
    else: 
        print("Leap year.")
else:
    print("Not leap year.")