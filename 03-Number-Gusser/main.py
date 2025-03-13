maxtries = 5
attempts = 0
print("what is your name?")
if input():
    print("Welcome")
import random
str = random.randint(1, 10)
print("I am guessing a number from 1-10. Can you guess the number?")
print(f"You can only get {maxtries} tries")
while attempts < maxtries:
    guess = int(input("Please guess a number"));
    attempts= attempts + 1;
    if guess > str:
            print("Guess is too high, try a smaller number");
    elif guess < str:
            print("Guess is too low, try a higher number");
    elif guess == str:
            print(f"Correct- you win in {attempts} guesses");
            exit();
else:
    if attempts == maxtries:
       print("You failed to guess in time") 