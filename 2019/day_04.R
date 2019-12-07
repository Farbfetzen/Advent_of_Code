# https://adventofcode.com/2019/day/4


password_range = readLines("2019/day_04_input.txt")
password_range = as.integer(strsplit(password_range, "-")[[1]])
passwords = password_range[1]:password_range[2]
passwords <- strsplit(as.character(passwords), "")
sorted <- passwords[!vapply(passwords, is.unsorted, TRUE)]
freq <- lapply(sorted, table)
total_1 <- sum(vapply(freq, function(x) any(x > 1), TRUE))
total_2 <- sum(vapply(freq, function(x) 2 %in% x, TRUE))
print(total_1)  # 1650
print(total_2)  # 1129
