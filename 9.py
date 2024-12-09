#!/usr/bin/env python3

myfile = open("9.in", "r")
lines = myfile.read().strip().splitlines()
myfile.close()

disk_map = lines[0]


def compact(files, spaces):
    for f in reversed(files):
        file_pos, file_size, _ = f
        for space in spaces:
            space_pos, space_size, _ = space
            if space_pos > file_pos:
                break
            if space_size >= file_size:
                # move file to start at free space start
                f[0] = space_pos
                # move free space to start at file end
                space[0] += file_size
                # reduce free space size
                space[1] -= file_size
                break


start_pos = 0
split_files, block_files = [], []
spaces_for_split, spaces_for_block = [], []
for i, c in enumerate(disk_map):
    is_file = i % 2 == 0

    size = int(c)

    if is_file:
        block_files.append([start_pos, size, str(i // 2)])
        for offset in range(size):
            split_files.append([start_pos + offset, 1, str(i // 2)])
    else:
        spaces_for_split.append([start_pos, size, "."])
        spaces_for_block.append([start_pos, size, "."])

    start_pos += size

compact(split_files, spaces_for_split)
compact(block_files, spaces_for_block)

part_one = 0
for pos, size, id in sorted(split_files, key=lambda x: x[0]):
    for x in range(pos, pos + size):
        part_one += int(id) * x

part_two = 0
for pos, size, id in sorted(block_files, key=lambda x: x[0]):
    for x in range(pos, pos + size):
        part_two += int(id) * x

print("Part One:", part_one)
print("Part Two:", part_two)
