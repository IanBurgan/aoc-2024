#!/usr/bin/env python3

from collections import defaultdict, deque

myfile = open("15.in", "r")
lines = myfile.read().strip().split("\n\n")
myfile.close()

map, moves = lines
maps = [
    map.splitlines(),
    map.replace("#", "##")
    .replace("O", "[]")
    .replace(".", "..")
    .replace("@", "@.")
    .splitlines(),
]
moves = moves.replace("\n", "")

robots = [(-1, -1), (-1, -1)]
grids = [defaultdict(str), defaultdict(str)]
for i, map in enumerate(maps):
    for y in range(len(map)):
        for x in range(len(map[y])):
            if map[y][x] == "@":
                robots[i] = (x, y)
            grids[i][(x, y)] = map[y][x]

part_one = 0
part_two = 0

for m in moves:
    dirs = {
        "<": (-1, 0),
        ">": (1, 0),
        "^": (0, -1),
        "v": (0, 1),
    }
    dir = dirs[m]

    for i, grid in enumerate(grids):
        new_robot = (robots[i][0] + dir[0], robots[i][1] + dir[1])

        if grid[new_robot] == ".":
            grid[robots[i]] = "."
            robots[i] = new_robot
            grid[robots[i]] = "@"
        # part 1
        elif grid[new_robot] == "O":
            offset = 1
            x = (new_robot[0] + dir[0] * offset, new_robot[1] + dir[1] * offset)
            while grid[x] == "O":
                offset += 1
                x = (new_robot[0] + dir[0] * offset, new_robot[1] + dir[1] * offset)

            if grid[x] == ".":
                grid[x] = "O"
                grid[robots[i]] = "."
                robots[i] = new_robot
                grid[robots[i]] = "@"
        # part 2
        elif grid[new_robot] == "[" or grid[new_robot] == "]":
            boxes = deque()
            seen = set()
            q = deque()
            if grid[new_robot] == "[":
                q.append(new_robot)
                q.append((new_robot[0] + 1, new_robot[1]))
            elif grid[new_robot] == "]":
                q.append(new_robot)
                q.append((new_robot[0] - 1, new_robot[1]))
            while q:
                curr = q.popleft()

                if curr in seen:
                    continue
                seen.add(curr)

                if grid[curr] == "[":
                    boxes.appendleft(curr)

                dest = (curr[0] + dir[0], curr[1] + dir[1])
                if grid[dest] == "[":
                    q.append(dest)
                    q.append((dest[0] + 1, dest[1]))
                elif grid[dest] == "]":
                    q.append((dest[0] - 1, dest[1]))
                    q.append(dest)
                elif grid[dest] == "#":
                    # movement prevented, blocked by wall
                    boxes.clear()
                    break

            for b in boxes:
                grid[b] = "."
                grid[(b[0] + 1, b[1])] = "."
                grid[(b[0] + dir[0], b[1] + dir[1])] = "["
                grid[(b[0] + 1 + dir[0], b[1] + dir[1])] = "]"

            if len(boxes) > 0:
                grid[robots[i]] = "."
                robots[i] = new_robot
                grid[robots[i]] = "@"

for grid in grids:
    for point, item in grid.items():
        if item == "O":
            part_one += 100 * point[1] + point[0]
        elif item == "[":
            part_two += 100 * point[1] + point[0]

print("Part One:", part_one)
print("Part Two:", part_two)
