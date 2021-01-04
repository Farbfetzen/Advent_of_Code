# https://adventofcode.com/2020/day/15


play <- function(numbers, end_turn) {
    # last_num is always +1 because in R vector indices start at 1.
    memory = integer(end_turn)
    for (turn in seq_along(numbers)) {
        last_num = numbers[turn] + 1L
        last_seen = memory[last_num]
        memory[last_num] = turn
    }
    for (turn in seq(turn + 1, end_turn)) {
        if (last_seen > 0) {
            last_num = turn - last_seen
        } else {
            last_num = 1L
        }
        last_seen = memory[last_num]
        memory[last_num] = turn
    }
    last_num - 1L
}


challenge_input = as.numeric(strsplit(readLines("2020/day_15_input.txt"), ",")[[1]])
print(play(challenge_input, 2020))  # 240
print(play(challenge_input, 30000000))  # 505
