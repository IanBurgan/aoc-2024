#!/usr/bin/env python3

from collections import defaultdict, deque

myfile = open("22.in", "r")
lines = myfile.read().strip().splitlines()
myfile.close()
lines = [int(x) for x in lines]

part_one = 0
part_two = 0

bananas = defaultdict(int)
for num in lines:
    seen = set()
    changes = deque()
    for _ in range(2000):
        start = num
        num = ((num * 64) ^ num) % 16777216
        num = ((num // 32) ^ num) % 16777216
        num = ((num * 2048) ^ num) % 16777216

        price = (num % 10)
        change = price - (start % 10)

        if len(changes) == 4:
            changes.popleft()
        changes.append(change)

        key = tuple(x for x in changes)
        if key not in seen:
            seen.add(key)
            bananas[key] += price

    part_one += num
part_two = max(bananas.values())
print("Part One:", part_one)
print("Part Two:", part_two)
