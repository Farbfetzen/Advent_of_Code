# https://adventofcode.com/2021/day/20


import itertools


SAMPLE_PATH = "../../input/2021-20-sample.txt"
INPUT_PATH = "../../input/2021-20-input.txt"
OFFSETS = tuple(itertools.product((1, 0, -1), repeat=2))


def get_data(filename):
    with open(filename) as file:
        algorithm, image = file.read().split("\n\n")
    algorithm = [int(char == "#") for char in algorithm]
    image = [[int(char == "#") for char in line] for line in image.splitlines()]
    return algorithm, image


def enhance(algorithm, image, times):
    padding_value = 0
    for _ in range(times):
        assert len(image) == len(image[0])
        image = pad_image(image, padding_value)
        new_image = [line[:] for line in image]
        for y, x in itertools.product(range(len(image)), repeat=2):
            algorithm_index = 0
            for i, (dy, dx) in enumerate(OFFSETS):
                px = x + dx
                py = y + dy
                if 0 <= px < len(image[0]) and 0 <= py < len(image):
                    pixel = image[py][px]
                else:
                    pixel = padding_value
                algorithm_index += pixel * 2**i
            new_image[y][x] = algorithm[algorithm_index]
        image = new_image
        padding_value = algorithm[0] if padding_value == 0 else algorithm[-1]
    return image


def pad_image(image, value):
    new_image = [[value] * (len(image[0]) + 2)]
    for row in image:
        new_image.append([value] + row + [value])
    new_image.append(new_image[0][:])
    return new_image


def count_lit_pixels(image):
    return sum(sum(line) for line in image)


def part_1(algorithm, image):
    return count_lit_pixels(enhance(algorithm, image, 2))


def part_2(algorithm, image):
    return count_lit_pixels(enhance(algorithm, image, 50))


if __name__ == "__main__":
    sample_data = get_data(SAMPLE_PATH)
    assert part_1(*sample_data) == 35
    assert part_2(*sample_data) == 3351

    challenge_data = get_data(INPUT_PATH)
    print(part_1(*challenge_data))  # 5081
    print(part_2(*challenge_data))  # 15088
