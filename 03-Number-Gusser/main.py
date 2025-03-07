print("what is your name?")
if input():
    print("Welcome")
from random import randrange
randrange(10)
print("I am guessing a number from 1-10. Can you guess the number?")
while True:
    guess = int(input("Enter your guess:"))
    if guess < randrange(10):
        print("Your guess is too low")
    elif guess > randrange(10):
        print("Your guess is too high")
        
    else:
        print("You guessed it!")
        break
        