# Project 4
# Name: Eeshan Mishra
# Instructor: S. Einakian
# Section: 05


from func_calcudoku import *


def main():

    cages, numberofcages = get_cages()
    grid = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

    check = 0
    backtrack = 0
    cell = 0

    while cell < 25:
        row = cell // 5
        col = cell % 5
        if grid[row][col] < 5:
            grid[row][col] += 1
            check += 1
            check_valid = validate_all(grid, cages)
            if check_valid:
                cell += 1
            if cell >= 25:
                break
        elif grid[row][col] >= 5 and not check_valid:
            grid[row][col] = 0
            cell -= 1
            backtrack += 1

    print()
    print("---Solution---")
    print()
    transpose(grid)
    print()
    print()
    print("checks:", check, "backtracks:", backtrack)


if __name__ == '__main__':
    main()

