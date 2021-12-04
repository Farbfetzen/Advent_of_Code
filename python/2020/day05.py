# https://adventofcode.com/2020/day/5


def get_data():
    with open("../../input/2020-05-input.txt") as file:
        data = file.read().splitlines()
    data.sort()
    return [get_seat_id(p) for p in data]


def get_seat_id(boarding_pass):
    # No need to separate rows from columns because the "row * 8" is
    # automatically handled if I treat the boarding pass as a 10 digit
    # binary number.
    binary_pass = "".join("1" if x in "BR" else "0" for x in boarding_pass)
    return int(binary_pass, 2)


def part_1(ids):
    return max(ids)


def part_2(ids):
    for i, id_ in enumerate(ids):
        if ids[i + 1] - id_ == 2:
            return id_ + 1


challenge_data = get_data()

if __name__ == "__main__":
    assert get_seat_id("FBFBBFFRLR") == 357
    assert get_seat_id("BFFFBBFRRR") == 567
    assert get_seat_id("FFFBBBFRRR") == 119
    assert get_seat_id("BBFFBBFRLL") == 820

    print(part_1(challenge_data))  # 848
    print(part_2(challenge_data))  # 682
