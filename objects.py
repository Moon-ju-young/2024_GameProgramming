import pygame
from math import dist
import setting as s

BlackBGImage = pygame.image.load("black_bg.png")
SpaceShipImage = pygame.image.load("spaceship.png")             #기본크기 80x80
SpaceShipImage = pygame.transform.scale(SpaceShipImage, (40,40))#크기 조정

class BlackHole:
    def __init__(self, x:int, y:int, r:int, s:pygame.Surface) -> None:
        '''x좌표, y좌표, 반지름, Surface 입력'''
        self.rad = r//10
        self.ran = r
        self.x = x
        self.y = y
        self.screen = s

    def show(self) -> None:
        BlackBGImage.set_alpha(120)
        self.screen.blit(
            pygame.transform.scale(BlackBGImage, (2*self.ran,2*self.ran)),
            (self.x-self.ran, self.y-self.ran))
        pygame.draw.circle(self.screen, (0,0,0), (self.x,self.y), self.rad)
    
    def gravity_acc(self, x:int, y:int) -> tuple:
        d = dist((x,y), (self.x,self.y))
        if d < self.ran:
            g = s.GRAVITY * (self.ran - d) / self.ran
            xg = g * (self.x - x) / d
            yg = g * (self.y - y) / d
            return (xg, yg)
        else:
            return (0,0)

class SpaceShip:
    def __init__(self,  x:int, y:int, s:pygame.Surface) -> None:
        '''x좌표, y좌표, Surface 입력'''
        self.angle = 45                 #각은 60분법을 사용
        self.x = x
        self.y = y
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
    
    def wall_collision(self) -> bool:
        return (self.x < 0 or self.y < 0 or self.x > s.WIDTH or self.y > s.HEIGHT)