# https://adventofcode.com/2019/day/16


fft_1 <- function(signal, n = 100) {
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
    signal[1:8]
}


fft_2 <- function(signal, n = 100) {
    # Took me a long time but then I saw the light with the help of
    # the nice people in this thread:
    # https://www.reddit.com/r/adventofcode/comments/ebf5cy/2019_day_16_part_2_understanding_how_to_come_up
    # Only works if the message is in the second half of the signal.
    offset <- as.numeric(paste(signal[1:7], collapse = ""))
    signal <- rep(signal, 1e4)
    len <- length(signal)
    stopifnot(offset >= len / 2)
    signal <- signal[len:(offset+1)]
    for (n_ in seq_len(n)) {
        signal <- cumsum(signal) %% 10
    }
    len <- length(signal)
    signal[len:(len-7)]
}


signal <- readLines("input/2019/16-input.txt")
signal <- as.numeric(strsplit(signal, "")[[1]])

# part 1:
cat(fft_1(signal), sep = "")  # 74608727

# part 2:
cat(fft_2(signal), sep = "")  # 57920757
