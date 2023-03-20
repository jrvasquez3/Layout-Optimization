import pygame

def scale_image(img, factor):
    size = round(img.get_width() * factor), round(img.get_height() * factor)
    return pygame.transform.scale(img, size)

def blit_rotate_center(win, image, top_left, angle):
    rotateed_image = pygame.transform.rotate(image, angle)
    new_rect = rotateed_image.get_rect(center=image.get_rect(topleft = top_left).center)
    win.blit(rotateed_image, new_rect.topleft)