# https://adventofcode.com/2020/day/6


# Minified solution because why not.

with open("day_06_input.txt") as file:
    groups = [[set(person) for person in group.splitlines()]
              for group in file.read().split("\n\n")]

# part 1
print(sum(len(set.union(*group)) for group in groups))  # 6686

# part 2
print(sum(len(set.intersection(*group)) for group in groups))  # 3476
