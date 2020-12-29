# https://adventofcode.com/2019/day/20


import math


DIRECTIONS = ((1, 0), (0, 1), (0, -1), (-1, 0))


def fix_maze(maze):
    """Fix uneven row lengths caused by the IDE's removal of trailing spaces."""
    max_width = max(len(row) for row in maze)
    for y, row in enumerate(maze):
        maze[y] = row.ljust(max_width, " ")
    return maze


def map_maze(maze):
    """Find all portals and walkable spaces."""
    portals = {}  # = walkable space closest to a portal
    walkable = set()
    maze = fix_maze(maze)
    width = len(maze[0])
    height = len(maze)
    x_outside = {2, width - 3}
    y_outside = {2, height - 3}
    for y, row in enumerate(maze):
        for x, char in enumerate(row):
            if char == ".":
                walkable.add((x, y))
    # Search for portals among the walkable positions.
    for x, y in walkable:
        label = ""
        for dx, dy in DIRECTIONS:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < width and 0 <= ny < height:
                char_1 = maze[ny][nx]
                if char_1.isalpha():
                    for dx_, dy_ in DIRECTIONS:
                        char_2 = maze[ny + dy_][nx + dx_]
                        if char_2.isalpha():
                            if dx_ == 1 or dy_ == 1:
                                label = char_1 + char_2
                            else:
                                label = char_2 + char_1
                            break
                    break
        if label:
            side = -1 if x in x_outside or y in y_outside else 1
            portals[(x, y)] = (label, side)
    walkable -= portals.keys()
    return walkable, portals


def map_connections(maze):
    walkable, portals = map_maze(maze)
    connections = {label: {} for label in portals.values()}
    for position, label in portals.items():
        seen = {position}
        queue = [(position, 0)]  # second number is distance
        while queue:
            (x, y), distance = queue.pop()
            distance += 1
            for dx, dy in DIRECTIONS:
                neighbor = (x + dx, y + dy)
                if neighbor not in seen:
                    seen.add(neighbor)
                    if neighbor in walkable:
                        queue.append((neighbor, distance))
                    elif neighbor in portals:
                        other_label = portals[neighbor]
                        dist = connections[label].get(other_label, 0)
                        if distance > dist:
                            connections[label][other_label] = distance
    return connections


def part_1(connections):
    """Use BFS to find all paths and return the shortest."""
    shortest_distance = math.inf
    queue = [([("AA", -1)], -1)]
    while queue:
        # Sort reversed by distance to pop the shortest distance first.
        queue.sort(key=lambda x: x[1], reverse=True)
        path, distance = queue.pop()
        last_portal = path[-1]
        if last_portal[0] == "ZZ":
            return distance
        distance += 1
        for other_portal, other_distance in connections[last_portal].items():
            if other_portal not in path:
                label, side = other_portal
                queue.append((
                    path + [other_portal, (label, -side)],
                    distance + other_distance)
                )
    return shortest_distance


def part_2(connections):
    """Walk through the maze using BFS and return the first path found."""
    # How to detect if there is no path? It could potentially go
    # infinitely many levels deep.

    # last portal, level, distance
    queue = [(("AA", -1), 0, -1)]
    while queue:
        # Sort reversed by distance to pop the shortest distance first.
        queue.sort(key=lambda x: x[2], reverse=True)
        last_portal, level, distance = queue.pop()
        if last_portal[0] == "ZZ":
            return distance
        distance += 1
        for other_portal, other_distance in connections[last_portal].items():
            label, side = other_portal
            new_level = level + side
            # - Prevent going in the same portal on the same level,
            #   because it may be that e.g. ("BC", 1) has a walking
            #   connection to ("BC", -1). Going that route would not make sense.
            # - Do not try to enter "AA".
            # - Outer portals except "ZZ" are only open on level > 0.
            if (label != last_portal[0]
                    and label != "AA"
                    and (label == "ZZ") == (new_level == -1)):
                queue.append((
                    (label, -side),
                    new_level,
                    distance + other_distance
                ))


with open("day_20_sample.txt") as file:
    test_inputs = file.read().split("\n\n")

test_input_1 = test_inputs[0].splitlines()
test_1_connections = map_connections(test_input_1)
assert part_1(test_1_connections) == 23
assert part_2(test_1_connections) == 26

test_input_2 = test_inputs[1].splitlines()
test_2_connections = map_connections(test_input_2)
assert part_1(test_2_connections) == 58
# No path in part 2.

test_input_3 = test_inputs[2].splitlines()
test_3_connections = map_connections(test_input_3)
assert part_2(test_3_connections) == 396


with open("day_20_input.txt") as file:
    challenge_input = file.read().splitlines()
challenge_connections = map_connections(challenge_input)
print(part_1(challenge_connections))  # 422
print(part_2(challenge_connections))  # 5040  (takes about a minute)
