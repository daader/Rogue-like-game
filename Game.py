import pygame

SCREEN_WIDTH = 800
SCREEN_HIGHT = int(SCREEN_WIDTH * 0.8)

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HIGHT))
clock = pygame.time.Clock()
running = True
player = pygame.image.load('player.bmp').convert()
position_man = ([0,0])

for x in range(10):                    #create 10 objects</i>
    man = GameObject( player , 0*40, 0)
    objects.append(man)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("yellow")

    # RENDER YOUR GAME HERE
    screen.blit( man , position_man)
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
