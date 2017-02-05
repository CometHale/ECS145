#!/bin/python
import os
import fs

small_test = "abc.txt" # 5 bytes
medium_test = "def.txt" # 300 bytes 
large_test = "ghi.txt" #3,000,000 bytes
first_file = "f1"
second_file = "f2"
third_file = "f3"
first_dir = "d1"
second_dir = "d2"
third_dir = "d3"

######### TESTS THAT SHOULD PASS #########


#SMALL SYSTEM
#Test creation of the file system
result = fs.init(small_test)

if result != 0:
	print "Error: Failed to init the system.\n"

#Test create file
print "Creating first_file (2 byte file)...\n"
fs.create(first_file,2)

if first_file not in fs.file_list:
	print "Error: Failed to create first_file.\n"

#Test writing
print "Opening 2 byte file for writing...\n"
fd_f1 = fs.open(first_file,"w")

if fd_f1 < 0:
	print "Error: Failed to open first_file."

fs.write(fd_f1,"aa")

test_length = fs.length(fd_f1)

if test_length < 2:
	print "Error: Failed to write to first_file.\n"

f1_pos = fs.pos(fd_f1)

if f1_pos != 2:
	print "Error: filepointer in incorrect place.\n"
fs.close(fd_f1)

if fs.fd_list[fd_f1] != -1:
	print "Error: File didn't close properly.\n"

print "Making the first directory...\n"
fs.mkdir(first_dir)

if first_dir not in fs.file_list:
	print "Error: directory not created.\n"

print "Creating second file in first directory...\n"
fs.chdir(first_dir)

if fs.cwd != "/" + first_dir:
	print "Error: chdir failed.\n"
fs.create(second_file,2)

if second_file not in fs.curr_file_list:
	print "Error: second file not created in the current directory (should be d1).\n"

print "Making second directory within first directory with one call...\n"

fs.chdir("..")

if fs.cwd != "/":
	print "Error: Failed to change back to root directory.\n"

fs.mkdir(first_dir + "/" + second_dir)

fs.chdir(first_dir)

if second_dir not in fs.curr_file_list:
	print "Error: Could not make second directory.\n"
print fs.file_list

print "Suspending " + small_test + " ...\n"
fs.suspend()
print "Resuming " + small_test + " ...\n"
fs.resume(small_test + ".fssave")
print fs.file_list
print "Suspending " + small_test + " ...\n"
fs.suspend()



#MEDIUM SYSTEM
#Test creation of the file system
result = fs.init(medium_test)

if result != 0:
	print "Error: Failed to init the system.\n"

#Test create file
print "Creating first_file (70 byte file)...\n"
fs.create(first_file,70)

if first_file not in fs.file_list:
	print "Error: Failed to create first_file.\n"

#Test writing
print "Opening 70 byte file for writing...\n"
fd_f1 = fs.open(first_file,"w")

if fd_f1 < 0:
	print "Error: Failed to open first_file."

fs.write(fd_f1,"aaaaaaaaa\naaaaaaaaa\naaaaaaaaa\naaaaaaaaa\naaaaaaaaa\naaaaaaaaa\naaaaaaaaa\naaaaaaaaa\naaaaaaaaa")

test_length = fs.length(fd_f1)
correct_length = len("aaaaaaaaa\naaaaaaaaa\naaaaaaaaa\naaaaaaaaa\naaaaaaaaa\naaaaaaaaa\naaaaaaaaa\naaaaaaaaa\naaaaaaaaa")
if test_length != correct_length:
	print "Error: Failed to write to first_file.\n"

f1_pos = fs.pos(fd_f1)

if f1_pos != correct_length:
	print "Error: filepointer in incorrect place.\n"
fs.close(fd_f1)

if fs.fd_list[fd_f1] != -1:
	print "Error: File didn't close properly.\n"

print "Making the first directory...\n"
fs.mkdir(first_dir)

if first_dir not in fs.file_list:
	print "Error: directory not created.\n"

