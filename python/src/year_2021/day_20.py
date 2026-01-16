# https://adventofcode.com/2021/day/20

import itertools

from src.util.inputs import Inputs
from src.util.solution import Solution


OFFSETS = tuple(itertools.product((1, 0, -1), repeat=2))


class Solution2021Day20(Solution):

    def solve(self, inputs: Inputs) -> None:
        prepared_input = self.prepare(inputs.samples[0])
        self.sample_results_1.append(self.solve_1(*prepared_input))
        self.sample_results_2.append(self.solve_2(*prepared_input))

        prepared_input = self.prepare(inputs.input)
        self.result_1 = self.solve_1(*prepared_input)
        self.result_2 = self.solve_2(*prepared_input)

    @staticmethod
    def prepare(data: str) -> tuple[list[int], list[list[int]]]:
        algorithm_, image_ = data.split("\n\n")
        algorithm = [int(char == "#") for char in algorithm_]
        image = [[int(char == "#") for char in line] for line in image_.splitlines()]
        return algorithm, image

    def solve_1(self, algorithm: list[int], image: list[list[int]]) -> int:
        return self.count_lit_pixels(self.enhance(algorithm, image, 2))

    def solve_2(self, algorithm: list[int], image: list[list[int]]) -> int:
        return self.count_lit_pixels(self.enhance(algorithm, image, 50))

    def enhance(self, algorithm: list[int], image: list[list[int]], times: int) -> list[list[int]]:
        padding_value = 0
        for _ in range(times):
            assert len(image) == len(image[0])
            image = self.pad_image(image, padding_value)
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

    @staticmethod
    def pad_image(image: list[list[int]], padding_value: int) -> list[list[int]]:
        new_image = [[padding_value] * (len(image[0]) + 2)]
        for row in image:
            new_image.append([padding_value] + row + [padding_value])
        new_image.append(new_image[0][:])
        return new_image

    @staticmethod
    def count_lit_pixels(image: list[list[int]]) -> int:
        return sum(sum(line) for line in image)
