# https://adventofcode.com/2021/day/23

import bisect
import itertools
from math import inf

from src.util.exceptions import ResultExpectedError
from src.util.inputs import Inputs
from src.util.solution import Solution


# I don't use Vector2 for the positions here because that makes it much slower. This solution runs both parts
# for the sample and puzzle input in less than 4 seconds on my machine.

type Position = tuple[int, int]

# Amphipod positions mapped to their names. Ones that reached their final position are renamed to "X".
type AmphipodPositionMap = dict[Position, str]

# The AmphipodPositionMap converted to a tuple so it can be inserted into a set.
type AmphipodPositionTuple = tuple[tuple[Position, str], ...]

# Positions mapped to their connected positions and the distances to them.
type ConnectionMap = dict[Position, dict[Position, int]]

# All positions that can be used for moves.
type Spaces = list[Position]


class Solution2021Day23(Solution):
    hallway_y = 1
    home_room_x = {"A": 3, "B": 5, "C": 7, "D": 9}
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
        amphipods, connection_map = self.parse_diagram(diagram)
        return self.find_min_energy(amphipods, connection_map)

    def solve_2(self, diagram: list[str]) -> int:
        diagram = diagram[:3] + ["  #D#C#B#A#", "  #D#B#A#C#"] + diagram[3:]
        amphipods, connection_map = self.parse_diagram(diagram)
        return self.find_min_energy(amphipods, connection_map)

    def parse_diagram(self, diagram: list[str]) -> tuple[AmphipodPositionMap, ConnectionMap]:
        amphipods: AmphipodPositionMap = {}
        spaces: Spaces = []
        max_y = len(diagram) - 1
        for y, line in enumerate(diagram):
            for x, char in enumerate(line):
                position = (x, y)
                if char == "." and diagram[y + 1][x] == "#":
                    spaces.append(position)
                elif char.isalpha():
                    if x == self.home_room_x[char] and all(char == diagram[yy][x] for yy in range(y + 1, max_y)):
                        # Mark amphipods that have reached their goal with "X" because they won't move.
                        amphipods[position] = self.satisfied_amphipod
                    else:
                        amphipods[position] = char
                        spaces.append(position)
        return amphipods, self.find_connections(spaces, amphipods)

    def find_connections(self, spaces: Spaces, amphipods: AmphipodPositionMap) -> ConnectionMap:
        """Returns the positions of all reachable spaces and the distances to a space."""
        connection_map: ConnectionMap = {space: {} for space in spaces}
        for space, other in itertools.combinations(spaces, 2):
            if space[0] == other[0] or self.hallway_y == space[1] == other[1]:
                # Skip because amphipods that are not satisfied must first move into the hallway
                # before moving back into the starting room.
                # And skip because amphipods won't move between hallway positions.
                continue
            if space[1] == self.hallway_y or other[1] == self.hallway_y:
                # Hallway spaces can only point to room spaces.
                # Room spaces can point to hallway spaces.
                distance = self.manhattan_distance(space, other)
                connection_map[space][other] = distance
                connection_map[other][space] = distance
            else:
                # Room spaces can point to spaces in other rooms if those belong to the correct amphipod type.
                # Get the distance to the hallway, then the manhattan distance to the target.
                distance = space[1] - self.hallway_y
                distance += self.manhattan_distance((space[0], self.hallway_y), other)

                if other[0] == self.home_room_x[amphipods[space]]:
                    # The other space is the home of the amphipod at the current space.
                    connection_map[space][other] = distance
                if space[0] == self.home_room_x[amphipods[other]]:
                    # The current space is the home of the amphipod at the other space.
                    connection_map[other][space] = distance
        return connection_map

    @staticmethod
    def manhattan_distance(a: Position, b: Position) -> int:
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    def find_min_energy(self, amphipods: AmphipodPositionMap, connection_map: ConnectionMap) -> int:  # noqa: S3776
        seen_states: dict[AmphipodPositionTuple, int] = {}
        # The queue is sorted by total energy, which is the sum of energy used so far plus potential remaining energy.
        # energy so far: sum of energy used to reach the current state
        # potential remaining energy: estimated energy to reach the target state
        # queue entry: (total energy, energy used so far, amphipod positions)
        queue: list[tuple[int, int, AmphipodPositionMap]] = [(0, 0, amphipods)]
        while queue:
            _, energy, amphipods = queue.pop()

            if all(amphipod == self.satisfied_amphipod for amphipod in amphipods.values()):
                # All amphipods have reached their goal positions.
                return energy

            for position, amphipod in amphipods.items():
                if amphipod == self.satisfied_amphipod:
                    continue
                for new_position, distance in self.find_moves(position, amphipod, amphipods, connection_map):
                    new_amphipods = amphipods.copy()
                    del new_amphipods[position]
                    if new_position[1] == self.hallway_y:
                        new_amphipods[new_position] = amphipod
                    else:
                        # Amphipod moves into a room. This is only possible if that is its home.
                        new_amphipods[new_position] = self.satisfied_amphipod

                    state = tuple(sorted(new_amphipods.items()))
                    seen_energy = seen_states.get(state, inf)
                    new_energy = energy + distance * self.energy_requirements[amphipod]
                    if new_energy >= seen_energy:
                        continue
                    seen_states[state] = new_energy

                    # Insert while keeping the queue sorted by descending total energy.
                    total_energy = new_energy + self.estimate_potential_energy(new_amphipods, connection_map)
                    bisect.insort(queue, (total_energy, new_energy, new_amphipods), key=lambda x: -x[0])

        raise ResultExpectedError

    def find_moves(
            self,
            position: Position,
            amphipod: str,
            amphipods: AmphipodPositionMap,
            connection_map: ConnectionMap
    ) -> list[tuple[Position, int]]:
        """Find all spaces that are reachable from the current position and return them with their distances."""
        moves: list[tuple[Position, int]] = []
        position_x, position_y = position
        if (position_x, position_y - 1) in amphipods:
            return moves
        for connection in connection_map[position].items():
            target = connection[0]
            if target in amphipods:
                continue
            target_x, target_y = target
            if target_y == self.hallway_y:
                if self.check_path_clear(position_x, target_x, amphipods):
                    moves.append(connection)
            elif target_x == self.home_room_x[amphipod]:
                # Target is at the amphipod home position.
                below = (target_x, target_y + 1)
                # If below is not in connections then there is a wall and this is the lowest position in the room.
                if ((below not in connection_map or amphipods.get(below) == self.satisfied_amphipod)
                        and self.check_path_clear(position_x, target_x, amphipods)):
                    # Return only this move because moving anywhere else wouldn't make sense.
                    return [connection]
        return moves

    def check_path_clear(self, position_x: int, target_x: int, amphipods: AmphipodPositionMap) -> bool:
        # Check if the hallway is clear between the two positions.
        for x, y in amphipods:
            if y == self.hallway_y and (position_x < x < target_x or position_x > x > target_x):
                return False
        return True

    def estimate_potential_energy(self, amphipods: AmphipodPositionMap, connection_map: ConnectionMap) -> int:
        """Return a lower bound for the remaining energy necessary for all amphipods to reach their goals.
        The goal in this case is the top space in the home room. This ignores blocked paths.
        """
        estimate = 0
        for position, amphipod in amphipods.items():
            if amphipod == self.satisfied_amphipod:
                continue
            amphipod_home_x = self.home_room_x[amphipod]
            distance = 0
            if position[0] == amphipod_home_x:
                # The amphipod is in its home room but, it's not satisfied because there's a stranger below
                # It needs to move out and come back in.
                position_outside = (amphipod_home_x + 1, self.hallway_y)
                distance += connection_map[position][position_outside]
                position = position_outside
            distance += connection_map[position][(amphipod_home_x, self.hallway_y + 1)]
            estimate += distance * self.energy_requirements[amphipod]
        return estimate
