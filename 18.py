#!/usr/bin/env python3

import re
from collections import defaultdict, deque

myfile = open("18.in", "r")
lines = myfile.read().strip().splitlines()
myfile.close()

blocks = [tuple(map(int, re.findall(r"\d+", line))) for line in lines]

part_one = 0
part_two = 0

height = width = 70


def search(block_count):
    grid = defaultdict(str)
    for x in range(width + 1):
        for y in range(height + 1):
            grid[(x, y)] = "."
    grid[(width, height)] = "$"
    for x, y in blocks[: block_count + 1]:
        grid[(x, y)] = ""

    visited = set()
    scores = defaultdict(lambda: float("inf"))
    scores[(0, 0)] = 0
    q = deque([(0, 0)])
    while q:
        pos = q.popleft()
        visited.add(pos)

        if grid[pos] == "$":
            return scores[pos]

        next_score = scores[pos] + 1
        for dir in [(1, 0), (0, -1), (-1, 0), (0, 1)]:
            next_pos = (pos[0] + dir[0], pos[1] + dir[1])
            if next_pos not in visited and next_score < scores[next_pos]:
                if grid[next_pos] != "":
                    scores[next_pos] = next_score
                    q.append(next_pos)

    return -1


part_one = search(1024)
unblocked, blocked = 1024, len(blocks)
while blocked - unblocked > 1:
    mid = (unblocked + blocked) // 2
    result = search(mid)
    if result == -1:
        blocked = mid
    else:
        unblocked = mid
part_two = ",".join(map(str, blocks[blocked]))

print("Part One:", part_one)
print("Part Two:", part_two)
