import collections
import re


claims = []
with open("day_03_input.txt", "r") as file:
    for line in file.read().splitlines():
        claim = []
        for s in re.split(r"(\d+)", line):
            if s.isdigit():
                claim.append(int(s))
        claims.append(claim)


all_coordinates = {}
for claim in claims:
    ID, left, top, width, height = claim
    claim_xy = []
    for x in range(left+1, left+width+1):
        for y in range(top+1, top+height+1):
            claim_xy.append(str(x)+" "+str(y))
    all_coordinates[ID] = claim_xy

all_coordinates_list = []
for v in all_coordinates.values():
    all_coordinates_list += list(v)

counter_1 = collections.Counter(all_coordinates_list)
counter_2 = collections.Counter(counter_1.values())
if (1 in counter_2):
    del counter_2[1]
print(sum(counter_2.values()))  # part 1


# alternativer Ansatz für part 2:
# 1. Suche dir aus dem counter_1 alle xy aus, die nur einmal vorkommen.
# 2. Suche den claim, der nur aus diesen coordinaten besteht.



# This is horrible nested mess but I'm too tired to fix it right now.
#def foo(coords):
    #IDs = list(coords.keys())
    #while True:
        #ID = IDs.pop()
        #claim = coords.pop(ID)
        #found = False
        #for k, v in coords.items():
            #for xy in claim:
                #if xy in v:
                    #found = True
                    #del coords[k]
                    #IDs.remove(k)
                    #break
            #if found:
                #break
        #if not found:
            #return ID
#print(foo(all_coordinates))


# 1244 ist falsch (zu hoch)
