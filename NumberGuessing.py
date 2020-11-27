import random

secretNumber = random.randint(1, 20)

print("Enter a number to check Your guess with computer")


for GuessTaken in range(1, 4):
    print("Take a guess.")
    guess = int(input())

    if guess < secretNumber:
        print("You are Too close to Number.")
    elif guess > secretNumber:
        print("Your number is Going far from guess")
    else:
        break

if guess == secretNumber:
    print("Good Job ! You have enterd The Right guess")
else:
    print("Nope You have enterd The Wrong Number .")
