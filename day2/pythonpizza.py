# 🚨 Don't change the code below 👇
# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M, or L ")
# add_pepperoni = input("Do you want pepperoni? Y or N ")
# extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆
""" 
Small Pizza: $15

Medium Pizza: $20

Large Pizza: $25

Pepperoni for Small Pizza: +$2

Pepperoni for Medium or Large Pizza: +$3

Extra cheese for any size pizza: + $1
"""

#Write your code below this line 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
bill = 0

if(size == 'S'):
    bill = bill + int(15)
elif(size == 'M'):
    bill = bill + int(20)
elif(size == 'L'):
    bill = bill + int(30)
add_pepperoni = input("Do you want pepperoni? Y or N ")
if(size == 'S' and add_pepperoni == 'Y'):
    bill = bill + int(2)
elif((size == 'M' or size =='L') and add_pepperoni == 'Y'):
    bill = bill + int(3)
extra_cheese = input("Do you want extra cheese? Y or N ")
if(extra_cheese == 'Y'):
    bill = bill + int(1)
print(f"your final bill is: ${bill}")