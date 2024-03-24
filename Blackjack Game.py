import random

card_choices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
players_cards = []
computers_cards = []
player_total = 0
computer_total = 0


def hit_or_stand():
    while True:
        hit_stand = input("Type \'hit\' to get another car or type \'stand\' to pass: ")
        if hit_stand == 'hit':
            players_cards.append(random.choice(card_choices))
            print(players_cards)
        else:
            break


while True:
    start_game = input("Do you want to play blackjack: (y/n) ")
    if start_game == "y":
        players_cards.append(random.choice(card_choices))
        players_cards.append(random.choice(card_choices))
        computers_cards.append(random.choice(card_choices))

        print(f"Your cards: {players_cards}")
        print(f"Computers cards: {computers_cards}")

        computers_cards.append(random.choice(card_choices))

        hit_or_stand()

        for num in players_cards:
            player_total += num

        for num in computers_cards:
            computer_total += num

        if 21 >= player_total > computer_total:
            print(f"These are the dealers cards: {computers_cards}")
            print("you won")
        else:
            print(f"These are the dealers cards: {computers_cards}")
            print("Womp Womp! You lost...")

    elif start_game == 'n':
        break
    else:
        print("invalid input. Let's try this again")
