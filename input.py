import pygame
def mouse(tile_size):
    if pygame.mouse.get_pressed():
        location = (pygame.mouse.get_pos()[0] // tile_size, pygame.mouse.get_pos()[1]// tile_size)  
        return location

def camera(keys, camera):
    if keys[pygame.K_w]:
        camera[1] +=10
    if keys[pygame.K_a]:
        camera[0] +=10
    if keys[pygame.K_s]:
        camera[1] -=10
    if keys[pygame.K_d]:
        camera[0] -=10

    return camera

        