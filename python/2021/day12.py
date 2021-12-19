# https://adventofcode.com/2021/day/12


from collections import defaultdict
from functools import cache


SAMPLE_PATH = "../../input/2021-12-sample.txt"
INPUT_PATH = "../../input/2021-12-input.txt"


def get_data(filename):
    with open(filename) as file:
        data = file.read().split("\n\n")
    cave_maps = []
    for d in data:
        cave_map = defaultdict(list)
        for line in d.splitlines():
            a, b = line.split("-")
            cave_map[a].append(b)
            cave_map[b].append(a)
        cave_maps.append(cave_map)
    return cave_maps


def count_paths(cave_map, single_small_twice):
    # Use functools.cache to eliminate unnecessary recursive calls.
    @cache
    def count_next_paths(origin, seen, twice):
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


def part_1(cave_map):
    return count_paths(cave_map, False)


def part_2(cave_map):
    return count_paths(cave_map, True)


if __name__ == "__main__":
    sample_data = get_data(SAMPLE_PATH)
    assert part_1(sample_data[0]) == 10
    assert part_1(sample_data[1]) == 19
    assert part_1(sample_data[2]) == 226
    assert part_2(sample_data[0]) == 36
    assert part_2(sample_data[1]) == 103
    assert part_2(sample_data[2]) == 3509

    challenge_data = get_data(INPUT_PATH)[0]
    print(part_1(challenge_data))  # 5920
    print(part_2(challenge_data))  # 155477
