# https://adventofcode.com/2019/day/8

import matplotlib.pyplot as plt
import numpy as np

from src.util.types import Data, Solution


WIDTH = 25
HEIGHT = 6
PIXELS_PER_LAYER = WIDTH * HEIGHT


def prepare_data(data: str) -> np.ndarray:
    n_layers = len(data) // PIXELS_PER_LAYER
    return np.array([int(i) for i in data]).reshape(n_layers, PIXELS_PER_LAYER)


def part_1(layers: np.ndarray) -> int:
    fewest_0_layer = layers[np.count_nonzero(layers, 1).argmax(), :]
    return (fewest_0_layer == 1).sum() * (fewest_0_layer == 2).sum()


def to_image(layers: np.ndarray) -> np.ndarray:
    return np.apply_along_axis(lambda x: x[np.argmax(x < 2)], 0, layers).reshape(HEIGHT, WIDTH)


def part_2_as_string(layers: np.ndarray) -> str:
    image = to_image(layers)
    image = image.astype(str)
    image[image == "0"] = " "
    image[image == "1"] = "█"
    image = np.apply_along_axis(lambda x: "".join(i for i in x), 1, image)
    return "\n".join(image)


def part_2_as_image(layers: np.ndarray) -> None:
    image = to_image(layers)
    plt.imshow(image, "binary")
    plt.show()


def solve(data: Data) -> Solution:
    solution = Solution()
    challenge_data = prepare_data(data.input)
    solution.part_1 = part_1(challenge_data)
    solution.part_2 = part_2_as_string(challenge_data)
    return solution
