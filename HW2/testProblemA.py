from ProblemA import *
import unittest



class TestEasyFile(unittest.TestCase):


	def test_calcfreqs(self):
		test_freqs = calcfreqs("test.txt",3,6)
		correct = {'2,3,6': 1, '2,6,3': 1, '1,6,1': 1, '5,4,1': 2.333333333333333}

		self.assertEqual(test_freqs,correct)

	def test_kfreqs_k_one(self):
		freqs = calcfreqs("test.txt",3,6)
		test_kfreqs = highfreqs(freqs,1)
		correct = {'5,4,1': 2.333333333333333}
		self.assertEqual(test_kfreqs,correct)

	def test_kfreqs_k_two(self):
		freqs = calcfreqs("test.txt",3,6)
		test_kfreqs = highfreqs(freqs,2)
		correct = {'2,3,6': 1, '2,6,3': 1, '1,6,1': 1, '5,4,1': 2.333333333333333}
		self.assertEqual(test_kfreqs,correct)

# class TestMildFile(unittest.TestCase):

# class TestHardFile(unittest.TestCase):

if __name__ == '__main__':
    unittest.main()
