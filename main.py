import pygame
from math import sin, cos, radians
from objects import BlackHole, SpaceShip

WIDTH = 800
HEIGHT = 800
FPS = 60

SPACESHIP_ACCLERATION = 0.0005

DARK_BLUE = (50, 50, 100)

GameQuit = False
clock = pygame.time.Clock()

pygame.init()                                       #초기화
pygame.display.set_caption("Avoid Blackhole")       #제목
screen = pygame.display.set_mode((WIDTH,HEIGHT))    #화면 크기

player = SpaceShip(500,500,screen)

while not GameQuit:
    clock.tick(FPS)

    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            GameQuit = True 

    milliseconds = clock.get_time()
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player.angle += milliseconds * 0.1
    if keys[pygame.K_RIGHT]:
        player.angle -= milliseconds * 0.1
    player.angle %= 360
    if keys[pygame.K_UP]:
        player.velx -= sin(radians(player.angle)) * SPACESHIP_ACCLERATION * milliseconds
        player.vely -= cos(radians(player.angle)) * SPACESHIP_ACCLERATION * milliseconds
    elif keys[pygame.K_DOWN]:
        player.velx += sin(radians(player.angle)) * SPACESHIP_ACCLERATION * milliseconds
        player.vely += cos(radians(player.angle)) * SPACESHIP_ACCLERATION * milliseconds

    screen.fill(DARK_BLUE)
    player.update()
    player.show()
    
    pygame.display.flip()