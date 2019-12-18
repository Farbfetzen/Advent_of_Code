# https://adventofcode.com/2019/day/15


from intcode import IntcodeComputer


with open("day_15_input.txt", "r") as file:
    code = [int(i) for i in file.read().split(",")]

# part 1:
# Try walkign forward. If there is a wall, turn right. If there isn't,
# walk forward and turn left. Only works if the maze has no loops.
droid = IntcodeComputer(code, True, True)
position = (0, 0)
steps = 0
status = 0
oxygen_system_position = None
world = {}
directions = (1, 4, 2, 3)  # turn clockwise
dx = (0, 1, 0, -1)
dy = (-1, 0, 1, 0)
directions_i = 0
while status != 2:
    status = droid.run([directions[directions_i]])
    if status == 0:
        directions_i = (directions_i + 1) % 4
        world[position] = "wall"
    elif status == 1 or status == 2:
        position = (position[0] + dx[directions_i],
                    position[1] + dy[directions_i])
        if position in world:
            steps -= 1
        else:
            steps += 1
            world[position] = "walkable"
        directions_i = (directions_i - 1) % 4

print(steps)
