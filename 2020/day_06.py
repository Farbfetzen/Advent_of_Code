# https://adventofcode.com/2020/day/6

# Unnecessarily compressed solution because why not.


groups = [[set(person) for person in group.splitlines()]
          for group in open("day_06_input.txt").read().split("\n\n")]

# part 1
print(sum(len(set.union(*group)) for group in groups))  # 6686

# part 2
print(sum(len(set.intersection(*group)) for group in groups))  # 3476
