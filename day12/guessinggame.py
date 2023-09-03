
"""
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
Choose a difficulty. Type 'easy' or 'hard':


#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).


"""
import random
import art



def difficulty_level():
    choose_difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if choose_difficulty.lower() == 'easy':
        # print(f"you selected: {choose_difficulty}")
        return 10
    elif choose_difficulty.lower() == 'hard':
        # print(f"you selected: {choose_difficulty}")
        return 5
    else:
        print(f"Please select the correct option ")
        """
        If correct options is not press you will call the function again - NOTE FOR return statement, if you don't
        put the return statement then you will see None being returned instead of the values of 5 or 10 

        So, even if you enter 'easy' or 'hard' during the recursive call,
        the result (either 10 or 5) is returned to the "new instance" of the function created by the recursive call,
        not to the original caller who started the whole process
        """
        return difficulty_level()




def guess_the_number():
    print(art.logo)
    print("Welcome to the Number Guessing Game!\n")
    print("I'm thinking of a number between 1 and 100.")
    number_guessed = int(random.randint(1, 100))
    print(f"Pssst, the correct answer is {number_guessed}")
    num_of_attempts = difficulty_level()
    # print(f"num_of_attempts: {num_of_attempts}")
    print(f"You have {num_of_attempts} attempts remaining to guess the number.")
    user_guess = int(input("Make a guess: "))
    # print("Run this line 1")

    while num_of_attempts > 1:
        # print(f"num_of_attempts: {num_of_attempts}")
        if (user_guess > number_guessed):
            print("Too High.")
            print("Guess again.")
            num_of_attempts = num_of_attempts - 1
            print(f"You have {num_of_attempts} attempts remaining to guess the number.")
            user_guess = int(input("Make a guess: "))

        elif (user_guess < number_guessed):
            print("Too Low.")
            print("Guess again.")
            num_of_attempts = num_of_attempts - 1
            print(f"You have {num_of_attempts} attempts remaining to guess the number.")
            user_guess = int(input("Make a guess: "))

        elif (user_guess == number_guessed):
            print(f"You got it! The answer was {user_guess}.")
            break
    else:
        print("Better Luck Next Time!")

guess_the_number()