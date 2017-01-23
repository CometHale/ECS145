from file_class import File
import pickle

class FileSystem:

	def __init__(self):

		self.fsname = ""
		self.flist = []

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

	def init(self,fsname):
		storage_file = fsname

		command = raw_input("\n>>")

		if command == "yep":
			print "awesome"

		return 0

