# Practicing for loops, examples in https://www.w3schools.com/python/python_for_loops.asp
# Author: Ross Downey

fruits = ["apple", "banana", "cherry"] # square brackets for list
for x in fruits: # selects all fruits in the list
  print(x)

for x in "banana": # loops through all letters in banana (Note: no brackets used)
  print(x)

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break # breaks loop when x becomes banana, only prints apple and banana

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x) # does not print banana, continues to end of list

for x in range(6): # range - starts at default 0, stops one below number i.e 0,1,2,3,4,5
  print(x)

for x in range(2, 6): # specifies the start of range instead of defaulting to 0
  print(x)

for x in range(2, 30, 3): # third value sets the increment, in this case increments of 3
  print(x)

for x in range(6):
  print(x)
else: # else do a subsequent task when the range loop is finished
  print("Finally finished!")

for x in range(6):
  if x == 3: break # because of the break the loop stops at 2, and does not print the "Else" statement
  print(x)
else:
  print("Finally finished!")

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits: # nested loop, runs through this for each part of the first loop (Note: Indentation)
    print(x, y)

for x in [0, 1, 2]:
  pass # pass avoids an error

adj = ["red", "blue", "black", "yellow"]
nouns = ["door", "wall", "car", "table"]

for x in adj:
  for y in nouns:
    print (x,y)
  if (x,y) == "blue wall":
    break
  else:
    print ("Finished!")