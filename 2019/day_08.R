# https://adventofcode.com/2019/day/8


library(grid)


transmission <- readLines("2019/day_08_input.txt")
transmission <- as.integer(strsplit(transmission, "")[[1]])
layers <- array(transmission,  c(25, 6, length(transmission) / (25 * 6)))
layers <- aperm(layers, c(2, 1, 3))

# part 1:
freq <- apply(layers, 3, table)
print(prod(freq[c("1", "2"), which.min(freq["0", ])]))  # 2520

# part 2:
visible <- apply(layers, c(1, 2), function(x) x[x < 2][1])
grid.newpage()
grid.raster(!visible, interpolate = FALSE)  # LEGJY
