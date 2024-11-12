from objects import BlackHole
import setting as s

class Stage:
    def __init__(self, sc) -> None:
        self.screen = sc
        self.PresentStage = s.STAGEMAIN
        self.stage = [0]
        self.stage.append( [BlackHole(s.WIDTH/2,s.HEIGHT/2,100,self.screen)] )

    def show(self) -> None:
        if self.PresentStage > 0:
            for i in self.stage[self.PresentStage]:
                i.show()
        elif self.PresentStage == s.STAGEMAIN:
            pass
        elif self.PresentStage == s.STAGELIST:
            pass
        elif self.PresentStage == s.STAGEALLCLEAR:
            pass