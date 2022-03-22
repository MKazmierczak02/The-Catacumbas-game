import os
import pygame
pygame.font.init()

pygame.display.set_caption("Space game")  # NAME OF APP

FPS = 100
VEL = 5
RED = (255, 0, 0)
MAX_BULLETS = 3
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))  # SHOWING UP THE WINDOW
WINNER_FONT = pygame.font.SysFont("comicsans", 80)
HEALTH_FONT = pygame.font.SysFont("comicsans", 40)

border = pygame.Rect(WIDTH//2-5, 0, 10, HEIGHT)

BULLET_VEL =5
MAX_BULLETS =3


YELLOW_HIT = pygame.USEREVENT + 1
RED_HIT = pygame.USEREVENT + 2


def draw_winner(text):
    draw_text = WINNER_FONT.render(text, 1, 'WHITE')
    WIN.blit(draw_text, (WIDTH//2-draw_text.get_width()//2,
             HEIGHT//2 - draw_text.get_height()//2))
    pygame.display.update()
    pygame.time.delay(5000)


def movement_red(keys_pressed, red):
    if keys_pressed[pygame.K_UP]:  # UP
        if red.y-VEL > 0:
            red.y -= VEL
    if keys_pressed[pygame.K_DOWN]:  # DOWN
        if red.y+player_height+VEL < HEIGHT:
            red.y += VEL
    if keys_pressed[pygame.K_RIGHT]:  # RIGHT
        if red.x + VEL + player_width < WIDTH+20:
            red.x += VEL
    if keys_pressed[pygame.K_LEFT]:  # LEFT
        if red.x - VEL > WIDTH//2:
            red.x -= VEL


def movement_yellow(keys_pressed, yellow):
    if keys_pressed[pygame.K_w]:
        if yellow.y - VEL > 0:
            yellow.y -= VEL
    if keys_pressed[pygame.K_s]:  # DOWN
        if yellow.y + VEL + player_height < HEIGHT:
            yellow.y += VEL
    if keys_pressed[pygame.K_a]:  # LEFT
        if yellow.x - VEL > 0:
            yellow.x -= VEL
    if keys_pressed[pygame.K_d]:  # RIGHT
        if yellow.x+VEL+player_width < WIDTH/2+10:
            yellow.x += VEL


player_width = 55
player_height = 40

background = pygame.transform.scale(pygame.image.load(os.path.join(
    'assets', 'space.png')), (WIDTH, HEIGHT))  # loading a background image

yellow_image = pygame.image.load(  # loading a yellow ship image
    os.path.join('assets', 'spaceship_yellow.png'))

red_image = pygame.image.load(os
                              .path.join('assets', 'spaceship_red.png'))                          # red one

yellow_image_transformed = pygame.transform.rotate(pygame.transform.scale(
    yellow_image, (player_width, player_height)), 90)

red_image_transformed = pygame.transform.rotate(pygame.transform.scale(
    red_image, (player_width, player_height)), 270)


def draw_window(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health):
    WIN.blit(background, (0, 0))
    pygame.draw.rect(WIN, 'BLACK', border)
    yellow_health_text = HEALTH_FONT.render(
        "Health: " + str(yellow_health), 1, 'WHITE')
    red_health_text = HEALTH_FONT.render(
        "Health: " + str(red_health), 1, 'WHITE')
    WIN.blit(red_health_text, (WIDTH - red_health_text.get_width() - 10, 5))
    WIN.blit(yellow_health_text, (10, 5))

    WIN.blit(red_image_transformed, (red.x, red.y))
    WIN.blit(yellow_image_transformed, (yellow.x, yellow.y))

    for bullet in red_bullets:
        pygame.draw.rect(WIN, RED, bullet)
    for bullet in yellow_bullets:
        pygame.draw.rect(WIN, 'YELLOW', bullet)

    pygame.display.update()


def handle_bullets(red_bullets, yellow_bullets, red, yellow):
    for bullet in red_bullets:
        bullet.x -= BULLET_VEL
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            red_bullets.remove(bullet)
        if bullet.x < 0:
            red_bullets.remove(bullet)
    for bullet in yellow_bullets:
        bullet.x += BULLET_VEL
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(RED_HIT))
            yellow_bullets.remove(bullet)
        if bullet.x > WIDTH:
            yellow_bullets.remove(bullet)


red_bullets = []
yellow_bullets = []


def main():
    red = pygame.Rect(800, HEIGHT//2, player_width, player_height)
    yellow = pygame.Rect(100, HEIGHT//2, player_width, player_height)
    clock = pygame.time.Clock()
    yellow_health = 5
    red_health = 5
    winner_text = ""

    game = True
    while game:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RCTRL and len(red_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(
                        red.x, red.y+player_height//2-2, 10, 5)
                    red_bullets.append(bullet)
                if event.key == pygame.K_LCTRL and len(yellow_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(
                        yellow.x+player_width, yellow.y+player_height//2-2, 10, 5)
                    yellow_bullets.append(bullet)

            if event.type == RED_HIT:
                red_health -= 1
            if event.type == YELLOW_HIT:
                yellow_health -= 1

        if red_health <= 0:
            winner_text = "YELLOW WINS"

        if yellow_health <= 0:
            winner_text = "RED WINS"

        if winner_text != "":
            draw_winner(winner_text)
            break
        keys_pressed = pygame.key.get_pressed()
        movement_red(keys_pressed, red)
        movement_yellow(keys_pressed, yellow)
        handle_bullets(red_bullets, yellow_bullets, red, yellow)
        draw_window(red, yellow, red_bullets, yellow_bullets,
                    red_health, yellow_health)
    main()


if __name__ == "__main__":
    main()
