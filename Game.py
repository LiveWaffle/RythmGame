import pygame

pygame.init()
screen = pygame.display.set_mode((540, 960))
clock = pygame.time.Clock()
running = True

background = pygame.image.load("background.png")
Abutton = pygame.image.load("Abutton.png")
Abuttonpressed = pygame.image.load("PressedA.png")

screen_width, screen_height = screen.get_size()
button_width, button_height = Abutton.get_size()

button_x = (screen_width - button_width) / 2
button_y = (screen_height - button_height) / 2

button_image = Abutton
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if event.type == pygame.MOUSEBUTTONDOWN:
            button_image = Abuttonpressed
    elif event.type == pygame.MOUSEBUTTONUP:
        button_image = Abutton

    screen.blit(background, (0, 0))
    screen.blit(button_image, (button_x, button_y))

    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
