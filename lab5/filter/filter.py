"""
Lab 5

Name: Derek Sit
Instructor: Mike Ryu
Section: 13
"""

def are_positive(nums):
	new = [n for n in nums if n > 0]
	return new

def are_greater_than_n(nums, n):
	new = []
	for i in range(len(nums)):
		if nums[i] > n:
			new.append(nums[i])
	return new

def are_divisible_by_n(nums, n):
	new = []
	i = 0
	while i < len(nums):
		if nums[i] % n == 0:
			new.append(nums[i])
		i += 1
	return new
