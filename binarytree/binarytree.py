# What we need for a binary tree
# a tree object
# a node object
# an arc object
# enforce only two children
# 	  left has to be less than
# 	  right has to be greater than


class Tree(object):

	def __init__(self):
		self.root = None
		self.size = 0
		self.nodes = []
		self.arcs = []

	def length(self):
		return self.size

	def __len__(self):
		return self.size

	def __iter__(self):
		return self.root.__iter__()

	def _gt(value0, value1):
		return value0 > value1

	def _lt(value0, value1):
		return value0 < value1


		

class Node(object):

	def __init__(self, value):
		self._value = value
		self._parent = None
		self._children = {}
		self._level = 1
		
	def child(self, name):
		return self.children[name]

	@increase_lvl
	def addchild(self, name, child)
		return self.children.add({name:child})

	def increase_lvl(self):
		self.level += 1

	@property
	def children(self):
		return self._children
	


@testw
def test():
	return 1

def testw(input):
	return 1+input

print(test())

