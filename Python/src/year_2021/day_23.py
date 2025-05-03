# https://adventofcode.com/2021/day/23

import bisect
import itertools

from src.util.exceptions import ResultExpectedError
from src.util.inputs import Inputs
from src.util.solution import Solution


# I don't use Vector2 for the positions here because that makes it much slower. This solution runs both parts
# for the sample and puzzle input in about 7-8 seconds on my machine. This performance is similar
# to other python solutions I saw on reddit. I spent a lot of time on this to reduce the search space
# and don't see much potential for improvement. It's good enough for me.


# Amphipod positions mapped to their names. Ones that reached their final position are renamed to "X".
type AmphipodPositionMap = dict[tuple[int, int], str]

# Positions mapped to their connected positions and the distances to them.
type Connections = dict[tuple[int, int], list[tuple[tuple[int, int], int]]]

# All positions that can be used for moves.
type Spaces = list[tuple[int, int]]


class Solution2021Day23(Solution):
    hallway_y = 1
    home_room_x = {3: "A", 5: "B", 7: "C", 9: "D"}
    energy_requirements = {"A": 1, "B": 10, "C": 100, "D": 1000}
    satisfied_amphipod = "X"

    def solve(self, inputs: Inputs) -> None:
        diagram = inputs.samples[0].splitlines()
        self.sample_results_1.append(self.solve_1(diagram))
        self.sample_results_2.append(self.solve_2(diagram))

        diagram = inputs.input.splitlines()
        self.result_1 = self.solve_1(diagram)
        self.result_2 = self.solve_2(diagram)

    def solve_1(self, diagram: list[str]) -> int:
        amphipods, spaces = self.parse_diagram(diagram)
        connections = self.find_connections(spaces)
        return self.find_min_energy(amphipods, connections)

    def solve_2(self, diagram: list[str]) -> int:
        diagram = diagram[:3] + ["  #D#C#B#A#", "  #D#B#A#C#"] + diagram[3:]
        amphipods, spaces = self.parse_diagram(diagram)
        connections = self.find_connections(spaces)
        return self.find_min_energy(amphipods, connections)

    def parse_diagram(self, diagram: list[str]) -> tuple[AmphipodPositionMap, Spaces]:
        amphipods: AmphipodPositionMap = {}
        spaces: Spaces = []
        max_y = len(diagram) - 1
        for y, line in enumerate(diagram):
            for x, char in enumerate(line):
                position = (x, y)
                if char == "." and diagram[y + 1][x] == "#":
                    spaces.append(position)
                elif char.isalpha():
                    if char == self.home_room_x[x] and all(char == diagram[yy][x] for yy in range(y + 1, max_y)):
                        # Mark amphipods that have reached their goal with "X" because they won't move.
                        amphipods[position] = self.satisfied_amphipod
                    else:
                        amphipods[position] = char
                        spaces.append(position)
        return amphipods, spaces

    def find_connections(self, spaces: Spaces) -> Connections:
        """Returns the positions of all reachable spaces and the distances to a space."""
        connections: Connections = {space: [] for space in spaces}
        for space, other in itertools.combinations(spaces, 2):
            if self.hallway_y == space[1] == other[1]:
                # Skip because amphipods won't move between hallway positions.
                continue
            if space[1] == self.hallway_y or other[1] == self.hallway_y:
                # Hallway spaces can only point to room spaces.
                # Room spaces can point to hallway spaces.
                distance = self.manhattan_distance(space, other)
                connections[space].append((other, distance))
                connections[other].append((space, distance))
            else:
                # Room spaces can point to spaces in other rooms.
                # Get the distance to the hallway, then the manhattan distance to the target.
                distance = space[1] - self.hallway_y
                distance += self.manhattan_distance((space[0], self.hallway_y), other)
                connections[space].append((other, distance))
                connections[other].append((space, distance))
        return connections

    @staticmethod
    def manhattan_distance(a: tuple[int, int], b: tuple[int, int]) -> int:
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    def find_min_energy(self, amphipods: AmphipodPositionMap, connections: Connections) -> int:
        seen_states: set[tuple[tuple[tuple[int, int], str], ...]] = set()
        energy = 0
        queue: list[tuple[int, AmphipodPositionMap]] = [(energy, amphipods)]
        while queue:
            energy, amphipods = queue.pop()

            if all(amphipod == self.satisfied_amphipod for amphipod in amphipods.values()):
                # All amphipods have reached their goal positions.
                return energy

            state = self.tuple_amphipods(amphipods)
            if state in seen_states:
                continue
            seen_states.add(state)

            for position, amphipod in amphipods.items():
                if amphipod == self.satisfied_amphipod:
                    continue
                for new_position, distance in self.find_moves(position, amphipod, amphipods, connections):
                    new_amphipods = amphipods.copy()
                    del new_amphipods[position]
                    if new_position[1] == self.hallway_y:
                        new_amphipods[new_position] = amphipod
                    else:
                        # Amphipod moves into a room. This is only possible if that is its home.
                        new_amphipods[new_position] = self.satisfied_amphipod
                    new_energy = energy + distance * self.energy_requirements[amphipod]
                    # Insert while keeping the queue sorted by descending energy.
                    bisect.insort(queue, (new_energy, new_amphipods), key=lambda x: -x[0])
        raise ResultExpectedError

    @staticmethod
    def tuple_amphipods(amphipods: AmphipodPositionMap) -> tuple[tuple[tuple[int, int], str], ...]:
        """Convert amphipods to a tuple so they can be inserted into a set."""
        return tuple(sorted(amphipods.items()))

    def find_moves(
            self,
            position: tuple[int, int],
            amphipod: str,
            amphipods: AmphipodPositionMap,
            connections: Connections
    ) -> list[tuple[tuple[int, int], int]]:
        """Find all spaces that are reachable from the current position and return them with their distances."""
        moves: list[tuple[tuple[int, int], int]] = []
        for connection in connections[position]:
            target = connection[0]
            if target in amphipods:
                continue
            if target[1] == self.hallway_y:
                if self.check_path_clear(position, target, amphipods):
                    moves.append(connection)
            elif self.home_room_x[target[0]] == amphipod:
                # Target is at the amphipod home position.
                below = (target[0], target[1] + 1)
                # If below is not in connections then there is a wall and this is the lowest position in the room.
                if ((below not in connections or amphipods.get(below) == self.satisfied_amphipod)
                        and self.check_path_clear(position, target, amphipods)):
                    # Return only this move because moving anywhere else wouldn't make sense.
                    return [connection]
        return moves

    def check_path_clear(
            self,
            position: tuple[int, int],
            target: tuple[int, int],
            amphipods: AmphipodPositionMap
    ) -> bool:
        # Check if the space directly above is empty. Other spaces above can be ignored
        # because there are never gaps in rooms.
        if (position[0], position[1] - 1) in amphipods:
            return False
        # Check if the hallway is clear between the two positions.
        position_x = position[0]
        target_x = target[0]
        for x, y in amphipods:
            if y == self.hallway_y and (position_x < x < target_x or position_x > x > target_x):
                return False
        return True
