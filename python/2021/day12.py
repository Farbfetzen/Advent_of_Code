# https://adventofcode.com/2021/day/12


from collections import defaultdict


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


def find_paths(cave_map, single_small_twice):
    complete_paths = []
    # The first element marks the small cave that may be visited twice.
    # Only relevant for part 2.
    queue = [[None, "start"]]
    while queue:
        path = queue.pop()
        for target in cave_map[path[-1]]:
            if target == "end":
                complete_paths.append(path + [target])
            elif target[0].isupper() or target not in path:
                queue.append(path + [target])
            elif single_small_twice and target != "start" and path[0] is None:
                new_path = path + [target]
                new_path[0] = target
                queue.append(new_path)
    return complete_paths


def part_1(cave_map):
    return len(find_paths(cave_map, False))


def part_2(cave_map):
    return len(find_paths(cave_map, True))


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
