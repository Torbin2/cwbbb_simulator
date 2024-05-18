import pygame
def mouse(tile_size, scroll):
    mouse_input = pygame.mouse.get_pressed()
    location = ((pygame.mouse.get_pos()[0] - scroll[0]) // tile_size , (pygame.mouse.get_pos()[1] - scroll[1])// tile_size)  
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

def select_crop(keys, selected, plants):
    plant_keys = list(plants.keys())  
    
    if keys[pygame.K_1] and len(plant_keys) > 0:
        selected = plant_keys[0]
    elif keys[pygame.K_2] and len(plant_keys) > 1:
        selected = plant_keys[1]
    elif keys[pygame.K_3] and len(plant_keys) > 2:
        selected = plant_keys[2]

    return selected

    

        