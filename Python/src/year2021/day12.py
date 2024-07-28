# https://adventofcode.com/2021/day/12

from collections import defaultdict
from functools import cache

from src.util.types import Data, Solution


def prepare_data(data: str) -> defaultdict[str, list]:
    cave_map = defaultdict(list)
    for line in data.splitlines():
        a, b = line.split("-")
        cave_map[a].append(b)
        cave_map[b].append(a)
    return cave_map


def count_paths(cave_map: defaultdict[str, list], single_small_twice: bool) -> int:
    # Use functools.cache to eliminate unnecessary recursive calls.
    @cache
    def count_next_paths(origin: str, seen: frozenset[str], twice: bool) -> int:
        if origin.islower():
            seen = seen.union({origin})
        n_paths = 0
        for target in cave_map[origin]:
            if target == "end":
                n_paths += 1
            elif target not in seen:
                n_paths += count_next_paths(target, seen, twice)
            elif target != "start" and twice:
                n_paths += count_next_paths(target, seen, False)
        return n_paths
    return count_next_paths("start", frozenset(), single_small_twice)


def part_1(cave_map: defaultdict[str, list]) -> int:
    return count_paths(cave_map, False)


def part_2(cave_map: defaultdict[str, list]) -> int:
    return count_paths(cave_map, True)


def solve(data: Data) -> Solution:
    solutions = Solution()
    for sample in data.samples:
        sample_data = prepare_data(sample)
        solutions.samples_part_1.append(part_1(sample_data))
        solutions.samples_part_2.append(part_2(sample_data))

    challenge_data = prepare_data(data.input)
    solutions.part_1 = part_1(challenge_data)
    solutions.part_2 = part_2(challenge_data)
    return solutions
