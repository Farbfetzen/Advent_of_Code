# https://adventofcode.com/2021/day/6


SAMPLE_PATH = "../../input/2021-06-sample.txt"
INPUT_PATH = "../../input/2021-06-input.txt"


def get_data(filename):
    with open(filename) as file:
        return [int(x) for x in file.read().split(",")]


def simulate(fish_ages):
    count = [fish_ages.count(i) for i in range(9)]
    result_at_day_80 = 0
    for day in range(1, 256+1):
        zeros = count[0]
        count[:-1] = count[1:]
        count[6] += zeros
        count[8] = zeros
        if day == 80:
            result_at_day_80 = sum(count)
    return result_at_day_80, sum(count)


if __name__ == "__main__":
    sample_data = get_data(SAMPLE_PATH)
    sample_part_1, sample_part_2 = simulate(sample_data)
    assert sample_part_1 == 5934
    assert sample_part_2 == 26984457539

    challenge_data = get_data(INPUT_PATH)
    challenge_part_1, challenge_part_2 = simulate(challenge_data)
    print(challenge_part_1)  # 372300
    print(challenge_part_2)  # 1675781200288
