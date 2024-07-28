# https://adventofcode.com/2019/day/6

from src.util.types import Data, Solution


def prepare_data(data: str) -> dict[str, str]:
    orbits = {}
    for line in data.splitlines():
        a, b = line.split(")")
        orbits[b] = a
    return orbits


def find_com(orbits: dict[str, str], start: str) -> list[str]:
    path = []
    position = orbits[start]
    while position != "COM":
        path.append(position)
        position = orbits[position]
    return path


def part_1(orbits: dict[str, str]) -> int:
    total = 0
    for o in orbits:
        total += len(find_com(orbits, o)) + 1
    return total


def part_2(orbits: dict[str, str]) -> int:
    you_to_com = find_com(orbits, "YOU")
    san_to_com = find_com(orbits, "SAN")
    jumps = set(you_to_com).symmetric_difference(san_to_com)
    return len(jumps)


def solve(data: Data) -> Solution:
    solution = Solution()
    sample_data_0 = prepare_data(data.samples[0])
    solution.samples_part_1.append(part_1(sample_data_0))
    sample_data_1 = prepare_data(data.samples[1])
    solution.samples_part_2.append(part_2(sample_data_1))

    challenge_data = prepare_data(data.input)
    solution.part_1 = part_1(challenge_data)
    solution.part_2 = part_2(challenge_data)
    return solution
