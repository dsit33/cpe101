"""
Project 3 - Calcudoku

Name: Derek Sit
Instructor: Mike Ryu
Section: 13
"""
from solverFuncs import *
#import functions from solverFuncs
solution = []
for i in range(5):
	solution.append([0, 0, 0, 0, 0])
print(solution)

#instantiate a list of 5 lists with all zeros
 
#create a while loop that runs until list is full

	#create nested for each loops to iterate through puzzle

		#increment the current value  until check_valid returns true
			#keep track of how many times check_valid is run

		#if it increments through all values and check_valid never returns true, increment the previous square again
			#keep track of how many times it has to return to an earlier square

#print the solution
 	
 	#use for each loop to print each individual value in the list
 	#print the value of checks and backtracks