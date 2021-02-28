# Practicing functions, examples in https://www.w3schools.com/python/python_functions.asp
# Author: Ross Downey

def my_function():
  print("Hello from a function")# function is defined as printing this string

my_function() # call the function by typing it with brackets afterwards

def my_function1(fname):
  print(fname + " Refsnes")

my_function1("Emil")
my_function1("Tobias")
my_function1("Linus")
# in this case function is "fname", printing "fname and "Refsnes", 
# calling function three times with different first names Emil, Tobias and Linus
# this is known as passing arguments into functions, in this case the argument is "fname"

#Difference between parameters and arguments
#From a function's perspective:
#A parameter is the variable listed inside the parentheses in the function definition.
#An argument is the value that is sent to the function when it is called.

def my_function2(fname, lname):
  print(fname + " " + lname)

my_function2("Emil", "Refsnes")

# inserting two functions and calling two functions

def my_function3(fname, lname):
  print(fname + " " + lname)

#my_function3("Emil")

# inserting two functions and calling one leads to an error

def my_function4(*kids):
  print("The youngest child is " + kids[2])# 2 being the third element

my_function4("Emil", "Tobias", "Linus")

# adding the * before the function name definition as we don't know how many items are inside

def my_function5(child3, child2, child1):
  print("The youngest child is " + child3)

my_function5(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

# defining the functions with "key = e.g. child 1 = Emil"

def my_function6(**kid):
  print("His last name is " + kid["lname"])

my_function6(fname = "Tobias", lname = "Refsnes")

# Arbitrary keyword arguments (kwargs)
# if you do not know the number of arguments use double asterisk **
# calls one function from two initially

def my_function7(country = "Norway"):
  print("I am from " + country)

my_function7("Sweden")
my_function7("India")
my_function7()
my_function7("Brazil")

# the default parameter value
# when calling my function with just (), Norway is called as this is the defined default

def my_function8(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function8(fruits)

# passing a list as an argument, send list to function, when called it's called as a list still

def my_function9(x):
  return 5 * x

print(my_function9(3))
print(my_function9(5))
print(my_function9(9))

# return function, in this case multiplies the function by 5

def myfunction():
  pass

# pass stops us getting an error when function is incorrectly defined

def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)

# recursion is when a function calls itself
# e.g. tri_recursion is the function, k is the variable, everytime it recurses k - 1 happens.

