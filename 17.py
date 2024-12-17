#!/usr/bin/env python3

import re

myfile = open("17.in", "r")
lines = myfile.read().strip().split("\n\n")
myfile.close()

values, instructions = lines
a, b, c = list(map(int, re.findall(r"\d+", values)))
program = list(map(int, re.findall(r"\d+", instructions)))


def run(a_start, b_start, c_start):
    a, b, c = a_start, b_start, c_start

    def combo(val):
        if val <= 3:
            return val
        elif val == 4:
            return a
        elif val == 5:
            return b
        elif val == 6:
            return c
        assert False

    ip = 0
    output = []
    while ip < len(program):
        op = program[ip]
        if op == 0:
            val = combo(program[ip + 1])
            a = a // (2**val)
            ip += 2
        elif op == 1:
            val = program[ip + 1]
            b = b ^ val
            ip += 2
        elif op == 2:
            val = combo(program[ip + 1])
            b = val % 8
            ip += 2
        elif op == 3:
            if a == 0:
                ip += 2
            else:
                val = program[ip + 1]
                ip = val
        elif op == 4:
            b = b ^ c
            ip += 2
        elif op == 5:
            val = combo(program[ip + 1])
            output.append(str(val % 8))
            ip += 2
        elif op == 6:
            val = combo(program[ip + 1])
            b = a // (2**val)
            ip += 2
        elif op == 7:
            val = combo(program[ip + 1])
            c = a // (2**val)
            ip += 2
    return output


part_one = ",".join(run(a, b, c))


# reverse engineered version of the program
# that gives the first output for a given a
def get_output(a):
    return (((a % 8) ^ 2) ^ (a // (2 ** ((a % 8) ^ 2))) ^ 7) % 8


part_two = 0
targets = reversed(program)
# the last a must be 7 or less
possible = list(range(8))
for target in targets:
    valid = []
    for a in possible:
        if get_output(a) == target:
            valid.append(a)
    part_two = min(valid)

    # n such that n // 8 == a for some valid a
    possible = []
    for a in valid:
        possible += list(range(a * 8, (a + 1) * 8))

print("Part One:", part_one)
print("Part Two:", part_two)
