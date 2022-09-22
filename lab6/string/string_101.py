def str_rot_13(string):
	new = []
	for char in string:
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
		new.append(chr(rotation))
	return "".join(new)

def str_translate_101(string, char1, char2):
	new = [char2 if ord(char) == ord(char1) else char for char in string]
	return "".join(new)
