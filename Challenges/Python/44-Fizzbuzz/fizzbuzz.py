for x in range(1, 101):
	s = ''
	if not x%15:
		s = 'Fizz Buzz'
	elif not x%3:
		s = 'Fizz'
	elif not x%5:
		s = 'Buzz'
	else:
		s = str(x)
	print(s)