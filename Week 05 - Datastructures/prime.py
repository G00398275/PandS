# This program lists out the prime numbers between 2 and 100
# Week 05, Tutorial
# Author: Ross Downey

primes = []
upto = 100000

for candidate in range (2, upto):
    isPrime = True # Required only to check if divisible by prime number
    for divisor in primes: # If it is divisible by an integer it isn't a prime number
        if (candidate % divisor == 0):
            isPrime = False
            break # No reason to keep checking if not prime number

    if isPrime:
        primes.append(candidate) # If it is a prime number, append it to the list
print (primes)