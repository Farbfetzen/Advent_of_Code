# https://adventofcode.com/2020/day/3


check_slope <- function(slope, map) {
    x = 1
    y = 1
    right = slope[1]
    down = slope[2]
    n_trees = 0
    n_steps = height %/% down - 1
    for (i in seq_len(n_steps)) {
        x = (x + right - 1) %% width + 1
        y = y + down
        n_trees = n_trees + map[y, x]
    }
    return(n_trees)
}


map = readLines("2020/day_03_input.txt")
width = nchar(map[1])
height = length(map)
map = matrix(unlist(strsplit(map, "")), ncol = width, nrow = height, byrow = TRUE)
map = map == "#"


# part 1
check_slope(c(3, 1), map)  # 211


# part 2
slopes = list(c(1, 1), c(3, 1), c(5, 1), c(7, 1), c(1, 2))
prod(unlist(lapply(slopes, check_slope, map)))  # 3584591857
