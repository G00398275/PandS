# Practicing JSON, examples in week 07 lecture
# Author: Ross Downey

import json

electricBill = {
    'name': 'Shannon',
     'amount': '567'
}

with open("storeData.json", "wt") as f:
    json.dump(electricBill, f)# creates a new file in JSON format in this folder, JSON format is "" around everything

with open ("storeData.json", "rt") as f:
    readDict = json.load(f) # loads the JSON file and puts into a new JS oblect called readDict
    print (readDict["name"]) # prints just the name from readDict, in this case "Shannon"