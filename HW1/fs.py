from file_class import File
import pickle
import os


def bytes_remaining():
	pass

def create(): # Angie
	pass

def open(): # Angie
	pass

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

def write(): # Sally 
	pass

def readlines(): # Sally
	pass

def delfile(): #Haley
	pass

def deldir(): # Haley
	pass

def mkdir():
	pass

def isdir():
	pass

def listdir():
	pass

# def suspend(): 
# 	pass

# def resume():
# 	pass

def chdir():# Haley 
	pass


def init(fsname):

	global system
	global system_name
	global system_size
	global system_bytes_left
	global file_list
	global fat

	system_name = fsname
	system = open(fsname,'w')
	system_size = os.path.getsize(fsname)
	file_list = []
	fat = [ -1 for i in range(system_size)]
	system_bytes_left = system_size

	
	return 0

