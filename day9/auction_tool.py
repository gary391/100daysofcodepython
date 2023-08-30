
#HINT: You can call clear() to clear the output in the console.

import os
# Clearing the Screen

from art import logo

print(logo)
print(f"Welcome to the secret auction program.")

bid_data = {}


def auction_tool(bidder_name, bid_amount):
    bid_data[bidder_name] = bid_amount
    return bid_data

def highest_bid (bid_data):
    higest_bid = 0
    winner = ""

    for bidder in bid_data:
        bid_amount = bid_data[bidder]
        if(bid_amount > higest_bid ):
            higest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner}, with a bid of ${higest_bid}.")

more_bidder = True
while more_bidder:
    bidder_name = input("What is your name? ")
    bid_amount = int(input("What's your bid? $"))
    auction_tool(bidder_name, bid_amount)

    do_we_more_bidders = input(
        "Are there any other bidders? Type 'yes' or 'no' \n")
    if(do_we_more_bidders.lower() == 'yes' ):
        os.system("clear")
    elif (do_we_more_bidders.lower() == 'no'):
        more_bidder = False
    else:
        print("Warning!")
print(bid_data)
highest_bid (bid_data)
# bidder_with_max_value = max(bid_data)
# max_bid_value = max(bid_data.values())
#
# print(f"The winner is {bidder_with_max_value}, with a bid of ${max_bid_value}.")
