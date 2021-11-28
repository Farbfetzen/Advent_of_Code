# https://adventofcode.com/2020/day/23


def get_data(filename):
    with open(filename) as file:
        data = file.read().strip()
    return [int(x) for x in list(data)]


def play(cups, n_moves, n_cups):
    """The list next_cup acts as a linked list
    where next_cup[c] points to the right neighbor of c."""
    current_cup = cups[0]
    cups = cups + list(range(len(cups) + 1, n_cups + 1))
    next_cup = [0] * (n_cups + 1)
    for i, c in enumerate(cups):
        next_cup[c] = cups[(i + 1) % n_cups]
    for _ in range(n_moves):
        removed_1st = next_cup[current_cup]
        removed_2nd = next_cup[removed_1st]
        removed_3rd = next_cup[removed_2nd]
        destination = current_cup
        while True:
            destination -= 1
            if destination < 1:
                destination = n_cups
            if destination not in (removed_1st, removed_2nd, removed_3rd):
                break
        next_cup[current_cup] = current_cup = next_cup[removed_3rd]
        next_cup[removed_3rd] = next_cup[destination]
        next_cup[destination] = removed_1st
    return next_cup


def part_1(cups):
    linked_cups = play(cups, 100, len(cups))
    result = ""
    current = 1
    for _ in range(len(cups) - 1):
        current = linked_cups[current]
        result += str(current)
    return result


def part_2(cups):
    linked_cups = play(cups, 10_000_000, 1_000_000)
    a = linked_cups[1]
    b = linked_cups[a]
    return str(a * b)


sample_data = get_data("day_23_sample.txt")
challenge_data = get_data("day_23_input.txt")

if __name__ == "__main__":
    assert part_1(sample_data) == "67384529"
    assert part_2(sample_data) == "149245887792"

    print(part_1(challenge_data))  # 24798635
    print(part_2(challenge_data))  # 12757828710
