# https://adventofcode.com/2018/day/1


with open("day_01_input.txt", "r") as file:
    changes = [int(i) for i in file.read().splitlines()]


# part 1
print(sum(changes))


# part 2
frequency = 0
i = 0
seen = set()
while True:
    for change in changes:
        if frequency in seen:
            break
        seen.add(frequency)
        frequency += change
    else:
        continue
    break
print(frequency)
