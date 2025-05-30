import pygame
import random

pygame.init()
dis_width = 500
dis_height = 500
screen = pygame.display.set_mode([dis_width,dis_height])
pygame.display.set_caption('Events')
color = (255,255,255)
bg_color = (255,255,255)
screen.fill(color)

# setup the circle
x = 250
y = 250

dx = 0 
dy = 0

radius = 5
circle_x = 150
circle_y = 150
circle_color = (0,0,0)

# load the image and recite it
pac = pygame.image.load('pacman.png')
pac = pygame.transform.scale(pac,(40,40))

# setup timing variables
clock = pygame.time.Clock()
last_move_time = pygame.time.get_ticks()

def draw_circle():
    pygame.draw.circle(screen,circle_color,[circle_x,circle_y],radius)

while True:
    for event in pygame.event.get():
        if event == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
        elif event.type == pygame.KEYDOWN:
            # move the circle in the direction of the arrow key that is pressed
            if event.key == pygame.K_LEFT:
                dx = -10
                dy = 0
            elif event.key == pygame.K_RIGHT:
                dx = 10
                dy = 0
            elif event.key == pygame.K_DOWN:
                dx = 0
                dy = 10
            elif event.key == pygame.K_UP:
                dx = 0
                dy = -10
            
            # update imager position
            x1 = x+dx
            y1 = y+dy

            # check if the image is inside the screen
            if 0 <= x1 <= dis_width -40 and 0 <= y1 <= dis_height -40:
                x = x1
                y = y1

    current_time = pygame.time.get_ticks()
    if current_time - last_move_time > 5000:
        circle_x = random.randint(0,dis_width)
        circle_y = random.randint(0,dis_height)
    
        last_move_time = current_time

    if x + 40 > circle_x > x -radius and y + 40 > circle_y > y-radius :
        color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
    screen.fill(color)
    draw_circle()
    screen.blit(pac,(x,y))
    pygame.display.update()

    
