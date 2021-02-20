# Practicing booleans, examples in https://www.w3schools.com/python/python_booleans.asp
# Author: Ross Downey

print(10 > 9) # True
print(10 == 9) # False
print(10 < 9) # False

a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

# defining two variables, confirming which is larger

print(bool("Hello"))
print(bool(15))

# printing bool - evaluates any variable giving a true / false answer

m = "Hello"
n = 15

print(bool(m))
print(bool(n))

# same as above but defining variables

# most values are true except 0, empty strings / lists

bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])
# All above are True
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})
# All above are False

class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))
# if len of string is 0 this will also return False

def myFunction() :
  return True

print(myFunction())
# defining a function and requesting true to be returned

def myFunction1() :
  return True

if myFunction1():
  print("YES!")
else:
  print("NO!")
# In this case requesting a different output if true / false

g = 200
print(isinstance(g, int))
# checking if g is an integer using "isinstance"