#function with two arguments
# name and location
def greet_with_two_arguments(name, location):
    print(f"My name is {name}, I am heading to {location}")

greet_with_two_arguments('gaurav', "india")
greet_with_two_arguments('nowhere', "gaurav")

#Function Using key word arguments
def greet_with_two_key_word_arguments(name, location):
    print(f"Using Key word arguments  - My name is {name}, I am heading to {location}")

greet_with_two_key_word_arguments(name='Gaurav', location='india')