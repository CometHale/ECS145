from file_class import File
import pickle
import os
import __builtin__

# Change error checking, use raise and Exception()

def bytes_remaining(nbytes):
	return system_bytes_left - nbytes

def create(file_name,nbytes): 
	#also deal with creating files in directories
	global system_bytes_left
	bytes_left = bytes_remaining(nbytes)

	# first go to the specified directory's dictionary:

	# cases where file_name is a path
	if file_name.count('/') != 0: 
		name = file_name[file_name.rfind('/')+1:] # gets the actual file name from the path
		path = file_name[:file_name.rfind('/')]
		if path == '':
			filelist = file_list
		else:
			filelist = traversedir(path)

	# file_name is literally just the file name
	else:
		name = file_name
		if cwd != "/": 
			filelist = curr_file_list # go to the current working directory's dictionary
		else:
			filelist = file_list

	# trying to allocate space for file_name

	if bytes_left >= 0:	
		numBytes = nbytes
		for i in range(0, len(fat)):
			if fat[i] == -1 and numBytes != 0: #index is empt
				fat[i] = name
				system.seek(i) #write in native as well
				system.write("\x00") # \0 is a null byte apparently
				numBytes -= 1
	
	else:
		raise Exception("Error: No Space left in native file.")
		
	# adds file_name to file_list
	filelist[name] = nbytes
	file_lengths[name] = 0 # initially zero
	system_bytes_left = bytes_left

def open(file_name,mode):
	exist = False
	# if system not suspended
	if system.closed:
		raise Exception("Error: System is suspended; cannot open file.")
	#if file doesn't exist
	if file_name in file_list.keys():
		exist = True
	
	if not exist:
		raise Exception("Error: File doesn't exist.")

	try:
		fd = fd_list.index(-1)
		fd_list[fd] = {'file_name':file_name,'pos':0,'length':file_lengths[file_name],'mode':mode}
		return fd
	except:
		fd_list.append({'file_name':file_name,'pos':0,'length':0,'mode':mode})
		return len(fd_list) - 1 # last index of fd_list


def close(fd): # Angie
	fd_list[fd] = -1 # frees up the space in fd_list

def length(fd): # Angie
	return fd_list[fd]['length']

def pos(fd): # Haley
	return fd_list[fd]['pos']

def seek(fd, pos): # Sally
	file_fd_dict = fd_list[fd] # {'file_name':file_name,'pos':0,'length':0,'mode':mode}

	nbytes = file_list[file_fd_dict['file_name']] # file_list[file_name] = nbytes

	#error check: pos is negative, larger than file size (nbytes), or makes bytes non-contiguous (pos > length)
	if pos < 0:
		raise Exception("Error: pos argument cannot be negative")
	if pos > nbytes - 1:
		raise Exception("Error: pos argument cannot be bigger than the file size")
	if pos > file_fd_dict['length'] + 1: 
		raise Exception("Error: Bytes must be contiguous")

	file_fd_dict['pos'] = pos;  

def posInFAT(file_name):
	#helper function: returns a list of all indices in FAT where file_name lies (files could be chunked and not contiguous). Indices of this list would be pos)
	#Example: [1, 2, 3, 5, 6] if pos = 2, then fat[3] would be where the byte is
	fat_list = []
	
	for i in range(0, len(fat)):
		if fat[i] == file_name:
			fat_list.append(i)
			
	return fat_list
	
def read(fd, nbytes): # Sally
	file_fd_dict = fd_list[fd] 
	nbytes = file_list[file_fd_dict['file_name']] # file_list[file_name] = nbytes
	list = posInFAT(file_fd_dict['file_name'])
	position = file_fd_dict['pos'] # Seek to the current filepointer position

	#error-check: if read extends beyond the current LENGTH of the file
	if nbytes > file_fd_dict['length']:
		raise Exception("Error: Read goes over size of file")
	
	x = "" #string of read characters
	for i in range(0, nbytes):
		system.seek(list[i + position])
		x = x + system.read(1) #read one byte at time
	
	file_fd_dict['pos'] += nbytes 
	
	return x
  
def write(fd, writebuf):	
	file_fd_dict = fd_list[fd] # {'file_name':file_name,'pos':0,'length':0,'mode':mode}

	if file_fd_dict['mode'] is not 'w':
		raise Exception("Error: Not in writing mode")

	fname = file_fd_dict['file_name']
	nbytes = file_list[file_fd_dict['file_name']] # file_list[file_name] = nbytes
	list = posInFAT(file_fd_dict['file_name'])
	position = file_fd_dict['pos'] # Seek to the current filepointer position
	
	fat_start = fat.index(file_fd_dict['file_name'])
	system.seek(fat_start + file_fd_dict['pos']) # Seek to the current filepointer position

	#error-check (if writebuf is bigger than file size)
	if len(writebuf) > nbytes or len(writebuf) > (nbytes - file_lengths[fname]):
		raise Excpetion("Error: Not enough bytes to write")

	#after the start index of the file in fat
	for i in range(0, len(writebuf)):
		system.seek(list[i + position]) 
		system.write(writebuf[i])
	
	file_fd_dict['pos'] += len(writebuf)  # pos is also changed by seek
	file_fd_dict['length'] += len(writebuf) # length is the # of bytes act written to
	file_lengths[fname] += len(writebuf) # update length in file_lengths too

