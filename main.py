import os
import pygame

FPS = 60

WIDTH, HEIGHT = 1280, 960
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Labirynth")
player_width = 55
player_height = 40

VEL = 1

map = pygame.image.load(os.path.join('assets', 'space.png'))
yellow_image = pygame.image.load(
    os.path.join('assets', 'spaceship_yellow.png'))
red_image = pygame.image.load(os.path.join('assets', 'spaceship_red.png'))

yellow_image_transformed = pygame.transform.scale(
    yellow_image, (player_width, player_height))
red_image_transformed = pygame.transform.scale(
    red_image, player_width, player_height)


def draw_window(red, yellow):
    WIN.blit(map, (0, 0))
    WIN.blit(red_image_transformed, (red.x, red.y))
    WIN.blit(yellow_image_transformed, (yellow.x, yellow.y))
    pygame.display.update()


def main():
    red = pygame.Rect(700, 100, player_width, player_height)
    yellow = pygame.Rect(100, 700, player_width, player_height)

    clock = pygame.time.Clock()
    clock.tick(FPS)
    game = True
    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keys_pressed = pygame.key.get_pressed()

            if keys_pressed[pygame.K_DOWN]:  # DOWN
                player.y += VEL
            if keys_pressed[pygame.K_RIGHT]:  # RIGHT
                player.x += VEL
            if keys_pressed[pygame.K_LEFT]:  # LEFT
                player.x -= VEL

        draw_window(player)
    pygame.quit()


if __name__ == "__main__":
    main()
