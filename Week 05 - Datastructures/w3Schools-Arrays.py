# Practicing arrays, examples in https://www.w3schools.com/python/python_arrays.asp
# Author: Ross Downey

cars = ["Ford", "Volvo", "BMW"] # Note: Square brackets

x = cars[0] # calling first item in array / list

print (x)

cars[0] = "Toyota" # changing first item from Ford to Toyota

print (cars)

y = len(cars) # len = number of items in array / list
print (y)

for x in cars: # prints all items in array / list, x can be anything as long as telling it to print
  print(x)

cars.append("Honda") # appending (adding) another item to the array

print (cars)

cars.pop(1) # popping (removing) an item from the array, in this case the second item (1)
print (cars)

cars.remove("Toyota") # remove also takes an item from the array
print (cars)