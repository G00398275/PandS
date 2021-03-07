# Lab 7.2.a; numberRead.py
# This program reads in a number from a file that already exists (count.txt)
# Author: Ross Downey

filename = "count.txt"
def readNumber():
    with open(filename) as f:
        number = int(f.read())
        return number # takes the number from count.txt file

num = readNumber()
print (num) # prints this number, originating from count.txt

