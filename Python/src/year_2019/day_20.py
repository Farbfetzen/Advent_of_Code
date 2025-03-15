# https://adventofcode.com/2019/day/20

from src.util.exceptions import ResultExpectedError
from src.util.inputs import Inputs
from src.util.solution import Solution


DIRECTIONS = ((1, 0), (0, 1), (0, -1), (-1, 0))


class Solution2019Day20(Solution):

    def solve(self, inputs: Inputs) -> None:
        connections = self.map_connections(inputs.samples[0].splitlines())
        self.sample_results_1.append(self.solve_1(connections))
        connections = self.map_connections(inputs.samples[1].splitlines())
        self.sample_results_1.append(self.solve_1(connections))
        connections = self.map_connections(inputs.samples[2].splitlines())
        self.sample_results_2.append(self.solve_2(connections))

        connections = self.map_connections(inputs.input.splitlines())
        self.result_1 = self.solve_1(connections)
        self.result_2 = self.solve_2(connections)

    def map_connections(self, maze: list[str]) -> dict[tuple[str, int], dict[tuple[str, int], int]]:
        walkable, portals = self.map_maze(maze)
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

    def map_maze(self, maze: list[str]) -> tuple[set[tuple[int, int]], dict[tuple[int, int], tuple[str, int]]]:
        """Find all portals and walkable spaces."""
        portals = {}  # = walkable space closest to a portal
        walkable = set()
        maze = self.fix_maze(maze)
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

    @staticmethod
    def fix_maze(maze: list[str]) -> list[str]:
        """Fix uneven row lengths caused by the IDE's removal of trailing spaces."""
        max_width = max(len(row) for row in maze)
        for y, row in enumerate(maze):
            maze[y] = row.ljust(max_width, " ")
        return maze

    @staticmethod
    def solve_1(connections: dict[tuple[str, int], dict[tuple[str, int], int]]) -> int:
        """Use BFS to find all paths and return the shortest."""
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
        raise ResultExpectedError

    @staticmethod
    def solve_2(connections: dict[tuple[str, int], dict[tuple[str, int], int]]) -> int:
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
                if label != last_portal[0] and label != "AA" and (label == "ZZ") == (new_level == -1):
                    queue.append((
                        (label, -side),
                        new_level,
                        distance + other_distance
                    ))
        raise ResultExpectedError
