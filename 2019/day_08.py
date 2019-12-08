# https://adventofcode.com/2019/day/8


import math
import collections


with open("day_08_input.txt") as file:
    transmission = [int(i) for i in file.read().strip()]
width = 25
height = 6
pixels_per_layer = width * height
assert len(transmission) % pixels_per_layer == 0
layers = []
while transmission:
    layers.append(transmission[:pixels_per_layer])
    del transmission[:pixels_per_layer]

# part 1:
n_zero = math.inf
n_zero_current = 0
layer_with_fewest_0 = []
for layer in layers:
    n_zero_current = len([i for i in layer if i == 0])
    if n_zero_current < n_zero:
        n_zero = n_zero_current
        layer_with_fewest_0 = layer
c = collections.Counter(layer_with_fewest_0)
print(c[1] * c[2])  # 2520

# part 2:
visible = []
for i in range(pixels_per_layer):
    for layer in layers:
        color = layer[i]
        if color < 2:
            visible.append(color)
            break
image = ""
x = 0
for y in range(height):
    for pixel in (i for i in visible[x:x+width]):
        if pixel == 0:
            image += " "
        elif pixel == 1:
            image += "#"
    image += "\n"
    x += width
print(image)  # LEGJY