def readlines(fd): # Sally
	file_fd_dict = fd_list[fd] # {'file_name':file_name,'pos':0,'length':0,'mode':mode}
	lines = []
	string = ""
	
	nbytes = file_list[file_fd_dict['file_name']] # file_list[file_name] = nbytes
	l = posInFAT(file_fd_dict['file_name'])

	for i in range(0, len(l)):
		system.seek(l[i])
		c = system.read(1)
		string = string + c
		if i == len(l) - 1: # reached end of contents
			lines.append(string)
		elif c == '\0xa':#new line character
			lines.append(string)
			string = "" #reset the string
	
	return lines

def delFileInDir(file_name, list): #helper function 
	if file_name in list:
		del list[file_name]
		return
	
	for file in list:
		if isinstance(file, dict): #directory
			delFileInDir(file_name, file)

def delfile(file_name): #Haley
	
	file_info = None

	if file_name in file_list.keys():
		file_size = file_list[file_name]
	else:
		raise Exception("Error: File does not exist.")

	for fd in fd_list:
		if fd != -1: # Angie: I changed fd_list[fd] to fd since fd could be a dictionary
			if fd['file_name'] == file_name:
				file_info = fd['file_name']
				break

	#check if file is open
	if file_info is not None:
		raise Exception("Error: File is open.")
	
	#delete the file from native file
	for i in range(0, len(fat)):
		if fat[i] == file_name: #clean this index out
			system.seek(i)
			system.write('\x00')
			fat[i] = -1

	# make sure to change curr_file_list
	delFileInDir(file_name, file_list)	#deletes with nested dictionaries too
		
def deldir(dirname): # Haley
	# make sure to change curr_file_list
	global cwd
	global curr_file_list
	#check to see if the dirname is a dir
	# if not isdir(dirname):
	# 	raise Exception("File is not a directory: use delfile instead.")
	#check to see if currently in dir
	last_slash = cwd.rfind("/")
	prev_dir_name = cwd[last_slash + 1:len(cwd)]
	if prev_dir_name == cwd:
		raise Exception("Error: Currently in " + dirname + ":Cannot delete an active directory.")
	if dirname not in curr_file_list:
		raise Exception("Error:" + dirname + ":No such directory.")

	curr_file_list.pop(dirname)

def traversedir(path):
	# goes through file_list to return the directory specified in the last portion of the path
	# only pass PATHS

	# paths are either ./a/b, ../a/b, /a/b, or a/b
	firstpart = path[:path.find('/')]
	if firstpart == "..": # ../a/b
		path = path[path.find('/')+1:] # a/b
		prevdirpath = cwd[:cwd.rfind('/') + 1] # /s/d/
		dirlist = prevdirpath + path # dirlist = /s/d/a/b
	elif firstpart == ".": # ./a/b
		path = path[path.find('/'):] # /a/b 
		dirlist = cwd + path
	elif firstpart == '': # absolute paths
		dirlist = path
	else: # a/b
		dirlist = cwd + '/' + path

	dirlist = dirlist.split('/') #/a/b/c -> ["", a, b, c]
	del dirlist[0] # deletes "" from the list 
	dir_count = len(dirlist)
	if dirlist[0] != "":
		#print dirlist[0]
		directory = file_list[dirlist[0]] # dir_list[0] = first directory
	else:
		directory = file_list
	for i in range(dir_count):
		if i == dir_count - 1:
			break
		directory = directory[dirlist[i+1]]
	return directory

def mkdir(dirname): # Angie

	if dirname.count('/') == 0: # if dirname is not a path, just the name
		curr_file_list[dirname] = {}
	else: # if dirname is a path like ../a/b, ./a/b, /a/b, or a/b
		last_slash = dirname.rfind('/')
		name = dirname[last_slash+1:]  # gets the name of the directory to create
		traversedir(dirname[:last_slash])[name] = {}

def isdir(dirname): # Sally
	# make sure to include '.', '..'
  if dirname == '.' or dirname == "..": #look at current directory 
    return True #they're obviously directories lol
  else: #relative or absolute path
    if dirname.count('/') == 0: #look in current dir (relative path)
      if isinstance(curr_file_list[dirname], (int, long)): #a file if True
        return False
      else:
        return True
    else: #must traverse thru multiple directories (using traverse(dir)
      #cut off the last part (ie. a/b/c we change to a/b)
      checkDir = dirname[dirname.rfind('/') : ] #finds last occurence of / (ie. checkDir is now /c)
      checkDir = checkDir[1:] #cut off the / (ie. check Dir is now c)
      dir = traversedir(cwd + dirname[: dirname.rfind('/')]) #traversedir(a/b)
      if isinstance(dir[checkDir], (int, long)):
        return False
      else: 
        return True

