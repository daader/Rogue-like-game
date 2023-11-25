
import pygame 
import sys

pygame.init() 

screen_hight = 800
screen_width = screen_hight*0.8
pygame.display.set_caption("Moving Rectangle")

position_x = 400
position_y = position_x*0.8

rect_higth = 30
rect_width = 30

color = (255,255,255) 
rect_color = (255,0,0) 
rect_speed = 1
rect = pygame.Rect(position_x,position_y,rect_higth,rect_width)
screen = pygame.display.set_mode((rect_width,rect_higth))

# CREATING CANVAS 
canvas = pygame.display.set_mode((screen_hight, screen_width)) 
  
# TITLE OF CANVAS 
pygame.display.set_caption("My Board")  
  
exit = False
  
while not exit: 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            exit = True
            sys.exit()

    keys = pygame.key.get_pressed()
    # Check for arrow key inputs
    if keys[pygame.K_LEFT]:
        rect.x -= rect_speed
    if keys[pygame.K_RIGHT]:
        rect.x += rect_speed
    if keys[pygame.K_UP]:
        rect.y -= rect_speed
    if keys[pygame.K_DOWN]:
        rect.y += rect_speed

    screen.fill('black')

    pygame.draw.rect(canvas, rect_color, rect) 

    pygame.display.update()