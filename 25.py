#!/usr/bin/env python3

myfile = open("25.in", "r")
lines = myfile.read().strip().split("\n\n")
myfile.close()

schematics = [line.split("\n") for line in lines]

part_one = 0

keys = set()
locks = set()
for schematic in schematics:
    is_lock = schematic[0][0] == "#"
    width = len(schematic[0])

    cols = [[row[i] for row in schematic] for i in range(width)]

    heights = tuple(c.count("#") - 1 for c in cols)
    if is_lock:
        locks.add(heights)
    else:
        keys.add(heights)

for lock in locks:
    for key in keys:
        max_key = tuple(5 - h for h in lock)
        if all(h <= max_key[i] for i, h in enumerate(key)):
            part_one += 1

print("Part One:", part_one)
