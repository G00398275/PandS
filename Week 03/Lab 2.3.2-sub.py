# Week 03: Lab 2.3.2 Variables and State
# This program reads in two numbers and subtracts the first one from the second one
# Author: Ross Downey

x = int (input("Please enter first number: "))
y = int (input("Please enter second number: "))# Inputs read as strings, "int" allows mathematical operations

answer = x-y

print ("{} minus {} is {} " .format (x, y, answer))