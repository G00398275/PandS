# Lab 7.3; json1.py
# This program stores a simple dict to a file as JSON. TEST IT
# Author: Ross Downey

import json
filename = "testdict.json"
sample = dict(name = 'fred', age = 31, grades = [1,34,55])

def writeDict(obj): # writeDict defined as obj
    with open (filename, 'wt') as f: # "w" mode for writing into files
        json.dump(obj,f) # json.dump for writing a dict/list to a file

writeDict(sample) # sample as function of writeDict

# new file created "testdict.json" with dict outlined above written in

