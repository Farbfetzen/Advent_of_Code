# https://adventofcode.com/2019/day/4


def check_increasing_digits(password):
    return list(password) == sorted(password)


def check_adjacent_pairs(password):
    return any(password[i] == password[i + 1] for i in range(len(password) - 1))


def check_adjacent_pairs_group(password):
    return 2 in (password.count(digit) for digit in password)


# part 1 test
assert check_increasing_digits("111111") and check_adjacent_pairs("111111")
assert not (check_increasing_digits("223450") and check_adjacent_pairs("223450"))
assert not (check_increasing_digits("123789") and check_adjacent_pairs("123789"))

# part 2 test
assert check_increasing_digits("112233") and check_adjacent_pairs_group("112233")
assert not (check_increasing_digits("123444") and check_adjacent_pairs_group("123444"))
assert check_increasing_digits("111122") and check_adjacent_pairs_group("111122")

day_04_input = "178416-676461"
day_04_input = [int(i) for i in day_04_input.split("-")]
total_part_1 = 0
total_part_2 = 0
for pw in range(day_04_input[0], day_04_input[1] + 1):
    pw = str(pw)
    if not check_increasing_digits(pw):
        continue
    total_part_1 += check_adjacent_pairs(pw)
    total_part_2 += check_adjacent_pairs_group(pw)
print(total_part_1)  # 1650
print(total_part_2)  # 1129
