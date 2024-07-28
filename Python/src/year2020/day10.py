# https://adventofcode.com/2020/day/10

from src.util.types import Data, Solution


def prepare_data(data: str) -> list[int]:
    return [int(x) for x in data.splitlines()]


def part_1(adapters):
    adapters.append(0)
    adapters.sort()
    adapters.append(adapters[-1] + 3)
    differences = [adapters[i + 1] - x for i, x in enumerate(adapters[:-1])]
    return differences.count(1) * (differences.count(3))


def part_2(adapters):
    # Requires that part_1() ran before because the adapters must be sorted
    # and they must include 0.
    possibilities = {adapters[-1]: 1}
    for a in adapters[-2::-1]:
        possibilities[a] = sum(possibilities.get(x, 0) for x in (a+1, a+2, a+3))
    return possibilities[0]


def solve(data: Data) -> Solution:
    solution = Solution()
    for i in range(2):
        sample_data = prepare_data(data.samples[i])
        solution.samples_part_1.append(part_1(sample_data))
        solution.samples_part_2.append(part_2(sample_data))

    challenge_data = prepare_data(data.input)
    solution.part_1 = part_1(challenge_data)
    solution.part_2 = part_2(challenge_data)
    return solution
