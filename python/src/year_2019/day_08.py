# https://adventofcode.com/2019/day/8

import matplotlib.pyplot as plt
import numpy

from src.util.inputs import Inputs
from src.util.solution import Solution


class Solution2019Day08(Solution):

    def solve(self, inputs: Inputs) -> None:
        layers = self.prepare(inputs.samples[0], 3 * 2)
        self.sample_results_1.append(self.solve_1(layers))
        layers = self.prepare(inputs.samples[1], 2 * 2)
        self.sample_results_2.append(self.solve_2_as_string(layers, 2, 2))

        layers = self.prepare(inputs.input, 25 * 6)
        self.result_1 = self.solve_1(layers)
        self.result_2 = self.solve_2_as_string(layers, 25, 6)

    @staticmethod
    def prepare(data: str, pixels_per_layer: int) -> numpy.ndarray:
        n_layers = len(data) // pixels_per_layer
        return numpy.array([int(i) for i in data]).reshape(n_layers, pixels_per_layer)

    @staticmethod
    def solve_1(layers: numpy.ndarray) -> int:
        fewest_0_layer = layers[numpy.count_nonzero(layers, 1).argmax(), :]
        count_1: int = (fewest_0_layer == 1).sum()
        count_2: int = (fewest_0_layer == 2).sum()
        return count_1 * count_2

    @staticmethod
    def to_image(layers: numpy.ndarray, width: int, height: int) -> numpy.ndarray:
        return numpy.apply_along_axis(lambda x: x[numpy.argmax(x < 2)], 0, layers).reshape(height, width)

    def solve_2_as_string(self, layers: numpy.ndarray, width: int, height: int) -> str:
        image = self.to_image(layers, width, height)
        image = image.astype(str)
        image[image == "0"] = " "
        image[image == "1"] = "█"
        image = numpy.apply_along_axis(lambda x: "".join(x), 1, image)
        return "\n".join(image)

    def solve_2_as_image(self, layers: numpy.ndarray, width: int, height: int) -> None:
        image = self.to_image(layers, width, height)
        plt.imshow(image, "binary")
        plt.show()
