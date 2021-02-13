# Week 04: isEven.py, Lab 4.1.1 Flow control if elif and else
# This program inputs a number and tells the user if it's even or odd
# Author: Ross Downey

number = int(input("Please enter an integer: "))

if (number % 2) == 0:
    print ("{} is an even number" .format (number))
else:
    print ("{} is an odd number" .format (number))