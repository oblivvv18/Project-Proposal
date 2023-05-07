import pygame
from sys import exit


class Charac(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('graphics/ninjo.png').convert_alpha()
        self.rect = self.image.get_rect(midleft=(610, 420))
        self.grav = 0


pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Naruto Storm 5")
time = pygame.time.Clock()
font = pygame.font.Font('fonts/rrr.ttf', 30)
GOfont = pygame.font.Font(None, 50)

bg_surface = pygame.image.load('graphics/bgbg.png').convert()
tsurf = font.render(
    'BATMAN ARKHAM FOREST', False, 'Black')
GOsurf = font.render('GAME OVER, NINJA', False, 'Yellow')

move_left = False
move_right = False
jumping = False

charac = Charac(610, 420)

enemy = pygame.image.load('graphics/ninjo.png').convert_alpha()
enemyrect = enemy.get_rect(midleft=(1000, 620))

gameon = True
maingame = True
while gameon:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameon = False
        if maingame:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if charac.rect.collidepoint(event.pos) and not jumping:
                    charac.grav = -7
                    jumping = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    move_left = True
                if event.key == pygame.K_w and not jumping:
                    charac.grav = -5
                    jumping = True
                if event.key == pygame.K_d:
                    move_right = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    move_left = False
                if event.key == pygame.K_d:
                    move_right = False
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                maingame = True
                move_left = False
                move_right = False
                jumping = False
                charac_xpos = 615
                charac.rect = charac.image.get_rect(
                    topright=(charac_xpos, 597))
                charac.grav = 0
                enemyrect = enemy.get_rect(midleft=(1000, 620))

    if maingame:
        screen.fill((19, 120, 191))
        screen.blit(bg_surface, (0, 0))
        screen.blit(enemy, enemyrect)
        screen.blit(tsurf, (470, 70))
        enemyrect.x -= 0.5

        if move_left:
            charac.rect.x -= 3
        if move_right:
            charac.rect.x += 3
        if enemyrect.left <= 0:
            enemyrect.right = 1280

        charac.grav += 0.1
        charac.rect.y += charac.grav

        screen.blit(charac.image, charac.rect)
        if charac.rect.x <= 0:
            charac.rect.x = 0

        if charac.rect.right >= 1280:
            charac.rect.x = 1246

        if charac.rect.bottom >= 625:
            charac.rect.bottom = 625
            charac.grav = 0
            jumping = False

        if enemyrect.colliderect(charac.rect):
            maingame = False
    else:
        screen.fill('Purple')
        screen.blit(GOsurf, (470, 310))
    pygame.display.update()
