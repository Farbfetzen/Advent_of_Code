# https://adventofcode.com/2021/day/23

from collections.abc import Sequence

from src.util.inputs import Inputs
from src.util.solution import Solution
from src.util.util import Point2


MOVEMENT_ENERGY = {"A": 1, "B": 10, "C": 100, "D": 1000}


class Solution2021Day23(Solution):

    def solve(self, inputs: Inputs) -> None:
        # TODO: Make it faster.
        #  Maybe it's so slow because bad paths are explored preferentially?
        #  Is there a better distance metric so good paths are explored first?
        #  Simply sorting the queue by decreasing energy makes it much slower.
        #  And maybe use faster data structures?
        prepared_input = inputs.samples[0].splitlines()
        self.sample_results_1.append(self.solve_1(prepared_input))
        self.sample_results_2.append(self.solve_2(prepared_input))

        prepared_input = inputs.input.splitlines()
        self.result_1 = self.solve_1(prepared_input)
        self.result_2 = self.solve_2(prepared_input)

    def solve_1(self, data: list[str]) -> int:
        destinations = {
            "A": ((3, 2), (3, 3)),
            "B": ((5, 2), (5, 3)),
            "C": ((7, 2), (7, 3)),
            "D": ((9, 2), (9, 3)),
        }
        neighbor_map, start_amphipod_positions = self.parse_map(data)
        return self.find_min_energy(neighbor_map, start_amphipod_positions, destinations)

    def solve_2(self, data: list[str]) -> int:
        destinations = {
            "A": ((3, 2), (3, 3), (3, 4), (3, 5)),
            "B": ((5, 2), (5, 3), (5, 4), (5, 5)),
            "C": ((7, 2), (7, 3), (7, 4), (7, 5)),
            "D": ((9, 2), (9, 3), (9, 4), (9, 5)),
        }
        neighbor_map, start_amphipod_positions = self.parse_map(data[:3] + ["  #D#C#B#A#", "  #D#B#A#C#"] + data[3:])
        return self.find_min_energy(neighbor_map, start_amphipod_positions, destinations)

    @staticmethod
    def parse_map(data: list[str]) -> tuple[dict[Point2, list[Point2]], dict[Point2, str]]:
        relevant_symbols = {".", "A", "B", "C", "D"}
        neighbor_map: dict[Point2, list[Point2]] = {}
        amphipod_positions = {}
        offsets = ((1, 0), (0, 1), (-1, 0), (0, -1))
        for y, line in enumerate(data):
            for x, char in enumerate(line):
                if char in relevant_symbols:
                    position = Point2(x, y)
                    neighbor_map[position] = []
                    if char.isalpha():
                        amphipod_positions[position] = char
                    for dy, dx in offsets:
                        neighbor = Point2(x + dx, y + dy)
                        if data[neighbor.y][neighbor.x] in relevant_symbols:
                            neighbor_map[position].append(neighbor)
        return neighbor_map, amphipod_positions

    def find_min_energy(
            self,
            neighbor_map: dict[Point2, list[Point2]],
            start_amphipod_positions: dict[Point2, str],
            destinations: dict[str, Sequence[tuple[int, int]]]
    ) -> int:
        forbidden_positions = self.get_forbidden_positions(destinations)
        non_stop_positions = {pos for pos in neighbor_map.keys() if len(neighbor_map[pos]) == 3}
        queue = [(0, start_amphipod_positions)]
        seen = {}
        min_energy = 10 ** 6
        while queue:
            current_energy, current_positions = queue.pop()

            for position, name in current_positions.items():
                current_destinations = destinations[name]

                # Check if amphipod is in destination room and all lower amphipods are
                # of the correct type.
                if position in current_destinations:
                    i = current_destinations.index(position)
                    for dest in current_destinations[i + 1:]:
                        if current_positions[dest] != name:
                            break
                    else:
                        continue

                reachable_positions = self.get_reachable_positions(
                        name, MOVEMENT_ENERGY[name], position, neighbor_map,
                        current_positions, non_stop_positions, forbidden_positions[name],
                        current_destinations
                )
                for new_position, additional_energy in reachable_positions:
                    # Move amphipod down into destination.
                    new_amphipod_positions = current_positions.copy()
                    del new_amphipod_positions[position]
                    new_amphipod_positions[new_position] = name
                    new_energy = current_energy + additional_energy
                    if self.check_finished(new_amphipod_positions, destinations) and new_energy < min_energy:
                        min_energy = new_energy
                        continue
                    new_state = (new_energy, new_amphipod_positions)
                    positions_hashable = frozenset((k, v) for k, v in new_amphipod_positions.items())
                    if positions_hashable in seen:
                        old_energy = seen[positions_hashable]
                        if old_energy > new_energy:
                            seen[positions_hashable] = new_energy
                            queue.append(new_state)
                    else:
                        seen[positions_hashable] = new_energy
                        queue.append(new_state)
            queue.sort(key=lambda state: state[0])

        return min_energy

    @staticmethod
    def get_forbidden_positions(destinations: dict[str, Sequence[tuple[int, int]]]) -> dict[str, set[tuple[int, int]]]:
        """The rooms of other amphipod types are forbidden."""
        forbidden_positions = {}
        for name in destinations:
            positions = set()
            for other_name, other_positions in destinations.items():
                if other_name == name:
                    continue
                positions.update(other_positions)
            forbidden_positions[name] = positions
        return forbidden_positions

    @staticmethod
    def check_finished(positions, destinations) -> bool:
        for position, name in positions.items():
            if position not in destinations[name]:
                return False
        return True

    @staticmethod
    def get_reachable_positions(
            name: str,
            movement_energy: int,
            start_position: Point2,
            neighbor_map: dict[Point2, list[Point2]],
            amphipod_positions: dict[Point2, str],
            non_stop_positions: set[Point2],
            forbidden_positions: set[tuple[int, int]],
            destinations: Sequence[tuple[int, int]]
    ) -> list[tuple[Point2, int]]:
        visited = {start_position}
        candidates = []
        queue = [(start_position, 0)]
        while queue:
            current = queue.pop()
            new_energy = current[1] + movement_energy
            for neighbor_position in neighbor_map[current[0]]:
                if neighbor_position not in visited and neighbor_position not in amphipod_positions:
                    visited.add(neighbor_position)
                    new_position_and_energy = (neighbor_position, new_energy)
                    queue.append(new_position_and_energy)
                    candidates.append(new_position_and_energy)
        candidates = [c for c in candidates
                      if c[0] not in non_stop_positions and c[0] not in forbidden_positions]

        # Moving to the destination room only makes sense of there are no amphipods
        # of the wrong type and no empty spaces below the candidate position.
        for candidate in reversed(candidates):
            if candidate[0] in destinations:
                i = destinations.index(candidate[0])
                for dest in destinations[i + 1:]:
                    other = amphipod_positions.get(dest)
                    if other is None or other != name:
                        candidates.remove(candidate)
                        break
                else:
                    # This is the best possible candidate position. Moving elsewhere
                    # wouldn't make sense.
                    return [candidate]

        if start_position not in forbidden_positions and start_position not in destinations:
            # The amphipod is in the hallway and can only move to its destination room.
            candidates = [c for c in candidates if c[0] in destinations]
        return candidates
