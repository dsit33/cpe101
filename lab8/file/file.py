file = open("in.txt")

for i, line in enumerate(file):
	charAmount = 0
	for char in line:
		if char != "\n":
			charAmount += 1
	print("Line", i, "({}".format(charAmount), "chars):", line, end = "")

file.close()