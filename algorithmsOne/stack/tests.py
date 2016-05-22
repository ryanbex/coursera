import unittest
from stack import Stack

class TestBasicStack(unittest.TestCase):

	def test_pop(self):
		s = BasicStack()
		s.push(5)
		s.push(4)
		self.assertEqual(s.pop(), 4)
		self.assertEqual(s.pop(), 5)
		self.assertRaises(IndexError, s.pop)

	def test_push(self):
		s0 = BasicStack()
		self.assertEqual(s0.push(5), None)
		self.assertEqual(s0.pop(), 5)
		s1 = BasicStack(1)
		s1.push(1)
		self.assertRaises(OverflowError, s1.push, 1)

	def test_empty(self):
		s0 = BasicStack()
		self.assertTrue(s0.empty())
		s0.push(5)
		self.assertFalse(s0.empty())

	def test_peek(self):
		s = BasicStack()
		self.assertRaises(IndexError, s.peek)
		s.push(5)
		self.assertTrue(s.peek(), 5)


if __name__ == '__main__':
    unittest.main()