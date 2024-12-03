#!/usr/bin/env python3

import re

myfile = open('3.in', 'r')
lines = myfile.read().strip()
myfile.close()

# regex for finding valid 'mul()' instructions
pattern = re.compile(r'mul\((\d+),(\d+)\)')

enabled = []
# split into enabled segments that started with a 'do()' instruction
for l in lines.split('do()'):
    # keep only the enabled part of the segment before a "don't" instruction
    enabled.append(l.split("don't()")[0])
# join the enabled segments back together
enabled = ''.join(enabled)

part_one = 0
for mul in pattern.findall(lines):
    part_one += int(mul[0]) * int(mul[1])

part_two = 0
for mul in pattern.findall(enabled):
    part_two += int(mul[0]) * int(mul[1])

print('Part One:', part_one)
print('Part Two:', part_two)
