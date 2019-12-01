# https://adventofcode.com/2018/day/2


import collections


with open("day_02_input.txt", "r") as file:
    IDs = file.read().splitlines()


# part 1
sum_2 = 0
sum_3 = 0
for ID in IDs:
    count = collections.Counter(ID)
    sum_2 += 2 in count.values()
    sum_3 += 3 in count.values()
print(sum_2 * sum_3)


# part 2
for i, ID in enumerate(IDs):
    for other_ID in IDs:
        count_differences = 0
        for a, b in zip(ID, other_ID):
            count_differences += a != b
        if count_differences == 1:
            break
    else:
        continue
    break

for x in enumerate(zip(ID, other_ID)):
    i = x[0]
    a, b = x[1]
    if a != b:
        break
print(ID[:i] + ID[i+1:])
