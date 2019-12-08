# https://adventofcode.com/2019/day/8


import numpy as np
from matplotlib import pyplot as plt


with open("day_08_input.txt") as file:
    transmission = [int(i) for i in file.read().strip()]
width = 25
height = 6
pixels_per_layer = width * height
assert len(transmission) % pixels_per_layer == 0
n_layers = len(transmission) // pixels_per_layer
layers = np.array(transmission).reshape(n_layers, pixels_per_layer)
# each row is a layer

# part 1:
fewest_0_layer = layers[np.count_nonzero(layers, 1).argmax(), :]
print((fewest_0_layer == 1).sum() * (fewest_0_layer == 2).sum())  # 2520

# part 2 as a console printout and an image:
image = np.apply_along_axis(lambda x: x[np.argmax(x < 2)], 0, layers)
image = image.reshape(height, width)
plt.imshow(image, "binary")
plt.show()  # LEGJY

# alternatively as a console printout:
# image = image.astype(str)
# image[image == "0"] = " "
# image[image == "1"] = "#"
# image = np.apply_along_axis(lambda x: "".join(i for i in x), 1, image)
# image = "\n".join(image)
# print(image)  # LEGJY
