# Week 04: grade.py, Lab 4.1.2 Flow control if elif and else
# This program reads in a students percentage mark and prints out the corresponding grade
# The program also checks that the percentage is valid
# Author: Ross Downey

percentage = float(input("Please enter the percentage: "))

if percentage < 0 or percentage > 100:
    print ("Please enter a number between 0 and 100")
elif percentage < 40: 
    print ("Fail")
elif percentage < 50: # i.e. between 40 and 49 inclusive as < 40 already accounted for
    print ("Pass")
elif percentage < 60: # i.e. between 50 and 59 inclusive as < 50 already accounted for
    print ("Merit 1")
elif percentage < 70: # i.e. between 60 and 69 inclusive as < 60 already accounted for
    print ("Merit 2")
else:
    print ("Distinction") # last possible outcome if all previous conditions not met