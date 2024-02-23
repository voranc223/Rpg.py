import pygame
from Stuff import *

pygame.init()


class Fighter:
    def __init__(self, x, y, width, height, hp):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hp = hp
        self.jumping = False
        self.vel_y = 0
        self.attacking = False
        self.health = 100
        self.turn = False
        self.rect = pygame.Rect(x, y, self.width, self.height)
        self.attack_cooldown = 0
        self.alive = True

    def draw(self, surface):
        round_over_text = font1.render("ROUND OVER", True, RED)
        round_over_text_rect = round_over_text.get_rect()
        round_over_text_rect.center = (400, 300)
        win_text = font.render("YOU WON", True, BLACK)
        win_text_rect = win_text.get_rect()
        win_text_rect.center = (400, 350)
        pygame.draw.rect(surface, WHITE, self.rect)
        if self.alive == False:
            surface.blit(round_over_text, round_over_text_rect)
            surface.blit(win_text, win_text_rect)




    def attack(self, surface, target):
        if self.rect.centerx > target.rect.centerx:
            self.turn = True
        else:
            self.turn = False
        self.attacking = True
        attack_rect = pygame.Rect(self.rect.centerx - (2 * self.rect.width * self.turn), self.rect.y,
                                  2 * self.rect.width, self.rect.height)
        if attack_rect.colliderect(target.rect):
            target.health -= 10
            if target.health < 0:
                target.health = 0
            if target.health <= 0:
                self.alive = False
        pygame.draw.rect(surface, RED, attack_rect)
        self.attack_cooldown = 30
        self.attacking = False

    def movement(self, screen_width, screen_height, surface, target):
        speed = 8
        gravity = 2
        dx = 0
        dy = 0
        key = pygame.key.get_pressed()
        if self.alive == True:
            if self.attack_cooldown > 0:
                self.attack_cooldown -= 1
            else:
                self.turn = False
            if self.attacking == False and self.attack_cooldown < 14:
                if key[pygame.K_a]:
                    dx -= speed
                if key[pygame.K_d]:
                    dx += speed
                if key[pygame.K_r]:
                    if self.attack_cooldown == 0:
                        self.attack(surface, target)
            if self.attacking == False:
                if key[pygame.K_w] and self.jumping == False:
                    self.vel_y = -30
                    self.jumping = True
            self.vel_y += gravity
            dy += self.vel_y
            if self.rect.left + dx < 0:
                dx = -self.rect.left
            if self.rect.right + dx > screen_width:
                dx = self.rect.right - screen_width
            if self.rect.bottom + dy > screen_height - 20:
                self.vel_y = 0
                self.jumping = False
                dy = screen_height - 20 - self.rect.bottom
            if self.rect.centerx > target.rect.centerx:
                self.turn = True
            else:
                self.turn = False
            self.rect.x += dx
            self.rect.y += dy
