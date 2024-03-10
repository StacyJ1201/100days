print("Welcome to Treasure Island!\n")
print("Your mission is to find the treasure\n")
print("Which direction would you like to go? left or right?")
direction = input().lower()
if direction == "right":
    print("Your game is over")
elif direction == "left":
    print("Great! You made it to the lake. Now you need to get across the lake. Would you like to wait or swim")
    lake_decision = input().lower()
    if lake_decision == "swim":
        print("Your game is over")
    elif lake_decision == "wait":
        print("Great! You made it across the lake. Now you need to open one of three doors. The Red door, the yellow door, or the blue door. Which one would you like to open?")
        door_decision = input().lower()
        if door_decision == "red" or door_decision == "blue":
            print("Your game is over")
        elif door_decision == "yellow":
            print("Congratulations! You won the game!")


