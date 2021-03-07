# Practicing JSON, examples in https://www.w3schools.com/python/python_json.asp
# Author: Ross Downey

#JSON is a syntax for storing and exchanging data.
#JSON is text, written with JavaScript Object Notation.

import json

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'
# parse x:
# to parse is to analyse the dict above and break into usable parts.
y = json.loads(x)
# the result is a Python dictionary:
print(y["age"])

import json

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))

# all of the above are converting Python objects to JSON strings and printing them using json dumps
# below are JSON outputs for python inputs

#Python	JSON
#dict	Object
#list	Array
#tuple	Array
#str	String
#int	Number
#float	Number
#True	true
#False	false
#None	null

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

#print(json.dumps(x, indent = 4, separators=(". ", " = ")))

# defining indents and separators to output the data in a more readable format

print(json.dumps(x, indent = 4, sort_keys=True))
#sort_keys specifiies whether the result should be sorted(True) or not(False)