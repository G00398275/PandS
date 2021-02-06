# Week 03: Lab 2.3.5 Variables and State
# This program reads in a string and strips any leading or trailing spaces
# It also outputs the length of the input and output strings
# Author: Ross Downey

rawString = input ("Please enter a string:")
normalisedString = rawString.strip() .lower()

lengthOfRawString = len (rawString)
lengthOfNormalised = len (normalisedString)

print ("That string normalised is : {}" .format(normalisedString))
print ("We reduced the input string from {} to {} characters" .format (
lengthOfRawString, lengthOfNormalised))