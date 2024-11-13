import pygame
from objects import BlackHole
import setting as s


class Stage:
    def __init__(self, sc) -> None:
        self.screen = sc
        self.PresentStage = s.STAGEMAIN
        self.StageList = [0]
        self.StageList.append( [BlackHole(s.WIDTH/2,s.HEIGHT/2,100,self.screen)] )


    def show(self) -> None:
        if self.PresentStage > 0:                       #스테이지
            for i in self.StageList[self.PresentStage]:
                i.show()

        elif self.PresentStage == s.STAGEMAIN:          #메인
            title = pygame.font.SysFont("Bauhaus 93", 80).render("Space Voyage",True,(255,255,255))
            new_rect = title.get_rect(center=(s.WIDTH/2,s.HEIGHT/4))
            self.screen.blit(title,new_rect)

        elif self.PresentStage == s.STAGELIST:          #스테이지 리스트
            pass

        elif self.PresentStage == s.STAGEALLCLEAR:      #올클리어
            pass