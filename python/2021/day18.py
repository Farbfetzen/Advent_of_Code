# https://adventofcode.com/2021/day/18


import copy
import itertools
import math


SAMPLE_PATH = "../../input/2021-18-sample.txt"
INPUT_PATH = "../../input/2021-18-input.txt"


class SnailfishNumber:

    def __init__(self, value=None, parent=None, left=None, right=None):
        self.value = value
        self.parent = parent
        self.left = left
        self.right = right

    def __repr__(self):
        if self.value is None:
            return f"[{repr(self.left)},{repr(self.right)}]"
        else:
            return repr(self.value)

    @property
    def magnitude(self):
        if self.value is None:
            return 3 * self.left.magnitude + 2 * self.right.magnitude
        return self.value


def get_data(filename):
    with open(filename) as file:
        data = file.read().splitlines()
    return [construct_number(line) for line in data]


def construct_number(input_str):
    root = SnailfishNumber()
    current = root
    for char in input_str:
        if char == "[":
            current.left = SnailfishNumber(parent=current)
            current.right = SnailfishNumber(parent=current)
            current = current.left
        elif char == "]":
            current = current.parent
        elif char == ",":
            current = current.parent.right
        else:
            # The rest are single digits.
            current.value = int(char)
    return root


def add(left, right):
    left = copy.deepcopy(left)
    right = copy.deepcopy(right)
    number = SnailfishNumber(left=left, right=right)
    left.parent = number
    right.parent = number
    while True:
        number_to_explode = find_explosion_candidate(number)
        if number_to_explode is not None:
            explode(number_to_explode)
        else:
            number_to_split = find_split_candidate(number)
            if number_to_split is not None:
                split(number_to_split)
            else:
                break
    return number


def find_explosion_candidate(number, depth=0):
    if number.value is None:
        if depth == 4:
            return number
        depth += 1
        return find_explosion_candidate(number.left, depth) or \
            find_explosion_candidate(number.right, depth)


def find_split_candidate(number, depth=0):
    if number.value is None:
        depth += 1
        return find_split_candidate(number.left, depth) or \
            find_split_candidate(number.right, depth)
    if number.value >= 10:
        return number


def explode(number):
    # left side:
    current = number
    while current.parent.left == current:
        current = current.parent
        if current.parent is None:
            break
    else:
        current = current.parent.left
        while current.value is None:
            current = current.right
        current.value += number.left.value

    # right side:
    current = number
    while current.parent.right == current:
        current = current.parent
        if current.parent is None:
            break
    else:
        current = current.parent.right
        while current.value is None:
            current = current.left
        current.value += number.right.value

    number.left = None
    number.right = None
    number.value = 0


def split(number):
    half = number.value / 2
    number.left = SnailfishNumber(value=math.floor(half), parent=number)
    number.right = SnailfishNumber(value=math.ceil(half), parent=number)
    number.value = None


def part_1(numbers):
    current = numbers[0]
    for next_number in numbers[1:]:
        current = add(current, next_number)
    return current.magnitude


def part_2(numbers):
    max_magnitude = 0
    for a, b in itertools.permutations(numbers, 2):
        max_magnitude = max(add(a, b).magnitude, max_magnitude)
    return max_magnitude


if __name__ == "__main__":
    sample_data = get_data(SAMPLE_PATH)
    assert part_1(sample_data) == 4140
    assert part_2(sample_data) == 3993

    challenge_data = get_data(INPUT_PATH)
    print(part_1(challenge_data))  # 3987
    print(part_2(challenge_data))  # 4500
