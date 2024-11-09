import pygame
from math import cos, sin

GRAVITY = 50
BlackBGImage = pygame.image.load("dark.png")

class BlackHole:
    def __init__(self, xy, r:int, s:pygame.Surface):
        '''sequence 형태로 xy좌표 위치와 반지름, Surface 입력'''
        self.rad = r//10
        self.ran = r
        self.x = xy[0]
        self.y = xy[1]
        self.screen = s

    def show(self):
        self.screen.blit(
            pygame.transform.scale(BlackBGImage, (2*self.ran,2*self.ran)),
            (self.x-self.ran, self.y-self.ran))
        pygame.draw.circle(self.screen, (0,0,0), (self.x,self.y), self.rad)
    
    def gravity_acc(self, xy) -> tuple:
        return ()