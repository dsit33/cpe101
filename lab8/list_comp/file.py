file = open("in.txt")

for i, line in enumerate(file):
	charAmount = 0
	for char in line:
		charAmount += 1
	print("Line", i, "("+charAmount, "chars):", line)