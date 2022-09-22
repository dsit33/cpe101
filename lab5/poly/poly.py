"""
Lab 5

Name: Derek Sit
Instructor: Mike Ryu
Section: 13
"""

def poly_add2(func1, func2):
	newFunc = [ ]
	newFunc.append(func1[0] + func2[0])
	newFunc.append(func1[1] + func2[1])
	newFunc.append(func1[2] + func2[2])
	return newFunc
def poly_mult2(func1, func2):
	newFunc = [ ]
	newFunc.append(func1[0] * func2[0])
	newFunc.append(func1[1] * func2[0] + func1[0] * func2[1])
	newFunc.append(func1[2] * func2[0] + func1[1] * func2[1] + func1[0] * func2[2])
	newFunc.append(func1[2] * func2[1] + func1[1] * func2[2])
	newFunc.append(func1[2] * func2[2])
	return newFunc