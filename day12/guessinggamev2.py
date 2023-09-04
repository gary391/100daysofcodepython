
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

EAST_LEVEL = 10
HARD_LEVEL = 5

def difficulty_level():
    choose_difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if choose_difficulty.lower() == 'easy':
        # print(f"you selected: {choose_difficulty}")
        return EAST_LEVEL
    elif choose_difficulty.lower() == 'hard':
        # print(f"you selected: {choose_difficulty}")
        return HARD_LEVEL
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

def check_answer(guess, answer, attempts):
    """
    :param guess: User guessed number
    :param answer: Random number generated by the computer
    :param attempts: Number of attempts based on the selection of the difficulty of the program i.e. easy or difficult
    :return: returns a number of attempts remaining after the guess has been cheaked
    """
    if(guess > answer):
        print("Too High.")
        return attempts - 1
    elif(guess < answer):
        print("Too Low.")
        return attempts - 1
    else:
        print(f"You got it! The answer was {guess}.")
        exit()


def guess_the_number():
    print(art.logo)
    print("Welcome to the Number Guessing Game!\n")
    print("I'm thinking of a number between 1 and 100.")
    answer = int(random.randint(1, 100))
    print(f"Pssst, the correct answer is {answer}")
    num_of_attempts = difficulty_level()
    # print(f"num_of_attempts this line!!!!!: {num_of_attempts}")
    user_guess = 0
    while user_guess != answer:
        print(f"You have {num_of_attempts} attempts remaining to guess the number.")
        user_guess = int(input("Make a guess: "))
        num_of_attempts = check_answer(user_guess, answer, num_of_attempts)
        print(f"attempts_remaining: {num_of_attempts}")
        if(num_of_attempts == 0):
            print("You run out of attempts!, try again!")
            return
        elif(user_guess != num_of_attempts):
            print("Guess again.")



guess_the_number()