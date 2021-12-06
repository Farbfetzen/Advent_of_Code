# https://adventofcode.com/2019/day/4


def get_data(filename):
    with open(filename) as file:
        return [int(i) for i in file.read().split("-")]


def check_increasing_digits(password):
    return list(password) == sorted(password)


def check_adjacent_pairs(password):
    return any(x == y for x, y in zip(password, password[1:]))


def check_adjacent_pairs_group(password):
    return 2 in (password.count(digit) for digit in password)


def count_passwords(password_range):
    total_part_1 = 0
    total_part_2 = 0
    for password in range(password_range[0], password_range[1] + 1):
        password = str(password)
        if check_increasing_digits(password):
            total_part_1 += check_adjacent_pairs(password)
            total_part_2 += check_adjacent_pairs_group(password)
    return total_part_1, total_part_2


challenge_data = get_data("../../input/2019-04-input.txt")

if __name__ == "__main__":
    assert check_increasing_digits("111111") and check_adjacent_pairs("111111")
    assert not (check_increasing_digits("223450") and check_adjacent_pairs("223450"))
    assert not (check_increasing_digits("123789") and check_adjacent_pairs("123789"))

    assert check_increasing_digits("112233") and check_adjacent_pairs_group("112233")
    assert not (check_increasing_digits("123444") and check_adjacent_pairs_group("123444"))
    assert check_increasing_digits("111122") and check_adjacent_pairs_group("111122")

    challenge_part_1, challenge_part_2 = count_passwords(challenge_data)
    print(challenge_part_1)  # 1650
    print(challenge_part_2)  # 1129



