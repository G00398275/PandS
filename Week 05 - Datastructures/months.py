# Week 05: months.py, Lab 5.2 Months
# This program stores the months of the year in a tuple
# and also contains another tuple with just the Summer months, printing them out one at a time
# Author: Ross Downey

months = ("January",
            "February",
            "March",
            "April",
            "May",
            "June",
            "July",
            "August",
            "September",
            "October",
            "November",
            "December",
) # First tuple created listing all months of the year
summer = months [4:7]
# second tuple within first identifying summer months, 4:7 being 5th, 6th and 7th months
for month in summer:
    print (month)
# for loop, printing out Summer months