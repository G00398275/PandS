data = [{'first': 'Guido', 'last': 'Von Rossum', 'YOB': 1956 },
        {'first': 'Alan', 'last': 'Turing', 'YOB': 1912},
        {'first': 'Grace', 'last': 'Hopper', 'YOB': 1906}]

newData = sorted (data, key = lambda item : item['last'])# to the left of colon, what goes in, 
# to the right of the colon what is returned
#print (newData)

for item in newData:
   print (item)