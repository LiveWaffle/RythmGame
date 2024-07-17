import pygame

pygame.init
screen = pygame.display.set_mode((540,960))
clock = pygame.time.Clock()
running = True

Background = pygame.image.load("")

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

  



    clock.tick(60)
pygame.quit()