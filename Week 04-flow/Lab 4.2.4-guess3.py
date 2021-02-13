# Week 04: evens.py, Lab 4.2.2 Flow control loops
# This program prompts the user to guess a randomly generated number and keeps prompting the user
# to guess the number until the user gets the right one,
# while telling the user if their guess is too high or too low
# Author: Ross Downey

import random
min = int(0)
max = int(100)
numberToGuess = random.randint (min, max) # importing random function and specifying the range

guess = int(input("Please guess the number:"))
while guess != numberToGuess:
    if guess < numberToGuess:
        print ("Too Low")
    else: # If it's not too low then it must be equal to or too high
        print ("Too High")
    guess = int(input("Please guess again:"))

print ("Well done! Yes the number was", numberToGuess)