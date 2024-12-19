#!/usr/bin/env python3

myfile = open("19.in", "r")
lines = myfile.read().strip().split("\n\n")
myfile.close()

towels, designs = lines
towels = towels.split(", ")
designs = designs.splitlines()

part_one = 0
part_two = 0

memo = {'': 1}

def count_ways(design):
    if design in memo:
        return memo[design]

    total = 0
    for t in towels:
        if design.startswith(t):
            total += count_ways(design.removeprefix(t))

    memo[design] = total
    return total

for design in designs:
    ways = count_ways(design)
    if ways > 0:
        part_one += 1
    part_two += ways

print("Part One:", part_one)
print("Part Two:", part_two)
