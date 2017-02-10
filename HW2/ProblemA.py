def calcfreqs(infile, nqs, maxrat):
	# infile: name of file; each line has the format: '5 4 NA'
	# nqs: # of questions in the survey
	# maxrat: choice of responses 1...maxrat

	freqs = {} # ex. {'5,4,5': 3} where '5,4,5' is the type of pattern 
	try:
		file = open(infile, 'r')
	except:
		raise Exception("Error: " + infile + " does not exist")
	allLines = file.readlines()

	# going through each entry
	for x in allLines:
		# currently, line = '5 4 NA'
		line = x.split() # line = ['5', '4', 'NA']
		freq = 0

		# check if inputs are part of the choice of responses and if there are enough inputs
		for i in line:
			if i != "NA" and (eval(i) not in range(maxrat+1)[1:]) or len(line) != nqs:
				raise Exception("Error: Input incorrect")

		# Don't count patterns with 'NA' and encountered patterns
		if "NA" in line or x in freqs.keys():
			continue
		else:
			freqs[','.join(line)] = 0

		# compare current line with each entry in file
		for entry in allLines:
			match = 0
			entrylist = entry.split() # entrylist = ['4', '3', '1']
			if entry == x:
				freq += 1
				continue
			for l, e in zip(line, entrylist):
				if l == e:
					match += 1

			if match > 1:
				freq += float(match)/nqs

		line = ','.join(line)	
		freqs[line] = freq
					
	return freqs

def highfreqs(freqs, k):
	pass