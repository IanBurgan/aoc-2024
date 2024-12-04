#!/usr/bin/env python3

myfile = open("4.in", "r")
grid = myfile.read().strip().splitlines()
myfile.close()

x_points = []
a_points = []
for y in range(len(grid)):
    for x in range(len(grid[y])):
        if grid[y][x] == "X":
            x_points.append((x, y))
        elif grid[y][x] == "A":
            a_points.append((x, y))

part_one = 0
for x, y in x_points:
    # check right
    if x + 3 < len(grid[y]):
        word = grid[y][x : x + 4]
        if word == 'XMAS':
            part_one += 1
    # check left
    if x - 3 >= 0:
        word = grid[y][x] + grid[y][x - 1] + grid[y][x - 2] + grid[y][x - 3]
        if word == 'XMAS':
            part_one += 1
    # check down
    if y + 3 < len(grid):
        word = grid[y][x] + grid[y + 1][x] + grid[y + 2][x] + grid[y + 3][x]
        if word == 'XMAS':
            part_one += 1
    # check up
    if y - 3 >= 0:
        word = grid[y][x] + grid[y - 1][x] + grid[y - 2][x] + grid[y - 3][x]
        if word == 'XMAS':
            part_one += 1
    # check down right
    if y + 3 < len(grid) and x + 3 < len(grid[y]):
        word = grid[y][x] + grid[y + 1][x + 1] + grid[y + 2][x + 2] + grid[y + 3][x + 3]
        if word == 'XMAS':
            part_one += 1
    # check up right
    if y - 3 >= 0 and x + 3 < len(grid[y]):
        word = grid[y][x] + grid[y - 1][x + 1] + grid[y - 2][x + 2] + grid[y - 3][x + 3]
        if word == 'XMAS':
            part_one += 1
    # check down left
    if y + 3 < len(grid) and x - 3 >= 0:
        word = grid[y][x] + grid[y + 1][x - 1] + grid[y + 2][x - 2] + grid[y + 3][x - 3]
        if word == 'XMAS':
            part_one += 1
    # check up left
    if y - 3 >= 0 and x - 3 >= 0:
        word = grid[y][x] + grid[y - 1][x - 1] + grid[y - 2][x - 2] + grid[y - 3][x - 3]
        if word == 'XMAS':
            part_one += 1

part_two = 0
for x, y in a_points:
    if x - 1 >= 0 and y - 1 >= 0 and x + 1 < len(grid[y]) and y + 1 < len(grid):
        diag_1 = grid[y - 1][x - 1] + grid[y][x] + grid[y + 1][x + 1]
        diag_2 = grid[y + 1][x - 1] + grid[y][x] + grid[y - 1][x + 1]
        if diag_1 in ["MAS", "SAM"] and diag_2 in ["MAS", "SAM"]:
            part_two += 1


print("Part One:", part_one)
print("Part Two:", part_two)
