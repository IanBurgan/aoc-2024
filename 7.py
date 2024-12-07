#!/usr/bin/env python3

from itertools import product

myfile = open("7.in", "r")
lines = myfile.read().strip().splitlines()
myfile.close()


def solve(nums, ops):
    total = int(nums[0])

    for i in range(len(ops)):
        operation, value = ops[i], nums[i + 1]
        if operation == "+":
            total += int(value)
        elif operation == "*":
            total *= int(value)
        elif operation == "|":
            total = int(str(total) + value)

    return total


part_one = 0
part_two = 0
for line in lines:
    result, nums = line.split(": ")
    result = int(result)
    nums = nums.split()

    operation_perms = set(product(["+", "*"], repeat=len(nums) - 1))

    try_concat = True
    for ops in operation_perms:
        if solve(nums, ops) == result:
            try_concat = False
            part_one += result
            part_two += result
            break

    if try_concat:
        operation_perms = (
            set(product(["+", "*", "|"], repeat=len(nums) - 1)) - operation_perms
        )
        for ops in operation_perms:
            if solve(nums, ops) == int(result):
                part_two += result
                break


print("Part One:", part_one)
print("Part Two:", part_two)
