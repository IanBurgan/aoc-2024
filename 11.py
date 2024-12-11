#!/usr/bin/env python3

myfile = open("11.in", "r")
lines = myfile.read().strip()
myfile.close()

stones = map(int, lines.split())

memo = {}


def calc(stone, blinks):
    if blinks == 0:
        return 1

    if (stone, blinks) not in memo:
        s = str(stone)
        if stone == 0:
            result = calc(1, blinks - 1)
        elif len(s) % 2 == 0:
            left = calc(int(s[: len(s) // 2]), blinks - 1)
            right = calc(int(s[len(s) // 2 :]), blinks - 1)
            result = left + right
        else:
            result = calc(stone * 2024, blinks - 1)

        memo[(stone, blinks)] = result

    return memo[(stone, blinks)]


part_one = 0
part_two = 0
for s in stones:
    part_one += calc(s, 25)
    part_two += calc(s, 75)

print("Part One:", part_one)
print("Part Two:", part_two)
