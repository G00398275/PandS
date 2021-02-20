# Week 05: studentGrades.py, Lab 5.3 studentGrades
# This program stores a student's name, a list of her courses and grades in a dict
# The program then prints out her data
# Author: Ross Downey

student = {
    "name" : "Mary",
    "modules": [
        {
            "courseName" : "Programming",
            "grade" : 45
        },
        {
            "courseName" : "History",
            "grade": 99
        }
    ]
}
#creating dict to store student's name, courses and grades
print ("Student: {}" .format (student ["name"]))
#printing student's name from dict
for module in student ["modules"]:
    print ("\t {} \t: {}" .format (module["courseName"], module ["grade"]))
# for loop from "modules" in dict, printing (tabbed) courses and grades from dictlea