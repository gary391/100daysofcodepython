"""
Execption lecture CS50 
SyntaxError
ValueError - Value
NameError - 
ele
"""


# print ("Hello world")
# This only accepts interger value including minus or zero
# x = int(input("What's x? "))
# print(f"x is {x}")

# while True: # This will loop forever
# ## Using try and except 
#     try: 
#         x = int(input("What's x? ")) # For none int value the int function is raising a value error.
#         print("I am after x assignment!") # This line does't get executed as we encounter a value error + the assignment also doesn't happen.
#         # If you encounter a valueError than you will print the message.
#         # Here we knew the type of error to catch.
#     except ValueError as e: 
#         # print(f"{e} is not an interger!")
#         print(f"x is not an interger!")
    
#     ## This will give a NameError as the value of the x is not defined at int(input("what's x?"))
#     ## as it encountered value error so the assignment doesn't happen, thus the variable doesn't exist.
#     ## This line also gets executed all the time.
#     # print(f"x is {x}") 
    
#     ## To fix the above exception 
#     ## Here the else will be executed only when try is executed successfuly.
#     else: # Here the else clause is tied to the try block
#     # print(f"x is {x}")
#         break
# print(f"x is {x}")


### Modified code 

# while True: # This will loop forever
# ## Using try and except 
#     try: 
#         x = int(input("What's x? ")) # For none int value the int function is raising a value error.
#         print("I am after x assignment!") # This line does't get executed as we encounter a value error + the assignment also doesn't happen.
#         # If you encounter a valueError than you will print the message.
#         # Here we knew the type of error to catch.
#         break
#     except ValueError as e: 
#         # print(f"{e} is not an interger!")
#         print(f"x is not an interger!")
    
#     ## This will give a NameError as the value of the x is not defined at int(input("what's x?"))
#     ## as it encountered value error so the assignment doesn't happen, thus the variable doesn't exist.
#     ## This line also gets executed all the time.
#     # print(f"x is {x}") 
    
#     ## To fix the above exception 
#     ## Here the else will be executed only when try is executed successfuly.
#     # else: # Here the else clause is tied to the try block
#     # print(f"x is {x}")
#         # break
# print(f"x is {x}")


### Define a function called get_int

# def main():
#     x = get_int()
#     print(f"x ix {x}")

# def get_int():
#     while True:
#         try:
#             x = int (input("what's x? "))
#         except ValueError:
#             print("x is not an integer")
#         else:
#             break
#     return x


## Compact version where we can skip the break, and return the value. 
## Note return is stronger than break.

# def main():
#     x = get_int()
#     print(f"x ix {x}")

# def get_int():
#     while True:
#         try:
#             x = int (input("what's x? "))
#         except ValueError:
#             print("x is not an integer")
#         else:
#             return x ## Here once we know the try was successful, we enter the else block and return the value.
    

## Further make the code more contact.

def main():
    x = get_int("What's x? ")
    print(f"x is {x}")

def get_int(prompt):
    while True:
        try:
            # x = int (input("What is x? "))
            # return x
            ## or 
            return int(input(prompt))
        except ValueError:
            # print("x is not a interger")
            pass ## Here we are catching the exception but we are pass it, and not printing it.
        


if __name__ == "__main__":
    main()