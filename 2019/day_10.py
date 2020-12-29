# https://adventofcode.com/2019/day/10


import math
import itertools
import collections


def create_visibility_map(map_str):
    asteroid_map = []
    for y, line in enumerate(map_str.splitlines()):
        for x, char in enumerate(line):
            if char == "#":
                asteroid_map.append((x, y))
    max_visible = 0
    most_unique_slopes = None
    best_position = None
    for a in asteroid_map:
        unique_slopes = {}
        for other in asteroid_map:
            if other == a:
                continue
            slope = (other[0] - a[0], other[1] - a[1])
            slope_gcd = math.gcd(*slope)
            slope = (slope[0] // slope_gcd, slope[1] // slope_gcd)
            if slope in unique_slopes:
                unique_slopes[slope].append(other)
            else:
                unique_slopes[slope] = [other]
        visible = len(unique_slopes)
        if visible > max_visible:
            max_visible = visible
            most_unique_slopes = unique_slopes
            best_position = a
    return most_unique_slopes, best_position


def vaporize(asteroid_map, station_pos):
    for slope in list(asteroid_map.keys()):
        # The laser sshooting tarts straight up and rotates clockwise. This
        # means the angles have to be sorted properly.
        angle = math.atan2(-slope[1], slope[0])
        if angle > math.pi / 2:
            angle -= math.pi * 2
        angle *= -1
        asteroid_map[angle] = asteroid_map.pop(slope)
    for v in asteroid_map.values():
        v.sort(
            key=(lambda x: abs(x[0] - station_pos[0]) + abs(x[1] - station_pos[1])),
            reverse=True
        )
    n = 0
    asteroid_map = collections.OrderedDict(sorted(asteroid_map.items()))
    for asteroids in itertools.cycle(asteroid_map.values()):
        if len(asteroids) > 0:
            n += 1
            vaporized_asteroid = asteroids.pop()
            if n == 200:
                return vaporized_asteroid


with open("day_10_sample.txt") as file:
    test = file.read()
test_visibility = create_visibility_map(test)
assert len(test_visibility[0]) == 210
assert test_visibility[1] == (11, 13)
assert vaporize(*create_visibility_map(test)) == (8, 2)

with open("day_10_input.txt") as file:
    the_map = file.read()
visibility_map, station_position = create_visibility_map(the_map)

# part 1:
print(len(visibility_map))  # 221

# part 2:
a_200 = vaporize(visibility_map, station_position)  # (8, 6)
print(a_200[0] * 100 + a_200[1])  # 806
