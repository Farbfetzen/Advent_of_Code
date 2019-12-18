# https://adventofcode.com/2019/day/15

# How the map exploration works:
# Try walkign forward. If there is a wall, turn right. If there isn't,
# walk forward and turn left. Only works if the maze has no loops.
# If the droid reaches the origin again then all paths have been explored.
# Works only if the origin is in a dead end, otherwise I would need more
# conditions to detect this.


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
oxygen_system_position = None
world = {position: "walkable"}
path = [position]
directions = (1, 4, 2, 3)  # turn clockwise
dx = (0, 1, 0, -1)
dy = (-1, 0, 1, 0)
directions_i = 0
x_min = 0
y_min = 0
surfaces = {}
for x in ("wall", "walkable", "droid", "origin", "oxygen_system", "path"):
    surfaces[x] = pg.Surface((tile_size, tile_size))
surfaces["wall"].fill(pg.Color("grey35"))
surfaces["walkable"].fill(pg.Color("white"))
surfaces["droid"].fill(pg.Color("firebrick"))
surfaces["origin"].fill(pg.Color("orange"))
surfaces["oxygen_system"].fill(pg.Color("purple"))
surfaces["path"].fill(pg.Color("deepskyblue"))
background_color = pg.Color("black")
fully_explored = False
running = True
clock = pg.time.Clock()
while running:
    clock.tick(20000)
    for event in pg.event.get():
        if event.type == pg.QUIT or \
                event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
            running = False

    if not fully_explored:
        new_position = (position[0] + dx[directions_i],
                        position[1] + dy[directions_i])
        if new_position == origin:
            fully_explored = True

        status = droid.run([directions[directions_i]])
        if status == 0:
            directions_i = (directions_i + 1) % 4
            world[new_position] = "wall"
        elif status == 1 or status == 2:
            if new_position in world:
                if oxygen_system_position is None:
                    path.pop()
            else:
                if status == 1:
                    world[new_position] = "walkable"
                else:
                    world[new_position] = "oxygen_system"
                    oxygen_system_position = new_position
                if oxygen_system_position is None:
                    path.append(new_position)
            directions_i = (directions_i - 1) % 4
            position = new_position
        x_min = min(x_min, position[0])
        y_min = min(y_min, position[1])

    window.fill(background_color)
    for pos, pos_type in world.items():
        window.blit(
            surfaces[pos_type],
            (pos[0] * tile_size, pos[1] * tile_size)
        )
    for p in path:
        window.blit(
            surfaces["path"],
            (p[0] * tile_size, p[1] * tile_size)
        )
    window.blit(
        surfaces["droid"],
        (position[0] * tile_size, position[1] * tile_size)
    )
    window.blit(
        surfaces["origin"],
        (origin[0] * tile_size, origin[1] * tile_size)
    )

    pg.display.flip()

# part 1:
print(len(path))  # 330
