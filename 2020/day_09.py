# https://adventofcode.com/2020/day/9


def part_1(numbers, pre_len):
    for i, n in enumerate(numbers[pre_len:]):
        preamble = numbers[i:(pre_len + i)]
        found_match = False
        for j, a in enumerate(preamble[:-1]):
            for b in preamble[(j + 1):]:
                if a + b == n:
                    found_match = True
                    break
            if found_match:
                break
        if not found_match:
            return n


def part_2(numbers, target):
    for i, a in enumerate(numbers):
        numbers_slice = [a]
        sum_ = a
        for b in numbers[(i + 1):]:
            sum_ += b
            numbers_slice.append(b)
            if sum_ == target:
                return min(numbers_slice) + max(numbers_slice)
            if sum_ > target:
                break


test_input = """35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576
"""
test_input = [int(i) for i in test_input.splitlines()]
assert part_1(test_input, 5) == 127
assert part_2(test_input, 127) == 62

with open("day_09_input.txt") as file:
    challenge_input = [int(i) for i in file.readlines()]
invalid_number = part_1(challenge_input, 25)
print(invalid_number)  # 21806024
print(part_2(challenge_input, invalid_number))  # 2986195
