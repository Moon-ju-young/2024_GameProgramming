import pygame
from math import dist

GRAVITY = 50
BlackBGImage = pygame.image.load("black_bg.png")
SpaceShipImage = pygame.image.load("spaceship.png")             #기본크기 80x80
SpaceShipImage = pygame.transform.scale(SpaceShipImage, (40,40))#크기 조정

class BlackHole:
    def __init__(self, xy, r:int, s:pygame.Surface) -> None:
        '''sequence 형태로 xy좌표 위치와 반지름, Surface 입력'''
        self.rad = r//10
        self.ran = r
        self.xy = (xy[0], xy[1])
        self.screen = s

    def show(self) -> None:
        BlackBGImage.set_alpha(120)
        self.screen.blit(
            pygame.transform.scale(BlackBGImage, (2*self.ran,2*self.ran)),
            (self.x-self.ran, self.y-self.ran))
        pygame.draw.circle(self.screen, (0,0,0), self.xy, self.rad)
    
    def gravity_acc(self, xy) -> tuple:
        d = dist(xy, self.xy)
        if d < self.ran:
            g = GRAVITY * (self.ran - d) / self.ran
            xg = g * (self.xy[0] - xy[0]) / d
            yg = g * (self.xy[1] - xy[1]) / d
            return (xg, yg)
        else:
            return (0,0)

class SpaceShip:
    def __init__(self, xy, s:pygame.Surface) -> None:
        '''sequence 형태로 xy좌표 위치와 Surface 입력'''
        self.angle = 45                 #각은 60분법을 사용
        self.x = xy[0]
        self.y = xy[1]
        self.velx = 0
        self.vely = 0
        self.screen = s
    
    def show(self) -> None:
        RotateSpaceShip = pygame.transform.rotate(SpaceShipImage, self.angle)
        new_rect = RotateSpaceShip.get_rect(center=(self.x,self.y))
        self.screen.blit(RotateSpaceShip,new_rect)

    def update(self) -> None:
        self.x += self.velx
        self.y += self.vely