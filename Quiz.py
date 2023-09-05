#Quiz MiniProject
print("Welcome to Swetha's First Quiz Game Code")
Playing = input("Are you ready kid??")
if Playing.lower() != "aye aye captain":
    quit()
print("I can't here youuuuu!")
score = 0

answer = input("Oooooooo....Who lives in a pineapple under the sea?")
if answer.lower() == "spongebob squarepants":
    score = score + 1
    print("...Ye'r Right!")
else:
    print("....Arrgh!")

answer = input("Bob The Builder....Can we fix it?")
if answer.lower() == "yes we can":
    score = score + 1
    print("You can join the Crew!")
else:
    print("You cannot join the Crew with that attitude")

answer = input("Sugar...Spice....and Everything Nice. This makes what?")
if answer.lower() == "the powerpuff girls":
    score = score + 1
    print("Once again the day is saved by you!")
else:
    print("The city of Townsville is in trouble!")

answer = input("I'm Popeye the Sailor Man, I'm strong as a Finich cause I eat my ____")
if answer.lower() == "spinach":
    score = score + 1
    print("Toot! Toot!")
else:
    print("Et tu Brute!")

answer = input("I'm a Barbie girl, In the Barbie world. Life in Plastic, it's _______")
if answer.lower() == "fantastic":
    score = score + 1
    print("It sure is!")
else:
    print("Someone needs this FANTASTIC song on their playlist")

print("You have got " +str(score)+ " out of 5 Correct!")
print("And that is " + str(score*25) + "%.")


