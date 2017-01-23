class File:
	"""
		File class: class 
	"""
	def __init__(self,name,size, mode,filetype):
		self.name = name
		self.size = size
		self.length = 0
		self.position = 0
		self.mode = mode
		self.type = filetype # make directory class or something