"""
Project 4 - Word Search

Name: Derek Sit
Instructor: Mike Ryu
Section: 13
"""
from funcs import *

puzzleStr = input()
words = input().split()
puzzle = []
for i in range(10):
	puzzle.append([None, None, None, None, None, None, None, None, None, None])
for j in range(len(puzzleStr)):
	puzzle[j//10][j%10] = puzzleStr[j]

print("Puzzle:")
for row in puzzle:
	print("")
	for letter in row:
		print(letter, end = "")
print("\n")
for word in words:
	if checkUp(word, puzzle) != -1:
		print(word + ": (UP) row:", checkUp(word,puzzle)[0], "column:", checkUp(word,puzzle)[1])
	if checkDown(word, puzzle) != -1:
		print(word + ": (DOWN) row:", checkDown(word,puzzle)[0], "column:", checkDown(word,puzzle)[1])
	if checkForward(word, puzzle) != -1:
		print(word + ": (FORWARD) row:", checkForward(word,puzzle)[0], "column:", checkForward(word,puzzle)[1])
	if checkBackward(word, puzzle) != -1:
		print(word + ": (BACKWARD) row:", checkBackward(word,puzzle)[0], "column:", checkBackward(word,puzzle)[1])
	if checkDiag(word, puzzle) != -1:
		print(word + ": (DIAGONAL) row:", checkDiag(word,puzzle)[0], "column:", checkDiag(word,puzzle)[1])
	if checkForward(word, puzzle) == -1 and checkBackward(word, puzzle) == -1 and checkUp(word, puzzle) == -1 and checkDown(word, puzzle) == -1 and checkDiag(word, puzzle) == -1:
		print(word + ": word not found")