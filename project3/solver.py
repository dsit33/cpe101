"""
Project 3 - Calcudoku

Name: Derek Sit
Instructor: Mike Ryu
Section: 13
"""
from solverFuncs import *

index = 0
row = 0
col = 0
backtracks = 0
checks = 0
cages = get_cages()
solution = []
for x in range(5):
	solution.append([0, 0, 0, 0, 0])
while index >= 0 and index < 25:
	row = index // 5
	#print("row ", row)
	col = index % 5
	#print("col ", col)
	solution[row][col] += 1
	if check_valid(solution, cages):
		index += 1
		checks += 1
	else:
		while solution[row][col] == 5:
			solution[row][col] = 0
			index -= 1
			backtracks += 1
			row = index//5
			col = index%5
		checks += 1

	"""if solution[row][col] == 0 or check_valid(solution, cages) == False and solution[row][col] < 5:
		solution[row][col] += 1
		print("value at ",index, ": ", solution[row][col])
		checks += 1
	elif check_valid(solution, cages) == True:
		print("next square")
		checks += 1
		index += 1
	if solution[row][col] == 5:
		if check_valid(solution, cages) == False:
			checks += 1
			print("backtrack")
			solution[row][col] = 0
			index -= 1
			backtracks += 1
			bt = True"""
print("")
print("---Solution---")
for row in solution:
	print("")
	for num in row:
		print(num, end = " ")
print("\n")
print("checks:", checks, "backtracks:", backtracks)