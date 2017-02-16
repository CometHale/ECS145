import thread 
import os

def countchar(pos):
# updates lenlist, do not count EOL as part of line length
	global lenlist, nthread, readlock, file

	for i in range(splitnum):
		# place locks here because we want to make sure that the threads are reading from where they left off when suspended
		readlock.acquire()
		file.seek(pos)
		char = file.read(1)
		readlock.release()

		pos += 1


	nthread -= 1;

def linelengths(filenm, ntrh):
# returns a Python list, the ith element of which is the number of characters in line i of the file.
	global lenlist, nthread, splitnum, readlock, file

	readlock = thread.allocate_lock()
	nthread = ntrh
	lenlist = []
	file = open(filenm, 'r')
	nbytes = os.path.getsize(filenm)
	splitnum = nbytes/ntrh
	startpos = 0

	for i in range(ntrh):
		if i != 0:
			startpos += splitnum
		thread.start_new_thread(countchar, (startpos))

	while nthread > 0: # busy wait
		pass

	return lenlist