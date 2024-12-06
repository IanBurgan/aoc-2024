#!/usr/bin/env python3

from collections import defaultdict

myfile = open("5.in", "r")
data = myfile.read().strip()
myfile.close()

rules, updates = data.split("\n\n")
rules, updates = rules.splitlines(), updates.splitlines()

ordering = defaultdict(set)
for line in rules:
    before, after = line.split("|")
    ordering[before].add(after)


def is_valid_order(pages):
    for i, page_i in enumerate(pages):
        for j, page_j in enumerate(pages):
            if i == j:
                pass
            elif i < j and page_i in ordering[page_j]:
                return False, i, j
            elif i > j and page_j in ordering[page_i]:
                return False, i, j

    return True, 0, 0


part_one = 0
part_two = 0
for update in updates:
    pages = update.split(",")

    valid, i, j = is_valid_order(pages)

    if valid:
        part_one += int(pages[len(pages) // 2])
        continue

    # swapping is slower than topological sort, but it works
    while not valid:
        pages[i], pages[j] = pages[j], pages[i]
        valid, i, j = is_valid_order(pages)
    part_two += int(pages[len(pages) // 2])

print("Part One:", part_one)
print("Part Two:", part_two)
