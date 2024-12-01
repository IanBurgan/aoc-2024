#!/usr/bin/env python3

myfile = open('X.in', 'r')
lines = myfile.read().strip().splitlines()
myfile.close()

part_one = ''
part_two = ''

for l in lines:
    l = l.strip()

print('Part One:', part_one)
print('Part Two:', part_two)
