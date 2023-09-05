#Guess the Random Number
import random
#Get Range
max = input("Enter the Range ")
#Proceed if it is a number else quit
if max.isdigit():
    max = int(max)
    if max <= 0:
        print("Please enter a number greater than zero")
        quit()
else:
    print("Please enter a number ")
    quit()

#print("**")
#Generate a random integer
random_number = random.randint(0,max)
count = 0

while True:
    count += 1
    guess = input("Enter your guess in the range 0 to " + str(max))
    if guess.isdigit():
        #if the guessed number is a digit then proceed
        guess = int(guess)
        if guess == random_number:
            print("You got it!")
            break
        #Hints for guessing
        elif guess > random_number:
            print("Try lower")
        else:
            print("Try higher")
    else:
        print("Please guess a number ")
#Number of guesses to get it right
print("You got the correct answer in "+str(count))
