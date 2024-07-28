# https://adventofcode.com/2021/day/20

from itertools import product

from src.util.types import Data, Solution


OFFSETS = tuple(product((1, 0, -1), repeat=2))


def prepare_data(data: str) -> tuple[list[int], list[list[int]]]:
    algorithm_, image_ = data.split("\n\n")
    algorithm = [int(char == "#") for char in algorithm_]
    image = [[int(char == "#") for char in line] for line in image_.splitlines()]
    return algorithm, image


def enhance(algorithm, image, times):
    padding_value = 0
    for _ in range(times):
        assert len(image) == len(image[0])
        image = pad_image(image, padding_value)
        new_image = [line[:] for line in image]
        for y, x in product(range(len(image)), repeat=2):
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


def solve(data: Data) -> Solution:
    solution = Solution()
    sample_data = prepare_data(data.samples[0])
    solution.samples_part_1.append(part_1(*sample_data))
    solution.samples_part_2.append(part_2(*sample_data))

    challenge_data = prepare_data(data.input)
    solution.part_1 = part_1(*challenge_data)
    solution.part_2 = part_2(*challenge_data)
    return solution
