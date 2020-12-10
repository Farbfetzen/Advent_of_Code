# https://adventofcode.com/2020/day/1


def part_1(data):
    # Add numbers to the set after checking to avoid possible error
    # if the data contains 1010.
    data_set = set()
    for x in data:
        y = 2020 - x
        if y in data_set:
            return x * y
        data_set.add(x)


def part_2(data):
    data_set = set()
    for i, x in enumerate(data):
        for j, y in enumerate(data[(i+1):]):
            z = 2020 - x - y
            if z in data_set:
                return x * y * z
            data_set.add(x)
            data_set.add(y)


test_data = (1721, 979, 366, 299, 675, 1456)
assert part_1(test_data) == 514579
assert part_2(test_data) == 241861950


with open("day_01_input.txt") as file:
    expenses = [int(i) for i in file.read().splitlines()]

print(part_1(expenses))  # 436404
print(part_2(expenses))  # 274879808
