# Castle Game pg. 21

print ("You are in a dark room in a mysterious castle.")

print ("In front of you are four doors.  You must choose one.")
player_choice=input("Type 1, 2, 3 or 4..:")

if player_choice=="1":
    print("You find a room full of treasure.  You're rich!")
    print("GAME OVER - YOU WIN!")

elif player_choice=="2":
    print("The door opens and an angry ogre hits you with his club.")
    print("GAVE OVER.  YOU LOSE.")

elif player_choice=="3":
    print("You go into the room and find a sleeping dragon.")
    print("You can either:")
    print("1) Try to steal some of the dragon's gold.")
    print("2) Try to sneak around the dragon to the exit.")

    dragonChoice=input("Type 1 or 2:")
    if dragonChoice=="1":
        print("The dragon wakes up and eats you.  You are delicious.")
        print("GAME OVER.  YOU LOSE.")

    elif dragonChoice=="2":
        print ("You sneak around the dragon and escape the castle, blinking in the sunshine.")
        print("GAME OVER - YOU WIN!")
    else:
        print ("Sorry... you didn't follow directions")

else:
    print("Try following directions.")

print("Run the game again to try again!")   