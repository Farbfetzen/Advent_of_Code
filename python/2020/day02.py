# https://adventofcode.com/2020/day/2


from collections import namedtuple


SAMPLE_PATH = "../../input/2020-02-sample.txt"
INPUT_PATH = "../../input/2020-02-input.txt"

PasswordEntry = namedtuple("password_data", "min,max,letter,password")


def get_data(filename):
    with open(filename) as file:
        data = file.read().strip().splitlines()
    converted_data = []
    for line in data:
        entry = line.split()
        i, j = entry[0].split("-")
        converted_data.append(PasswordEntry(
            int(i),
            int(j),
            entry[1][0],
            entry[2]
        ))
    return converted_data


def part_1(password_data):
    sum_valid = 0
    for password_entry in password_data:
        letter_count = password_entry.password.count(password_entry.letter)
        if password_entry.min <= letter_count <= password_entry.max:
            sum_valid += 1
    return sum_valid


def part_2(password_data):
    sum_valid = 0
    for password_entry in password_data:
        a = password_entry.password[password_entry.min - 1] == password_entry.letter
        b = password_entry.password[password_entry.max - 1] == password_entry.letter
        if a != b:
            sum_valid += 1
    return sum_valid


if __name__ == "__main__":
    sample_data = get_data(SAMPLE_PATH)
    assert part_1(sample_data) == 2
    assert part_2(sample_data) == 1

    challenge_data = get_data(INPUT_PATH)
    print(part_1(challenge_data))  # 434
    print(part_2(challenge_data))  # 509
