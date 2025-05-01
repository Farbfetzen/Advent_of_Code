# https://adventofcode.com/2019/day/20

from typing import NamedTuple

from src.util.exceptions import ResultExpectedError
from src.util.inputs import Inputs
from src.util.solution import Solution
from src.util.vector import Vector2


class Portal(NamedTuple):
    label: str
    # 1 if the portal is at the inner edge of the donut or -1 if it's at the outer edge.
    # This simplifies calculating the new level of a path.
    edge: int


# Dictionary mapping portals to other portals and the distances between them.
type Connections = dict[Portal, dict[Portal, int]]


class Solution2019Day20(Solution):

    def solve(self, inputs: Inputs) -> None:
        for i, sample in enumerate(inputs.samples):
            connections = self.map_connections(sample.splitlines())
            self.sample_results_1.append(self.solve_1(connections))
            # The second example has no solution for part 2.
            if i != 1:
                self.sample_results_2.append(self.solve_2(connections))

        connections = self.map_connections(inputs.input.splitlines())
        self.result_1 = self.solve_1(connections)
        self.result_2 = self.solve_2(connections)

    def map_connections(self, maze: list[str]) -> Connections:
        walkable, portal_map = self.map_maze(maze)
        connections: Connections = {}
        for portal_position, portal in portal_map.items():
            if portal.label != "ZZ":
                connections[portal] = self.get_distances_to_connecting_portals(portal_position, walkable, portal_map)
        return connections

    def map_maze(self, maze: list[str]) -> tuple[set[Vector2], dict[Vector2, Portal]]:
        """Find all walkable spaces and portals."""
        portals: dict[Vector2, Portal] = {}  # keys: position of the walkable space closest to a portal
        # Iterate over all lines to get the width because the IDE's may remove trailing spaces.
        width = max(len(row) for row in maze)
        height = len(maze)
        walkable = self.find_walkable_positions(maze)
        # Search for portals among the walkable positions.
        for position in walkable:
            for neighbor_position in position.neighbors_4():
                char_1 = maze[neighbor_position.y][neighbor_position.x]
                if not char_1.isalpha():
                    continue
                neighbor_direction = neighbor_position - position
                char_2_x, char_2_y = neighbor_position + neighbor_direction
                char_2 = maze[char_2_y][char_2_x]
                assert char_2.isalpha()
                label = char_1 + char_2 if neighbor_direction.x > 0 or neighbor_direction.y > 0 else char_2 + char_1
                edge = 1 if 0 < char_2_x < (width - 1) and 0 < char_2_y < (height - 1) else -1
                portals[position] = Portal(label, edge)
                break
        walkable -= portals.keys()
        return walkable, portals

    @staticmethod
    def find_walkable_positions(maze: list[str]) -> set[Vector2]:
        walkable = set()
        for y, row in enumerate(maze):
            for x, char in enumerate(row):
                if char == ".":
                    walkable.add(Vector2(x, y))
        return walkable

    @staticmethod
    def get_distances_to_connecting_portals(
            portal_position: Vector2,
            walkable: set[Vector2],
            portal_map: dict[Vector2, Portal]
    ) -> dict[Portal, int]:
        distances: dict[Portal, int] = {}
        seen = {portal_position}
        queue = [(portal_position, 0)]
        while queue:
            position, distance = queue.pop()
            distance += 1
            for neighbor_position in position.neighbors_4():
                if neighbor_position in seen:
                    continue
                seen.add(neighbor_position)
                other_portal = portal_map.get(neighbor_position)
                if other_portal is not None and other_portal.label != "AA":
                    distances[other_portal] = distance
                elif neighbor_position in walkable:
                    queue.append((neighbor_position, distance))
        return distances

    @staticmethod
    def solve_1(connections: Connections) -> int:
        """Use BFS to find all paths and return the shortest."""
        queue = [([Portal("AA", -1)], -1)]
        while queue:
            # Find the path with the shortest distance:
            min_q = min(queue, key=lambda x: x[1])
            queue.remove(min_q)
            path, distance = min_q
            last_portal = path[-1]
            if last_portal.label == "ZZ":
                return distance
            distance += 1
            for other_portal, other_distance in connections[last_portal].items():
                if other_portal not in path:
                    other_portal_exit = Portal(other_portal.label, -other_portal.edge)
                    queue.append((
                        path + [other_portal, other_portal_exit],
                        distance + other_distance)
                    )
        raise ResultExpectedError

    @staticmethod
    def solve_2(connections: Connections) -> int:
        """Walk through the maze using BFS and return the first path found."""
        queue = [(Portal("AA", -1), 0, -1)]  # last portal, level, distance
        while queue:
            # Sort reversed by distance to pop the shortest distance first.
            queue.sort(key=lambda x: x[2], reverse=True)
            last_portal, level, distance = queue.pop()
            if last_portal.label == "ZZ":
                return distance
            distance += 1
            for other_portal, other_distance in connections[last_portal].items():
                # - Outer portals except "ZZ" are only open on level > 0.
                other_portal_is_open = other_portal.edge == 1 or (level == 0) == (other_portal.label == "ZZ")
                # - Prevent going in the same portal on the same level,
                #   because it may be that e.g. ("BC", 1) has a walking
                #   connection to ("BC", -1). Going that route would not make sense.
                if other_portal_is_open and other_portal.label != last_portal.label:
                    queue.append((
                        Portal(other_portal.label, -other_portal.edge),
                        level + other_portal.edge,
                        distance + other_distance
                    ))
        raise ResultExpectedError
