# https://adventofcode.com/2021/day/24


INPUT_PATH = "../../input/2021-24-input.txt"


def get_data(filename):
    with open(filename) as file:
        return file.read().splitlines()


def solve(program):
    """I could not figure this out on my own at all.
    At first, I tried implementing the ALU and simply running the program. But of course
    that would take way too long to finish. Then I tried converting the input to a set
    of equations but that failed, too. So in the end I went to the solutions thread on Reddit:
    https://www.reddit.com/r/adventofcode/comments/rnejv5/2021_day_24_solutions/
    - The input consists of 14 chunks, each beginning with an "inp w". All chunks are identical
      except for three numbers at indices 4, 5 and 15.
    - The value of z acts as a stack. By multiplying with 26 a number is pushed
      and by using modulo 26 a number is popped.
    - Pushing and popping has to balance so that at the end the stack is empty.
    I still don't really understand how that information leads to the results. I looked at
    a lot of the actual programming solutions in the thread and cobbled together this function.
    """

    chunks = []
    for i in range(14):
        chunk = [int(program[i*18+j].split()[-1]) for j in (4, 5, 15)]
        chunks.append(chunk)

    max_value = [0] * 14
    min_value = [0] * 14
    z = []
    for i, chunk in enumerate(chunks):
        div_z, add_x, add_y = chunk
        if div_z == 26:
            j, add_y = z.pop()
            sum_xy = add_x + add_y
            max_value[i] = 9 + sum_xy
            max_value[j] = 9 - sum_xy
            min_value[i] = 1 + sum_xy
            min_value[j] = 1 - sum_xy
        else:
            z.append((i, add_y))

    max_value = [min(max(x, 1), 9) for x in max_value]
    min_value = [min(max(x, 1), 9) for x in min_value]
    max_value = "".join(str(x) for x in max_value)
    min_value = "".join(str(x) for x in min_value)
    return max_value, min_value


if __name__ == "__main__":
    part_1, part_2 = solve(get_data(INPUT_PATH))
    print(part_1)  # 29991993698469
    print(part_2)  # 14691271141118
