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

	def test_setUp(self):
		global nqs
		global maxrat

		hard = open("hard.txt","wr+")
		nqs = random.randint(10,50)
		maxrat = random.randint(5,30)
		num_responses = random.randint(50,200)

		for resp in range(num_responses):
			response = []
			for i in range(nqs):
				response.append(random.randint(1,nqs))

			num_na = random.randint(1,nqs - 1)
			rand_indices = random.sample(range(len(response)),num_na)

			for i in range(num_na):
				if i in rand_indices:
					response[i] = "NA"
			# reponse = response.join(" ")

		print response
		# print rand_indices
		self.assertEqual(True,1)


	# def test_hard_calcfreqs(self):
	# 	global nqs

	# 	test_freqs = calcfreqs("y",3,5)
	# 	correct = {'5,4,5': 3.6666666666666665, '1,4,2': 2, '5,4,1': 1.6666666666666665,\
	# 		'3,3,3': 1.6666666666666665, '5,2,3': 2}
	# 	self.assertEqual(test_freqs,correct)

	# def test_hard_highfreqs_k_two(self):
	# 	global nqs

	# 	freqs = calcfreqs("y",3,5)
	# 	test_kfreqs = highfreqs(freqs,2)
	# 	correct = {'5,4,5': 3.6666666666666665, '1,4,2': 2, '5,2,3': 2}
	# 	self.assertEqual(test_kfreqs,correct)

	# def test_hard_highfreqs_k_neg_one(self):
	# 	global nqs

	# 	freqs = calcfreqs("y",3,5)
	# 	test_kfreqs = highfreqs(freqs,-1)
	# 	correct = {'5,4,1': 1.6666666666666665,'3,3,3': 1.6666666666666665}
	# 	self.assertEqual(test_kfreqs,correct)


if __name__ == '__main__':
    unittest.main()
