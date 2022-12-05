
import pygame as pg
import tile_map as tilemap


window = pg.display.set_mode((tilemap.mapheight,tilemap.mapwidth))
clock = pg.time.Clock()
#WIN = pygame.display.set_mode((WIDTH,HEIGHT))
LAYOUT = pg.image.load("images/bg.png")


# ------------------------------------------------------------------------
# Drawing to screen 
def draw_game():
    global window, clock

    # Background
    window.blit(LAYOUT, (0, 0))

    # Tiles
    for row in range(0, len(tilemap.tilemap)):
        for column in range(0, len(tilemap.tilemap[row])):
            if tilemap.tilemap[row][column] == 'crane':
                window.blit(tilemap.textures[0],(column*tilemap.width, row*tilemap.height))
            window.blit(tilemap.textures[tilemap.tilemap[row][column]],(column*tilemap.width, row*tilemap.height))

    # crane
    window.blit(tilemap.textures['crane'], (200, 150))

    # updating 60 fps
    clock.tick(60)
    pg.display.update()


# run
run = True
while run:


    clock.tick(60)
    draw_game()
    #WIN.blit(LAYOUT, (0,0))

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
            break




    
pg.quit()