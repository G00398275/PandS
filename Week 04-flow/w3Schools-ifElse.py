# Practicing ifElse loops, examples in https://www.w3schools.com/python/python_conditions.asp
# Author: Ross Downey

a = 33
b = 200
if b > a: # condition is IF b is greater than a
  print("b is greater than a") # Ensure indentation is present for print, i.e. indent for condition code

a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b: # condition is ELSE/IF a and b are equal
  print("a and b are equal")

a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else: # Condition is ELSE, when the preceding if/elif conditions aren't met
  print("a is greater than b")

a = 200
b = 33
if b > a:
  print("b is greater than a")
else: # same above without the elif condition, can use just IF and ELSE if needed
  print("b is not greater than a")

if a > b: print("a is greater than b")
# shorthand if, can do on one line if only one simple condition needed

a = 2
b = 330
print("A") if a > b else print("B")
# shorthand if / else, done on one line


a = int(input("Please enter integer a:"))
b = int(input("Please enter integer b:")) # changing code to inputs, ensure integer is used
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else: 
  print("a is greater than b")