
import random

guessestaken = 0 

print("Hello user! Welcome to the Guessing Game v2. ")
print("I will choose a number and we'll see how many guesses it takes for you to guess the number. \n")

x = int(input("What is the lowest number you want me to choose from? "))
y = int(input("What is the highest number you want me to choose from? "))


num = random.randint (x, y)
print("Okay, I've chosen a number from " + str(x) + " - " + str(y) + ".")
guess = int(input("Guess the number: "))

while (guessestaken != num):
	guessestaken = guessestaken + 1
	
	if guess < num:
		print("Try higher.")
		guess = int(input("Guess the number: "))

	elif guess > num:
		print("Try lower.")
		guess = int(input("Guess the number: "))
	
	elif guess == num:
		break

if guess == num:
	guessestaken = str(guessestaken)
	print("You got it!")


print("It took you " + guessestaken + " tries to guess the number.")