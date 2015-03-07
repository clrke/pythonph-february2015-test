def squares(n):
	for i in range(n):
		yield i*i

for i in squares(10):
	print(i)
