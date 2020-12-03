# https://adventofcode.com/2020/day/1


def part_1(data):
    for i, x in enumerate(data):
        y = 2020 - x
        if y in data[(i+1):]:
            return x * y


def part_2(data):
    for i, x in enumerate(data):
        for j, y in enumerate(data[(i+1):]):
            z = 2020 - x - y
            if z in data[(i+j):]:
                return x * y * z


test_data = (1721, 979, 366, 299, 675, 1456)
assert part_1(test_data) == 514579
assert part_2(test_data) == 241861950


with open("day_01_input.txt", "r") as file:
    expenses = [int(i) for i in file.read().splitlines()]

print(part_1(expenses))  # 436404
print(part_2(expenses))  # 274879808
