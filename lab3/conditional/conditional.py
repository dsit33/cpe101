"""
Name: Derek Sit
Instructor: Mike Ryu
Section: 13

"""

def max_101(num, num2):
	if num >= num2:
		return num
	else:
		return num2

def max_of_three(num, num2, num3):
	if num >= num2 and num >= num3:
		return num
	elif num2 >= num and num2 >= num3:
		return num2
	else:
		return num3

def rental_late_fee(daysLate):
	if daysLate <= 0:
		return 0
	elif daysLate <= 9:
		return 5
	elif daysLate <= 15:
		return 7
	elif daysLate <= 24:
		return 19
	else:
		return 100
