# https://adventofcode.com/2020/day/3


check_slope <- function(slope, map) {
    right <- slope[1]
    down <- slope[2]
    width <- ncol(map)
    height <- nrow(map)
    y <- seq(1, height, down)
    x <- seq(1, by = right, length.out = length(y))
    x <- (x - 1) %% width + 1
    sum(map[cbind(y, x)])
}


map <- readLines("2020/day_03_input.txt")
map <- matrix(unlist(strsplit(map, "")), nrow = length(map), byrow = TRUE)
map <- map == "#"


# part 1
print(check_slope(c(3, 1), map))  # 211


# part 2
slopes <- list(c(1, 1), c(3, 1), c(5, 1), c(7, 1), c(1, 2))
print(prod(unlist(lapply(slopes, check_slope, map))))  # 3584591857
