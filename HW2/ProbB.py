import thread 
import os

def countchar(pos):
# updates lenlist, do not count EOL as part of line length
	global lenlist, nthread, readlock, file, listlock, threadlock

	index = 0

	readlock.acquire()
	file.seek(0)
	line = file.read(pos)
	readlock.release()

	# gets the line number (index) to start counting bytes for
	for i in line:
		if i == '\n':
			index += 1

	for i in range(splitnum):
		# place locks here because we want to make sure that the threads are reading from where they left off when suspended
		readlock.acquire()
		file.seek(pos)
		char = file.read(1)
		readlock.release()

		if char != '\n':
			listlock.acquire()
			lenlist[index] += 1
			listlock.release()
		else: # goes to the next line
			index += 1

		pos += 1

	threadlock.acquire()
	nthread -= 1;
	threadlock.release()

def linelengths(filenm, ntrh):
# returns a Python list, the ith element of which is the number of characters in line i of the file.
	global lenlist, nthread, splitnum, readlock, file, listlock, threadlock

	readlock = thread.allocate_lock()
	listlock = thread.allocate_lock()
	threadlock = thread.allocate_lock()
	nthread = ntrh
	file = open(filenm, 'r')
	lenlist = sum(1 for i in file) * [0]
	nbytes = os.path.getsize(filenm)
	splitnum = nbytes/ntrh
	startpos = 0

	for i in range(ntrh):
		if i != 0:
			startpos += splitnum
		print startpos
		thread.start_new_thread(countchar, (startpos,))

	while nthread > 0: # busy wait
		pass

	return lenlist