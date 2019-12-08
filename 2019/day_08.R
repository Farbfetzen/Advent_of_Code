# https://adventofcode.com/2019/day/8

# TODO: There are better ways to do this. Storing the layers in a 3d array
# would be smart.


library(grid)


transmission <- readLines("2019/day_08_input.txt")
transmission <- as.integer(strsplit(transmission, "")[[1]])
width <- 25
height <- 6
pixels_per_layer <- width * height
stopifnot(length(transmission) %% pixels_per_layer == 0)
n_layers <- length(transmission) / pixels_per_layer
layers <- matrix(transmission, ncol = pixels_per_layer, byrow = TRUE)

# part 1:
n_0 <- Inf
n_0_current <- 0
layer_with_fewest_0 <- NULL
for (i in seq_len(n_layers)) {
    layer = layers[i, ]
    n_0_current = sum(layer == 0)
    if (n_0_current < n_0) {
        n_0 <- n_0_current
        layer_with_fewest_0 <- layer
    }
}
print(sum(layer_with_fewest_0 == 1) * sum(layer_with_fewest_0 == 2))  # 2520

# part 2:
visible = integer(pixels_per_layer)
for (i in seq_len(pixels_per_layer)) {
    for (j in seq_len(n_layers)) {
        value = layers[j, i]
        if (value < 2) {
            visible[i] <- value
            break
        }
    }
}
image = matrix(!visible, nrow = height, byrow = TRUE)
grid.raster(image, interpolate = FALSE)  # LEGJY
