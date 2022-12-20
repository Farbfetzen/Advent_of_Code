# https://adventofcode.com/2019/day/16

from itertools import accumulate, chain, cycle, islice, repeat

from src.util.types import Data, Solution


def prepare_data(data: str) -> list[int]:
    return [int(x) for x in data]


def part_1(signal: list[int]) -> str:
    base_pattern = (0, 1, 0, -1)
    length = len(signal)
    patterns = []
    for i in range(1, length + 1):
        pattern = cycle(chain.from_iterable(repeat(x, i) for x in base_pattern))
        next(pattern)
        patterns.append(tuple(islice(pattern, length)))
    for _ in range(100):
        output = [0] * length
        for i, pattern in enumerate(patterns):
            n = sum(x * pattern[j] for j, x in enumerate(signal))
            output[i] = abs(n) % 10
        signal = output
    return "".join(str(x) for x in signal[:8])


def part_2(signal: list[int]) -> str:
    # Took me a long time, but then I saw the light with the help of this thread:
    # https://www.reddit.com/r/adventofcode/comments/ebf5cy/2019_day_16_part_2_understanding_how_to_come_up
    offset = int("".join(str(x) for x in signal[:7]))
    # Only works if the message is in the second half of the signal.
    assert offset >= len(signal) * 5_000
    signal = list(islice(chain.from_iterable(repeat(signal, 10_000)), offset, None))
    signal.reverse()
    for _ in range(100):
        signal = [x % 10 for x in accumulate(signal)]
    return "".join(str(x) for x in signal[-1:-9:-1])


def solve(data: Data) -> Solution:
    solution = Solution()
    for sample in data.samples[:3]:
        sample_data = prepare_data(sample)
        solution.samples_part_1.append(part_1(sample_data))
    for sample in data.samples[3:]:
        sample_data = prepare_data(sample)
        solution.samples_part_2.append(part_2(sample_data))

    challenge_data = prepare_data(data.input)
    solution.part_1 = part_1(challenge_data)
    solution.part_2 = part_2(challenge_data)
    return solution
