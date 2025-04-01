maxtries = 5
attempts = 0
print("What is your name?")
print("Hello, " + input() + "!")
print("Welcome to the number guessing game!")
import random
number = random.randint(1, 10)
print("I am guessing a number from 1-10. Can you guess the number?")
print(f"You can only get {maxtries} tries")
while attempts < maxtries:
    guess = int(input("Please guess a number:"));
    attempts= attempts + 1;
    if guess > number:
            print("Guess is too high, try a smaller number");
    elif guess < number:
            print("Guess is too low, try a higher number");
    elif guess == number:
            print(f"Correct- you win in {attempts} guesses");
            exit();
else:
    if attempts == maxtries:
       print("You failed to guess in time. The correct number was " + number + ". Better luck next time!") 