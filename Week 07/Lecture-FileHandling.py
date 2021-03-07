# Practicing file handling, examples in week 07 lecture
# Author: Ross Downey

#with open(".\lecture1.txt", "r") as f:
#    print ("create a file")
# as the file doesn't exist the "r" mode (opening existing file) doesn't work, neither does r+ mode.

#with open(".\lecture1.txt", "w") as f:
#    print ("create a file")
#change to "w" mode, open / create a file, file is created and command  is printed
# append mode "a" will also work
# "x" mode will only work if the file doesn't exist already

#with open(".\lecture1.txt", "w") as f:
 #   print ("create a file")

with open("testData.txt", "rt") as f: # ***using "with" and "as" ensures we don't need to close it again***
    data = f.read(2) # f.read() reads in the data
    print (data) # prints the data from the file 

# can put a number in the brackets after "f.read" to select a number of characters from the file

with open("testData.txt", "rt") as f:
    for line in f: # prints each line in txt file
        print ("We got: ", line.strip()) # strip() remove unnecessary spaces from strings of data

with open ("output.txt", "wt") as f: # creates new file "output.txt" using "w" mode
    f.write("Hello World \ntest") # \n = new line

with open ("output2.txt", "at") as f: # if you are adding to a file use "a" instead of "w" to append
    f.write("Blah\nBlah\nBlah") # \n = new line
    print ("\nmydata", file = f)

    # use "../ to write a file into the parent directory"

