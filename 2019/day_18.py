# https://adventofcode.com/2019/day/18


# This works fine for test inputs 1, 2, 3, and 5 but takes forever on 4.
# I'm not sure if it ever finishes on 4 and I haven't tested it on the real
# input yet. Need to find a better solution that runs in a resonable time for
# many keys.

# Maybe an idea from the solutions thread on Reddit:
# https://www.reddit.com/r/adventofcode/comments/ec8090/2019_day_18_solutions
# First get the distances from all keys (and start position) to all other keys
# and save which doors are in the way:
# {
#     "@": {
#         "a": (2, {}),    # 2 steps to "a", no door blocking
#         "b": (4, {"A"})  # 4 steps to "b", blocked by door A
#     },
#     "a": {"b": (6, {"A"})},
#     "b": {"a": (6, {"A"})}
# }
# Use this as the map.
# Make sure to not calculate the distance from the keys to the start position!
# Then recursively go from key to key while keeing track of which doors
# have already been opened and which keys have been visited.
# This way I don't have to recalculate all the distances on every step.
#
# Also a nice solution I found: https://repl.it/@joningram/AOC-2019#day18.py
# This one has a nicer BFS and no recursion!
#
# Important observation: When searching one level at a time, the first complete
# path found will be the shortest. So as soon as all keys are found I can
# break out of the loop. That's also why it might be a good idea to not only
# remember the blocking doors between keys but also the keys between keys. So
# I can add them to the collection faster.


from pprint import pprint
import math


# Global dictionaries, useful for the recursion.
maze = {}
key_positions = {}
doors_by_position = {}  # position: character
doors_by_character = {}  # character: position


def build_maze(maze_input):
    maze.clear()
    key_positions.clear()
    doors_by_position.clear()
    doors_by_character.clear()
    start_position = None
    for y, row in enumerate(maze_input):
        for x, symbol in enumerate(row):
            position = (x, y)
            if symbol != "#":
                maze[position] = []
            if symbol == "@":
                start_position = position
            elif symbol.islower():
                key_positions[position] = symbol
            elif symbol.isupper():
                doors_by_position[position] = symbol
    doors_by_character.update({v: k for k, v in doors_by_position.items()})
    for pos in maze:
        for delta_pos in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            neighbor = (pos[0] + delta_pos[0], pos[1] + delta_pos[1])
            if neighbor in maze:
                maze[pos].append(neighbor)
    return start_position


def find_reachable_keys(start, ignore_positions):
    """Use a flood fill to find the distances to all reachable keys."""
    queue = [start]
    seen = set()
    keys_found = []  # value = distance
    n_steps = 0
    while queue:
        new_queue = []
        n_steps += 1
        for current_pos in queue:
            for neighbor in maze[current_pos]:
                if neighbor in seen:
                    continue
                if neighbor not in ignore_positions:
                    if neighbor in doors_by_position:
                        continue
                    if neighbor in key_positions:
                        keys_found.append({
                            "position": neighbor,
                            "key": key_positions[neighbor],
                            "n_steps": n_steps
                        })
                new_queue.append(neighbor)
                seen.add(neighbor)
        queue = new_queue
    return keys_found


def walk_maze(start, ignore_positions):
    reachable_keys = find_reachable_keys(start, ignore_positions)
    # print(reachable_keys)
    if not reachable_keys:
        return 0
    distances = []
    for key in reachable_keys:
        ignore_positions_new = ignore_positions.copy()
        ignore_positions_new.add(key["position"])
        door = key["key"].upper()
        if door in doors_by_character:
            ignore_positions_new.add(doors_by_character[door])
        next_distance = key["n_steps"] + walk_maze(
            key["position"],
            ignore_positions_new
        )
        distances.append(next_distance)
    return min(distances)


def part_1(maze_input):
    start_pos = build_maze(maze_input)
    # pprint(find_reachable_keys(start_pos, set()))
    return walk_maze(start_pos, set())


test_input_1 = """#########
#b.A.@.a#
#########
""".splitlines()
test_input_2 = """########################
#f.D.E.e.C.b.A.@.a.B.c.#
######################.#
#d.....................#
########################
""".splitlines()
test_input_3 = """########################
#...............b.C.D.f#
#.######################
#.....@.a.B.c.d.A.e.F.g#
########################
""".splitlines()
test_input_4 = """#################
#i.G..c...e..H.p#
########.########
#j.A..b...f..D.o#
########@########
#k.E..a...g..B.n#
########.########
#l.F..d...h..C.m#
#################
""".splitlines()
test_input_5 = """########################
#@..............ac.GI.b#
###d#e#f################
###A#B#C################
###g#h#i################
########################
""".splitlines()

assert part_1(test_input_1) == 8
assert part_1(test_input_2) == 86
assert part_1(test_input_3) == 132
# assert part_1(test_input_4) == 136
assert part_1(test_input_5) == 81

# print(part_1(test_input_4))

with open("day_18_input.txt") as file:
    challenge_input = file.read().splitlines()
# print(part_1(challenge_input))
