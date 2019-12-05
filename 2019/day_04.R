# https://adventofcode.com/2019/day/4


passwords <- strsplit(as.character(178416:676461), "")
sorted <- passwords[!vapply(passwords, is.unsorted, TRUE)]
freq <- lapply(sorted, table)
total_1 <- sum(vapply(freq, function(x) any(x > 1), TRUE))
total_2 <- sum(vapply(freq, function(x) 2 %in% x, TRUE))
print(total_1)  # 1650
print(total_2)  # 1129
