import pygame
from fighter_methods import Fighter
from Stuff import *

pygame.init()
clock = pygame.time.Clock()
fps = 60
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
bg_image = pygame.transform.scale(pygame.image.load('Images/combat_bg_image.png'), (screen_width, screen_height))
fighter_1 = Fighter(200, 430, 64, 150, 100)
fighter_2 = Fighter(536, 430, 64, 150, 100)
score = [0, 0]
last_count_update = pygame.time.get_ticks()
intro_count = 3
round_over = False
ROUND_OVER_COOLDOWN = 2000

def draw_text(text, font, text_col, x, y):
  img = font.render(text, True, text_col)
  screen.blit(img, (x, y))
def helth_bar():
    ratio = (100 - fighter_1.health) / 10 * 30
    pygame.draw.rect(screen, WHITE, (17, 17, 306, 26))
    pygame.draw.rect(screen, WHITE, (477, 17, 306, 26))
    hp_bar_rect_1 = pygame.Rect(20 + ratio, 20, 300 - ratio, 20)
    hp_bar_rect_1_red = pygame.Rect(20, 20, 300, 20)
    hp_bar_rect_2 = pygame.Rect(480, 20, 300 * (fighter_2.health / 100), 20)
    hp_bar_rect_2_red = pygame.Rect(480, 20, 300, 20)
    pygame.draw.rect(screen, RED, hp_bar_rect_1_red)
    pygame.draw.rect(screen, RED, hp_bar_rect_2_red)
    pygame.draw.rect(screen, GREEN, hp_bar_rect_1)
    pygame.draw.rect(screen, YELLOW, hp_bar_rect_2)
    screen.blit(font.render(str(fighter_1.health), True, RED), (330, 15))
    screen.blit(font.render(str(fighter_2.health), True, RED), (400, 15))


run = True
while run:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    screen.blit(bg_image, (0, 0))
    draw_text("P1: " + str(score[0]), font, RED, 20, 60)
    draw_text("P2: " + str(score[1]), font, RED, 700, 60)
    if intro_count <= 0:
        # move fighters
        fighter_1.movement(screen_width, screen_height, screen, fighter_2)
        #fighter_2.movement(screen_width, screen_height, screen, fighter_1)
    else:
        # display count timer
        draw_text(str(intro_count),font, RED, screen_width / 2, screen_height / 3)
        # update count timer
        if (pygame.time.get_ticks() - last_count_update) >= 1000:
            intro_count -= 1
            last_count_update = pygame.time.get_ticks()
    if round_over == False:
        if fighter_1.alive == False:
            score[0] += 1
            round_over = True
            round_over_time = pygame.time.get_ticks()
        if fighter_2.alive == False:
            score[1] += 1
            round_over = True
            round_over_time = pygame.time.get_ticks()
    else:
        if pygame.time.get_ticks() - round_over_time > ROUND_OVER_COOLDOWN:
            round_over = False
            intro_count = 3
            fighter_1 = Fighter(200, 430, 64, 150, 100,)
            fighter_2 = Fighter(536, 430, 64, 150, 100)
    helth_bar()
    fighter_1.draw(screen)
    fighter_2.draw(screen)
    pygame.display.update()
pygame.quit()
