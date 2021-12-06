import os
import pygame
from pygame.constants import K_y

pygame.display.set_caption("Space game")    #NAME OF APP

FPS = 100
VEL = 5
RED = (255,0,0)
MAX_BULLETS = 3
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT)) # SHOWING UP THE WINDOW



def movement_red(keys_pressed, red):
    if keys_pressed[pygame.K_w]: #UP
        if red.y-VEL>0:
            red.y -= VEL
    if keys_pressed[pygame.K_s]:  # DOWN
        if red.y+player_height+VEL<HEIGHT:
            red.y += VEL
    if keys_pressed[pygame.K_d]:  # RIGHT
        if red.x + VEL + player_width < WIDTH:
            red.x += VEL    
    if keys_pressed[pygame.K_a]:  # LEFT
        if red.x - VEL > WIDTH//2:
            red.x -= VEL

def movement_yellow(keys_pressed, yellow):
    if keys_pressed[pygame.K_UP]:
        yellow.y-=VEL
    if keys_pressed[pygame.K_DOWN]:  # DOWN
        yellow.y += VEL
    if keys_pressed[pygame.K_LEFT]:  # RIGHT
        yellow.x -= VEL
    if keys_pressed[pygame.K_RIGHT]:  # LEFT
        yellow.x += VEL
    
player_width = 55
player_height = 40

background = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'space.png')),(WIDTH,HEIGHT))   #loading a background image

yellow_image = pygame.image.load(                                            #loading a yellow ship image
    os.path.join('assets', 'spaceship_yellow.png'))

red_image = pygame.image.load(os
    .path.join('assets', 'spaceship_red.png'))                          # red one

yellow_image_transformed = pygame.transform.rotate(pygame.transform.scale(
    yellow_image, (player_width, player_height)),90)

red_image_transformed = pygame.transform.rotate(pygame.transform.scale(
    red_image, (player_width, player_height)), 270)


def draw_window(red, yellow,red_bullets):
    WIN.blit(background, (0, 0))
    WIN.blit(red_image_transformed, (red.x, red.y))
    WIN.blit(yellow_image_transformed, (yellow.x, yellow.y))
        
    pygame.display.update()
    
red_bullets = []
yellow_bullets = []




def main():
    red = pygame.Rect(700, 100, player_width, player_height)
    yellow = pygame.Rect(100, 300, player_width, player_height)
    clock = pygame.time.Clock()
    
    game = True
    while game:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False

                
        keys_pressed = pygame.key.get_pressed()
        movement_red(keys_pressed, red)
        movement_yellow(keys_pressed,yellow)
        

        draw_window(red,yellow, red_bullets)
    pygame.quit()


if __name__ == "__main__":
    main()
