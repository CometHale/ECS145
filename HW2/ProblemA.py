def calcfreqs(infile, nqs, maxrat):
	# infile: name of file; each line has the format: '5 4 NA'
	# nqs: # of questions in the survey
	# maxrat: choice of responses 1...maxrat

	freqs = {} # ex. {'5,4,5': 3} where '5,4,5' is the type of pattern 
	try:
		file = open(infile, 'r')
	except:
		raise Exception("Error: " + infile + " does not exist")
	allLines = file.readlines() #get rid of newlines

	# going through each entry
	for x in allLines:
		# currently, line = '5 4 NA\n'
		line = x.split("\n") #get rid of new line first -> line = ['5 4 NA']
		line = "".join(line)
		line = line.split() # join new line and split again, line = ['5', '4', 'NA']
		freq = 0

		# check if inputs are part of the choice of responses and if there are enough inputs
		for i in line:
			if i != "NA" and not i.isdigit():
				raise Exception("Error: Input incorrect")
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
			if entrylist == line:
				freq += 1
				continue
			for l, e in zip(line, entrylist):
				if l == e and "NA" in entrylist: # only do partial matching with nonintact patterns
					match += 1
				elif l != e and "NA" != e: 
					match = 0 #reset
					break #only match if all patterns match IN ORDER [1, 4, 2] is NOT 1/3 of [3, 4, NA]

			if match >= 1:
				freq += float(match)/nqs

		line = ','.join(line)	
		freqs[line] = freq
					
	return freqs

def highfreqs(freqs, k):

	if k == 0:
		raise Exception("Value of k cannot be 0.")

	kfreqs = {}
	kvals = sorted(list(set(freqs.values()))) #kvals is the list of k highest or lowest vals in freqs
	# set() eliminates any duplicate values

	if k > 0: # k > 0: return the k most frequent patterns
		kvals = kvals[len(kvals) - k: len(kvals)]
	else: # k < 0 : return the k least frequent patterns
		kvals = kvals[0:(-k)]
	
	for key in freqs:
		if freqs[key] in kvals:
			kfreqs[key] = freqs[key]
		else: continue


	return kfreqs
