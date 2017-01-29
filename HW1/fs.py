from file_class import File
import pickle
import os
import __builtin__

# Change error checking, use raise and Exception()

def bytes_remaining(nbytes):
	return system_bytes_left - nbytes

def create(file_name,nbytes): 
	global system_bytes_left
	bytes_left = bytes_remaining(nbytes)

	# trying to allocate space for file_name

	if bytes_left >= 0:
		chunk = nbytes * [-1]
		start = -1
		for i in range(0,len(fat) - len(chunk)+1):
			if fat[i:i+len(chunk)] == chunk:
				start = i
		
		if start < 0:
			raise Exception("Cannot fit file anywhere")
		
	else:
		raise Exception('ERROR ERROR SYSTEM IS NOT DANK:NO SPACE LEFT BRO')

	# need to fill fat starting at index, start, for n bytes
	for byte in range(0,nbytes):
		fat[start + byte] = file_name
		system.seek(start + byte)
		system.write("\0") # \0 is a null byte apparently

	# adds file_name to file_list
	file_list[file_name] = nbytes
	system_bytes_left = bytes_left

def open(file_name,mode):
	exist = False
	# if system not suspended
	
	#if file doesn't exist
	if file_name in file_list.keys():
		exist = True
	
	if not exist:
		raise Exception("ERROR OPENING FILE: FILE DON'T EXIST BRO")

	try:
		fd = fd_list.index(-1)
		fd_list[fd] = {'file_name':file_name,'pos':0,'length':0,'mode':mode}
		return fd
	except:
		fd_list.append({'file_name':file_name,'pos':0,'length':0,'mode':mode})
		return len(fd_list)


def close(fd): # Angie
	fd_list[fd] = -1 

def length(fd): # Angie
	return fd_list[fd]['length']

def pos(fd): # Haley
	return fd_list[fd].pos

def seek(): # Sally
	pass 

def read(): # Sally
	pass

def write(fd, writebuf):
	
	file_fd_dict = fd_list[fd] # {'file_name':file_name,'pos':0,'length':0,'mode':mode}

	file_obj = file_list[file_fd_dict['file_name']] # file_list[file_name] = nbytes
	fat_start = fat.index(file_fd_dict['file_name'])
	system.seek(fat_start + file_fd_dict['pos']) # Seek to the current filepointer position
	#after the start index of the file in fat
	system.write(writebuf)
	file_fd_dict['pos'] += len(writebuf)  # pos is also changed by seek
	file_fd_dict['length'] += len(writebuf) # length is the # of bytes


def readlines(): # Sally
	pass

def delfile(file_name): #Haley
	file_info = None

	if file_name in file_list.keys():
		file_size = file_list[file_name]
	else:
		raise Exception("File does not exist.")

	for fd in fd_list:
		if fd != -1: # Angie: I changed fd_list[fd] to fd since fd could be a dictionary
			if fd['file_name'] == file_name:
				file_info = fd['file_name']
				#fd_num = fd -- Angie: not sure what this is for??
				break

	#check if file is open
	if file_info is not None: #if we choose to 'delete' fds in close()
		raise Exception("File is open.")
	
	# if file_info['mode'] == "r" or file_info['mode'] == "w": 
	# 	#if we don't 'delete' fds in close
	# 	raise Exception("File is open.")
	#delete the file from native file
	fat_start = fat.index(file_name)

	for i in range(0,file_size - 1):
		system.seek(fat_start + i)
		system.write('\0')
		fat[fat_start + i] = -1

	# fd_list[fd_num] = None
	file_list.pop(file_name)



def deldir(): # Haley
	pass

def mkdir(): # Angie
	pass

def isdir(): # Sally
	pass

def listdir(): # Sally
	pass

def suspend(): # Angie
	pass

def resume(): # Haley
	pass

def chdir():# Haley 
	pass


def init(fsname):

	global system
	global system_name
	global system_size
	global system_bytes_left
	global file_list # A dictionary; {name: size}
	global fat # list of file_names
	global fd_list # list of dictionaries: file_name, pos, length, mode

	system_name = fsname
	system_size = os.path.getsize(fsname)
	system_bytes_left = system_size
	file_list = {}
	fat = [ -1 for i in range(system_size)]
	fd_list = [ -1 for i in range(10)]
	
	try:
		system = __builtin__.open(fsname,'w')
	except:
		print "ERROR SYSTEM NOT DANK: NATIVE FILE DIDN'T OPEN BRO"
	
	return 0