#!/usr/bin/env python3

from collections import defaultdict

myfile = open("X.in", "r")
lines = myfile.read().strip().splitlines()
myfile.close()

grid = defaultdict(str)
for y in range(len(lines)):
    for x in range(len(lines[y])):
        grid[(x,y)] = lines[y][x]

part_one = 0
part_two = 0

for line in lines:
    line = line.strip()

print("Part One:", part_one)
print("Part Two:", part_two)
