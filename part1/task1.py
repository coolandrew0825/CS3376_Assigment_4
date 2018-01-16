#!/usr/bin/python

import os, sys

# create multiple directory paths and assign them to different variables
dir1Path = "/home/011/a/ax/axc142230/cs3376assignment4/dir1"
dir11Path = "/home/011/a/ax/axc142230/cs3376assignment4/dir1/dir11"
dir12Path = "/home/011/a/ax/axc142230/cs3376assignment4/dir1/dir12"
dir111Path = "/home/011/a/ax/axc142230/cs3376assignment4/dir1/dir11/dir111"
dir121Path = "/home/011/a/ax/axc142230/cs3376assignment4/dir1/dir12/dir121"

# create dir1 and give full access to the user
os.mkdir(dir1Path, 0755);

# change to dir1 from the current directory
os.chdir(dir1Path)

# create files in dir1
fo = open("c100.c", "w+")
fo = open("c200.c", "w+")
fo = open("c300.c", "w+")
fo = open("p010.pl", "w+")
fo = open("p020.pl", "w+")
fo = open("p030.pl", "w+")
fo = open("t001.txt", "w+")
fo = open("t002.txt", "w+")
fo = open("t003.txt", "w+")
fo = open("f100", "w+")
fo = open("f200", "w+")

# create dir11 and give full access to the user
os.mkdir(dir11Path, 0755);

# change to dir11 from dir1
os.chdir(dir11Path)

# create files in dir11
fo = open("c100.c", "w+")
fo = open("c200.c", "w+")
fo = open("c300.c", "w+")
fo = open("p010.pl", "w+")
fo = open("p020.pl", "w+")
fo = open("p030.pl", "w+")
fo = open("t001.txt", "w+")
fo = open("t002.txt", "w+")
fo = open("t003.txt", "w+")
fo = open("f100", "w+")
fo = open("f200", "w+")

# create dir111 and give full access to the user
os.mkdir(dir111Path, 0755);

# Use os.fchdir() method to change back to dir1
fd = os.open(dir1Path, os.O_RDONLY)
os.fchdir(fd)

# create dir12 and give full access to the user
os.mkdir(dir12Path, 0755);

# change to dir12 from the current directory
os.chdir(dir12Path)

# create files in dir12
fo = open("c100.c", "w+")
fo = open("c200.c", "w+")
fo = open("c300.c", "w+")
fo = open("p010.pl", "w+")
fo = open("p020.pl", "w+")
fo = open("p030.pl", "w+")
fo = open("t001.txt", "w+")
fo = open("t002.txt", "w+")
fo = open("t003.txt", "w+")
fo = open("f100", "w+")
fo = open("f200", "w+")

# create dir121 and give full access to the user
os.mkdir(dir121Path, 0755);
