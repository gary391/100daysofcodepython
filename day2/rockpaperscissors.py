"""
rock win against the scissors
scissors wins against papers
Paper wins against rocks
"""
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

your_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
if (your_choice == 0):
    print(rock)
elif(your_choice == 1):
    print(paper)
elif (your_choice == 2):
    print(scissors)
    


print("Computer choose: ")
computer_choice = random.randint(0,2)

if (computer_choice == 0):
    print(rock)
elif(computer_choice == 1):
    print(paper)
elif (computer_choice == 2):
    print(scissors)

if(your_choice == 0 and computer_choice == 2):
    print("You win!")
elif(your_choice == 2 and computer_choice == 1):
    print("You win!")
elif(your_choice == 1 and computer_choice == 0):
    print("You win!")
elif(your_choice ==computer_choice):
    print("It's a draw!")
else:
    print("Computer Win!")