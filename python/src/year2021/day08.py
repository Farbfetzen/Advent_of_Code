# https://adventofcode.com/2021/day/8

from src.util.types import Data, Solution


LENGTH_TO_DIGIT = {
    2: (1, ),
    3: (7, ),
    4: (4, ),
    5: (2, 3, 5),
    6: (0, 6, 9),
    7: (8, )
}


def prepare_data(data: str) -> tuple[list[list[frozenset]], list[list[frozenset]]]:
    all_patterns = []
    all_outputs = []
    for line in data.splitlines():
        patterns, outputs = line.split("|")
        all_patterns.append([frozenset(pattern) for pattern in patterns.split()])
        all_outputs.append([frozenset(output) for output in outputs.split()])
    return all_patterns, all_outputs


def part_1(all_outputs: list[list[frozenset]]) -> int:
    unique_lengths = {2, 3, 4, 7}
    result = 0
    for outputs in all_outputs:
        for signals in outputs:
            if len(signals) in unique_lengths:
                result += 1
    return result


def determine_mapping(patterns: list[frozenset]) -> dict[frozenset, int]:
    candidates: list[list[frozenset]] = [[] for _ in range(10)]
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


def part_2(all_patterns: list[list[frozenset]], all_outputs: list[list[frozenset]]) -> int:
    result = 0
    for patterns, outputs in zip(all_patterns, all_outputs):
        pattern_to_numbers = determine_mapping(patterns)
        for i, magnitude in enumerate((1000, 100, 10, 1)):
            result += pattern_to_numbers[outputs[i]] * magnitude
    return result


def solve(data: Data) -> Solution:
    solution = Solution()
    sample_patterns, sample_outputs = prepare_data(data.samples[0])
    solution.samples_part_1.append(part_1(sample_outputs))
    solution.samples_part_2.append(part_2(sample_patterns, sample_outputs))

    challenge_patterns, challenge_outputs = prepare_data(data.input)
    solution.part_1 = part_1(challenge_outputs)
    solution.part_2 = part_2(challenge_patterns, challenge_outputs)
    return solution
