# Week 03: Lab 2.3.3 Variables and State
# This program reads in two numbers and divides the first by the second,
# This program then outputs the integer result and the remainder
# Author: Ross Downey

x = int(input ("Please enter the first number: "))
y = int(input ("Please enter the number you want to divide by: "))

answer = int (x//y) # // gives the integer division, rounded down)
remainder = x%y # % symbol gives the remainder

print ("{} divided by {} is {} with remainder {} " .format ( x, y, answer, remainder))