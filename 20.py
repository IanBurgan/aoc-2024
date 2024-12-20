#!/usr/bin/env python3

from collections import defaultdict, deque

myfile = open("20.in", "r")
lines = myfile.read().strip().splitlines()
myfile.close()

end = start = (-1, -1)
grid = defaultdict(str)
for y in range(len(lines)):
    for x in range(len(lines[y])):
        if lines[y][x] == "S":
            start = (x, y)
        elif lines[y][x] == "E":
            end = (x, y)
        grid[(x, y)] = lines[y][x]

part_one = 0
part_two = 0

visited = set()
scores = defaultdict(lambda: float("inf"))
scores[start] = 0
q = deque([start])
while q:
    pos = q.popleft()
    visited.add(pos)

    for dir in [(1, 0), (0, -1), (-1, 0), (0, 1)]:
        next_pos = (pos[0] + dir[0], pos[1] + dir[1])
        if next_pos not in visited and grid[next_pos] != "#" and grid[next_pos] != "":
            scores[next_pos] = scores[pos] + 1
            q.append(next_pos)

for a in visited:
    for i in range(-20, 21):
        for j in range(-20, 21):
            dist = abs(i) + abs(j)
            if dist > 20:
                continue
            b = (a[0] + i, a[1] + j)
            if b not in visited:
                continue
            savings = scores[b] - scores[a] - dist
            if savings < 100:
                continue

            if dist <= 2:
                part_one += 1
            part_two += 1

print("Part One:", part_one)
print("Part Two:", part_two)
