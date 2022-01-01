# https://adventofcode.com/2021/day/23


SAMPLE_PATH = "../../input/2021-23-sample.txt"
INPUT_PATH = "../../input/2021-23-input.txt"
MOVEMENT_ENERGY = {"A": 1, "B": 10, "C": 100, "D": 1000}


def get_data(filename, is_part_2=False):
    with open(filename) as file:
        data = file.read().splitlines()
    if is_part_2:
        data = data[:3] + ["  #D#C#B#A#", "  #D#B#A#C#"] + data[3:]
    relevant_symbols = {".", "A", "B", "C", "D"}
    neighbor_map = {}
    amphipod_positions = {}
    offsets = ((1, 0), (0, 1), (-1, 0), (0, -1))
    for y, line in enumerate(data):
        for x, char in enumerate(line):
            if char in relevant_symbols:
                position = (x, y)
                neighbor_map[position] = []
                if char.isalpha():
                    amphipod_positions[position] = char
                for dy, dx in offsets:
                    neighbor = (x + dx, y + dy)
                    if data[neighbor[1]][neighbor[0]] in relevant_symbols:
                        neighbor_map[position].append(neighbor)
    return neighbor_map, amphipod_positions


def solve(neighbor_map, start_amphipod_positions, destinations):
    forbidden_positions = get_forbidden_positions(destinations)
    non_stop_positions = {pos for pos in neighbor_map.keys() if len(neighbor_map[pos]) == 3}
    queue = [(0, start_amphipod_positions)]
    seen = {}
    min_energy = 10**6
    while queue:
        current_energy, current_positions = queue.pop()

        for position, name in current_positions.items():
            current_destinations = destinations[name]

            # Check if amphipod is in destination room and all lower amphipods are
            # of the correct type.
            if position in current_destinations:
                i = current_destinations.index(position)
                for dest in current_destinations[i+1:]:
                    if current_positions[dest] != name:
                        break
                else:
                    continue

            reachable_positions = get_reachable_positions(
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
                if check_finished(new_amphipod_positions, destinations) and new_energy < min_energy:
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


def get_forbidden_positions(destinations):
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


def check_finished(positions, destinations):
    for position, name in positions.items():
        if position not in destinations[name]:
            return False
    return True


def get_reachable_positions(name, movement_energy, start_position, neighbor_map, amphipod_positions,
                            non_stop_positions, forbidden_positions, destinations):
    visited = {start_position}
    candidates = set()
    queue = [(start_position, 0)]
    while queue:
        current = queue.pop()
        new_energy = current[1] + movement_energy
        for neighbor_position in neighbor_map[current[0]]:
            if neighbor_position not in visited and neighbor_position not in amphipod_positions:
                visited.add(neighbor_position)
                new_position_and_energy = (neighbor_position, new_energy)
                queue.append(new_position_and_energy)
                candidates.add(new_position_and_energy)
    candidates = [c for c in candidates
                  if c[0] not in non_stop_positions and c[0] not in forbidden_positions]

    # Moving to the destination room only makes sense of there are no amphipods
    # of the wrong type and no empty spaces below the candidate position.
    for candidate in reversed(candidates):
        if candidate[0] in destinations:
            i = destinations.index(candidate[0])
            for dest in destinations[i+1:]:
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


def part_1(neighbor_map, start_amphipod_positions):
    destinations = {
        "A": ((3, 2), (3, 3)),
        "B": ((5, 2), (5, 3)),
        "C": ((7, 2), (7, 3)),
        "D": ((9, 2), (9, 3)),
    }
    return solve(neighbor_map, start_amphipod_positions, destinations)


def part_2(neighbor_map, start_amphipod_positions):
    destinations = {
        "A": ((3, 2), (3, 3), (3, 4), (3, 5)),
        "B": ((5, 2), (5, 3), (5, 4), (5, 5)),
        "C": ((7, 2), (7, 3), (7, 4), (7, 5)),
        "D": ((9, 2), (9, 3), (9, 4), (9, 5)),
    }
    return solve(neighbor_map, start_amphipod_positions, destinations)


if __name__ == "__main__":
    # TODO: Make it faster.
    #  Maybe it's so slow because bad paths are explored preferentially?
    #  Is there a better distance metric so good paths are explored first?
    #  Simply sorting the queue by decreasing energy makes it much slower.
    #  And maybe use faster data structures?
    sample_data_1 = get_data(SAMPLE_PATH)
    assert part_1(*sample_data_1) == 12521
    sample_data_2 = get_data(SAMPLE_PATH, True)
    assert part_2(*sample_data_2) == 44169

    challenge_data_1 = get_data(INPUT_PATH)
    print(part_1(*challenge_data_1))  # 12240
    challenge_data_2 = get_data(INPUT_PATH, True)
    print(part_2(*challenge_data_2))  # 44618
