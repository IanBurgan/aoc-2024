#!/usr/bin/env python3

from collections import defaultdict
from itertools import combinations

myfile = open("23.in", "r")
lines = myfile.read().strip().splitlines()
myfile.close()

conns = defaultdict(set)

part_one = 0
part_two = ""

for line in lines:
    a, b = line.split("-")
    conns[a].add(b)
    conns[b].add(a)


maximum_clique = set()


def bron_kerbosch(clique, possible, excluded):
    global maximum_clique
    if len(clique) + len(possible) <= len(maximum_clique):
        return

    if not possible and not excluded:
        if len(clique) > len(maximum_clique):
            maximum_clique = clique
        return
    for comp in possible.copy():
        bron_kerbosch(
            clique.union(set([comp])),
            possible.intersection(conns[comp]),
            excluded.intersection(conns[comp]),
        )
        possible.remove(comp)
        excluded.add(comp)


trios = set()
for comp, others in conns.items():
    pairs = combinations(others, 2)
    for a, b in pairs:
        if b in conns[a]:
            trios.add(frozenset([comp, a, b]))

for t in trios:
    if any(x.startswith("t") for x in t):
        part_one += 1

bron_kerbosch(set(), set(conns.keys()), set())
part_two = ",".join(sorted(list(maximum_clique)))

print("Part One:", part_one)
print("Part Two:", part_two)
