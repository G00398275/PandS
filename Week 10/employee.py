# Lab 10.4 Objects; employee.py
# This program has an attribute called timesheets and an init function takes in a first and last name
# Author: Ross Downey

class Employee:
    timesheets = []

    def __init__ (self, first, last):
        self.first = first
        self.last = last

    def __str__(self):
        return self.first + '' + self.last

if __name__ == '__main__':
    test = Employee ('some', 'one')
    print (test)
    assert ('someone' == str(test))

from timesheetentry import Timesheetentry # error noted on importing wildcard, imported function instead
import datetime as dt # as only function imported, need to import datetime again

def logminutes (self, project, minutes):
    now = dt.datetime.now
    timesheetentry = Timesheetentry(project, now, minutes)
    self.timesheets.append(timesheetentry)

def gettotaltime(self):
    'total_minutes' = 0
    for ts in self.timesheets:
        total_minutes += ts.duration
    return total_minutes

if __name__ == '__main__':
    test = Employee ('some', 'one')
    print (test)
    assert ('someone') == str(test))
    test.logminutes ('p1', 30)
    test.logminutes ('p1', 60)
    mins = test.gettotaltime()
    print (mins)
    assert ( mins = 90)

    print ('all good')

    