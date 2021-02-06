# Week 03: Lab 3.3.2 Strings
# This program reads in a string and removes any leading or trailing spaces
# It also converts all letters to lower case
# This program also outputs the length of the original string
# Author: Ross Downey

rawString = input("Please enter a string: ")
normalisedString = rawString.strip().lower()

lengthOfRawString = len(rawString)
lengthOfNormalised = len(normalisedString)

print("That string normalised is: {}" .format(normalisedString))
print("We reduced the input string from {} to {} characters" .format (
lengthOfRawString, lengthOfNormalised))