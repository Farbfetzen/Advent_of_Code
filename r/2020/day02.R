# https://adventofcode.com/2020/day/2


library(stringr)


input <- strsplit(readLines("../input/2020/02-input.txt"), " ")
low_high <- strsplit(sapply(input, function(x) x[1]), "-")
low <- as.integer(sapply(low_high, function(x) x[1]))
high <- as.integer(sapply(low_high, function(x) x[2]))
char <- sub(":", "", sapply(input, function(x) x[2][1]))
password <- sapply(input, function(x) x[3])


# part 1
count <- str_count(password, char)
sum(low <= count & count <= high)  # 434


# part 2
a <- substr(password, low, low) == char
b <- substr(password, high, high) == char
sum(xor(a, b))  # 509
