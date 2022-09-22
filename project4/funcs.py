"""
Project 4 - Word Search

Name: Derek Sit
Instructor: Mike Ryu
Section: 13
"""

from math import sqrt

def checkForward(word, puzzle):
    """
    CONTRACT | checkForward : str list -> tuple
    PURPOSE  | takes in a word in the puzzle and if the word is found while iterating to the right it will where the start of the string is
    EXAMPLES | UNIX [["W" "A" "Q" "H" "G" "T" "T" "W" "E" "E"] ["C" "B" "M" "I" "V" "Q" "Q" "E" "L" "S"] ["A" "P" "X" "W" "K" "W" "I" "I" "I" "L"] ["L" "D" "E" "L" "F" "X" "P" "I" "P" "V"] ["P" "O" "N" "D" "T" "M" "V" "A" "M" "N"] ["O" "E" "D" "S" "O" "Y" "Q" "G" "O" "B"] ["L" "G" "Q" "C" "K" "G" "M" "M" "C" "T"] ["Y" "C" "S" "L" "O" "A" "C" "U" "Z" "M"] ["X" "V" "D" "M" "G" "S" "X" "C" "Y" "Z"] ["U" "U" "I" "U" "N" "I" "X" "F" "N" "U"]] -> (9, 3)
             | CODE [["W" "A" "Q" "H" "G" "T" "T" "W" "E" "E"] ["C" "B" "M" "I" "V" "Q" "Q" "E" "L" "S"] ["A" "P" "X" "W" "K" "W" "I" "I" "I" "L"] ["L" "D" "E" "L" "F" "X" "P" "I" "P" "V"] ["P" "O" "N" "D" "T" "M" "V" "A" "M" "N"] ["O" "E" "D" "S" "O" "Y" "Q" "G" "O" "B"] ["L" "G" "Q" "C" "K" "G" "M" "M" "C" "T"] ["Y" "C" "S" "L" "O" "A" "C" "U" "Z" "M"] ["X" "V" "D" "M" "G" "S" "X" "C" "Y" "Z"] ["U" "U" "I" "U" "N" "I" "X" "F" "N" "U"]] -> -1
             | ZEBRA [["E" "O" "A" "R" "B" "R" "N" "I" "A" "B"] ["Z" "E" "B" "R" "A" "E" "B" "R" "B" "H"] ["A" "R" "R" "A" "C" "C" "O" "O" "N" "R"] ["A" "A" "C" "B" "R" "R" "C" "H" "E" "C"] ["C" "N" "A" "B" "O" "Z" "O" "B" "K" "A"] ["B" "O" "N" "I" "R" "B" "B" "N" "C" "A"] ["E" "E" "R" "T" "C" "B" "R" "A" "I" "A"] ["A" "B" "C" "E" "R" "I" "C" "R" "H" "R"] ["B" "O" "I" "O" "R" "O" "R" "C" "C" "O"] ["B" "O" "A" "A" "K" "R" "K" "E" "A" "R"]] -> (1, 0)
             | RACCOON [["E" "O" "A" "R" "B" "R" "N" "I" "A" "B"] ["Z" "E" "B" "R" "A" "E" "B" "R" "B" "H"] ["A" "R" "R" "A" "C" "C" "O" "N" "N" "R"] ["A" "A" "C" "B" "R" "R" "C" "H" "E" "C"] ["C" "N" "A" "B" "O" "Z" "O" "B" "K" "A"] ["B" "O" "N" "I" "R" "B" "B" "N" "C" "A"] ["E" "E" "R" "T" "C" "B" "R" "A" "I" "A"] ["A" "B" "C" "E" "R" "I" "C" "R" "H" "R"] ["B" "O" "I" "O" "R" "O" "R" "C" "C" "O"] ["B" "O" "A" "A" "K" "R" "K" "E" "A" "R"]] -> -1
             | LLAR [["L" "L" "A" "R" "S" "H" "A" "H" "L" "C"] ["A" "O" "O" "L" "L" "A" "M" "I" "L" "L"] ["O" "I" "D" "N" "A" "L" "H" "G" "I" "H"] ["R" "B" "A" "M" "C" "E" "T" "U" "H" "S"] ["S" "M" "O" "S" "K" "A" "G" "E" "T" "R"] ["C" "O" "R" "C" "H" "O" "R" "R" "O" "A"] ["I" "D" "B" "S" "L" "S" "A" "A" "O" "M"] ["I" "G" "O" "S" "M" "O" "N" "D" "F" "L"] ["H" "H" "N" "G" "M" "S" "D" "C" "M" "A"] ["C" "M" "I" "R" "R" "S" "M" "L" "H" "P"]] -> (0, 0)
    """
    
    for i, row in enumerate(puzzle):
        rowStr = "".join(row)
        if rowStr.find(word) != -1:
            return (i, rowStr.find(word))
    return -1



    # use a for each loop to iterate through a single list at a time

        # use another for each to iterate through each letter of the puzzle at a time

            # if the current letter we are looking at is the same as the first letter of the string passed through then execute the following

                # while loop that runs until a counter variable reaches the length of the string passed through and while the value subscripted in the puzzle doesn't exceed 9

                    # increment the index of the beginning spot by one and join that character to a string

                # if the outcome of the while loop is equivalent to the string passed through then return (row, col)

    # if the whole loop finishes and never finds a match for the word then return -1


