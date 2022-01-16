# https://adventofcode.com/2019/day/8


import matplotlib.pyplot as plt
import numpy as np


INPUT_PATH = "../../input/2019-08-input.txt"
WIDTH = 25
HEIGHT = 6
PIXELS_PER_LAYER = WIDTH * HEIGHT


def get_data(filename):
    with open(filename) as file:
        data = [int(i) for i in file.read().strip()]
    n_layers = len(data) // PIXELS_PER_LAYER
    return np.array(data).reshape(n_layers, PIXELS_PER_LAYER)


def part_1(layers_):
    fewest_0_layer = layers_[np.count_nonzero(layers_, 1).argmax(), :]
    return (fewest_0_layer == 1).sum() * (fewest_0_layer == 2).sum()


def to_image(layers):
    return np.apply_along_axis(lambda x: x[np.argmax(x < 2)], 0, layers).reshape(HEIGHT, WIDTH)


def part_2_as_string(layers):
    image = to_image(layers)
    image = image.astype(str)
    image[image == "0"] = " "
    image[image == "1"] = "█"
    image = np.apply_along_axis(lambda x: "".join(i for i in x), 1, image)
    image = "\n".join(image)
    return image


def part_2_as_image(layers):
    image = to_image(layers)
    plt.imshow(image, "binary")
    plt.show()


if __name__ == "__main__":
    challenge_data = get_data(INPUT_PATH)
    print(part_1(challenge_data))  # 2520
    print(part_2_as_string(challenge_data))  # LEGJY
    # part_2_as_image(challenge_data)
