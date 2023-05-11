#Auction Program

bidders = {}

def add_bidder(name,value):
    bidders[name] = value
 

def highest_bid(bidders):
    highest_bid = 0
    winner = ""
    for key in bidders:
        bid_amount = bidders[key]
        if bid_amount > highest_bid:
            highest_bid = bid_amount    
            winner = key
    print(f"Highest bidder is {winner} with a bid of {highest_bid}")


while True: 
    name = input("What is your name? ")
    value= int(input("What is your bid amount: "))

    add_bidder(name,value)

    action =input("Are there any more bidders: Yes or No: ").lower()

    if action == "no":
        highest_bid(bidders)
        print(bidders)
        break