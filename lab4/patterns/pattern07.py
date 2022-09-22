import driver

def letter(row, col):
	if row >= 4 and row <= 5 and col >= 7 and col <= 9:
		return "X"
	elif row >= 2 and row <=5 and col >= 4 and col <= 9:
		return "Z"
	elif row >= 4 and row <= 6 and col >= 7 and col <= 12:
		return "B"
	else:
		return "T"

if __name__ == '__main__':
   driver.comparePatterns(letter)