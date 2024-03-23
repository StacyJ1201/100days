import random

word_list = ["aardvark", "baboon", "camel"]
player_chances = 5

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

print(f"Psst the chosen word is {chosen_word}")

display = []
for letter in chosen_word:
    display += "_"

end_of_game = False

if word_length == 0:
    end_of_game = True
    print("You won!")

while not end_of_game:
    guess = input("\nGuess a letter: ").lower()
    for char in chosen_word:
        if char == guess:
            print(char, end="  ")
            word_length -= 1
        else:
            print("_", end="  ")
            player_chances -= 1



if player_chances == 0:
    print("You lost, game is over")