print "Creating second file in first directory...\n"
fs.chdir(first_dir)

if fs.cwd != "/" + first_dir:
	print "Error: chdir failed.\n"
fs.create(second_file,50)

if second_file not in fs.curr_file_list:
	print "Error: second file not created in the current directory (should be d1).\n"

print "Making second directory within first directory with one call...\n"

fs.chdir("..")

if fs.cwd != "/":
	print "Error: Failed to change back to root directory.\n"

fs.mkdir(first_dir + "/" + second_dir)

fs.chdir(first_dir)

if second_dir not in fs.curr_file_list:
	print "Error: Could not make second directory.\n"


print fs.file_list

print "Suspending " + medium_test + " ...\n"
fs.suspend()
print "Resuming " + medium_test + " ...\n"
fs.resume(small_test + ".fssave")
print fs.file_list

fs.delfile(first_file)
print "Creating /d1/d2/d3/d4/f3 ...\n"
fs.create("/d1/d2/d3/d4/" + third_file,30)
print fs.file_list



#MEGA SYSTEM
#Test creation of the file system
result = fs.init(large_test)

if result != 0:
	print "Error: Failed to init the system.\n"

#Test create file
print "Creating first_file (100000 byte file)...\n"
fs.create(first_file,100000)

if first_file not in fs.file_list:
	print "Error: Failed to create first_file.\n"

#Test writing
print "Opening 100000 byte file for writing...\n"
fd_f1 = fs.open(first_file,"w")

if fd_f1 < 0:
	print "Error: Failed to open first_file."

fs.write(fd_f1,"aaaaaaaaaaaaaaaaaaaaaaa\naaaaaaaaaaaaaaaaaaaa\naaaaaaaaaaaaaaaaaaa\naaaaaaaaaaaa\naaaaaaaaaaaaaaaaaaaaaaa\naaaaaaaaaaaaaaaaaaaa\naaaaaaaaaaaaaaaaaaa\naaaaaaaaaaaa\n")

correct_length = len("aaaaaaaaaaaaaaaaaaaaaaa\naaaaaaaaaaaaaaaaaaaa\naaaaaaaaaaaaaaaaaaa\naaaaaaaaaaaa\naaaaaaaaaaaaaaaaaaaaaaa\naaaaaaaaaaaaaaaaaaaa\naaaaaaaaaaaaaaaaaaa\naaaaaaaaaaaa\n")
test_length = fs.length(fd_f1)

if test_length != correct_length:
	print "Error: Failed to write to first_file.\n"

f1_pos = fs.pos(fd_f1)

if f1_pos != correct_length:
	print "Error: filepointer in incorrect place.\n"
fs.close(fd_f1)

if fs.fd_list[fd_f1] != -1:
	print "Error: File didn't close properly.\n"	

print "Making the first directory...\n"
fs.mkdir(first_dir)

if first_dir not in fs.file_list:
	print "Error: directory not created.\n"

print "Creating second file in first directory...\n"
fs.chdir(first_dir)

if fs.cwd != "/" + first_dir:
	print "Error: chdir failed.\n"
fs.create(second_file,150)

if second_file not in fs.curr_file_list:
	print "Error: second file not created in the current directory (should be d1).\n"

print "Making second directory within first directory with one call...\n"

fs.chdir("..")

if fs.cwd != "/":
	print "Error: Failed to change back to root directory.\n"

fs.mkdir(first_dir + "/" + second_dir)

fs.chdir(first_dir)

if second_dir not in fs.curr_file_list:
	print "Error: Coule not make second directory.\n"
print fs.file_list

print fs.file_list


######### TESTS THAT SHOULD FAIL #########


#creating a file far down a nest of dirs
# writing multiple lines and reading them
# overwriting a file
# test deleting files with paths like ./a, ../a, /a, ./a/b, ../a/b, /a/b, a/b 
# test deleting files from other directories without being side them
# test if reading and writing incontinguous files work (aka. delete files that are in between other files to write incontinguous files)






