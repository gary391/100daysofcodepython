############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game:
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here:
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements:
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created:
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
import os
import random
import art

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def deal_card():
    return random.choice(cards)
# print(deal_card())
#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
user_cards = []
computer_cards = []
for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())


#Hint 6: Create a function called calculate_score() that takes a List of cards as input
#and returns the score.
#Look up the sum() function to help you do this.

def calculate_score(list_of_card):

    # BJ condition a hand with only 2 cards: ace + 10
    # Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.
    if(len(list_of_card) == 2) and sum(list_of_card) == 21:
        return 0
    # Using list comprehension
    """
    new_list = [<Conditional Expression> for <item> in <iterable>]

    new_list = [<Exp1> if condition else <Exp2> if condition else <Exp3> for <item> in <iterable>]
    """
    # Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().
    list_of_card = [ 1 if(item == 11 and sum(list_of_card)> 21) else item for item in list_of_card ]
    list_score = sum(list_of_card)
    return list_score

def compare(user_score,computer_score):
    if(user_score==computer_score):
        return ("Draw!")
    elif(computer_score == 0):
        return("You lose! and Computer has a BJ")
    elif(user_score ==0):
        return("You Win! with a blackJack")
    elif(user_score >21):
        return("You went over and You lose!")
    elif(computer_score >21):
        return("Your opponent went over, You Win!")
    elif (user_score>computer_score):
        return "You win!"
    else:
        return "You Lose!"
def play_backjack():
    print(art.logo)      
    game_continue = True
    while game_continue:
        #Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.
        print(f'Usercard: {user_cards}')
        print(f'ComputerCard: {computer_cards[0]}')

        print(f'user_score: {calculate_score(user_cards)}')
        user_score = (calculate_score(user_cards))
        # print(f'computer_score: {calculate_score(computer_cards)}')
        computer_score = (calculate_score(computer_cards))

        if (user_score) == 0 or (computer_score) == 0 or (user_score) > 21:
            game_continue = False
            # print("You lose!")

        #Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if(user_should_deal == "y"):
                user_cards.append(deal_card())
            else:
                game_continue = False

    #Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

    #Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17 and doesn't have blackjack.  ????THIS IS NOT CLEAR????????
    while ((computer_score) < 17) and (computer_score !=0):
        computer_cards.append(deal_card())
        computer_score = (calculate_score(computer_cards)) # We need to evaluate the computer score
    print(f"Your final hand was {user_cards}, and your final score was {user_score}")
    print(f"Computer your final hand was {computer_cards}, and your final score was {computer_score}")
    print(compare(user_score,computer_score ))
#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses.
# If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses.
# If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") =='y':
    os.system("clear")
    play_backjack()
