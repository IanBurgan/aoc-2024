#!/usr/bin/env python3

from collections import defaultdict
from fractions import Fraction
from itertools import combinations

myfile = open("8.in", "r")
lines = myfile.read().strip().splitlines()
myfile.close()

antennas = defaultdict(list)
grid = defaultdict(str)
for y in range(len(lines)):
    for x in range(len(lines[y])):
        grid[(x, y)] = lines[y][x]
        if lines[y][x] != ".":
            antennas[lines[y][x]].append((x, y))

p1_antinodes = set()
p2_antinodes = set()
for freq, locs in antennas.items():
    pairs = combinations(locs, 2)
    for a, b in pairs:
        dx = a[0] - b[0]
        dy = a[1] - b[1]

        antinode_1 = (a[0] + dx, a[1] + dy)
        if grid[antinode_1] != "":
            p1_antinodes.add(antinode_1)
        antinode_2 = (b[0] - dx, b[1] - dy)
        if grid[antinode_2] != "":
            p1_antinodes.add(antinode_2)

        p2_antinodes.add(a)
        p2_antinodes.add(b)
        # reduce the dx and dy
        slope = Fraction(dx, dy)
        rdx = slope.numerator
        rdy = slope.denominator

        # start at a and check all points on the line in both directions
        next_point = (a[0] - rdx, a[1] - rdy)
        while grid[next_point] != "":
            p2_antinodes.add(next_point)
            next_point = (next_point[0] - rdx, next_point[1] - rdy)

        next_point = (a[0] + rdx, a[1] + rdy)
        while grid[next_point] != "":
            p2_antinodes.add(next_point)
            next_point = (next_point[0] + rdx, next_point[1] + rdy)

print("Part One:", len(p1_antinodes))
print("Part Two:", len(p2_antinodes))
