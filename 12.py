#!/usr/bin/env python3

from collections import defaultdict, deque

myfile = open("12.in", "r")
lines = myfile.read().strip().splitlines()
myfile.close()

grid = defaultdict(str)
for y in range(len(lines)):
    for x in range(len(lines[y])):
        grid[(x, y)] = lines[y][x]


def is_corner(node, dir):
    left_in_region = grid[(node[0] - 1, node[1])] == grid[node]
    up_left_in_region = grid[(node[0] - 1, node[1] - 1)] == grid[node]
    up_in_region = grid[(node[0], node[1] - 1)] == grid[node]
    up_right_in_region = grid[(node[0] + 1, node[1] - 1)] == grid[node]
    right_in_region = grid[(node[0] + 1, node[1])] == grid[node]
    down_right_in_region = grid[(node[0] + 1, node[1] + 1)] == grid[node]
    down_in_region = grid[(node[0], node[1] + 1)] == grid[node]
    down_left_in_region = grid[(node[0] - 1, node[1] + 1)] == grid[node]

    if dir == (-1, 0):  # left
        return not up_in_region or up_left_in_region
    if dir == (0, -1):  # up
        return not right_in_region or up_right_in_region
    if dir == (1, 0):  # right
        return not down_in_region or down_right_in_region
    if dir == (0, 1):  # down
        return not left_in_region or down_left_in_region

    return False


part_one = 0
part_two = 0

visited = set()
for y in range(len(lines)):
    for x in range(len(lines[y])):
        if (x, y) in visited:
            continue

        edges = set()
        area = perimeter = sides = 0
        q = deque([(x, y)])
        while q:
            curr = q.pop()
            if curr in visited:
                continue
            visited.add(curr)
            area += 1

            for dir in [(1, 0), (0, -1), (-1, 0), (0, 1)]:
                next = (curr[0] + dir[0], curr[1] + dir[1])
                if grid[next] == grid[curr]:
                    q.append(next)
                else:
                    perimeter += 1
                    if is_corner(curr, dir):
                        sides += 1

        part_one += area * perimeter
        part_two += area * sides

print("Part One:", part_one)
print("Part Two:", part_two)
