# https://adventofcode.com/2019/day/18


# This was a very hard one for me. I finally gave up and looked at the other
# solutions in the solutions thread on Reddit and shamelessly adapted my script
# from this one: https://repl.it/@joningram/AOC-2019#day18.py.
# I use lots of continue to flatten the nested loops with many ifs.


import string


KEYS = string.ascii_lowercase


def find_paths(start_x, start_y, maze):
    """Find the paths from the start to all reachable keys or doors."""
    seen = {(start_x, start_y)}
    # Each item in the queue has x, y, distance so far,
    # and path (keys and doors encountered en route).
    queue = [(start_x, start_y, 0, "")]
    paths = {}
    ignored_symbols = {char for char in ".#@1234"}
    dxy = ((1, 0), (-1, 0), (0, 1), (0, -1))
    for (x, y, distance, path) in queue:
        seen.add((x, y))
        symbol = maze[y][x]
        if distance > 0 and symbol not in ignored_symbols:
            # Found a key or a door.
            # But keep only the keys as dictionary keys because the
            # distances between doors are not relevant.
            if symbol.islower():
                paths[symbol] = (distance, path)
            path += symbol
        # Search for walkable spaces among neigboring positions.
        distance += 1
        for (dx, dy) in dxy:
            nx = x + dx
            ny = y + dy
            if (nx, ny) not in seen and maze[ny][nx] != "#":
                queue.append((nx, ny, distance, path))
    return paths


def build_maze(maze):
    """Find all points of interest on the map and construct all
    paths between them.
    """
    interesting = {k for k in KEYS}
    interesting.update("@1234")
    all_paths = {}
    for y, row in enumerate(maze):
        for x, symbol in enumerate(row):
            if symbol in interesting:
                all_paths[symbol] = find_paths(x, y, maze)
    return all_paths


def part_1(maze):
    all_paths = build_maze(maze)
    keys = frozenset({k for k in all_paths if k in KEYS})
    # info = (current location, collected keys): distance so far
    info = {('@', frozenset()): 0}
    for _ in keys:
        new_info = {}
        for item in info:
            current_position = item[0]
            collected_keys = item[1]
            current_distance = info[item]
            for next_key in keys:
                if next_key in collected_keys:
                    continue
                distance, path = all_paths[current_position][next_key]
                # Is the next key reachable?
                is_reachable = all(
                    (c in collected_keys or c.lower() in collected_keys) for c in path
                )
                if not is_reachable:
                    continue
                new_distance = current_distance + distance
                new_keys = frozenset({next_key}.union(collected_keys))
                if ((next_key, new_keys) not in new_info
                        or new_distance < new_info[(next_key, new_keys)]):
                    new_info[(next_key, new_keys)] = new_distance
        info = new_info
    return min(info.values())


def part_2(maze):
    # Update the maze:
    maze = [list(row) for row in maze]
    for y, row in enumerate(maze):
        for x, symbol in enumerate(row):
            if symbol == '@':
                for (dx, dy) in [(0, 0), (1, 0), (-1, 0), (0, 1), (0, -1)]:
                    maze[y + dy][x + dx] = '#'
                maze[y - 1][x - 1] = '1'
                maze[y - 1][x + 1] = '2'
                maze[y + 1][x - 1] = '3'
                maze[y + 1][x + 1] = '4'
    maze = ["".join(row) for row in maze]

    # Same algorithm as in part one but now with four simultaneous positions.
    # I'm sure I could write a shared function for part 1 and part 2 that
    # contains this loop but I'm done with this day's challenge.
    all_paths = build_maze(maze)
    keys = frozenset(k for k in all_paths if k in KEYS)
    # info is almost the same as in part 1 but now has the positions of
    # all four robots.
    info = {(('1', '2', '3', '4'), frozenset()): 0}
    for _ in keys:
        new_info = {}
        for item in info:
            current_positions = item[0]
            collected_keys = item[1]
            current_distance = info[item]
            for next_key in keys:
                if next_key in collected_keys:
                    continue
                for robot in range(4):
                    if next_key not in all_paths[current_positions[robot]]:
                        continue
                    distance, path = all_paths[current_positions[robot]][next_key]
                    is_reachable = all(
                        (c in collected_keys or c.lower() in collected_keys) for c in path
                    )
                    if not is_reachable:
                        continue
                    new_distance = current_distance + distance
                    new_keys = frozenset({next_key}.union(collected_keys))
                    new_positions = list(current_positions)
                    new_positions[robot] = next_key
                    new_positions = tuple(new_positions)
                    if ((new_positions, new_keys) not in new_info
                            or new_distance < new_info[(new_positions, new_keys)]):
                        new_info[(new_positions, new_keys)] = new_distance
        info = new_info
    return min(info.values())


with open("../../input/2019-18-sample.txt") as file:
    test_inputs = file.read().split("\n\n")
assert part_1(test_inputs[0].splitlines()) == 8
assert part_1(test_inputs[1].splitlines()) == 86
assert part_1(test_inputs[2].splitlines()) == 132
assert part_1(test_inputs[3].splitlines()) == 136
assert part_1(test_inputs[4].splitlines()) == 81

with open("../../input/2019-18-input.txt") as file:
    challenge_input = file.read().splitlines()
print(part_1(challenge_input))  # 4406
print(part_2(challenge_input))  # 1964
