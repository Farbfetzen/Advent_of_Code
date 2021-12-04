# https://adventofcode.com/2019/day/4


password_range <- readLines("../input/2019-04-input.txt")
password_range <- as.integer(strsplit(password_range, "-")[[1]])
passwords <- password_range[1]:password_range[2]
passwords <- strsplit(as.character(passwords), "")
sorted <- passwords[!vapply(passwords, is.unsorted, TRUE)]
freq <- lapply(sorted, table)
total_1 <- sum(vapply(freq, function(x) any(x > 1), TRUE))
total_2 <- sum(vapply(freq, function(x) 2 %in% x, TRUE))
print(total_1)  # 1650
print(total_2)  # 1129


# And just for fun here is the solution as a single magrittr pipeline:
library(magrittr)
readLines("2019/day_04_input.txt") %>%
    strsplit("-") %>%
    unlist() %>%
    as.integer() %>%
    {seq(.[1], .[2])} %>%
    as.character() %>%
    strsplit("") %>%
    .[!vapply(., is.unsorted, TRUE)] %>%
    lapply(., table) %>%
    {c(
        sum(vapply(., function(x) any(x > 1), TRUE)),
        sum(vapply(., function(x) 2 %in% x, TRUE))
    )} %>%
    print()

# And again but in a ridiculously compact format:
as.integer(unlist(strsplit(readLines("2019/day_04_input.txt"), "-"))) %>%
    {strsplit(as.character(seq(.[1], .[2])), "")} %>%
    {apply(sapply(lapply(.[!vapply(., is.unsorted, TRUE)], table), function(x) c(any(x > 1), 2 %in% x)), 1, sum)} %>%
    print()