def listdir(dirname): # Sally
	# make sure to include '.', '..'
  list = []
  
  if dirname == '.': # its the current directory
    return curr_file_list
  elif dirname == "..": #find the previous directory
    #cwd is the absolute path
    dirPath = cwd[: cwd.find('/')] #get rid of last / (ie. a/b/c -> a/b)
  else: #absolute or relative path
    if dirname[0] == '/': #absolute path
      dirPath = dirname
    else: #relative path ->traverseDir needs an absolute path
      dirPath = cwd + dirname
   
  dir = traversedir(dirPath) #we get a dictionary
  #put keys into a list
  for key in dir:
    list.append(key)
   
  return list

def suspend(): # Angie
	
	for fd in fd_list:
		if type(fd) is dict:
			if fd['mode'] == 'w':
				raise Exception("There are files still opened for writing")

	pickleFile = __builtin__.open(system_name + ".fssave", "wb")

	system.close()
	pickle.dump(system_name, pickleFile)
	pickle.dump(system_bytes_left, pickleFile)
	pickle.dump(file_list, pickleFile)
	pickle.dump(file_lengths, pickleFile)
	pickle.dump(fat, pickleFile)
	pickle.dump(fd_list, pickleFile)

	pickleFile.close()

def resume(pFile): # Angie

	global system
	global system_name
	global system_size
	global system_bytes_left
	global file_list # A dictionary; {'name1': size1, 'name2': size2,'dir': {'file': size} ...}
	global curr_file_list # make sure to change this list whenever we call chdir
	global cwd # to determine what files go in curr_file_list
	global file_lengths # A dictionary; {'name1': length1, 'name2': length2...}
	global fat # list of file_names
	global fd_list # list of dictionaries: file_name, pos, length, mode


	pickleFile = __builtin__.open(pFile, 'rb')
	
	system_name = pickle.load(pickleFile)
	system_bytes_left = pickle.load(pickleFile)
	file_list = pickle.load(pickleFile)
	curr_file_list = file_list
	print curr_file_list
	cwd = '/'
	file_lengths = pickle.load(pickleFile)
	fat = pickle.load(pickleFile)
	fd_list = pickle.load(pickleFile)
	system = __builtin__.open(system_name, 'r+')
	system_size = os.path.getsize(system_name)
	pickleFile.close()

def chdir(dirname):# Haley 
	#make sure to change curr_file_list
	# . and ..
	# might need to be able to handle a long string of dirs

	# Haley: Have to declare the globals 
	#in any function that assigns to them
	#http://stackoverflow.com/questions/423379/using-global-variables-in-a-function-other-than-the-one-that-created-them
	global curr_file_list
	global cwd
	global file_list
	# "." doesn't change the cwd

	if dirname.count('/') > 0: # dirname is some sort of path
		curr_file_list = traversedir(dirname)
		print dirname[0]
		if dirname[0] == '/': # root
			cwd = dirname
		elif dirname[0] == '.': # ./a
			dirname = dirname[dirname.find('/'):] # gets rid of '.', or '..'
			cwd = cwd + dirname
		elif dirname[1] == '.': #../a
			dirname = dirname[dirname.find('/'):]
			cwd = cwd[:cwd.rfind('/')] + dirname
		else: # a/b
			if cwd == '/':
				cwd = cwd + dirname
			else:
				cwd = cwd + '/' + dirname

	else: # dirname is just a name or .. or .
		if dirname == "..":
			if cwd[:cwd.rfind('/')] == '': # prev dir is root
				cwd = '/'
				curr_file_list = file_list
			else:
				cwd = cwd[:cwd.rfind('/')]
				curr_file_list = traversedir(cwd)
		elif dirname == ".":
			pass # do nothing
		elif dirname in curr_file_list:
			curr_file_list = curr_file_list[dirname]
			if cwd == '/':
				cwd = cwd + dirname
			else:
				cwd = cwd + '/' + dirname
		else:
			raise Exception("Error:" + dirname + ":No such directory.")

def init(fsname):

	global system
	global system_name
	global system_size
	global system_bytes_left
	global file_list # A dictionary; {'name1': size1, 'name2': size2,'dir': {'file': size} ...}
	global curr_file_list # make sure to change this list whenever we call chdir
	global cwd # to determine what files go in curr_file_list
	global file_lengths # A dictionary; {'name1': length1, 'name2': length2...}
	global fat # list of file_names
	global fd_list # list of dictionaries: file_name, pos, length, mode

	system_name = fsname
	system_size = os.path.getsize(fsname)
	system_bytes_left = system_size
	file_list = {}
	file_lengths = {}
	curr_file_list = file_list
	cwd = '/'
	fat = [ -1 for i in range(system_size)]
	fd_list = [ -1 for i in range(10)]
	
	try:
		system = __builtin__.open(fsname,'w+')
	except:
		raise Exception("Error opening the native file.")
	
	return 0