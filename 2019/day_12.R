# https://adventofcode.com/2019/day/12


# At first I struggled with part 2 but then I found this comment on Reddit:
# https://www.reddit.com/r/adventofcode/comments/e9j0ve/2019_day_12_solutions/faja0lj
# The key insights are:
# 1) The axes (x,y,z) are totally independent. So it suffices to find the period
# for each axis separately. Then the answer is the lcm of these.
# 2) Each axis will repeat "relatively quickly" (fast enough to brute force)
# 3) Since each state has a unique parent, the first repeat must be a repeat of
# state 0.


positions <- readLines("2019/day_12_input.txt")
positions <- regmatches(positions, gregexpr("-?\\d+", positions))
positions <- do.call(rbind, positions)
class(positions) <- "numeric"
moons <- cbind(positions, matrix(0, ncol = 3, nrow = 4))
colnames(moons) <- c("x", "y", "z", "vx", "vy", "vz")
moons

x_original <- moons[, c("x", "vx")]
y_original <- moons[, c("y", "vy")]
z_original <- moons[, c("z", "vz")]
x_period <- NA
y_period <- NA
z_period <- NA

moon_pairs <- t(combn(1:4, 2))
n_pairs <- nrow(moon_pairs)

pos <- 1:3
vel <- 4:6
n_energy <- 1000
i <- 0
while (TRUE) {
    i <- i + 1

    # apply gravity
    for (p in seq_len(n_pairs)) {
        a <- moon_pairs[p, 1]
        b <- moon_pairs[p, 2]
        a_greater_b <- moons[a, pos] > moons[b, pos]
        b_greater_a <- moons[b, pos] > moons[a, pos]
        moons[a, vel][a_greater_b] <- moons[a, vel][a_greater_b] - 1
        moons[b, vel][a_greater_b] <- moons[b, vel][a_greater_b] + 1
        moons[a, vel][b_greater_a] <- moons[a, vel][b_greater_a] + 1
        moons[b, vel][b_greater_a] <- moons[b, vel][b_greater_a] - 1
    }

    # apply velocity
    moons[, pos] <- moons[, pos] + moons[, vel]

    if (i == n_energy) {
        energy <- sum(apply(abs(moons), 1, function(x) sum(x[pos]) * sum(x[vel])))
    }

    if (is.na(x_period) && identical(moons[, c(1, 4)], x_original)) {
        x_period <- i
    }
    if (is.na(y_period) && identical(moons[, c(2, 5)], y_original)) {
        y_period <- i
    }
    if (is.na(z_period) && identical(moons[, c(3, 6)], z_original)) {
        z_period <- i
    }

    if (i %% 10000 == 0) cat("step", i, "\n")
    if (i >= n_energy && !any(is.na(c(x_period, y_period, z_period)))) break
}


gcd <- function(a, b) {
    while (b > 0) {
        temp = b
        b = a %% b
        a = temp
    }
    a
}

lcm <- function(a, b) {
    a * b / gcd(a, b)
}


# part 1:
print(energy)  # 8742

# part 2:
match_step <- lcm(lcm(x_period, y_period), z_period)
print(format(match_step, scientific = FALSE))  # 325433763467176
