

class BasicStack(object):

	def __init__(self, N=10):
		"""Stack is a list of items that follow 
		the last in first out model.
		Args:
			:N [int]: the max number of elements.
				Default: 10
		"""
		self._limit = N
		self._stack = []
		self._top = -1

	def empty(self):
		return self._top == -1

	def pop(self):
		self._err_ifempty()
		value = self._stack[self._top]
		self._stack[self._top] = None
		self._top -= 1
		return value

	def push(self, value):
		if (self._top + 1) < self._limit:
			self._stack += [value]
			self._top += 1
			return
		raise OverflowError('Stack is full')

	def peek(self):
		self._err_ifempty()
		return self._stack[self._top]

	def _err_ifempty(self):
		if self.empty():
			raise IndexError('Stack is Empty')
		return

	@property
	def stack(self):
	    return self._stack
	
	@property
	def limit(self):
	    return self._limit
	
	@property
	def top(self):
	    return self._top
	
