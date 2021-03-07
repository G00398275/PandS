# Lab 7.2.b; runCount.py
# This program outputs how many times it has been run
# Author: Ross Downey

filename = "count.txt"
def readNumber():
    with open(filename) as f:
        number = int(f.read())
        return number

def writeNumber(number):
    with open(filename, "wt") as f:
        f.write(str(number)) # comments explaining the above in previous two programs

num = readNumber() # taking the number from the above functions
num += 1 # adding 1 each time it is run
print ("We have run this program {} times" .format (num)) # printimg our required statement
writeNumber(num) # num as a function of writeNumber