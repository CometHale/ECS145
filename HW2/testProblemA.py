from ProblemA import *
import unittest
import random


class TestEasyFile(unittest.TestCase):

	def test_calcfreqs(self):
		test_freqs = calcfreqs("test.txt",3,6)
		correct = {'2,3,6': 1, '2,6,3': 1, '1,6,1': 1, '5,4,1': 2.333333333333333}

		self.assertEqual(test_freqs,correct)

	def test_highfreqs_k_one(self):
		freqs = calcfreqs("test.txt",3,6)
		test_kfreqs = highfreqs(freqs,1)
		correct = {'5,4,1': 2.333333333333333}
		self.assertEqual(test_kfreqs,correct)

	def test_highfreqs_k_two(self):
		freqs = calcfreqs("test.txt",3,6)
		test_kfreqs = highfreqs(freqs,2)
		correct = {'2,3,6': 1, '2,6,3': 1, '1,6,1': 1, '5,4,1': 2.333333333333333}
		self.assertEqual(test_kfreqs,correct)

class TestMildFile(unittest.TestCase):

	def test_mild_calcfreqs(self):
		test_freqs = calcfreqs("y",3,5)
		correct = {'5,4,5': 3.6666666666666665, '1,4,2': 2, '5,4,1': 1.6666666666666665,\
			'3,3,3': 1.6666666666666665, '5,2,3': 2}
		self.assertEqual(test_freqs,correct)

	def test_mild_highfreqs_k_two(self):
		freqs = calcfreqs("y",3,5)
		test_kfreqs = highfreqs(freqs,2)
		correct = {'5,4,5': 3.6666666666666665, '1,4,2': 2, '5,2,3': 2}
		self.assertEqual(test_kfreqs,correct)

	def test_mild_highfreqs_k_neg_one(self):
		freqs = calcfreqs("y",3,5)
		test_kfreqs = highfreqs(freqs,-1)
		correct = {'5,4,1': 1.6666666666666665,'3,3,3': 1.6666666666666665}
		self.assertEqual(test_kfreqs,correct)


class TestHardFile(unittest.TestCase):

	def setUp(self):
		global nqs
		global maxrat
		global non_na_resps
		global na_resps
		global all_resps

		# self.maxDiff = None # Use this to show full error read out

		hard = open("hard.txt","w+")
		nqs = random.randint(10,50)
		maxrat = random.randint(5,30)
		num_responses = random.randint(50,200)
		non_na_resps = []
		na_resps = []
		all_resps = []

		count = nqs / random.randint(1,10)
		for resp in range(num_responses):
			response = []
			for i in range(nqs):
				response.append(random.randint(1,maxrat))


			if count > 10:
				num_na = random.randint(0,nqs - 1)
				rand_indices = random.sample(range(len(response)),num_na)

				for i in range(num_na):
					if i in rand_indices:
						response[i] = "NA"
				response = ' '.join(str(num) for num in response)
				na_resps.append(response)
			else:
				response = ' '.join(str(num) for num in response)
				non_na_resps.append(response)

			count -= random.randint(1,3)
			all_resps.append(response)
			hard.write(response + "\n")

		hard.close()


	def test_hard_calcfreqs(self):
		global nqs
		global maxrat
		global non_na_resps
		global na_resps
		self.setUp()

		correct = {}
		
		for resp in non_na_resps:
			match = 0
			freq = 0
			tmp = resp.replace(" ",",")
			if resp not in correct:
				freq = 1
			else:
				freq += 1

			for na_resp in na_resps:
				for na,non_na in zip(na_resp,resp):
					if na == non_na:
						match += 1
					elif na != non_na and na != "NA":
						match = 0

				freq += float(match)/nqs
			correct[tmp] = freq

		test_freqs = calcfreqs("hard.txt",nqs,maxrat)
		self.assertEqual(test_freqs,correct)

	def test_hard_highfreqs_k_two(self):
		global nqs
		global maxrat
		global non_na_resps
		global na_resps
		global all_resps
		self.setUp()

		correct = {}
		freqs = calcfreqs("hard.txt",nqs,maxrat)
		kvals = sorted(list(set(freqs.values())))
		kvals = kvals[len(kvals) - 2:len(kvals)]

		for key in freqs:
			if freqs[key] in kvals:
				correct[key] = freqs[key]


		test_kfreqs = highfreqs(freqs,2)
		self.assertEqual(test_kfreqs,correct)

	def test_hard_highfreqs_k_neg_five(self):
		global maxrat
		global non_na_resps
		global na_resps
		global all_resps
		self.setUp()

		correct = {}
		freqs = calcfreqs("hard.txt",nqs,maxrat)
		kvals = sorted(list(set(freqs.values())))
		kvals = kvals[0:5]

		for key in freqs:
			if freqs[key] in kvals:
				correct[key] = freqs[key]


		test_kfreqs = highfreqs(freqs,-5)
		self.assertEqual(test_kfreqs,correct)




if __name__ == '__main__':
    unittest.main()
