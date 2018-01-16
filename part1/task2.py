#!/usr/bin/python

import os

# assigning path
directory = "/home/011/a/ax/axc142230/cs3376assignment4"

# declaraing variables that keep track of file size and the number of file
cSize = 0
plSize = 0
txtSize = 0
miscSize = 0
totalSize = 0
cCounter = 0
plCounter = 0
txtCounter = 0
miscCounter = 0

# looping through the targeted directory
for filename in os.listdir(directory):
    if filename.endswith(".pl"):
        plCounter += 1
        plSize += os.path.getsize(filename)
    elif filename.endswith(".c"):
        cCounter += 1
        cSize += os.path.getsize(filename)
    elif filename.endswith(".txt"):
	    txtCounter += 1
	    txtSize += os.path.getsize(filename)
    else:
      miscCounter += 1
      miscSize += os.path.getsize(filename)

# caculating the total size of all files and the total number of files
totalSize = cSize + plSize + txtSize + miscSize
totalCounter = cCounter + txtCounter + plCounter + miscCounter

# output
print "file extension      count"
print "----------------    -------"
print ".c               ",cCounter
print ".txt             ",txtCounter
print ".pl              ",plCounter
print "*                ",miscCounter
print "---------------------------"
print "total            ",totalCounter
print "                           "
print "                           "
print "file extension       total size"
print "----------------    -----------"
print ".c                    ",cSize
print ".txt                  ",txtSize
print ".pl                   ",plSize
print "*                     ",miscSize
print "-------------------------------"
print "total                 ",totalSize
