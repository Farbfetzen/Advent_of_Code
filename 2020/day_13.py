# https://adventofcode.com/2020/day/13


from sympy.ntheory.modular import crt


def get_data(filename):
    with open(filename) as file:
        return file.read().splitlines()


def part_1(bus_info):
    time = int(bus_info[0])
    bus_ids = [int(bid) for bid in bus_info[1].split(",") if bid != "x"]
    # I have to wait at most max(bus_ids) minutes.
    for wait_time, t in enumerate(range(time, time + max(bus_ids))):
        for bid in bus_ids:
            if t % bid == 0:
                return wait_time * bid


def part_2(bus_info):
    # I had to look at the subreddit and Stackoverflow to see
    # the chinese remainder theorem mentioned which I have never heard
    # of before. I still have no idea how it works but at least I get the
    # correct result now, thanks to crt() from sympy.
    bus_ids = []
    offsets = []
    for i, char in enumerate(bus_info[1].split(",")):
        if char != "x":
            bus_ids.append(int(char))
            offsets.append(-i)
    return crt(bus_ids, offsets)[0]


def part_2_without_crt(bus_info):
    # Turns out crt() is not necessary to solve this problem.
    # I found this clever algorithm in the solutions thread on Reddit:
    # https://www.reddit.com/r/adventofcode/comments/kc4njx/2020_day_13_solutions/gfo4b1z
    data = [(i, int(bus_id)) for i, bus_id in enumerate(bus_info[1].split(","))
            if bus_id != "x"]
    jump = data[0][1]  # first bus_id
    time = 0
    for delta, bus_id in data[1:]:
        while (time + delta) % bus_id != 0:
            time += jump
        jump *= bus_id
    return time


sample_data = get_data("day_13_sample.txt")
challenge_data = get_data("day_13_input.txt")

if __name__ == "__main__":
    assert part_1(sample_data) == 295
    assert part_2(sample_data) == 1068781
    assert part_2_without_crt(sample_data) == 1068781

    print(part_1(challenge_data))  # 3882
    print(part_2(challenge_data))  # 867295486378319
    print(part_2_without_crt(challenge_data))  # 867295486378319
