"""
Lab 5

Name: Derek Sit
Instructor: Mike Ryu
Section: 13
"""

def square_all(func):
	new = [n**2 for n in func]
	return new

def add_n_all(func, n):
	new = []
	for i in range(len(func)):
		new.append(func[i] + n)
	return new

def even_or_odd_all(func):
	new = []
	i = 0
	while i < len(func):
		if func[i] % 2 == 0:
			new.append(True)
		else:
			new.append(False)
		i += 1
	return new

	