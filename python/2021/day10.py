# https://adventofcode.com/2021/day/10


from statistics import median


SAMPLE_PATH = "../../input/2021-10-sample.txt"
INPUT_PATH = "../../input/2021-10-input.txt"
PAIRS = {")": "(", "]": "[", "}": "{", ">": "<"}
VALUES = {")": 3, "]": 57, "}": 1197, ">": 25137, "(": 1, "[": 2, "{": 3, "<": 4}


def get_data(filename):
    with open(filename) as file:
        return file.read().splitlines()


def get_scores(data):
    part_1_score = 0
    part_2_scores = []
    for line in data:
        autocomplete_score = 0
        stack = []
        for character in line:
            if character in PAIRS:
                opening = stack.pop()
                if opening != PAIRS[character]:
                    # Line is corrupted.
                    part_1_score += VALUES[character]
                    break
            else:
                stack.append(character)
        else:
            # Line is not corrupted and therefore incomplete.
            while stack:
                autocomplete_score = autocomplete_score * 5 + VALUES[stack.pop()]
            part_2_scores.append(autocomplete_score)
    part_2_score = median(part_2_scores)
    return part_1_score, part_2_score


if __name__ == "__main__":
    sample_data = get_data(SAMPLE_PATH)
    sample_part_1, sample_part_2 = get_scores(sample_data)
    assert sample_part_1 == 26397
    assert sample_part_2 == 288957

    challenge_data = get_data(INPUT_PATH)
    challenge_part_1, challenge_part_2 = get_scores(challenge_data)
    print(challenge_part_1)  # 362271
    print(challenge_part_2)  # 1698395182
