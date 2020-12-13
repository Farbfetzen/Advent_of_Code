# https://adventofcode.com/2020/day/13


from sympy.ntheory.modular import crt


def part_1(bus_info):
    time = int(bus_info[0])
    bus_ids = [int(bid) for bid in bus_info[1].split(",") if bid != "x"]
    # I have to wait at most max(bus_ids) minutes.
    for wait_time, t in enumerate(range(time, time + max(bus_ids))):
        for bid in bus_ids:
            if t % bid == 0:
                return wait_time * bid


def part_2(bus_info):
    # This part was not fun. It's more of a number theory problem than a
    # programming challenge. I had to look at the subreddit and stackoverflow
    # to see the chinese remainder theorem mentioned which I have never heard
    # of before. I still have no idea how it works but at least I get the
    # correct result now, thanks to crt() from sympy.
    bus_ids = []
    offsets = []
    for i, char in enumerate(bus_info[1].split(",")):
        if char != "x":
            bus_ids.append(int(char))
            offsets.append(-i)
    return crt(bus_ids, offsets)[0]


test_input = """\
939
7,13,x,x,59,x,31,19
""".splitlines()
assert part_1(test_input) == 295
assert part_2(test_input) == 1068781


with open("day_13_input.txt") as file:
    challenge_input = file.read().splitlines()
print(part_1(challenge_input))  # 3882
print(part_2(challenge_input))  # 867295486378319
