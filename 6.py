#!/usr/bin/env python3

from collections import defaultdict

myfile = open("6.in", "r")
lines = myfile.read().strip().splitlines()
myfile.close()

guard_pos = (-1, -1)
grid = defaultdict(str)
for y in range(len(lines)):
    for x in range(len(lines[y])):
        grid[(x, y)] = lines[y][x]
        if lines[y][x] == "^":
            guard_pos = (x, y)

initial_pos = guard_pos
dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)]
dir_idx = 0

visited = set()
while grid[guard_pos] != "":
    dir = dirs[dir_idx]
    visited.add(guard_pos)
    new_pos = (guard_pos[0] + dir[0], guard_pos[1] + dir[1])

    while grid[new_pos] == "#":
        dir_idx = (dir_idx + 1) % 4
        dir = dirs[dir_idx]
        new_pos = (guard_pos[0] + dir[0], guard_pos[1] + dir[1])

    guard_pos = new_pos

part_one = len(visited)
part_two = 0

# test putting an obstacle on every point in the path from part one
for point in visited:
    # we can't place an obstacle where the guard starts
    if point == initial_pos:
        continue

    # reset state
    cycle_points = set()
    dir_idx = 0
    guard_pos = initial_pos
    # add obstacle
    grid[point] = "#"

    while grid[guard_pos] != "":
        dir = dirs[dir_idx]

        # check for a cycle
        if (guard_pos, dir) in cycle_points:
            part_two += 1
            break

        cycle_points.add((guard_pos, dir))
        new_pos = (guard_pos[0] + dir[0], guard_pos[1] + dir[1])

        while grid[new_pos] == "#":
            dir_idx = (dir_idx + 1) % 4
            dir = dirs[dir_idx]
            new_pos = (guard_pos[0] + dir[0], guard_pos[1] + dir[1])

        guard_pos = new_pos

    # reset obstacle to try another
    grid[point] = "."

print("Part One:", part_one)
print("Part Two:", part_two)
