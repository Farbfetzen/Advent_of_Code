# https://adventofcode.com/2018/day/4

# This looked so easy at first, but then it turned out the be rather convoluted.


library(zoo)


records <- readLines("../input/2018-04-input.txt")
records <- unlist(strsplit(records, "\n"))
records <- strsplit(records, "] ")
records <- as.data.frame(do.call(rbind, records), stringsAsFactors = FALSE)
names(records) <- c("datetime", "activity")
records$datetime <- sub("[", "", records$datetime, fixed = TRUE)
records$datetime <- strptime(records$datetime, "%Y-%m-%d %H:%M", tz = "GMT")
records <- records[order(records$datetime), ]
records$guard <- as.character(as.numeric(gsub("\\D", "", records$activity)))
records$guard <- na.locf(records$guard)
records$date <- as.Date(records$datetime)
records$minute <- as.numeric(format(records$datetime, "%M"))
guards <- list()
for (g in unique(records$guard)) {
    guards[[g]] <- numeric()
}
# I assume they are awake when their shifts start and end.
sleep_start <- NA
sleep_end <- NA
for (i in seq_len(nrow(records))) {
    if (records$activity[i] == "falls asleep") {
        sleep_start <- records$minute[i]
    } else if (records$activity[i] == "wakes up") {
        sleep_end <- records$minute[i] - 1
        guards[[records$guard[i]]] <- c(
            guards[[records$guard[i]]],
            sleep_start:sleep_end
        )
    }
}

# part 1:
sum_sleep <- sapply(guards, length)
i <- which.max(sum_sleep)
sleepiest_guard <- names(guards)[i]
most_sleep_minute <- names(which.max(table(guards[[sleepiest_guard]])))
print(as.integer(sleepiest_guard) * as.integer(most_sleep_minute))  # 60438

# part 2:
max_minute_all <- -Inf
for (id in names(guards)) {
    g <- guards[[id]]
    freq <- table(g)
    max_minute <- max(freq)
    if (max_minute > max_minute_all) {
        max_minute_all <- max_minute
        best_guard <- as.integer(id)
        best_minute <- as.integer(names(which.max(freq)))
    }
}
print(best_guard * best_minute)  # 47989
