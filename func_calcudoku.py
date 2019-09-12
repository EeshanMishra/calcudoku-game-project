# Project 4
# Name: Eeshan Mishra
# Instructor: S. Einakian
# Section: 05


import sys


# Prompts user for the number of cages and gets the required values for all those cages
# None --> int, int
def get_cages():
    cages = []
    numberofcages = int(input("Please enter the number of cages: "))
    for x in range(numberofcages):
        n = input("Cage number {}: ".format(x))
        map(int, n.split(" "))
        cagelist = [int(s) for s in n.split(" ")]
        cages.append(cagelist)
    return cages, numberofcages


# checks if any of the rows contain duplicate positive numbers and returns True if there are none
# int --> boolean
def validate_rows(grid):
    for row in range(len(grid)):  # breaks puzzle up into each row
        for col in range(len(grid[row])):  # breaks puzzle up into each column
            if grid[row].count(grid[row][col]) > 1 and grid[row][col] != 0:  # runs through each row and column and counts each individual value and if the count is greater than 1 then it returns false
                return False
    return True


# checks if any of the rows contain duplicate positive numbers and returns True if there are none
# int --> boolean
def validate_cols(grid):
    for row in range(len(grid[0])):
        new_list = []
        for col in range(len(grid)):
            new_list.append(grid[col][row])
        for i in range(len(new_list)):  # breaks puzzle up into each column
            if new_list.count(new_list[i]) > 1 and new_list[i] != 0:  # runs through each row and column and counts each individual value and if the count is greater than 1 then it returns false
                return False
    return True


# Checks if the values in a cage equal the required sum or if a partially populated cage is less than the required sum
# int, int --> boolean
def validate_cages(grid, cages):
    for acage in cages:  # calls each list from mini cage
        sum1 = 0
        temp_cage = []
        for puzzleNum in range(1, len(acage)):
            row = acage[puzzleNum] // 5
            col = acage[puzzleNum] % 5
            temp_cage.append(grid[row][col])  # puts whatever values in the parentheses into tempCage
        for i in range(len(temp_cage)):
            sum1 = sum1 + temp_cage[i]
        if temp_cage.count(0) >= 1:
            if sum1 < acage[0]:
                continue
            else:
                return False
        else:
            if sum1 != acage[0]:
                return False
    return True


# checks if all the validation functions returns true
# int, int --> boolean
def validate_all(grid, cages):
    if validate_rows(grid) and validate_cols(grid) and validate_cages(grid, cages):
        return True
    else:
        return False


# creates the grid
# int --> None
def transpose(grid):
    for row in range(0, 5):
        for col in range(0, 5):
            sys.stdout.write(str(grid[row][col]) + " ")  # replace this with a pr
        print()

