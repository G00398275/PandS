# Week 04: gradeRounded.py, Lab 4.1.4 Flow control if elif and else
# This program uses a while loop to keep prompting a user for a number until -1 is entered
# Author: Ross Downey

correctInteger = -1

answer = int(input("Please enter an integer: "))
while answer != correctInteger:
    print ("That's not the correct one!")
    answer = int(input("Please enter another integer:"))

print ("Great, the correct integer is", correctInteger)
