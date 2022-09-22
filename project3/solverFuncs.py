"""
Project 3 Calcudoku

Name: Derek Sit
Instructor: Mike Ryu
Section: 13
"""

from math import sqrt

def check_valid(puzzle, cages):
    """
    CONTRACT | check_valid : list list -> bool
    PURPOSE  | take in list puzzle and another list cages in order to call all the other check_valid functions all in one function. return true if all are true  false if any are false
    EXAMPLES | [[1 5 4 2 3] [3 1 2 4 5] [4 2 5 3 1] [5 4 3 1 2] [2 3 1 5 4]] [[5 3 0 5 6] [9 2 1 2] [14 4 3 4 8 9] [9 3 6 11 12] [9 2 10 15] [4 2 13 14] [12 4 16 17 20 21] [7 3 18 22 23] [6 2 19 24]] -> true
             | [[2 4 5 3 1] [3 5 4 2 1] [5 1 3 2 4] [4 5 2 3 4] [1 5 2 4 3]] [[5 3 0 5 6] [9 2 1 2] [14 4 3 4 8 9] [9 3 6 11 12] [9 2 10 15] [4 2 13 14] [12 4 16 17 20 21] [7 3 18 22 23] [6 2 19 24]] -> false
             | [[2 4 3 1 5] [5 1 4 2 3] [3 2 1 5 4] [4 5 2 3 1] [1 3 5 4 2]] [[11 4 0 5 6 10] [11 3 1 2 7] [16 5 3 4 8 9 13] [10 4 11 12 16 17] [7 3 14 19 24] [12 4 15 20 21 22] [7 2 18 23]] -> true
             | [[5 4 3 1 5] [2 3 4 2 3] [1 2 1 5 4] [4 5 2 3 1] [1 3 5 4 2]] [[11 4 0 5 6 10] [11 3 1 2 7] [16 5 3 4 8 9 13] [10 4 11 12 16 17] [7 3 14 19 24] [12 4 15 20 21 22] [7 2 18 23]] -> false
    """
    if check_cages_valid(puzzle, cages) and check_columns_valid(puzzle) and check_rows_valid(puzzle):
        return True
    else:
        return False


