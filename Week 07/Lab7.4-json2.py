# Lab 7.4; json2.py
# This program reads a dict. from file testdict.json
# Author: Ross Downey

import json
filename = "testdict.json" # specifying file

def readDict():
    with open(filename) as f:
        return json.load(f) # loads dict from json file testdict.json

somedict = readDict() # calling readDict function "somedict" to set up printing
print (somedict)


