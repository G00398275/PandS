# Practicing modules, examples in https://www.w3schools.com/python/python_modules.asp
# Author: Ross Downey

# Consider a module to be the same as a code library.
# A file containing a set of functions you want to include in your application.

import mymodule # importing module from mymodule.py in Week 06 folder
mymodule.greeting("Jonathan")

# ***ensure to use module_name.function_name***

import mymodule
a = mymodule.person1["age"]
print(a)

# calling one item from the dict in mymodule.py

import mymodule as mx # importing under an alias, used for sensitive information
a = mx.person1["country"]
print(a)

import platform # built in module, in this case = Windows
x = platform.system()
print(x)

import platform
x = dir(platform)  # directory in Windows platform
print(x)

from mymodule import person1 # choosing only one module from mymodule.py. Dont need all of them.
print (person1["age"])

# Modules can be handy to reduce the amount of code in one program 