def checkBackward(word, puzzle):
    """
    CONTRACT | checkBackward : str list -> tuple
    PURPOSE  | takes in a word and checks to see if it exists in the puzzle backwards returns where the start of the string is if match is found
    EXAMPLES | HIGHLAND [["L" "L" "A" "R" "S" "H" "A" "H" "L" "C"] ["A" "O" "O" "L" "L" "A" "M" "I" "L" "L"] ["O" "I" "D" "N" "A" "L" "H" "G" "I" "H"] ["R" "B" "A" "M" "C" "E" "T" "U" "H" "S"] ["S" "M" "O" "S" "K" "A" "G" "E" "T" "R"] ["C" "O" "R" "C" "H" "O" "R" "R" "O" "A"] ["I" "D" "B" "S" "L" "S" "A" "A" "O" "M"] ["I" "G" "O" "S" "M" "O" "N" "D" "F" "L"] ["H" "H" "N" "G" "M" "S" "D" "C" "M" "A"] ["C" "M" "I" "R" "R" "S" "M" "L" "H" "P"]] -> (2, 9)
             | CHORRO [["L" "L" "A" "R" "S" "H" "A" "H" "L" "C"] ["A" "O" "O" "L" "L" "A" "M" "I" "L" "L"] ["O" "I" "D" "N" "A" "L" "H" "G" "I" "H"] ["R" "B" "A" "M" "C" "E" "T" "U" "H" "S"] ["S" "M" "O" "S" "K" "A" "G" "E" "T" "R"] ["C" "O" "R" "C" "H" "O" "R" "R" "O" "A"] ["I" "D" "B" "S" "L" "S" "A" "A" "O" "M"] ["I" "G" "O" "S" "M" "O" "N" "D" "F" "L"] ["H" "H" "N" "G" "M" "S" "D" "C" "M" "A"] ["C" "M" "I" "R" "R" "S" "M" "L" "H" "P"]] -> -1
             | HARAMBE [["E" "O" "A" "R" "B" "R" "N" "I" "A" "B"] ["Z" "E" "B" "R" "A" "E" "B" "R" "B" "H"] ["A" "R" "R" "A" "C" "C" "O" "O" "N" "R"] ["A" "A" "C" "B" "R" "R" "C" "H" "E" "C"] ["C" "N" "A" "B" "O" "Z" "O" "B" "K" "A"] ["B" "O" "N" "I" "R" "B" "B" "N" "C" "A"] ["E" "E" "R" "T" "C" "B" "R" "A" "I" "A"] ["A" "B" "C" "E" "R" "I" "C" "R" "H" "R"] ["B" "O" "I" "O" "R" "O" "R" "C" "C" "O"] ["B" "O" "A" "A" "K" "R" "K" "E" "A" "R"]] -> -1
             | AOLS [["W" "A" "Q" "H" "G" "T" "T" "W" "E" "E"] ["C" "B" "M" "I" "V" "Q" "Q" "E" "L" "S"] ["A" "P" "X" "W" "K" "W" "I" "I" "I" "L"] ["L" "D" "E" "L" "F" "X" "P" "I" "P" "V"] ["P" "O" "N" "D" "T" "M" "V" "A" "M" "N"] ["O" "E" "D" "S" "O" "Y" "Q" "G" "O" "B"] ["L" "G" "Q" "C" "K" "G" "M" "M" "C" "T"] ["Y" "C" "S" "L" "O" "A" "C" "U" "Z" "M"] ["X" "V" "D" "M" "G" "S" "X" "C" "Y" "Z"] ["U" "U" "I" "U" "N" "I" "X" "F" "N" "U"]] -> (7, 5)
             | PIPE [["W" "A" "Q" "H" "G" "T" "T" "W" "E" "E"] ["C" "B" "M" "I" "V" "Q" "Q" "E" "L" "S"] ["A" "P" "X" "W" "K" "W" "I" "I" "I" "L"] ["L" "D" "E" "L" "F" "X" "P" "I" "P" "V"] ["P" "O" "N" "D" "T" "M" "V" "A" "M" "N"] ["O" "E" "D" "S" "O" "Y" "Q" "G" "O" "B"] ["L" "G" "Q" "C" "K" "G" "M" "M" "C" "T"] ["Y" "C" "S" "L" "O" "A" "C" "U" "Z" "M"] ["X" "V" "D" "M" "G" "S" "X" "C" "Y" "Z"] ["U" "U" "I" "U" "N" "I" "X" "F" "N" "U"]] -> -1
    """
    rowStr = ""
    reverse = word[::-1]
    for i, row in enumerate(puzzle):
        rowStr = "".join(row)
        if rowStr.find(reverse) != -1:
            return (i, rowStr.find(reverse) + len(word) - 1)
    return -1

    # use a for each loop to iterate through a single list at a time

        # use another for each to iterate through each letter of the puzzle at a time

            # if the current letter we are looking at is the same as the first letter of the string passed through then execute the following

                # while loop that runs until a counter variable reaches the length of the string passed through and while the value subscripted in the puzzle doesn't go below 0

                    # decrement the index of the beginning spot by one and join that character to a string

                # if the outcome of the while loop is equivalent to the string passed through then return (row, col)

    # if the whole loop finishes and never finds a match for the word then return -1


