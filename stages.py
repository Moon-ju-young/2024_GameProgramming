import pygame
from objects import BlackHole
import setting as s


class Stage:
    def __init__(self, sc) -> None:
        self.screen = sc
        self.PresentStage = s.STAGEMAIN
        self.StageList = [0]
        self.StageList.append( [BlackHole(s.WIDTH/2,s.HEIGHT/2,100,self.screen)] )
        self.point = 0      # main/list에서 가리키는 선택지


    def show(self) -> None:
        if self.PresentStage > 0:                       #스테이지
            for i in self.StageList[self.PresentStage]:
                i.show()

        elif self.PresentStage == s.STAGEMAIN:          #메인
            title = pygame.font.SysFont("Bauhaus 93", 80).render("Space Voyage",True,(255,255,255))
            new_rect = title.get_rect(center=(s.WIDTH/2,s.HEIGHT/4))
            self.screen.blit(title,new_rect)

            location = [(s.WIDTH/2,s.HEIGHT*5/8),(s.WIDTH/2,s.HEIGHT*3/4),(s.WIDTH/2,s.HEIGHT*7/8)]
            box = pygame.Rect(0,0,10+s.WIDTH/3,10+s.HEIGHT/10)
            box.center = location[self.point]
            pygame.draw.rect(self.screen,(255, 255, 255),box)
            box = pygame.Rect(0,0,s.WIDTH/3,s.HEIGHT/10)
            for i in location:
                box.center = i
                pygame.draw.rect(self.screen,(100, 100, 200),box)

            text = [] 
            text.append(pygame.font.SysFont("휴먼 엑스포", 40).render("Game Start",True,(255,255,255)))
            text.append(pygame.font.SysFont("휴먼 엑스포", 40).render("How to Play",True,(255,255,255)))
            text.append(pygame.font.SysFont("휴먼 엑스포", 40).render("Quit",True,(255,255,255)))
            for i in range(3):
                new_rect = text[i].get_rect(center=location[i])
                self.screen.blit(text[i],new_rect)

        elif self.PresentStage == s.STAGELIST:          #스테이지 리스트
            pass

        elif self.PresentStage == s.STAGEALLCLEAR:      #올클리어
            pass