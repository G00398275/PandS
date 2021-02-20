# Practicing lists, examples in https://www.w3schools.com/python/python_lists.asp
# Author: Ross Downey

thislist = ["apple", "banana", "cherry"]
print(thislist)

# creating list, note square brackets
# list are ordered, changeable and allow duplicate values

thislist = ["apple", "banana", "cherry", "apple", "cherry"] # duplicates
print(thislist)

thislist = ["apple", "banana", "cherry"]
print(len(thislist))
# len function gives the  length of the list, in this case 3 items in list

list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
# different data types e.g. strings, ints, booleans

list4 = ["abc", 34, True, 40, "male"]
# different data types in one list

mylist = ["apple", "banana", "cherry"]
print(type(mylist))
# type will give the type of array, in this case it's a list

thislist = list(("apple", "banana", "cherry")) # double round-brackets
print(thislist)
# list constructor, square brackets not used

thislist = ["apple", "banana", "cherry"]
print(thislist[1])
# calling items from a list by index; 0 is first, 1 is second etc. banana is called here for example

thislist = ["apple", "banana", "cherry"]
print(thislist[-1])
# can also call items in reverese index; -1 is last, -2 is second last. cherry is called here

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
# calling a range of items in a list using index values, 2:5 calls 3rd to 5th values inclusive

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])
# leaving no value before the colon, defaults to zero, same as putting 0:4 in the brackets
# calls 1st to 4th values

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])
# leaving the end value blank calls the list to the end. in this case "cherry" to "mango"

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])
# doesn't return "mango", if wanted to include mango leave blank instead of -1

thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")
# can check if an item is in a list with if and in functions

thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)
# can change an item in a list, can also change a range it needed using [0:2] for example

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)
# can insert new items in a list if needed, number specified position to be inserted

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)
# can append new itemss (add to end of list)

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
# Extending a list with another list: Returns both lists combined

thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)
# extends a list with a tuple; note stays as list, adding items from tuple to list

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)
# removes an item from a list

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)
# removes or pops out an item by its index (1 is second item)

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)
# del function also deleted by index position

