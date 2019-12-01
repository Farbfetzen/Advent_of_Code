# https://adventofcode.com/2019/day/1


def calculate_fuel(m):
    return(max(m // 3 - 2, 0))


with open("day_01_input.txt", "r") as file:
    masses = [int(i) for i in file.read().splitlines()]


# part 1
total = 0
for m in masses:
    total += calculate_fuel(m)

print(total)


# part 2
total = 0
for m in masses:
    additional_fuel = calculate_fuel(m)
    while additional_fuel > 0:
        total += additional_fuel
        additional_fuel = calculate_fuel(additional_fuel)

print(total)
