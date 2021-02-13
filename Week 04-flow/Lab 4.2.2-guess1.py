# Week 04: evens.py, Lab 4.2.2 Flow control loops
# This program prompts the user to guess a number and keeps prompting the user
# to guess the number until the user gets the right one.
# Author: Ross Downey

numberToGuess = 30

guess = int(input("Please guess the number:"))
while guess != numberToGuess:
    print ("Wrong!")
    guess = int(input("Please guess again:"))

print ("Well done! Yes the number was", numberToGuess)