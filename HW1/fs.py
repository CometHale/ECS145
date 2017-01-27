from file_class import File
import pickle
import os


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

# def suspend(): 
# 	pass

# def resume():
# 	pass

def chdir():# Haley 
	pass

def init(fsname):

	global system
	global system_name = fsname
	global system_size = os.path.getsize(fsname)
	global file_list = []
	global fat = [ -1 for i in range(system_size)]

	system = open(fsname,'w')





	
	return 0

