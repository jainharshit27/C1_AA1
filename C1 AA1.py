import pygame

pygame.init()

screen = pygame.display.set_mode((400, 600))

while True:
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            
    
    pygame.display.update()
