# https://adventofcode.com/2020/day/1


part_1 <- function(data) {
    for (i in seq_along(data)) {
        x <- data[i]
        y <- 2020 - x
        if (y %in% tail(data, -i)) {
            return(x * y)
        }
    }
}


part_2 <- function(data) {
    n <- length(data)
    for (i in seq_len(n)) {
        x <- data[i]
        for (j in seq(i + 1, n)) {
            y <- data[j]
            z <- 2020 - x - y
            if (z %in% tail(data, -j)) {
                return(x * y * z)
            }
        }
    }
}


expenses <- as.integer(readLines("input/2020/01-input.txt"))
print(part_1(expenses))  # 436404
print(part_2(expenses))  # 274879808
