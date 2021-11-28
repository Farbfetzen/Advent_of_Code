# https://adventofcode.com/2020/day/10


def get_data(filename):
    with open(filename) as file:
        data = file.read().split("\n\n")
    return [[int(x) for x in block.splitlines()] for block in data]


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


sample_data = get_data("day_10_sample.txt")
challenge_data = get_data("day_10_input.txt")[0]

if __name__ == "__main__":
    assert part_1(sample_data[0]) == 35
    assert part_2(sample_data[0]) == 8
    assert part_1(sample_data[1]) == 220
    assert part_2(sample_data[1]) == 19208

    print(part_1(challenge_data))  # 2760
    print(part_2(challenge_data))  # 13816758796288
