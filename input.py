import pygame
def mouse(tile_size):
    mouse_input = pygame.mouse.get_pressed()
    location = (pygame.mouse.get_pos()[0] // tile_size, pygame.mouse.get_pos()[1]// tile_size)  
    return location, mouse_input

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

def select_crop(keys, selected):
    if keys[pygame.K_1]:
        selected = "wheat"
    elif keys[pygame.K_2]:
        selected = "lemon"
    elif keys[pygame.K_3]:
        selected = "watermelon"
    return selected
    

        