def calcfreqs(infile, nqs, maxrat):
	# infile: name of file; each line has the format: '5 4 NA'
	# nqs: # of questions in the survey
	# maxrat: choice of responses 1...maxrat

	freqs = {} # ex. {'5,4,5': 3} where '5,4,5' is the type of pattern
	file = open(infile, 'r')
	allLines = file.readlines()

	# going through each entry
	for line in allLines:
		# currently, line = '5 4 NA'
		line = line.split() # line = ['5', '4', 'NA']
		freq = 1

		for key in freqs.keys():
			keyanswers = key.split(',') # keyanswers = ['4', '3', '1']
			print keyanswers
			print line
			for l, k in zip(line, keyanswers):
				if l == k:
					freq += float(1)/nqs
					freqs[key] += float(1)/nqs
		line = ','.join(line)
		freqs[line] = freq
					
	return freqs

def highfreqs(freqs, k):
	pass