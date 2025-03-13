attempts = 0
print("what is your name?")
if input():
    print("Welcome")
import random
str = random.randint(1, 10)
print("I am guessing a number from 1-10. Can you guess the number?")
print("You can only get 10 tries")
while attempts < 5:
    guess = int(input("Please guess a number"));
    attempts_used= attempts + 1;
    if guess > str:
            print("Guess is too high, try a smaller number");
    elif guess < str:
            print("Guess is too low, try a higher number");
    elif guess == str:
            attempts_used=str(attempts_used)
            print("Correct- you win in", attempts_used, "guesses");
            exit();
else:
    if attempts == 5:
       print("You failed to guess in time") 