# https://adventofcode.com/2020/day/25

# No part 2 on the 25th.

from src.util.types import Data, Solution


def prepare_data(data: str) -> list[int]:
    return [int(x) for x in data.splitlines()]


def part_1(public_keys):
    value = 1
    found = 0
    loop_sizes = [0, 0]
    i = 0
    while True:
        i += 1
        value = (value * 7) % 20201227
        if value in public_keys:
            loop_sizes[public_keys.index(value)] = i
            found += 1
        if found == 2:
            break

    loop_size = min(loop_sizes)  # Save time by using the smaller loop size.
    public_key = public_keys[loop_sizes.index(max(loop_sizes))]
    value = 1
    for _ in range(loop_size):
        value = (value * public_key) % 20201227
    return value


def solve(data: Data) -> Solution:
    solution = Solution()
    sample_data = prepare_data(data.samples[0])
    solution.samples_part_1.append(part_1(sample_data))

    challenge_data = prepare_data(data.input)
    solution.part_1 = part_1(challenge_data)
    solution.part_2 = "No part 2 on day 25. Merry Christmas!"
    return solution
