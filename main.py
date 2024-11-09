import pygame
from objects import BlackHole

WIDTH = 800
HEIGHT = 800
FPS = 30

DARK_BLUE = (50, 50, 100)

GameQuit = False

pygame.init()                                           #초기화
pygame.display.set_caption("Avoid Blackhole")           #제목
screen = pygame.display.set_mode((WIDTH,HEIGHT))    #화면 크기

while not GameQuit:

    screen.fill(DARK_BLUE)

    for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                GameQuit = True 
    
    pygame.display.update()