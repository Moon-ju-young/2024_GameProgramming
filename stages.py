import pygame
from math import dist
from objects import BlackHole, SpaceShip
import setting as s


class Stage:
    def __init__(self, sc) -> None:
        self.screen = sc
        self.PresentStage = s.STAGEMAIN
        self.StageList = [0]
        self.point = 0      # main/list에서 가리키는 선택지

        self.StageList.append( [BlackHole(s.WIDTH/2,s.HEIGHT/2,200,self.screen)] )
        self.StageList.append( [BlackHole(s.WIDTH*2/3,s.HEIGHT/3,300,self.screen), 
                                BlackHole(s.WIDTH/4,s.HEIGHT*3/4,100,self.screen)] )
        self.StageList.append( [BlackHole(s.WIDTH/4,s.HEIGHT/2,200,self.screen), 
                                BlackHole(s.WIDTH*3/4,s.HEIGHT/2,200,self.screen)] )
        self.StageList.append( [BlackHole(s.WIDTH/4,s.HEIGHT/2,150,self.screen),
                                BlackHole(s.WIDTH*3/4,s.HEIGHT/2,150,self.screen), 
                                BlackHole(s.WIDTH/2,s.HEIGHT/4,150,self.screen),
                                BlackHole(s.WIDTH/2,s.HEIGHT*3/4,150,self.screen)] )
        self.StageList.append( [BlackHole(s.WIDTH/4,s.HEIGHT/4,150,self.screen),
                                BlackHole(s.WIDTH*3/4,s.HEIGHT/4,150,self.screen), 
                                BlackHole(s.WIDTH/4,s.HEIGHT*3/4,150,self.screen),
                                BlackHole(s.WIDTH*3/4,s.HEIGHT*3/4,150,self.screen)] )
        self.StageList.append( [BlackHole(s.WIDTH/3,s.HEIGHT/3,150,self.screen),
                                BlackHole(s.WIDTH*3/4,s.HEIGHT/4,200,self.screen), 
                                BlackHole(s.WIDTH/4,s.HEIGHT*3/4,200,self.screen),
                                BlackHole(s.WIDTH*2/3,s.HEIGHT*2/3,150,self.screen)] )


    def show(self) -> None:   
        if self.PresentStage > 0:                       #스테이지
            for i in self.StageList[self.PresentStage]:
                i.show()

        elif self.PresentStage == s.STAGEMAIN:          #메인
            # 타이틀
            title = pygame.font.SysFont("Bauhaus 93", 80).render("Space Voyage",True,(255,255,255))
            new_rect = title.get_rect(center=(s.WIDTH/2,s.HEIGHT/4))
            self.screen.blit(title,new_rect)

            LocRatio = [(1/2,5/8),(1/2,3/4),(1/2,7/8)]          #각각의 박스 위치
            # 현재 가리키는 선택지 표시
            box = pygame.Rect(0,0,10+s.WIDTH/3,10+s.HEIGHT/10)
            box.center = (s.WIDTH*LocRatio[self.point][0], s.HEIGHT*LocRatio[self.point][1])
            pygame.draw.rect(self.screen,(255, 255, 255),box)
            # 선택지 박스
            box = pygame.Rect(0,0,s.WIDTH/3,s.HEIGHT/10)
            for i in LocRatio:
                box.center = (s.WIDTH*i[0], s.HEIGHT*i[1])
                pygame.draw.rect(self.screen,(100, 100, 200),box)
            # 텍스트 표시
            text = [] 
            text.append(pygame.font.SysFont("휴먼 엑스포", 40).render("Game Start",True,(255,255,255)))
            text.append(pygame.font.SysFont("휴먼 엑스포", 40).render("How to Play",True,(255,255,255)))
            text.append(pygame.font.SysFont("휴먼 엑스포", 40).render("Quit",True,(255,255,255)))
            for i in range(3):
                new_rect = text[i].get_rect(center=(s.WIDTH*LocRatio[i][0], s.HEIGHT*LocRatio[i][1]))
                self.screen.blit(text[i],new_rect)


        elif self.PresentStage == s.STAGELIST:          #스테이지 리스트
            LocRatio = [(1/4,1/3),(1/2,1/3),(3/4,1/3),(1/4,2/3),(1/2,2/3),(3/4,2/3)]    #각각의 박스 위치
            # 현재 가리키는 스테이지 박스
            box = pygame.Rect(0,0,10+s.WIDTH/6,10+s.WIDTH/6)
            box.center = (s.WIDTH*LocRatio[self.point][0], s.HEIGHT*LocRatio[self.point][1])
            pygame.draw.rect(self.screen,(255, 255, 255),box)
            # 스테이지 박스
            box = pygame.Rect(0,0,s.WIDTH/6,s.WIDTH/6)
            for i in LocRatio:
                box.center = (s.WIDTH*i[0], s.HEIGHT*i[1])
                pygame.draw.rect(self.screen,(100, 100, 200),box)
            for i in range(6):
                text = pygame.font.SysFont("휴먼 엑스포", 50).render(str(i+1),True,(255,255,255))
                new_rect = text.get_rect(center=(s.WIDTH*LocRatio[i][0], s.HEIGHT*LocRatio[i][1]))
                self.screen.blit(text,new_rect)
                

        elif self.PresentStage == s.STAGEALLCLEAR:      #올클리어
            pass

    
    def blackhole_collision(self, s:SpaceShip) -> bool:
        for i in self.StageList[self.PresentStage]:
            if dist((s.x,s.y),(i.x,i.y)) < (10+i.rad):
                return True
        return False
    
    def blackhole_pull(self, s:SpaceShip) -> None:
        for i in self.StageList[self.PresentStage]:
            s.velx += i.gravity_acc(s.x,s.y)[0]
            s.vely += i.gravity_acc(s.x,s.y)[1]