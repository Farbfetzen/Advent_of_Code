# https://adventofcode.com/2021/day/13


from collections import namedtuple


SAMPLE_PATH = "../../input/2021-13-sample.txt"
INPUT_PATH = "../../input/2021-13-input.txt"
Fold = namedtuple("Fold", ("index", "value"))
Point = namedtuple("Point", ("x", "y"))


def get_data(filename):
    with open(filename) as file:
        top, bottom = file.read().split("\n\n")
    points = set()
    for line in top.splitlines():
        x, y = line.split(",")
        points.add(Point(int(x), int(y)))
    folds = []
    for line in bottom.splitlines():
        along, value = line.split("=")
        fold = Fold(along[-1] == "y", int(value))
        folds.append(fold)
    return points, folds


def fold_once(points, fold):
    new_points = set()
    for point in points:
        if point[fold.index] > fold.value:
            p = list(point)
            p[fold.index] = fold.value - (point[fold.index] - fold.value)
            point = Point(*p)
        new_points.add(point)
    return new_points


def part_1(points, folds):
    points = fold_once(points, folds[0])
    return len(points)


def part_2(points, folds):
    for fold in folds:
        points = fold_once(points, fold)
    len_horizontal = max(points, key=lambda p: p.x).x + 1
    len_vertical = max(points, key=lambda p: p.y).y + 1
    code = [[" "] * len_horizontal for _ in range(len_vertical)]
    for point in points:
        code[point.y][point.x] = "█"
    return "\n".join("".join(line) for line in code)


if __name__ == "__main__":
    sample_data = get_data(SAMPLE_PATH)
    assert part_1(*sample_data) == 17
    assert part_2(*sample_data) == (
        "█████\n"
        "█   █\n"
        "█   █\n"
        "█   █\n"
        "█████"
    )

    challenge_data = get_data(INPUT_PATH)
    print(part_1(*challenge_data))  # 807
    print(part_2(*challenge_data))  # LGHEGUEJ
