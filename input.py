import pygame
def mouse_plantside(tile_size, scroll):
    mouse_input = pygame.mouse.get_pressed()
    location = ((pygame.mouse.get_pos()[0] - scroll[0]) // tile_size , (pygame.mouse.get_pos()[1] - scroll[1])// tile_size)  
    return location, mouse_input

def mouse_upgrades(plants):
    mouse_input = pygame.mouse.get_pressed()
    selected = (pygame.mouse.get_pos()[1] -len(plants)*30 - 25) // 64
    return selected, mouse_input


def camera(keys, camera):
    if keys[pygame.K_w]:
        camera[1] +=10
    if keys[pygame.K_a]:
        camera[0] +=10
    if keys[pygame.K_s]:
        camera[1] -=10
    if keys[pygame.K_d]:
        camera[0] -=10
   
    if keys[pygame.K_q]:
        camera[0] +=50
    if keys[pygame.K_e]:
        camera[0] -=50
    
    if keys[pygame.K_SPACE]:
        camera = [0,0]
    return camera

def select_crop(keys, selected, plants):
    plant_keys = list(plants.keys())
    for i in range(9):
        key = getattr(pygame, f'K_{i}')  
        if keys[key] and len(plant_keys) >= i:
            selected = plant_keys[i - 1]  
    return selected

    

        