auction_list = []

while True:
    name_of_person = input("What is your name: ")
    bid_amount = int(input("What is your bid: "))

    info = {'name': name_of_person, 'bid': bid_amount}

    auction_list.append(info)

    new_member = input("Is anyone else bidding? (yes or no) ")

    if new_member == "no":
        all_bids = [bid['bid'] for bid in auction_list]
        highest_bid = max(all_bids)
        highest_bidder_name = next(bid for bid in auction_list if bid['bid'] == highest_bid)
        highest_bidder = highest_bidder_name['name']
        print(f"{highest_bidder} is the highest bidder with {highest_bid}")
        break
