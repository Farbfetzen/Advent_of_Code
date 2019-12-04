# https://adventofcode.com/2019/day/4


# At first I tried to do it in a vectorized way but that was far slower than
# this simple loop.

passwords <- strsplit(as.character(178416:676461), "")
total_1 <- 0
total_2 <- 0
for (pw in passwords) {
    if (is.unsorted(pw)) next
    freq <- table(pw)
    total_1 <- total_1 + any(freq > 1)
    total_2 <- total_2 + (2 %in% freq)
}
print(total_1)  # 1650
print(total_2)  # 1129
