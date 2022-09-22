def groups_of_3(vals):
	final = []
	temp = []
	count = 0
	i = 0
	for val in vals:
		temp.append(val)
		count += 1
		i += 1
		if count == 3:
			count = 0
			final.append(temp)
			temp = []
		if len(vals) % 3 != 0 and i == len(vals) - 1:
			final.append(temp)
	return final