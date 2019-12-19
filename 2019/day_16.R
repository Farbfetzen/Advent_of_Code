# https://adventofcode.com/2019/day/16


# Part 2 is messed up. Need to read more of the comments on Reddit.


fft <- function(signal, n = 100) {
    base_pattern <- c(1, 0, -1, 0)
    output_signal <- numeric(length(signal))
    for (n_ in seq_len(n)) {
        for (i in seq_along(signal)) {
            pattern <- rep(base_pattern, each = i, length.out = length(signal))
            output_signal[i] <- abs(sum(signal * pattern)) %% 10
            signal <- signal[-1]
        }
        signal <- output_signal
    }
    signal
}

# fft2 <- function(signal, n = 100) {
#     base_pattern <- c(1, 0, -1, 0)
#     output_signal <- numeric(length(signal))
#     for (n_ in seq_len(n)) {
#         for (i in seq_along(signal)) {
#             pattern <- rep(base_pattern, each = i, length.out = length(signal))
#             a <- sum(signal[pattern == 1]) - sum(signal[pattern == -1])
#             output_signal[i] <- abs(sum(signal * pattern)) %% 10
#             signal <- signal[-1]
#         }
#         signal <- output_signal
#     }
#     signal
# }


signal <- readLines("2019/day_16_input.txt")
signal <- as.numeric(strsplit(signal, "")[[1]])

#part_1:
part_1 <- fft2(signal, 100)[1:8]
print(paste(part_1, collapse = ""))  # 74608727


library(microbenchmark)
microbenchmark(
    fft(rep(signal, 1)),
    fft2(rep(signal, 1)),
    check = "identical",
    times = 5
)

t <- c(0.7, 2.7, 5.8, 10, 15.7)
x <- 1:5
plot(x, t)
mod <- lm(t~x)
abline(mod)
predict(mod, data.frame(x = 1e4))

# part_2 <- fft(rep(signal, 1e4), 1)


microbenchmark(
    sum(signal[pattern == 1]) - sum(signal[pattern == -1]),
    sum(signal * pattern),
    check = "identical"
)

