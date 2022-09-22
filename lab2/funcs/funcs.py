import math
"""
CONTRACT | f : float -> float
--------:|:--------------------------------------------------------------------
PURPOSE  | take input x and return the outcome when plugged into the equation
EFFECTS  | none/none
EXAMPLES | 1.0 -> 9.0
         | 2.0 -> 32.0
         | 3.0 -> 69.0
"""
# first-outline
def f(x):
	return 7 * x**2 + 2*x

"""
CONTRACT | g : float float -> float
--------:|:--------------------------------------------------------------------
PURPOSE  | take inputs x and y and return a result
EFFECTS  | none/none
EXAMPLES | 1.0 2.0 -> 1.6666666
		 | 1.0 3.0 -> 3.3333333
"""
# first-outline
def g(x, y):
	return (x**2 + y**2) / (3*x)

"""
CONTRACT | hypotenuse : float float -> float
--------:|:--------------------------------------------------------------------
PURPOSE  | calculate the length of a hypotenuse given two sides of a right triangle
EFFECTS  | none/none
EXAMPLES | 3 4 -> 5
		 | 5 12 -> 13
		 | 8 15 -> 17
"""
# first-outline
def hypotenuse(x, y):
	return math.sqrt(x**2 + y**2)

"""
CONTRACT | is_positive : float -> boolean
--------:|:--------------------------------------------------------------------
PURPOSE  | determine whether the input is positive
EFFECTS  | none/none
EXAMPLES | 1 -> true
         | 2 -> true
         | -1 -> false
"""
# first-outline
def is_positive(x):
	return x >= 0