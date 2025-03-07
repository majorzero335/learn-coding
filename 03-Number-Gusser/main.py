print("what is your name?")
if input():
    print("Welcome")
from random import randrange
randrange(10)
print("I am guessing a number from 1-10. Can you guess the number?")
while True:
    guess = int(input())
    if guess == randrange(10):
        print("You guessed it!")
        break
    else:
        print("Try again")