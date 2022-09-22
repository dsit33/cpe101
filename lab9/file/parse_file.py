import sys

ints = 0
floats = 0
other = 0
total = 0
sumFlag = False
afterFile = False

if len(sys.argv) == 3:
	if sys.argv[len(sys.argv)-1] != '-s':
		if sys.argv[len(sys.argv)-2] == '-s':
			sumFlag= True
		else:
			print("Usage: [-s] file_name")
			exit()
	elif sys.argv[len(sys.argv)-2] != '-s':
		if sys.argv[len(sys.argv)-1] == '-s':
			afterFile = True
			sumFlag = True
		else:
			print("Usage: [-s] file_name")
			exit()
	

try:
	if afterFile:
		file = open(sys.argv[len(sys.argv)-2])
	else:
		file = open(sys.argv[len(sys.argv)-1])
except:
	if afterFile:
		print("Unable to open {}".format(sys.argv[len(sys.argv)-2]))
	else:
		print("Unable to open {}".format(sys.argv[len(sys.argv)-1]))
	exit()

for line in file:
	j = 0
	strings = line.split()
	while j < len(strings):
		if strings[j].isdigit():
			ints += 1
			if sumFlag == True:
				total += int(strings[j])
		elif strings[j].find(".") != -1 and strings[j].replace(".","",1).isdigit():
			floats += 1
			if sumFlag == True:
				total += float(strings[j])
		elif strings[j][0] == "-" and strings[j][1:].replace(".","",1).isdigit():
			floats += 1
			if sumFlag == True:
				total += float(strings[j])
		else:
			other += 1
		j += 1

print("Ints:", ints)
print("Floats:", floats)
print("Other:", other)
if sumFlag == True:
	print("Sum:", total)
