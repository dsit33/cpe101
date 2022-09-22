"""
Lab 6

Name: Derek Sit
Instructor: Mike Ryu
Section: 13
"""

def sum(nums):
	totalSum = 0
	for num in nums:
		totalSum += num
	return totalSum

def index_of_smallest(nums):
	smallest = 0
	index = 0
	if len(nums) <= 0:
		return -1
	smallest = nums[0]
	for i in range(len(nums)):
		if nums[i] < smallest:
			smallest = nums[i]
			index = i
	return index