def checkDown(word, puzzle):
    """
    CONTRACT | checkDown : str list -> tuple
    PURPOSE  | takes in word and checks to see if it appears in puzzle going from top to bottom if so return where the start of the string is
    EXAMPLES | CALPOLY [["W" "A" "Q" "H" "G" "T" "T" "W" "E" "E"] ["C" "B" "M" "I" "V" "Q" "Q" "E" "L" "S"] ["A" "P" "X" "W" "K" "W" "I" "I" "I" "L"] ["L" "D" "E" "L" "F" "X" "P" "I" "P" "V"] ["P" "O" "N" "D" "T" "M" "V" "A" "M" "N"] ["O" "E" "D" "S" "O" "Y" "Q" "G" "O" "B"] ["L" "G" "Q" "C" "K" "G" "M" "M" "C" "T"] ["Y" "C" "S" "L" "O" "A" "C" "U" "Z" "M"] ["X" "V" "D" "M" "G" "S" "X" "C" "Y" "Z"] ["U" "U" "I" "U" "N" "I" "X" "F" "N" "U"]] -> (1, 0)
             | PCV [["L" "L" "A" "R" "S" "H" "A" "H" "L" "C"] ["A" "O" "O" "L" "L" "A" "M" "I" "L" "L"] ["O" "I" "D" "N" "A" "L" "H" "G" "I" "H"] ["R" "B" "A" "M" "C" "E" "T" "U" "H" "S"] ["S" "M" "O" "S" "K" "A" "G" "E" "T" "R"] ["C" "O" "R" "C" "H" "O" "R" "R" "O" "A"] ["I" "D" "B" "S" "L" "S" "A" "A" "O" "M"] ["I" "G" "O" "S" "M" "O" "N" "D" "F" "L"] ["H" "H" "N" "G" "M" "S" "D" "C" "M" "A"] ["C" "M" "I" "R" "R" "S" "M" "L" "H" "P"]] -> -1
             | RABBIT [["E" "O" "A" "R" "B" "R" "N" "I" "A" "B"] ["Z" "E" "B" "R" "A" "E" "B" "R" "B" "H"] ["A" "R" "R" "A" "C" "C" "O" "O" "N" "R"] ["A" "A" "C" "B" "R" "R" "C" "H" "E" "C"] ["C" "N" "A" "B" "O" "Z" "O" "B" "K" "A"] ["B" "O" "N" "I" "R" "B" "B" "N" "C" "A"] ["E" "E" "R" "T" "C" "B" "R" "A" "I" "A"] ["A" "B" "C" "E" "R" "I" "C" "R" "H" "R"] ["B" "O" "I" "O" "R" "O" "R" "C" "C" "O"] ["B" "O" "A" "A" "K" "R" "K" "E" "A" "R"]] -> (1, 3)
             | CHICKEN [["E" "O" "A" "R" "B" "R" "N" "I" "A" "B"] ["Z" "E" "B" "R" "A" "E" "B" "R" "B" "H"] ["A" "R" "R" "A" "C" "C" "O" "O" "N" "R"] ["A" "A" "C" "B" "R" "R" "C" "H" "E" "C"] ["C" "N" "A" "B" "O" "Z" "O" "B" "K" "A"] ["B" "O" "N" "I" "R" "B" "B" "N" "C" "A"] ["E" "E" "R" "T" "C" "B" "R" "A" "I" "A"] ["A" "B" "C" "E" "R" "I" "C" "R" "H" "R"] ["B" "O" "I" "O" "R" "O" "R" "C" "C" "O"] ["B" "O" "A" "A" "K" "R" "K" "E" "A" "R"]] -> -1
             | RAMS [["L" "L" "A" "R" "S" "H" "A" "H" "L" "C"] ["A" "O" "O" "L" "L" "A" "M" "I" "L" "L"] ["O" "I" "D" "N" "A" "L" "H" "G" "I" "H"] ["R" "B" "A" "M" "C" "E" "T" "U" "H" "S"] ["S" "M" "O" "S" "K" "A" "G" "E" "T" "R"] ["C" "O" "R" "C" "H" "O" "R" "R" "O" "A"] ["I" "D" "B" "S" "L" "S" "A" "A" "O" "M"] ["I" "G" "O" "S" "M" "O" "N" "D" "F" "L"] ["H" "H" "N" "G" "M" "S" "D" "C" "M" "A"] ["C" "M" "I" "R" "R" "S" "M" "L" "H" "P"]] -> -1
    """
    colLst = []
    for j in range(10):
        colStr = ""
        colLst = []
        for i, row in enumerate(puzzle):
            colLst.append(row[j])
        colStr = "".join(colLst)
        if colStr.find(word) != -1:
            #return colStr, colLst
            return (colStr.find(word), j)
    return -1


    # use two index based for loops so that I can keep track of rows and columns simultaneously

        # if the current letter we are looking at is the same as the first letter of the string passed through then execute the following

            # while loop that runs until a counter variable reaches the length of the string passed through and while the value subscripted in the puzzle doesn't exceed 9

                # increment the value of row and join that character to a string

            # if the outcome of the while loop is equivalent to the string passed through then return (row, col)

    # if the whole loop finishes and never finds a match for the word then return -1


