# Author: Nathan Calderon
# Filename: evenORodd.py

# This program determines if a list of integers are even or odd 

list = [1,2,3,4,5,6,7,8,9,]
for item in list:
    if (item % 2 != 0):
        print item,
        print 'is odd'
    else:
        print item,
        print 'is even'
