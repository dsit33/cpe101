def is_lower_101(char):
	"""if char == "a" or char == "b" char == "c" or char == "d" or char == "e" or char == "f" or char == "g" or char == "h" or char == "i" or char == "j" or char == "k" or char == "l" or char == "m" or char == "n" or char == "o" or char == "p" or char == "q" or char == "r" or char == "s" or char == "t" or char == "u" or char == "v" or char == "w" or char == "x" or char == "y" or char == "z":
		return True
	else:
		return False"""

	if ord(char) >= 97 and ord(char) <= 122:
		return True
	else:
		return False

def char_rot_13(char):
	rotation = 0
	if char.isalpha():
		if char.islower():
			if ord(char) + 13 > 122:
				rotation = ord(char) - 13
			else:
				rotation = ord(char) + 13
		if char.isupper():
			if ord(char) + 13 > 90:
				rotation = ord(char) - 13
			else:
				rotation = ord(char) + 13
	else:
		rotation = ord(char)
	return chr(rotation)