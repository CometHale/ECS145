from ProblemA import *
import unittest



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

# class TestHardFile(unittest.TestCase):

if __name__ == '__main__':
    unittest.main()
