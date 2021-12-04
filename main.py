import os
import pygame

FPS = 60

WIDTH, HEIGHT = 1280, 960
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Labirynth")
player_width = 55
player_height = 40
start_position_x = 1000
start_position_y = 900


map = pygame.image.load(os.path.join('assets', 'mapa.png'))
player_image = pygame.image.load(os.path.join('assets', 'player.png'))
player_image_transformed = pygame.transform.scale(
    player_image, (player_width, player_height))


def draw_window(player):
    WIN.blit(map, (0, 0))
    WIN.blit(player_image_transformed, (player.x, player.y))
    pygame.display.update()


def main():
    player = pygame.Rect(start_position_x, start_position_y,
                         player_height, player_width)
    clock = pygame.time.Clock()
    clock.tick(FPS)
    game = True
    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
        player.y -= 1
        draw_window(player)
    pygame.quit()


if __name__ == "__main__":
    main()
