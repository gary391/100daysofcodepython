def difficulty_level():
    choose_difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if choose_difficulty.lower() == 'easy':
        return 10
    elif choose_difficulty.lower() == 'hard':
        return 5
    else:
        print(f"Please select the correct option ")
        return difficulty_level() # If correct options is not press you will call the function again
print(difficulty_level())