def check_cages_valid(puzzle, cages):
    """
    CONTRACT | check_cages_valid : list list -> bool
    PURPOSE  | take in list puzzle and another list cages and iterate through both to make sure the numbers in puzzle add up correctly to the details specified in cages  return true if adds up correctly and all spaces are filled  false if not
    EXAMPLES | [[1 5 4 2 3] [3 1 2 4 5] [4 2 5 3 1] [5 4 3 1 2] [2 3 1 5 4]] [[5 3 0 5 6] [9 2 1 2] [14 4 3 4 8 9] [9 3 6 11 12] [9 2 10 15] [4 2 13 14] [12 4 16 17 20 21] [7 3 18 22 23] [6 2 19 24]] -> true
             | [[1 1 1 1 1] [1 1 1 1 1] [1 1 1 1 1] [1 1 1 1 1] [1 1 1 1 1]] [[5 3 0 5 6] [9 2 1 2] [14 4 3 4 8 9] [9 3 6 11 12] [9 2 10 15] [4 2 13 14] [12 4 16 17 20 21] [7 3 18 22 23] [6 2 19 24]] -> false
             | [[2 4 3 1 5] [5 1 4 2 3] [3 2 1 5 4] [4 5 2 3 1] [1 3 5 4 2]] [[11 4 0 5 6 10] [11 3 1 2 7] [16 5 3 4 8 9 13] [10 4 11 12 16 17] [7 3 14 19 24] [12 4 15 20 21 22] [7 2 18 23]] -> true
             | [[5 4 3 1 5] [2 3 4 2 3] [1 2 1 5 4] [4 5 2 3 1] [1 3 5 4 2]] [[11 4 0 5 6 10] [11 3 1 2 7] [16 5 3 4 8 9 13] [10 4 11 12 16 17] [7 3 14 19 24] [12 4 15 20 21 22] [7 2 18 23]] -> true
    """
    
    for cage in cages:
        #print(cage, puzzle)
        sumCage = 0
        total = 0
        total = int(cage[0])
        numCells = int(cage[1])
        for i in range(2, numCells + 2, 1):
            index = int(cage[i])
            if index < 5:
                if puzzle[0][index] == 0 and sumCage >= total:
                    return False
                sumCage += puzzle[0][index]
            elif index < 10:
                if puzzle[1][index - 5] == 0 and sumCage >= total:
                    return False
                sumCage += puzzle[1][index - 5]
            elif index < 15:
                if puzzle[2][index - 10] == 0 and sumCage >= total:
                    return False
                sumCage += puzzle[2][index - 10]
            elif index < 20:
                if puzzle[3][index - 15] == 0 and sumCage >= total:
                    return False
                sumCage += puzzle[3][index - 15]
            else:
                if puzzle[4][index - 20] == 0 and sumCage >= total:
                    return False
                sumCage += puzzle[4][index - 20]
        if sumCage != total and puzzle[index//5][index%5] != 0:
            return False
    return True

        
    # iterate through 'puzzle' and compare the numbers to 'cages' to check to see if all the numbers in the cages specified by the user add up to the user's guidelines

    # return true if all cells are filled and the number add up correctly  return false if either of those are false


def check_columns_valid(puzzle):
    """
    CONTRACT | check_columns_valid : list -> bool
    PURPOSE  | iterate through the list puzzle in order to see if any numbers in a given column are duplicate  return false if there are  true if not
    EXAMPLES | [[1 2 3 4 5]  [1 2 3 4 5]  [1 2 3 4 5]  [1 2 3 4 5]  [1 2 3 4 5]] -> false
             | [[1 1 1 1 1]  [2 2 2 2 2]  [3 3 3 3 3]  [4 4 4 4 4]  [5 5 5 5 5]] -> true
             | [[2 4 5 3 1]  [3 5 4 1 2]  [5 1 3 2 4]  [4 3 2 5 5]  [1 2 1 4 3]] -> true
             | [[2 4 5 3 1]  [3 5 4 2 1]  [5 1 3 2 4]  [4 5 2 3 4]  [1 5 2 4 3]] -> false
    """
    i = 0
    while i < 5:
        if (puzzle[0][i] == puzzle[1][i] or puzzle[0][i] == puzzle[2][i] or puzzle[0][i] == puzzle[3][i] or puzzle[0][i] == puzzle[4][i]) and puzzle[0][i] != 0:
            return False
        if (puzzle[1][i] == puzzle[2][i] or puzzle[1][i] == puzzle[3][i] or puzzle[1][i] == puzzle[4][i]) and puzzle[1][i] != 0:
            return False
        if (puzzle [2][i] == puzzle[3][i] or puzzle[2][i] == puzzle[4][i]) and puzzle[2][i] != 0:
            return False
        if puzzle[3][i] == puzzle[4][i] and puzzle[3][i] != 0:
            return False
        i += 1
    return True

        

    # pass 'puzzle' through to iterate through the list and check whether the corresponding spot in each list has duplicate numbers

    # return true if all columns have no duplicates  else return false


def check_rows_valid(puzzle):
    """
    CONTRACT | check_rows_valid : list -> bool
    PURPOSE  | iterate through the list puzzle to see if any given row contains duplicate numbers  return false if there are  true if not
    EXAMPLES | [[1 2 3 4 5]  [1 2 3 4 5]  [1 2 3 4 5]  [1 2 3 4 5]  [1 2 3 4 5]] -> true
             | [[1 2 3 4 4]  [1 2 3 4 5]  [1 2 3 4 5]  [1 2 3 4 5]  [1 2 3 4 5]] -> false
             | [[2 4 5 3 1]  [3 5 4 2 1]  [5 1 3 2 4]  [4 5 2 3 1]  [1 5 2 4 3]] -> true
             | [[2 4 5 3 1]  [3 5 4 2 1]  [5 1 3 2 4]  [4 5 2 3 4]  [1 5 2 4 3]] -> false
    """
    for row in puzzle:
        for i in range(5):
            count = i - 1
            while count >= 0:
                if row[i] == row[count] and row[i] != 0:
                    return False
                count -= 1
    return True


    # iterate through 'puzzle' and check if any lists within the list has duplicate numbers

    # return true if no duplicates in a row  else return false


def get_cages():
    """
    CONTRACT | get_cages : none -> list
    PURPOSE  | prompt the user for the number of cages he or she wants  then how he or she wants to design those cages  print the list of cages out
    EXAMPLES | n/a
    """

    numCages = int(input("Number of cages: "))
    user = []
    cages = []
    for i in range(numCages):
        user = input("Cage number {:}: ".format(i)).split()
        cages.append(user)

    return cages




