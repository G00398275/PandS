# Lab 7.2.b; overwriteNumber.py
# This program reads in a number from a file and overwrites that number (count.txt)
# Author: Ross Downey

filename = "count.txt"
def writeNumber(number):
    with open(filename, "wt") as f: # opening file with "w" mode
        f.write(str(number)) # write mode takes a string so conversion required

writeNumber(3)
# overwrites the number in count.txt with 3

