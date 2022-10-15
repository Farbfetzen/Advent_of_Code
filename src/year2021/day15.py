# https://adventofcode.com/2021/day/15

from queue import PriorityQueue

from src.util.types import Data, Solution


def prepare_data(data: str) -> list[list[int]]:
    return [[int(x) for x in line] for line in data.splitlines()]


def manhattan_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def find_lowest_risk(cave_map):
    """Pathfinding using A*"""
    start = (0, 0)
    destination = (len(cave_map[0]) - 1, len(cave_map) - 1)
    frontier = PriorityQueue()
    frontier.put((0, start))
    came_from = {start: None}
    risk_so_far = {start: 0}
    offsets = ((1, 0), (0, 1), (-1, 0), (0, -1))
    pos = None
    while not frontier.empty():
        pos = frontier.get()[1]
        if pos == destination:
            break
        for offset in offsets:
            new_pos = (pos[0] + offset[0], pos[1] + offset[1])
            if 0 <= new_pos[0] < len(cave_map[0]) and 0 <= new_pos[1] < len(cave_map):
                new_risk = risk_so_far[pos] + cave_map[new_pos[1]][new_pos[0]]
                if new_pos not in came_from or new_risk < risk_so_far[new_pos]:
                    risk_so_far[new_pos] = new_risk
                    priority = new_risk + manhattan_distance(new_pos, destination)
                    frontier.put((priority, new_pos))
                    came_from[new_pos] = pos
    return risk_so_far[pos]


def part_1(cave_map):
    return find_lowest_risk(cave_map)


def part_2(cave_map):
    original_width = len(cave_map[0])
    original_hight = len(cave_map)
    for i in range(4):
        for line in cave_map:
            right_part = [x % 9 + 1 for x in line[-original_width:]]
            line.extend(right_part)
        for line in cave_map[original_hight*i:original_hight*(i+1)]:
            new_line = [x % 9 + 1 for x in line]
            cave_map.append(new_line)

    return find_lowest_risk(cave_map)


def solve(data: Data) -> Solution:
    solution = Solution()
    sample_data = prepare_data(data.samples[0])
    solution.samples_part_1.append(part_1(sample_data))
    solution.samples_part_2.append(part_2(sample_data))

    challenge_data = prepare_data(data.input)
    solution.part_1 = part_1(challenge_data)
    solution.part_2 = part_2(challenge_data)
    return solution
