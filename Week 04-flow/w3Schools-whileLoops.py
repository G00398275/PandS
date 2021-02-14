# Practicing while loops, examples in https://www.w3schools.com/python/python_while_loops.asp
# Author: Ross Downey

i = 1
while i < 6: # initiaing while loop
  print(i)
  i += 1 # increment i or else loop will be infinite

i = 1
while i < 6:
  print(i)
  if i == 3:
    break # breaking loop when i becomes 3, even though 3 < 6
  i += 1

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue # continuing on the loop if i = 3, starts a new iteration until i becomes 6
  print(i)

i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6") # else statement, prints when i reaches 6 in the loop