def checkUp(word, puzzle):
    """
    CONTRACT | checkUp : str list -> tuple
    PURPOSE  | takes in word and checks to see if it appears in puzzle from bottom to top is so return where the start of the string is
    EXAMPLES | MOUSE [["L" "L" "A" "R" "S" "H" "A" "H" "L" "C"] ["A" "O" "O" "L" "L" "A" "M" "I" "L" "L"] ["O" "I" "D" "N" "A" "L" "H" "G" "I" "H"] ["R" "B" "A" "M" "C" "E" "T" "U" "H" "S"] ["S" "M" "O" "S" "K" "A" "G" "E" "T" "R"] ["C" "O" "R" "C" "H" "O" "R" "R" "O" "A"] ["I" "D" "B" "S" "L" "S" "A" "A" "O" "M"] ["I" "G" "O" "S" "M" "O" "N" "D" "F" "L"] ["H" "H" "N" "G" "M" "S" "D" "C" "M" "A"] ["C" "M" "I" "R" "R" "S" "M" "L" "H" "P"]] -> -1
             | COMPILE [["W" "A" "Q" "H" "G" "T" "T" "W" "E" "E"] ["C" "B" "M" "I" "V" "Q" "Q" "E" "L" "S"] ["A" "P" "X" "W" "K" "W" "I" "I" "I" "L"] ["L" "D" "E" "L" "F" "X" "P" "I" "P" "V"] ["P" "O" "N" "D" "T" "M" "V" "A" "M" "N"] ["O" "E" "D" "S" "O" "Y" "Q" "G" "O" "B"] ["L" "G" "Q" "C" "K" "G" "M" "M" "C" "T"] ["Y" "C" "S" "L" "O" "A" "C" "U" "Z" "M"] ["X" "V" "D" "M" "G" "S" "X" "C" "Y" "Z"] ["U" "U" "I" "U" "N" "I" "X" "F" "N" "U"]] -> (6, 8)
             | SAGGY [["W" "A" "Q" "H" "G" "T" "T" "W" "E" "E"] ["C" "B" "M" "I" "V" "Q" "Q" "E" "L" "S"] ["A" "P" "X" "W" "K" "W" "I" "I" "I" "L"] ["L" "D" "E" "L" "F" "X" "P" "I" "P" "V"] ["P" "O" "N" "D" "T" "M" "V" "A" "M" "N"] ["O" "E" "D" "S" "O" "Y" "Q" "G" "O" "B"] ["L" "G" "Q" "C" "K" "G" "M" "M" "C" "T"] ["Y" "C" "S" "L" "O" "A" "C" "U" "Z" "M"] ["X" "V" "D" "M" "G" "S" "X" "C" "Y" "Z"] ["U" "U" "I" "U" "N" "I" "X" "F" "N" "U"]] -> -1
             | BROAD [["L" "L" "A" "R" "S" "H" "A" "H" "L" "C"] ["A" "O" "O" "L" "L" "A" "M" "I" "L" "L"] ["O" "I" "D" "N" "A" "L" "H" "G" "I" "H"] ["R" "B" "A" "M" "C" "E" "T" "U" "H" "S"] ["S" "M" "O" "S" "K" "A" "G" "E" "T" "R"] ["C" "O" "R" "C" "H" "O" "R" "R" "O" "A"] ["I" "D" "B" "S" "L" "S" "A" "A" "O" "M"] ["I" "G" "O" "S" "M" "O" "N" "D" "F" "L"] ["H" "H" "N" "G" "M" "S" "D" "C" "M" "A"] ["C" "M" "I" "R" "R" "S" "M" "L" "H" "P"]] -> (6, 2)
             | BAE [["E" "O" "A" "R" "B" "R" "N" "I" "A" "B"] ["Z" "E" "B" "R" "A" "E" "B" "R" "B" "H"] ["A" "R" "R" "A" "C" "C" "O" "O" "N" "R"] ["A" "A" "C" "B" "R" "R" "C" "H" "E" "C"] ["C" "N" "A" "B" "O" "Z" "O" "B" "K" "A"] ["B" "O" "N" "I" "R" "B" "B" "N" "C" "A"] ["E" "E" "R" "T" "C" "B" "R" "A" "I" "A"] ["A" "B" "C" "E" "R" "I" "C" "R" "H" "R"] ["B" "O" "I" "O" "R" "O" "R" "C" "C" "O"] ["B" "O" "A" "A" "K" "R" "K" "E" "A" "R"]] -> (8, 0)
    """
    colLst = []
    reverse = word[::-1]
    for j in range(10):
        colStr = ""
        colLst = []
        for i, row in enumerate(puzzle):
            colLst.append(row[j])
        colStr = "".join(colLst)
        if colStr.find(reverse) != -1:
            #return colStr, colLst
            return (colStr.find(reverse) + len(word) - 1, j)
    return -1


    # use two index based for loops so that I can keep track of rows and columns simultaneously

        # if the current letter we are looking at is the same as the first letter of the string passed through then execute the following

            # while loop that runs until a counter variable reaches the length of the string passed through and while the value subscripted in the puzzle doesn't go below 0

                # decrement the value of row and join that character to a string

            # if the outcome of the while loop is equivalent to the string passed through then return (row, col)

    # if the whole loop finishes and never finds a match for the word then return -1


