import pygame
pygame.init()
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

font = pygame.font.SysFont('Calibri', 40, True, False)
font1 = pygame.font.SysFont('Calibri', 80, True, False)

Warrior_attack_1 = pygame.image.load('Images/Sprites/Attack1.png').convert_alpha()
Warrior_attack_2 = pygame.image.load('Images/Sprites/Attack2.png').convert_alpha()
Warrior_death = pygame.image.load('Images/Sprites/Death.png').convert_alpha()
Warrior_idle = pygame.image.load('Images/Sprites/Idle.png').convert_alpha()
Warrior_jump = pygame.image.load('Images/Sprites/Jump.png').convert_alpha()
Warrior_run = pygame.image.load('Images/Sprites/Run.png').convert_alpha()
Warrior_Take_hit = pygame.image.load('Images/Sprites/Take hit.png').convert_alpha()
Warrior_Fall = pygame.image.load('Images/Sprites/Fall.png').convert_alpha()
