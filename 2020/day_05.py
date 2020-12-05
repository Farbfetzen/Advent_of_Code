# https://adventofcode.com/2020/day/5


def get_seat_id(boarding_pass):
    # No need to separate rows from columns because the "row * 8" is
    # automatically handled if I treat the boarding pass as a 10 digit
    # binary number.
    binary_pass = "".join("1" if x in "BR" else "0" for x in boarding_pass)
    return int(binary_pass, 2)


assert get_seat_id("FBFBBFFRLR") == 357
assert get_seat_id("BFFFBBFRRR") == 567
assert get_seat_id("FFFBBBFRRR") == 119
assert get_seat_id("BBFFBBFRLL") == 820


with open("day_05_input.txt", "r") as file:
    passes = file.read().splitlines()

ids = [get_seat_id(p) for p in passes]

# part 1
print(max(ids))  # 848

# part 2
ids.sort()
for i, id_ in enumerate(ids):
    if ids[i + 1] - id_ == 2:
        print(id_ + 1)  # 682
        break
