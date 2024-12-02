#!/usr/bin/env python3

def is_valid(nums):
    is_inc = nums[1] > nums[0]

    for i in range(1, len(nums)):
        if (nums[i] > nums[i - 1]) != is_inc:
            return False
        if abs(nums[i] - nums[i - 1]) > 3 or abs(nums[i] - nums[i - 1]) < 1:
            return False

    return True


myfile = open('2.in', 'r')
lines = myfile.read().strip().splitlines()
myfile.close()

part_one = 0
part_two = 0

for l in lines:
    nums = [int(x) for x in l.strip().split()]

    if is_valid(nums):
        part_one += 1
        part_two += 1
    else:
        for i in range(len(nums)):
            new_nums = nums.copy()
            del new_nums[i]
            if is_valid(new_nums):
                part_two += 1
                break

print('Part One:', part_one)
print('Part Two:', part_two)
