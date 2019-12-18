# https://adventofcode.com/2019/day/15

# How the map exploration works:
# Try walkign forward. If there is a wall, turn right. If there isn't,
# walk forward and turn left. Only works if the maze has no loops.
# If the droid reaches the origin again then all paths have been explored.
# Works only if the origin is in a dead end, otherwise I would need more
# conditions to detect this?


import os

os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"
import pygame as pg

from intcode import IntcodeComputer


os.environ["SDL_VIDEO_CENTERED"] = "1"
pg.init()
# I know from previous runs that the maze is 40 tiles wide and high,
# so a tile size of 15 fits nicely into a 600 by 600 window.
window = pg.display.set_mode((600, 600))
tile_size = 15

with open("day_15_input.txt", "r") as file:
    code = [int(i) for i in file.read().split(",")]

droid = IntcodeComputer(code, True, True)
# Set the origin to its final position learned from previous runs. This
# prevents the maze from shifting around:
origin = (20, 20)
position = origin
new_position = position
status = 0
found_oxygen_system = False
world = {position: "walkable"}
path = [position]
contains_oxygen = set()
check_neighbors = set()  # those have oxygen but their neighbors might not
walkable = set()
directions = (1, 4, 2, 3)  # turn clockwise
dx = (0, 1, 0, -1)
dy = (-1, 0, 1, 0)
offsets = tuple(zip(dx, dy))
directions_i = 0
x_min = 0
y_min = 0
surfaces = {}
for x in ("wall", "walkable", "droid", "origin", "path", "oxygen"):
    surfaces[x] = pg.Surface((tile_size, tile_size))
surfaces["wall"].fill(pg.Color("grey35"))
surfaces["walkable"].fill(pg.Color("white"))
surfaces["droid"].fill(pg.Color("firebrick"))
surfaces["origin"].fill(pg.Color("orange"))
surfaces["path"].fill(pg.Color("lightgreen"))
surfaces["oxygen"].fill(pg.Color("deepskyblue"))
background_color = pg.Color("black")
fully_explored = False
oxygen_minutes = 0
running = True
clock = pg.time.Clock()
while running:
    clock.tick(60)
    for event in pg.event.get():
        if event.type == pg.QUIT or \
                event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
            running = False

    if not fully_explored:
        new_position = (position[0] + dx[directions_i],
                        position[1] + dy[directions_i])
        if new_position == origin:
            fully_explored = True
            walkable = {k for k, v in world.items() if v == "walkable"}

        status = droid.run([directions[directions_i]])
        if status == 0:
            directions_i = (directions_i + 1) % 4
            world[new_position] = "wall"
        elif status == 1 or status == 2:
            if new_position in world:
                if not found_oxygen_system:
                    path.pop()
            else:
                world[new_position] = "walkable"
                if status == 2:
                    contains_oxygen.add(new_position)
                    check_neighbors.add(new_position)
                    found_oxygen_system = True
                if not found_oxygen_system:
                    path.append(new_position)
            directions_i = (directions_i - 1) % 4
            position = new_position
        x_min = min(x_min, position[0])
        y_min = min(y_min, position[1])
    else:
        oxygen_minutes += 1
        new_check_neighbors = set()
        while check_neighbors:
            pos = check_neighbors.pop()
            for o in offsets:
                neighbor = (pos[0] + o[0], pos[1] + o[1])
                if world.get(neighbor) == "walkable" and \
                        neighbor not in contains_oxygen and \
                        neighbor not in new_check_neighbors:
                    contains_oxygen.add(neighbor)
                    new_check_neighbors.add(neighbor)
        check_neighbors = new_check_neighbors
        if contains_oxygen == walkable:
            running = False

    window.fill(background_color)
    for pos, pos_type in world.items():
        window.blit(
            surfaces[pos_type],
            (pos[0] * tile_size, pos[1] * tile_size)
        )
    for pos in path:
        window.blit(
            surfaces["path"],
            (pos[0] * tile_size, pos[1] * tile_size)
        )
    window.blit(
        surfaces["droid"],
        (position[0] * tile_size, position[1] * tile_size)
    )
    for pos in contains_oxygen:
        window.blit(
            surfaces["oxygen"],
            (pos[0] * tile_size, pos[1] * tile_size)
        )
    window.blit(
        surfaces["origin"],
        (origin[0] * tile_size, origin[1] * tile_size)
    )
    pg.display.flip()

# part 1:
print(len(path))  # 330

# part 2:
print(oxygen_minutes)  # 352
