#!/usr/bin/env python3

from collections import defaultdict, deque

myfile = open("10.in", "r")
lines = myfile.read().strip().splitlines()
myfile.close()

starts = []
grid = defaultdict(str)
for y in range(len(lines)):
    for x in range(len(lines[y])):
        grid[(x, y)] = lines[y][x]
        if lines[y][x] == "0":
            starts.append((x, y))

part_one = 0
part_two = 0

for start in starts:
    ends = set()
    q = deque([start])
    while q:
        curr = q.pop()
        height = int(grid[curr])
        if height == 9:
            part_two += 1
            ends.add(curr)
            continue

        for dir in [(1, 0), (0, -1), (-1, 0), (0, 1)]:
            next = (curr[0] + dir[0], curr[1] + dir[1])
            if grid[next] == str(height + 1):
                q.appendleft(next)

    part_one += len(ends)

print("Part One:", part_one)
print("Part Two:", part_two)
