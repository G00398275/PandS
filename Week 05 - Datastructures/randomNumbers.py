# Week 05: randomNumbers.py, Lab 5.3 randomNumbers
# This program puts 10 random numbers in queue
# then outputs all values in this queue
# the numbers are taken from the queue one at a time and prints the remaining numbers
# Author: Ross Downey

import random
queue = []
numberOfNumbers = 10
rangeTo = 100
#setting up program, variable type, number of random numbers and range

for n in range (0, numberOfNumbers):
    queue.append(random.randint (0, rangeTo))
# appending required random numbers to queue in the required range

print ("queue is {}" .format (queue))
#printing ten random numbers in queue intially

while len(queue) != 0:

    currentNumber = queue.pop (0)
    print ("current Number is {} and the queue is {} " .format (currentNumber, queue))
# while loop, removing one digit from queue and printing remaining digits, until none are left

print ("The queue is now empty!")
# Final print statement on removal off all numbers from queue