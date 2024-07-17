import pygame

pygame.init()
pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=512, devicename=None,)
screen = pygame.display.set_mode((540, 960))
clock = pygame.time.Clock()
running = True

background = pygame.image.load("background.png")
Abutton = pygame.image.load("Abutton.png")
Abuttonpressed = pygame.image.load("PressedA.png")
click_sound = pygame.mixer.Sound("button.mp3")
played = False

screen_width, screen_height = screen.get_size()
button_width, button_height = Abutton.get_size()

button_x = (screen_width - button_width) / 2
button_y = (screen_height - button_height) / 2

button_image = Abutton
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                button_image = Abuttonpressed
                if not played:
                    click_sound.play()
                    played = True
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                button_image = Abutton
                played = False


    screen.blit(background, (0, 0))
    screen.blit(button_image, (button_x, button_y))

    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
