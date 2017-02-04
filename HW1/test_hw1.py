#!/bin/python
import os
import fs

small_test = "abc.txt" # 5 bytes
medium_test = "" # 300 bytes 
large_test = "" #300,000 bytes
first_file = "f1"
second_file = "f2"
third_file = "f3"
first_dir = "d1"
second_dir = "d2"
third_dir = "d3"



######### TESTS THAT SHOULD PASS #########
#Test creation of the file system
result = fs.init(small_test)

if result != 0:
	print "Failed to init the system.\n"

#Test create file
print "Creating first_file (2 byte file)...\n"
fs.create(first_file,2)

if first_file not in fs.file_list:
	print "Failed to create first_file.\n"

#Test writing
print "Opening 2 byte file for writing...\n"
fd_f1 = fs.open(first_file,"w")

if fd_f1 < 0:
	print "Failed to open first_file."

fs.write(fd_f1,"aa")

test_length = fs.length(fd_f1)

if test_length < 2:
	print "Failed to write to first_file.\n"

f1_pos = fs.pos(fd_f1)
fs.close(fd_f1)


######### TESTS THAT SHOULD FAIL #########


#creating a file far down a nest of dirs
# writing multiple lines and reading them
# overwriting a file
# test deleting files with paths like ./a, ../a, /a, ./a/b, ../a/b, /a/b, a/b 
# test deleting files from other directories without being side them
# test if reading and writing incontinguous files work (aka. delete files that are in between other files to write incontinguous files)






