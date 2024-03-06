import os
clear = lambda: os.system('clear')
clear()

from art import logo

print(logo)
print("Welcome to sylent auction!")

bidders = []
highest_bidder = {"bid": 0, "name": ""}
keep_bidding = True

while keep_bidding:
    name = input("What is your name?\n")
    bid = input("What is your bid\n")
    clear()
    entry = {
        "name": name,
        "bid": int(bid)
    }

    bidders.append(entry)

    bid_more = input("Another bidder?").lower()
    if bid_more == 'no':
        keep_bidding = False
else:
    for bidder in bidders:
        if bidder["bid"] > highest_bidder["bid"]:
            highest_bid = bidder["bid"]
            highest_bidder = bidder

print(f"The winner is {highest_bidder['name']} with a bid of ${highest_bidder['bid']}")