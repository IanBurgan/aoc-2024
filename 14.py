#!/usr/bin/env python3

import re
from collections import defaultdict

myfile = open("14.in", "r")
lines = myfile.read().strip().splitlines()
myfile.close()

part_one = 0
part_two = 0

width = 101
height = 103
robots = []
for line in lines:
    p, v = line.split()
    p = [int(x) for x in re.findall(r"-?\d+", p)]
    v = [int(x) for x in re.findall(r"-?\d+", v)]
    robots.append((p, v))

found_tree = False
for s in range(1, 10000):
    if found_tree:
        break

    grid = defaultdict(bool)
    for i, r in enumerate(robots):
        p, v = r
        new_p = ((p[0] + v[0]) % width, (p[1] + v[1]) % height)
        grid[new_p] = True
        robots[i] = (new_p, v)

    if s == 100:
        quad_1 = quad_2 = quad_3 = quad_4 = 0
        for r in robots:
            mid_x = width // 2
            mid_y = height // 2

            p = r[0]
            if p[0] < mid_x and p[1] < mid_y:
                quad_1 += 1
            elif p[0] > mid_x and p[1] < mid_y:
                quad_2 += 1
            elif p[0] < mid_x and p[1] > mid_y:
                quad_3 += 1
            elif p[0] > mid_x and p[1] > mid_y:
                quad_4 += 1
        part_one = quad_1 * quad_2 * quad_3 * quad_4

    for y in range(0, height - 3, 3):
        if found_tree:
            break
        for x in range(0, width - 3, 3):
            # look for 4x4 cluster of robots
            if all(grid[(x + i, y + j)] for i in range(4) for j in range(4)):
                part_two = s
                found_tree = True
                break

print("Part One:", part_one)
print("Part Two:", part_two)
