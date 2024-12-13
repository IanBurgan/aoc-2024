#!/usr/bin/env python3

import re

myfile = open("13.in", "r")
lines = myfile.read().strip().split('\n\n')
myfile.close()

part_one = 0
part_two = 0

for machine in lines:
    a, b, z = machine.split('\n')
    a = [int(x) for x in re.findall(r'\d+', a)]
    b = [int(x) for x in re.findall(r'\d+', b)]
    z = [int(x) for x in re.findall(r'\d+', z)]

    # the math below is derived from manually solving the system of equations
    # rounding is used to handle the imprecision
    a_count = round((z[0] - ((b[0] * z[1]) / b[1])) / (a[0] - ((b[0]*a[1]) / b[1])))
    b_count = round((z[1] - (a[1] * a_count)) / b[1])
    if (a[0] * a_count) + (b[0] * b_count) == z[0] and (a[1] * a_count) + (b[1] * b_count) == z[1]:
        part_one += 3 * a_count + b_count

    # update prize location and recalculate
    z = [x + 10000000000000 for x in z]
    a_count = round((z[0] - ((b[0] * z[1]) / b[1])) / (a[0] - ((b[0]*a[1]) / b[1])))
    b_count = round((z[1] - (a[1] * a_count)) / b[1])
    if (a[0] * a_count) + (b[0] * b_count) == z[0] and (a[1] * a_count) + (b[1] * b_count) == z[1]:
        part_two += 3 * a_count + b_count

print("Part One:", part_one)
print("Part Two:", part_two)
