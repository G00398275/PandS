# Week 04: evens.py, Lab 4.2.5 Flow control loops
# This program keeps reading numbers until the user enters a 0
# The program then prints out each number listed and gives the average
# Author: Ross Downey

numbers = []

number = int(input("Please enter number (0 to quit): ")) #prompting number entry

while number != 0:
    numbers.append(number) # appending numbers to the list

    number = int(input("Please enter another (0 to quit): ")) # input of appended numbers

for value in numbers:
    print (value) 

average = float (sum(numbers)) / len(numbers)
print ("The average is {}" .format (average)) #printing average of numbers entered as float