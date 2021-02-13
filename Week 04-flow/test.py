i = int(input("Please enter integer:"))
numbers = []
numbers.append(i)
x = i

while x!=1:
    if x % 2 == 0:
        numbers.append (x/2)
        x = x/2
    else:
        numbers.append ((x *3) + 1)
        x = x*3 + 1

for value in numbers:
    print (int(value))