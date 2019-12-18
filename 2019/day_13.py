# https://adventofcode.com/2019/day/13


import collections
import os

os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"
import pygame as pg

from intcode import IntcodeComputer


with open("day_13_input.txt", "r") as file:
    game_code = [int(i) for i in file.read().split(",")]
arcade = IntcodeComputer(game_code, True, True)

grid = {}
while not arcade.has_halted:
    x = arcade.run()
    y = arcade.run()
    tile = arcade.run()
    if x is None or y is None or tile is None:
        break
    grid[(x, y)] = tile

# part 1:
print(collections.Counter(grid.values())[2])  # 268

# part 2:
x_min = min(grid)[0]
x_max = max(grid)[0]
y_min = min(grid, key=lambda v: v[1])[1]
y_max = max(grid, key=lambda v: v[1])[1]
assert x_min == 0 and y_min == 0

arcade.reset()
arcade.intcode[0] = 2

tile_size = 20
os.environ["SDL_VIDEO_CENTERED"] = "1"
pg.init()
score = 0
paddle_x = -1
ball_x = -1
show = False
if show:
    screen = pg.display.set_mode((
        x_max * tile_size + tile_size,
        y_max * tile_size + tile_size)
    )
    colors = [
        pg.Color("black"),        # background
        pg.Color("gray30"),       # wall
        pg.Color("forestgreen"),  # block
        pg.Color("orange"),       # paddle
        pg.Color("firebrick")     # ball
    ]
    font = pg.font.Font(None, 30)
    score_surf = font.render(str(score), False, colors[4], colors[0])
    score_rect = score_surf.get_rect(centerx=screen.get_rect().centerx)
running = True
while running:
    joystick_pos = 0
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                running = False

    # let the game play automatically
    if ball_x > paddle_x:
        joystick_pos = 1
    elif ball_x < paddle_x:
        joystick_pos = -1

    x = arcade.run([joystick_pos])
    y = arcade.run()
    tile = arcade.run()
    if x is None or y is None or tile is None:
        break
    if x == -1 and y == 0:
        score = tile
        if show:
            score_surf = font.render(str(score), False, colors[4], colors[0])
            score_rect = score_surf.get_rect(centerx=screen.get_rect().centerx)
    else:
        if tile == 3:
            paddle_x = x
        elif tile == 4:
            ball_x = x
        if show:
            pg.draw.rect(
                screen,
                colors[tile],
                pg.Rect(
                    x * tile_size,
                    y * tile_size,
                    tile_size,
                    tile_size
                )
            )
    if show:
        screen.blit(score_surf, score_rect)
        pg.display.flip()

print(score)  # 13989
