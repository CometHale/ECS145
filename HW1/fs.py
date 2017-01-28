from file_class import File
import pickle
import os

# Change error checking, use raise and Exception()

def bytes_remaining(nbytes):
	return system_bytes_left - nbytes

def create(file_name,nbytes): 
	
	bytes_left = bytes_remaining(nbytes)

	
	if bytes_left >= 0:
		chunk = nbytes * [-1]
		start = 0
		for i in range(0,len(fat) - len(chunk)+1):
			if fat[i:i+len(chunk)] == chunk:
				start = i

		if start > 0:
			return "ERROR"

	else:
		return "ERROR ERROR SYSTEM IS NOT DANK:NO SPACE LEFT BRO"

	# need to fill fat start at index start for n bytes
	for byte in range(0,nbytes):
		fat[start + byte] = file_name
		system.seek(start + byte)
		system.write(None)

	file_list[file_name] = nbytes


def open(file_name,mode): 
	exist = False
	# if system not suspended

	#if file doesn't exist
	if file_name in file_obj.values():
		exist = True
	
	if not exist:
		return "ERROR OPENING FILE: FILE DON'T EXIST BRO"

	try:
		fd = fd_list.index(-1)
		fd_list[fd] = {'file_name':file_name,'pos':0,'length':0,'mode':mode}
		return fd
	except:
		fd_list.append({'file_name':file_name,'pos':0,'length':0,'mode':mode})
		return len(fd_list)


def close(): # Angie
	pass 

def length(): # Angie
	pass

def pos(): # Haley
	pass 

def seek(): # Sally
	pass 

def read(): # Sally
	pass

def write(fd, writebuf):
	
	file_fd_dict = fd_list[fd] # {'file_name':file_name,'pos':0,'length':0,'mode':mode}
	file_obj = file_list[file_fd_dict[file_name]] # file_list[file_name] = nbytes
	fat_start = fat.index(file_name)
	system.seek(fat_start + file_fd_dict[pos]) # Seek to the current filepointer position
	#after the start index of the file in fat
	system.write(writebuf)
	file_fd_dict[pos] += len(writebuf)  # pos is also changed by seek
	file_fd_dict[length] += len(writebuf) # length is the # of bytes


def readlines(): # Sally
	pass

def delfile(): #Haley
	pass

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
	global file_list # name, size
	global fat # list of file_names
	global fd_list # list of dictionaries: file_name, pos, length, mode

	system_name = fsname
	try:
		system = open(fsname,'w')
	except:
		print "ERROR SYSTEM NOT DANK: NATIVE FILE DIDN'T OPEN BRO"
	
	system_size = os.path.getsize(fsname)
	file_list = {}
	fat = [ -1 for i in range(system_size)]
	fd_list = [ -1 for i in range(10)]
	system_bytes_left = system_size

	
	return 0

