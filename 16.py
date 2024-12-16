#!/usr/bin/env python3

import heapq
from collections import defaultdict, deque

myfile = open("16.in", "r")
lines = myfile.read().strip().splitlines()
myfile.close()

start = end = (-1, -1)
grid = defaultdict(str)
for y in range(len(lines)):
    for x in range(len(lines[y])):
        if lines[y][x] == "S":
            start = (x, y)
        elif lines[y][x] == "E":
            end = (x, y)
        grid[(x, y)] = lines[y][x]

dirs = [(1, 0), (0, -1), (-1, 0), (0, 1)]

part_one = 0
part_two = 0

scores = defaultdict(lambda: float("inf"))
prev = defaultdict(set)
# score, pos, direction
q = [(0, start, 0)]
heapq.heapify(q)
while q:
    curr_score, curr_pos, curr_dir = heapq.heappop(q)
    if grid[curr_pos] == "E":
        if part_one == 0:
            part_one = curr_score

        if curr_score > part_one:
            break

    for next_dir in range(len(dirs)):
        next_pos = (curr_pos[0] + dirs[next_dir][0], curr_pos[1] + dirs[next_dir][1])
        next_score = curr_score + 1 if curr_dir == next_dir else curr_score + 1001

        if next_score < scores[(next_pos, next_dir)]:
            if grid[next_pos] != "#":
                heapq.heappush(q, (next_score, next_pos, next_dir))
                scores[(next_pos, next_dir)] = next_score
                prev[(next_pos, next_dir)].clear()
                prev[(next_pos, next_dir)].add((curr_pos, curr_dir))
        elif next_score == scores[(next_pos, next_dir)]:
            scores[(next_pos, next_dir)] = next_score
            prev[(next_pos, next_dir)].add((curr_pos, curr_dir))

path_nodes = set()
remaining = deque([(end, i) for i in range(len(dirs))])
while remaining:
    node, dir = remaining.popleft()
    path_nodes.add(node)

    for prev_node, prev_dir in prev[(node, dir)]:
        if prev_node not in path_nodes:
            remaining.append((prev_node, prev_dir))
part_two = len(path_nodes)

print("Part One:", part_one)
print("Part Two:", part_two)
