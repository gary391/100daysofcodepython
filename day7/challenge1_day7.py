import random

#Step 1 

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
# chosen_word = random.sample(word_list, 1)

# print(f'Random word choosen is: {chosen_word}')
chosen_word = random.choice(word_list)
print(type(chosen_word))

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess = input(f'Guess a letter in the word: ').lower()

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

for letter in chosen_word:
    # print(f'Letter is: {letter}')
    if guess in letter:
        print(f'Present')
    else:
        print(f'Not Present')