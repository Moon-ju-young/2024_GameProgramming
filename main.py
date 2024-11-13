import pygame
from math import sin, cos, radians
import setting as s
from stages import Stage
from objects import SpaceShip

DARK_BLUE = (50, 50, 100)

GameQuit = False
clock = pygame.time.Clock()

pygame.init()                                       #초기화
pygame.display.set_caption("Space Voyage")          #제목
screen = pygame.display.set_mode((s.WIDTH,s.HEIGHT))#화면 크기
stage = Stage(screen)                               #스테이지 구분

player = SpaceShip(s.WIDTH-50,s.HEIGHT-50,screen)

while not GameQuit:
    clock.tick(s.FPS)
    milliseconds = clock.get_time()

    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:           #종료 시
            GameQuit = True 

        elif event.type == pygame.KEYDOWN:      #key 단일 입력
            if stage.PresentStage == s.STAGEMAIN:
                if event.key == pygame.K_SPACE:
                    stage.PresentStage = s.STAGELIST

            elif stage.PresentStage == s.STAGELIST:
                point = 1   #커서?가 가리키는 스테이지
                if event.key == pygame.K_z:
                    stage.PresentStage = s.STAGEMAIN
                elif event.key == pygame.K_SPACE:
                    stage.PresentStage = point


    if stage.PresentStage > 0:
        keys = pygame.key.get_pressed()         #key 지속 입력

        if keys[pygame.K_LEFT]:
            player.angle += milliseconds * 0.1
        if keys[pygame.K_RIGHT]:
            player.angle -= milliseconds * 0.1
            player.angle %= 360
        if keys[pygame.K_UP]:
            player.velx -= sin(radians(player.angle)) * s.SPACESHIP_ACCLERATION * milliseconds
            player.vely -= cos(radians(player.angle)) * s.SPACESHIP_ACCLERATION * milliseconds
        elif keys[pygame.K_DOWN]:
            player.velx += sin(radians(player.angle)) * s.SPACESHIP_ACCLERATION * milliseconds
            player.vely += cos(radians(player.angle)) * s.SPACESHIP_ACCLERATION * milliseconds
    

    screen.fill(DARK_BLUE)
    player.update()
    stage.show()
    player.show()
    
    pygame.display.flip()