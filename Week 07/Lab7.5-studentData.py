# Lab7.5-studentData.py
# This program is taken from the previous week's labsheet and modified
# Author: Ross Downey
import json
students = []
filename = "students.json"
def writeDict(obj):
    with open(filename, "wt") as f:
        json.dump (obj , f) # creating json file to dump data into


def displayMenu ():
    print ("What would you like to do?")
    print ("\t (a) Add new student")
    print ("\t (v) View students")
    print ("\t (s) Save students")
    print ("\t (q) Quit")
    choice = input("Type one letter (a/v/s/q) :") .strip() # strip removes all spaces from a string
    return choice

def doAdd (students):
    currentStudent = {}
    currentStudent ["Name"] = input("Enter Name :")
    currentStudent ["modules"] = readModules()
    students.append (currentStudent)

def readModules():
    modules = []
    moduleName = input("\tEnter the first module name; blank to quit:") .strip()
    while moduleName != "":
        module = {}
        module ["name"] = moduleName # no error handling
        module ["grade"] = int(input("\tEnter grade:"))
        modules.append(module) # now reading next module name
        moduleName = input("\tEnter next module name; blank to quit:") .strip()
    
    return modules
def displayModules (modules):
    print ("\tName  \tGrade")
    for module in modules:
        print ("\t{}    \t{}" .format (module["name"], module["grade"]))

def doView (students):
    for currentStudent in students:
        print (currentStudent ["Name"])
        displayModules (currentStudent["modules"])

def doSave(students):
    writeDict(students)
    print ("student saved")


# main program, following creation of functions above
students = []
choice = displayMenu()
while (choice != 'q'):
    # not using lambda functions, keeping it basic for now
    if choice == 'a':
        doAdd(students)
    elif choice == 'v':
        doView(students)
    elif choice == 's':
        doSave(students)
    elif choice != 'q':
        print ("n\nPlease select either a,v or q")
    choice = displayMenu()

