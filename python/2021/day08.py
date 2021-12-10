# https://adventofcode.com/2021/day/8


SAMPLE_PATH = "../../input/2021-08-sample.txt"
INPUT_PATH = "../../input/2021-08-input.txt"
LENGTH_TO_DIGIT = {
    2: (1, ),
    3: (7, ),
    4: (4, ),
    5: (2, 3, 5),
    6: (0, 6, 9),
    7: (8, )
}


def get_data(filename):
    with open(filename) as file:
        lines = file.read().splitlines()
    data = []
    for line in lines:
        patterns, output = line.split("|")
        patterns = [frozenset(pattern) for pattern in patterns.split()]
        output = [frozenset(output) for output in output.split()]
        data.append((patterns, output))
    return data


def part_1(data):
    unique_lengths = {2, 3, 4, 7}
    result = 0
    for _, output in data:
        for signals in output:
            if len(signals) in unique_lengths:
                result += 1
    return result


def determine_mapping(patterns):
    candidates = [[] for _ in range(10)]
    for pattern in patterns:
        for digit in LENGTH_TO_DIGIT[len(pattern)]:
            candidates[digit].append(pattern)

    # 1 and 4 have unique numbers of segments.
    d1 = candidates[1][0]
    d4 = candidates[4][0]

    # 2, 5, and 6 must not contain both segments of 1.
    for i in (2, 5, 6):
        candidates[i] = [c for c in candidates[i] if not d1.issubset(c)]

    # The intersection of 5 and 4 must have length 3.
    candidates[5] = [c for c in candidates[5] if len(d4.intersection(c)) == 3]

    # The intersection of 2 and 4 must have length 2.
    candidates[2] = [c for c in candidates[2] if len(d4.intersection(c)) == 2]

    # The intersection of 9 and 4 must have length 4.
    candidates[9] = [c for c in candidates[9] if len(d4.intersection(c)) == 4]

    # The intersection of 3 and 1 must have length 2.
    candidates[3] = [c for c in candidates[3] if len(d1.intersection(c)) == 2]

    # The intersection of 0 and 1 must have length 2 and between 0 and 4 is must have length 3.
    candidates[0] = [c for c in candidates[0]
                     if len(d1.intersection(c)) == 2 and len(d4.intersection(c)) == 3]

    assert all(len(c) == 1 for c in candidates)
    return {c[0]: i for i, c in enumerate(candidates)}


def part_2(data):
    result = 0
    for patterns, output in data:
        pattern_to_numbers = determine_mapping(patterns)
        for i, magnitude in enumerate((1000, 100, 10, 1)):
            result += pattern_to_numbers[output[i]] * magnitude
    return result


if __name__ == "__main__":
    sample_data = get_data(SAMPLE_PATH)
    assert part_1(sample_data) == 26
    assert part_2(sample_data) == 61229

    challenge_data = get_data(INPUT_PATH)
    print(part_1(challenge_data))  # 352
    print(part_2(challenge_data))  # 936117
