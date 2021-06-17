# Castle Game pg. 21

print ("You are in a dark room in a mysterious castle.")

print ("In front of you are three doors.  You must choose one.")
player_choice=input("Choose 1, 2 or 3...")

if player_choice=="1":
    print("You find a room full of treasure.  You're rich!")
    print("GAME OVER - YOU WIN!")

elif player_choice=="2":
    print("The door opens and an angry ogre hits you with his club.")
    print("GAVE OVER.  YOU LOSE.")

elif player_choice=="3":
    print("You go into the room and find a sleeping dragon.")
    print("The dragon wakes up and eats you.  You are delicious.")
    print("GAME OVER.  YOU LOSE.")

else:
    print("Try following directions.")

print("Run the game again to try again!")   