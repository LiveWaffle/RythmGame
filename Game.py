import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((540, 960))
clock = pygame.time.Clock()
running = True

background = pygame.image.load("background.png")
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(background, (0, 0))

    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()