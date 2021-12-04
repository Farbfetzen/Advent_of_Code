# https://adventofcode.com/2018/day/3


import collections
import re


with open("../../input/2018-03-input.txt") as file:
    claims = []
    pattern = re.compile(r"(\d+)")
    for line in file.read().splitlines():
        claim = []
        for s in pattern.split(line):
            if s.isdigit():
                claim.append(int(s))
        claims.append(claim)


all_coordinates = {}
all_coordinates_list = []
for claim in claims:
    ID, left, top, width, height = claim
    claim_xy = []
    for x in range(left+1, left+width+1):
        for y in range(top+1, top+height+1):
            claim_xy.append(str(x)+" "+str(y))
    all_coordinates[ID] = claim_xy
    all_coordinates_list += claim_xy

counter_1 = collections.Counter(all_coordinates_list)
counter_2 = collections.Counter(counter_1.values())
if 1 in counter_2:
    del counter_2[1]
print(sum(counter_2.values()))  # part 1: 104126

unique = {k for k, v in counter_1.items() if v == 1}
for ID, claim in all_coordinates.items():
    if set(claim).issubset(unique):
        break
print(ID)  # part 2: 695
