# Do you like robots?
user_reply=input("Do you like robots? (Type Yes or No)")
# If yes, then hello!
if user_reply=="Yes":
    print("Beep Boop!")

# If no, they don't like you either
elif user_reply=="No":
    print("Well, robots don't like you either.")

# Easter egg - laser eyes - watch out
elif user_reply=="only ones with laser eyes":
    print("ZZAPP")

else:
    print("Your human nonsense offends us.")

input("Press enter to exit.")