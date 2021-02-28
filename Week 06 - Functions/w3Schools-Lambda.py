# Practicing lambda functions, examples in https://www.w3schools.com/python/python_lambda.asp
# Author: Ross Downey

# A lambda is a small anonymous function, can take a number of arguments, but has only one expression

x = lambda a : a + 10
print(x(5))
# argument is a, this lambda adds 10 to this argument.  Adding 5 to this lambda gives 15

x = lambda a, b : a * b
print(x(5, 6))
# In this case, two arguments a and b are multiplied when called.

x = lambda a, b, c : a + b + c
print(x(5, 6, 2))
# Three arguments, added together when called.

# Lambdas are better utilized when they are an anonymous function inside another function

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2) 
print(mydoubler(11))

#In this case, myfunc(n) is defined as a * n, second function added as a doubler (myfunc(2)).
#Can also be done as a triple function using (myfunc(3)), and can be combined as below.

def myfunc2(n):
  return lambda a : a * n

mydoubler = myfunc2(2)
mytripler = myfunc2(3)

print(mydoubler(100))
print(mytripler(100))

#***Use lambda functions when an anonymous function is required for a short period of time***