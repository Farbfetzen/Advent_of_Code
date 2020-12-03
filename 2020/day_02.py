# https://adventofcode.com/2020/day/2


from collections import namedtuple


PasswordEntry = namedtuple("password_entry", "min,max,letter,password")


def convert_input(data_str):
    data = []
    for line in data_str.splitlines():
        entry = line.split()
        i, j = entry[0].split("-")
        data.append(PasswordEntry(
            int(i),
            int(j),
            entry[1][0],
            entry[2]
        ))
    return data


def part_1(data):
    return sum(entry.min <= entry.password.count(entry.letter) <= entry.max
               for entry in data)


def part_2(data):
    sum_ = 0
    for entry in data:
        a = entry.password[entry.min - 1] == entry.letter
        b = entry.password[entry.max - 1] == entry.letter
        if a ^ b:
            sum_ += 1
    return sum_


test_input = convert_input("""1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc
""")
assert part_1(test_input) == 2
assert part_2(test_input) == 1


with open("day_02_input.txt", "r") as file:
    password_entries = convert_input(file.read())

print(part_1(password_entries))  # 434
print(part_2(password_entries))  # 509
