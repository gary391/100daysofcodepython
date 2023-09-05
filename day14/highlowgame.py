import random
import art
import game_data
import os

def select_next_data_sample(game_data):
    """
    Returns informaion and number of followers
    :param game_data:
    :return:
    """
    sample_list = random.sample(game_data.data, 1)
    sample = f"{sample_list[0]['name']}, a {sample_list[0]['description']}, from {sample_list[0]['country']}"
    num_followers_A = int({sample_list[0]['follower_count']}.pop())
    return (sample, num_followers_A)


def select_data_sample(game_data):
    """
    Returns informaion and number of followers
    :param game_data:
    :return:
    """
    sample_list = random.sample(game_data.data, 2)
    sample_a = f"{sample_list[0]['name']}, a {sample_list[0]['description']}, from {sample_list[0]['country']}"
    num_followers_A = int({sample_list[0]['follower_count']}.pop())
    sample_b = f"{sample_list[1]['name']}, a {sample_list[1]['description']}, from {sample_list[1]['country']}"
    num_followers_B = int({sample_list[1]['follower_count']}.pop())
    return (sample_a, num_followers_A, sample_b, num_followers_B )

your_score = 0
continue_play = True
while continue_play:
    sample_a, num_followers_A, sample_b, num_followers_B = select_data_sample(game_data)
    print(art.logo)
    print(f"Compare A: {sample_a}, {num_followers_A} ")
    if(your_score > 0):
        print(f"You're right! Current score: {your_score}")
    print(art.vs)
    print(f"Against B: {sample_b}, {num_followers_B}")

    user_put = input("Who has more followers? Type 'A' or 'B': ")
    if (user_put.lower() == 'a'):
        if (num_followers_A > num_followers_B):
            your_score = your_score +1
            sample_a, num_followers_A = sample_b, num_followers_B
            sample_b, num_followers_B = select_next_data_sample(game_data)
            os.system("clear")
        else:
            os.system("clear")
            print(f"Sorry, that's wrong. Final score: {your_score}")
            continue_play = False
    elif (user_put.lower() == 'b'):

        if (num_followers_A < num_followers_B):
            your_score = your_score +1
            sample_a, num_followers_A = sample_b, num_followers_B
            sample_b, num_followers_B = select_next_data_sample(game_data)
            os.system("clear")
        else:
            os.system("clear")
            print(f"Sorry, that's wrong. Final score: {your_score}")
            continue_play = False




