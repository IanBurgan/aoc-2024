#!/usr/bin/env python3

from collections import Counter

myfile = open('1.in', 'r')
lines = myfile.read().strip().splitlines()
myfile.close()

part_one = 0
part_two = 0

left = []
right = []

for l in lines:
    a, b = l.split()
    left.append(int(a))
    right.append(int(b))

left.sort()
right.sort()
counts = Counter(right)

for l,r in zip(left,right):
    part_one += abs(l - r)
    part_two += l * counts[l]

print('Part One:', part_one)
print('Part Two:', part_two)