def checkDiag(word, puzzle):
    """
    CONTRACT | checkDiag : str list -> tuple
    PURPOSE  | takes in word and checks to see if it appears in puzzle diagonally going from top left to bottom right if so return where the start of the string is
    EXAMPLES | MASON [["E" "O" "A" "R" "B" "R" "N" "I" "A" "B"] ["Z" "E" "B" "R" "A" "E" "B" "R" "B" "H"] ["A" "R" "R" "A" "C" "C" "O" "O" "N" "R"] ["A" "A" "C" "B" "R" "R" "C" "H" "E" "C"] ["C" "N" "A" "B" "O" "Z" "O" "B" "K" "A"] ["B" "O" "N" "I" "R" "B" "B" "N" "C" "A"] ["E" "E" "R" "T" "C" "B" "R" "A" "I" "A"] ["A" "B" "C" "E" "R" "I" "C" "R" "H" "R"] ["B" "O" "I" "O" "R" "O" "R" "C" "C" "O"] ["B" "O" "A" "A" "K" "R" "K" "E" "A" "R"]] -> -1
             | CORE [["E" "O" "A" "R" "B" "R" "N" "I" "A" "B"] ["Z" "E" "B" "R" "A" "E" "B" "R" "B" "H"] ["A" "R" "R" "A" "C" "C" "O" "O" "N" "R"] ["A" "A" "C" "B" "R" "R" "C" "H" "E" "C"] ["C" "N" "A" "B" "O" "Z" "O" "B" "K" "A"] ["B" "O" "N" "I" "R" "B" "B" "N" "C" "A"] ["E" "E" "R" "T" "C" "B" "R" "A" "I" "A"] ["A" "B" "C" "E" "R" "I" "C" "R" "H" "R"] ["B" "O" "I" "O" "R" "O" "R" "C" "C" "O"] ["B" "O" "A" "A" "K" "R" "K" "E" "A" "R"]] -> (4, 0)
             | GCC [["W" "A" "Q" "H" "G" "T" "T" "W" "E" "E"] ["C" "B" "M" "I" "V" "Q" "Q" "E" "L" "S"] ["A" "P" "X" "W" "K" "W" "I" "I" "I" "L"] ["L" "D" "E" "L" "F" "X" "P" "I" "P" "V"] ["P" "O" "N" "D" "T" "M" "V" "A" "M" "N"] ["O" "E" "D" "S" "O" "Y" "Q" "G" "O" "B"] ["L" "G" "Q" "C" "K" "G" "M" "M" "C" "T"] ["Y" "C" "S" "L" "O" "A" "C" "U" "Z" "M"] ["X" "V" "D" "M" "G" "S" "X" "C" "Y" "Z"] ["U" "U" "I" "U" "N" "I" "X" "F" "N" "U"]] -> (6, 5)
             | DOGGY [["W" "A" "Q" "H" "G" "T" "T" "W" "E" "E"] ["C" "B" "M" "I" "V" "Q" "Q" "E" "L" "S"] ["A" "P" "X" "W" "K" "W" "I" "I" "I" "L"] ["L" "D" "E" "L" "F" "X" "P" "I" "P" "V"] ["P" "O" "N" "D" "T" "M" "V" "A" "M" "N"] ["O" "E" "D" "S" "O" "Y" "Q" "G" "O" "B"] ["L" "G" "Q" "C" "K" "G" "M" "M" "C" "T"] ["Y" "C" "S" "L" "O" "A" "C" "U" "Z" "M"] ["X" "V" "D" "M" "G" "S" "X" "C" "Y" "Z"] ["U" "U" "I" "U" "N" "I" "X" "F" "N" "U"]] -> -1
             | SOB [["L" "L" "A" "R" "S" "H" "A" "H" "L" "C"] ["A" "O" "O" "L" "L" "A" "M" "I" "L" "L"] ["O" "I" "D" "N" "A" "L" "H" "G" "I" "H"] ["R" "B" "A" "M" "C" "E" "T" "U" "H" "S"] ["S" "M" "O" "S" "K" "A" "G" "E" "T" "R"] ["C" "O" "R" "C" "H" "O" "R" "R" "O" "A"] ["I" "D" "B" "S" "L" "S" "A" "A" "O" "M"] ["I" "G" "O" "S" "M" "O" "N" "D" "F" "L"] ["H" "H" "N" "G" "M" "S" "D" "C" "M" "A"] ["C" "M" "I" "R" "R" "S" "M" "L" "H" "P"]] -> (4, 0)
    """
    for i in range(10):
        for j in range(10):
            diagStr = ""
            diagLst = []
            count = 0
            while count < len(word) and i + count < 10 and j + count < 10:
                diagLst.append(puzzle[i + count][j + count])
                count += 1
            diagStr = "".join(diagLst)
            if diagStr.find(word) != -1:
                return (i, j)
    return -1

    # use two index based for loops so that I can keep track of rows and columns simultaneously

        # if the current letter we are looking at is the same as the first letter of the string passed through then execute the following

            # while loop that runs until a counter variable reaches the length of the string passed through and while the values subscripted in the puzzle don't exceed 9

                # increment the value of row and column and join that character to a string

            # if the outcome of the while loop is equivalent to the string passed through then return (row, col)

    # if the whole loop finishes and never finds a match for the word then return -1


