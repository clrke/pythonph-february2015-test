class squares:
	def __init__(self, n):
		self.i = 0
		self.n = n

	def __iter__(self):
		return self

	def next(self):
		if self.i < self.n:
			i = self.i
			self.i += 1
			return i*i
		else:
			raise StopIteration()

for i in squares(10):
	print i
