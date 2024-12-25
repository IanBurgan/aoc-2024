#!/usr/bin/env python3

from collections import deque

myfile = open("24.in", "r")
lines = myfile.read().strip().split("\n\n")
myfile.close()
in_vals, out_vals = lines[0].splitlines(), lines[1].splitlines()

wires = {}
for line in in_vals:
    wire, val = line.split(": ")
    wires[wire] = int(val)

q = deque(out_vals)
while q:
    curr = q.popleft()
    wires_in, out_wire = curr.split(" -> ")
    left, op, right = wires_in.split(" ")

    if left not in wires or right not in wires:
        q.append(curr)
        continue

    result = -1
    if op == "XOR":
        result = wires[left] ^ wires[right]
    elif op == "OR":
        result = wires[left] | wires[right]
    elif op == "AND":
        result = wires[left] & wires[right]

    wires[out_wire] = result

x_wires, y_wires, z_wires = [], [], []
for wire in wires.keys():
    if "x" in wire:
        x_wires.append(wire)
    elif "y" in wire:
        y_wires.append(wire)
    elif "z" in wire:
        z_wires.append(wire)

x_wires.sort(reverse=True)
y_wires.sort(reverse=True)
z_wires.sort(reverse=True)
x_digits = [str(wires[w]) for w in x_wires]
y_digits = [str(wires[w]) for w in y_wires]
z_digits = [str(wires[w]) for w in z_wires]
x_dec = int("".join(x_digits), 2)
y_dec = int("".join(y_digits), 2)
z_dec = int("".join(z_digits), 2)

part_one = z_dec

print("Part One:", part_one)

# part two analysis for manual solving
print()
print("Part Two Analysis")
width = len(z_digits)
expected = f"{x_dec + y_dec:0{width}b}"[::-1]
actual = f"{z_dec:0{width}b}"[::-1]

# z wires that must swap
must_swap = []
for line in out_vals:
    wires_in, out_wire = line.split(" -> ")
    left, op, right = wires_in.split(" ")
    if out_wire.startswith("z"):
        if out_wire != f"z{width - 1}" and op != "XOR":
            must_swap.append(out_wire)
        elif out_wire == f"z{width - 1}" and op != "OR":
            must_swap.append(out_wire)
print("Must swap:")
print(", ".join(must_swap))

# z wires where something is wrong
wrong_z = []
for i, digit in enumerate(expected):
    if digit != actual[i]:
        wrong_z.append(f"z{i:02}")
print("Investigate:")
print(", ".join(wrong_z))
