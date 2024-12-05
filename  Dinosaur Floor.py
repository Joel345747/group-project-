import pygame

# Variable

game_speed = 5


# Surfaces

ground = pygame.image.load("ground.png")
ground = pygame.transform.scale(ground, (1280, 20))
ground_x = 0
ground_rect = ground.get_rect(center=(640, 400))

ground_x -= game_speed
screen.blit(ground, (ground_x, 360))
screen.blit(ground, (ground_x + 1280, 360))
if ground_x <= -1280:
            ground_x = 0

    
