import random

while True:

    choices = ['rock', 'paper', 'scissors']
    computer = random.choice(choices)

    player = input("Choose your weapon... ").lower()

    if player == "quit":
        break

    else:
        if computer == player:
            print(f"I chose {computer}. It's a tie")
        elif computer == 'rock' and player == "scissors":
            print(f"I chose {computer}. You lose!")
        elif computer == 'paper' and player == "rock":
            print(f"I chose {computer}. You lose!")
        elif computer == 'scissor' and player == 'paper':
            print(f"I chose {computer}. You lose!")
        else:
            print(f"I chose {computer}. You win!")


