"""
Project 3 - Calcudoku Solver

Name: Derek Sit
Instructor: Mike Ryu
Section: 13
"""

"""
CONTRACT | check_valid : list list -> bool
--------:|:--------------------------------------------------------------------
PURPOSE  | take in list `puzzle` and another list `cages` in order to call all the other check_valid functions all in one function. return true if all are true  false if any are false
EFFECTS  | none/none
EXAMPLES | [[1 5 4 2 3] [3 1 2 4 5] [4 2 5 3 1] [5 4 3 1 2] [2 3 1 5 4]] [[5 3 0 5 6] [9 2 1 2] [14 4 3 4 8 9] [9 3 6 11 12] [9 2 10 15] [4 2 13 14] [12 4 16 17 20 21] [7 3 18 22 23] [6 2 19 24]] -> true
         | [[2 4 5 3 1] [3 5 4 2 1] [5 1 3 2 4] [4 5 2 3 4] [1 5 2 4 3]] [[5 3 0 5 6] [9 2 1 2] [14 4 3 4 8 9] [9 3 6 11 12] [9 2 10 15] [4 2 13 14] [12 4 16 17 20 21] [7 3 18 22 23] [6 2 19 24]] -> false
         | [[2 4 3 1 5] [5 1 4 2 3] [3 2 1 5 4] [4 5 2 3 1] [1 3 5 4 2]] [[10 4 0 5 6 10] [11 3 1 2 7] [16 5 3 4 8 9 13] [10 4 11 12 16 17] [7 3 14 19 24] [12 4 15 20 21 22] [7 2 18 23]] -> true
         | [[5 4 3 1 5] [2 3 4 2 3] [1 2 1 5 4] [4 5 2 3 1] [1 3 5 4 2]] [[10 4 0 5 6 10] [11 3 1 2 7] [16 5 3 4 8 9 13] [10 4 11 12 16 17] [7 3 14 19 24] [12 4 15 20 21 22] [7 2 18 23]] -> false

"""
# call all other check valid functions  passing through 'puzzle' and 'cages'
# if all are true return true else return false

"""
CONTRACT | check_cages_valid : list list -> bool
--------:|:--------------------------------------------------------------------
PURPOSE  | take in list `puzzle` and another list `cages` and iterate through both to make sure the numbers in puzzle add up correctly to the details specified in cages  return true if adds up correctly and all spaces are filled  false if not
EFFECTS  | none/none
EXAMPLES | [[1 5 4 2 3] [3 1 2 4 5] [4 2 5 3 1] [5 4 3 1 2] [2 3 1 5 4]] [[5 3 0 5 6] [9 2 1 2] [14 4 3 4 8 9] [9 3 6 11 12] [9 2 10 15] [4 2 13 14] [12 4 16 17 20 21] [7 3 18 22 23] [6 2 19 24]] -> true
         | [[1 1 1 1 1] [1 1 1 1 1] [1 1 1 1 1] [1 1 1 1 1] [1 1 1 1 1]] [[5 3 0 5 6] [9 2 1 2] [14 4 3 4 8 9] [9 3 6 11 12] [9 2 10 15] [4 2 13 14] [12 4 16 17 20 21] [7 3 18 22 23] [6 2 19 24]] -> false
         | [[2 4 3 1 5] [5 1 4 2 3] [3 2 1 5 4] [4 5 2 3 1] [1 3 5 4 2]] [[10 4 0 5 6 10] [11 3 1 2 7] [16 5 3 4 8 9 13] [10 4 11 12 16 17] [7 3 14 19 24] [12 4 15 20 21 22] [7 2 18 23]] -> true
         | [[5 4 3 1 5] [2 3 4 2 3] [1 2 1 5 4] [4 5 2 3 1] [1 3 5 4 2]] [[10 4 0 5 6 10] [11 3 1 2 7] [16 5 3 4 8 9 13] [10 4 11 12 16 17] [7 3 14 19 24] [12 4 15 20 21 22] [7 2 18 23]] -> true

"""
# iterate through 'puzzle' and compare the numbers to 'cages' to check to see if all the numbers in the cages specified by the user add up to the user's guidelines
# return true if all cells are filled and the number add up correctly  return false if either of those are false

"""
CONTRACT | check_columns_valid : list -> bool
--------:|:--------------------------------------------------------------------
PURPOSE  | iterate through the list `puzzle` in order to see if any numbers in a given column are duplicate  return false if there are  true if not
EFFECTS  | none/none
EXAMPLES | [[1 2 3 4 5]  [1 2 3 4 5]  [1 2 3 4 5]  [1 2 3 4 5]  [1 2 3 4 5]] -> false
         | [[1 1 1 1 1]  [2 2 2 2 2]  [3 3 3 3 3]  [4 4 4 4 4]  [5 5 5 5 5]] -> true
         | [[2 4 5 3 1]  [3 5 4 1 2]  [5 1 3 2 4]  [4 3 2 5 5]  [1 2 1 4 3]] -> true
         | [[2 4 5 3 1]  [3 5 4 2 1]  [5 1 3 2 4]  [4 5 2 3 4]  [1 5 2 4 3]] -> false

"""
# pass 'puzzle' through to iterate through the list and check whether the corresponding spot in each list has duplicate numbers
# return true if all columns have no duplicates  else return false

"""
CONTRACT | check_rows_valid : list -> bool
--------:|:--------------------------------------------------------------------
PURPOSE  | iterate through the list `puzzle` to see if any given row contains duplicate numbers  return false if there are  true if not
EFFECTS  | none/none
EXAMPLES | [[1 2 3 4 5]  [1 2 3 4 5]  [1 2 3 4 5]  [1 2 3 4 5]  [1 2 3 4 5]] -> true
         | [[1 2 3 4 4]  [1 2 3 4 5]  [1 2 3 4 5]  [1 2 3 4 5]  [1 2 3 4 5]] -> false
         | [[2 4 5 3 1]  [3 5 4 2 1]  [5 1 3 2 4]  [4 5 2 3 1]  [1 5 2 4 3]] -> true
         | [[2 4 5 3 1]  [3 5 4 2 1]  [5 1 3 2 4]  [4 5 2 3 4]  [1 5 2 4 3]] -> false

"""
# iterate through 'puzzle' and check if any lists within the list has duplicate numbers
# return true if no duplicates in a row  else return false



"""
CONTRACT | get_cages : none -> none
--------:|:--------------------------------------------------------------------
PURPOSE  | prompt the user for the number of cages he or she wants  then how he or she wants to design those cages  print the list of cages out
EFFECTS  | int list/list
EXAMPLES | n/a

"""
# prompt user for amount of cages they want
# prompt user for cage specifications for as many cages as they just input




