import pygame as pg
import tools

F1 = 0
F2 = 1
F3 = 2
C0 = 'coil'
CR = 'crane'




textures = {
    F1 : pg.image.load("images/floor_concrete.png"),
    F2 : pg.image.load("images/floor_concrete_1.png"),
    F3 : pg.image.load("images/floor_concrete_2.png"),
    C0 : pg.image.load("images/coil_1.png"),
    CR : pg.image.load("images/crane.png")


    }

textures[F1] = tools.scale_image(textures[F1], 0.5)
textures[F2] = tools.scale_image(textures[F2], 0.5)
textures[F3] = tools.scale_image(textures[F3], 0.5)
textures[C0] = tools.scale_image(textures[C0], 0.5)
textures[CR] = tools.scale_image(textures[CR], 0.5)


tilemap = [
    [F1, F1, F1, F1, F1, F1, F1, F1, F1, F1, F1, F1, F1, F1, F1, F1, F1, F1, F1, F1, F1, F1, F1, F1, F1, F1, F1],
    [F1, F1, F1, F1, F1, F1, F1, F1, F1, F1, F1, F1, F1, F1, F1, F1, F1, F1, F1, F1, F1, F1, F1, F1, F1, F1, F1],
    [F1, F1, F1, F1, F1, F1, F1, F1, F1, F1, F1, F1, F1, F1, F1, F1, F1, F1, F1, F1, F1, F1, F1, F1, F1, F1, F1],
    [F1, F1, F1, F1, F1, F1, F1, F1, F1, F1, F1, F1, F1, F1, F1, F1, F1, F1, F1, F1, F1, C0, C0, C0, C0, C0, F1],
    [F1, F1, F1, F1, F1, F1, F1, F1, F1, F1, F1, F1, F1, F1, F1, F1, F1, F1, F1, F1, F3, F2, F2, F2, F2, F2, F2],
    [F1, F1, F1, F1, F1, F1, F1, F1, F1, F1, F1, F1, F1, F1, F1, F1, F1, F1, F1, F1, F1, C0, C0, C0, C0, C0, F1],
    [F1, F1, F1, F1, F1, F1, F1, F1, F1, F1, F1, F1, F1, F1, F1, F1, F1, F1, F1, F1, F3, F2, F2, F2, F2, F2, F2],
    [F1, F1, F1, F1, F1, F1, F1, F1, F1, F1, F1, F1, F1, F1, F1, F1, F1, F1, F1, F1, F1, C0, C0, C0, C0, C0, F1],
    [F1, F1, F1, F1, F1, F1, F1, F1, F1, F1, F1, F1, F1, F1, F1, F1, F1, F1, F1, F1, F3, F2, F2, F2, F2, F2, F2],
    [F1, F1, F1, F1, F1, F1, F1, F1, F1, F1, F1, F1, F1, F1, F1, F1, F1, F1, F1, F1, F1, C0, C0, C0, C0, C0, F1],
    [F1, F1, F1, F1, F1, F1, F1, F1, F1, F1, F1, F1, F1, F1, F1, F1, F1, F1, F1, F1, F1, F1, F1, F1, F1, F1, F1],
    [F1, F1, F1, F1, F1, F1, F1, F1, F1, F1, F1, F1, F1, F1, F1, F1, F1, F1, F1, F1, F1, F1, F1, F1, F1, F1, F1]    
    ]

scale_factor = 1
width, height = scale_factor*textures[F1].get_width(), scale_factor*textures[F1].get_height()
mapwidth = len(tilemap) * width
mapheight = len(tilemap[0]) * height
