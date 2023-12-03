import pygame 

pygame.init() 

screen_hight = 800
screen_width = screen_hight*0.8
screen_color = (255,255,255) 

screen = pygame.display.set_mode((screen_hight, screen_width))

player_x = 400
player_y = player_x*0.8
player_higth = 30
player_width = 30
player_color = (255,0,0) 
player_speed = 1

player = pygame.Rect(player_x, player_y, player_higth, player_width)


exit = False

while not exit: 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            exit = True

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player.x -= player_speed
    if keys[pygame.K_RIGHT]:
        player.x += player_speed
    if keys[pygame.K_UP]:
        player.y -= player_speed
    if keys[pygame.K_DOWN]:
        player.y += player_speed

    screen.fill(screen_color)

    pygame.draw.rect(screen, player_color, player) 

    pygame.display.update()