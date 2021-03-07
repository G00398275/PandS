# Practicing OS module, examples in week 07 lecture
# Author: Ross Downey

import os

# os module can be used to check if a file / directory exists
fileName = "amIHere.txt"

if (os.path.exists(fileName)):
    print ("file exists")
else:
    with open(fileName, "x") as f:
        print("Creating the file")

# First time program is run the else part of the loop is run i.e. the file is created
# Run it again and the if part is run i.e. file exists is printed.

