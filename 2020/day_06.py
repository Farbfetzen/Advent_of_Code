# https://adventofcode.com/2020/day/6


with open("day_06_input.txt") as file:
    groups = file.read().split("\n\n")
    groups = [group.splitlines() for group in groups]

# part 1
group_sets = [set("".join(person for person in group)) for group in groups]
print(sum(len(gs) for gs in group_sets))  # 6686

# part 2
person_sets = [[set(x) for x in group] for group in groups]
print(sum(len(set.intersection(*ps)) for ps in person_sets))  # 3476
