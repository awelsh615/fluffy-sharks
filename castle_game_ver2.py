# Castle Game pg. 21
import random

# Choose from four doors
print ("You are in a dark room in a mysterious castle.")
print("")
print ("In front of you are four doors.  You must choose one.")
player_choice=input("Type 1, 2, 3 or 4..:")

if player_choice=="1":
    print("")
    print("You find a room full of treasure.  You're rich!")
    print("GAME OVER - YOU WIN!")

elif player_choice=="2":
    print("")
    print("The door opens and an angry ogre hits you with his club.")
    print("GAVE OVER.  YOU LOSE.")

elif player_choice=="3":
    print("")
    print("You go into the room and find a sleeping dragon.")
    print("You can either:")
    print("1) Try to steal some of the dragon's gold.")
    print("2) Try to sneak around the dragon to the exit.")

    dragonChoice=input("Type 1 or 2:")
    if dragonChoice=="1":
        print("")
        print("The dragon wakes up and eats you.  You are delicious.")
        print("GAME OVER.  YOU LOSE.")

    elif dragonChoice=="2":
        print("")
        print ("You sneak around the dragon and escape the castle, blinking in the sunshine.")
        print("GAME OVER - YOU WIN!")
    else:
        print("")
        print ("Sorry... you didn't follow directions")

elif player_choice=="4":
    print("")
    print("You enter a room with a sphinx.")
    print('It asks you to guess what number it is thinking of, between 1 and 5.')
    number=int(input("What number do you choose?"))

    if number==random.randint(1,5):
        print("")
        print("The spinx hisses in disappointment.  You guessed correctly.")
        print("She must let you go free.")
        print("GAME OVER - YOU WIN!")

    else:
        print("")
        print('The sphinx tells you that your guess is incorrect.')
        print("You are now her prisoner forever.")
        print("GAME OVER.  YOU LOSE.")
else:
    print("")
    print("Try following directions.")

print("")
input("Press enter to exit.")   