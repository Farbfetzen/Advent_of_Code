# https://adventofcode.com/2020/day/9


def get_data(filename):
    with open(filename) as file:
        return [int(i) for i in file.readlines()]


def valid(preamble, n):
    for i, a in enumerate(preamble[:-1]):
        for b in preamble[(i + 1):]:
            if a + b == n:
                return True
    return False


def part_1(numbers, pre_len):
    for i, n in enumerate(numbers[pre_len:]):
        if not valid(numbers[i:(pre_len + i)], n):
            return n


def part_2(numbers, target):
    for i in range(len(numbers)):
        for j in range(i + 2, len(numbers)):
            numbers_slice = numbers[i:j]
            sum_ = sum(numbers_slice)
            if sum_ == target:
                return min(numbers_slice) + max(numbers_slice)
            if sum_ > target:
                break


sample_data = get_data("day_09_sample.txt")
challenge_data = get_data("day_09_input.txt")

if __name__ == "__main__":
    assert part_1(sample_data, 5) == 127
    assert part_2(sample_data, 127) == 62

    invalid_number = part_1(challenge_data, 25)
    print(invalid_number)  # 21806024
    print(part_2(challenge_data, invalid_number))  # 2986195
