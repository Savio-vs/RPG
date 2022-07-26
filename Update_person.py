from Lista_Personagens import *
class AlterPerson :
    def __init__(self,lvl,xp,forc,con,des,int,pt) -> None:
        self.int = int
        self.des = des
        self.forc = forc
        self.con = con 
        self.xp = xp
        self.lvl = lvl
        self.pontos = pt
        
    # incremento de XP 
    def _up (self,valor):
        xp_up = self.lvl * 100
        self.xp_atual += valor 
        if self.xp_atual > xp_up:
            while self.xp_atual > xp_up:
                sobra = self.xp_atual - xp_up
                self.lvl +=1
                self.pontos +=5
                self.xp_atual=sobra
                xp_up = self.lvl*100
            
        elif self.xp_atual == xp_up:
            self.xp_atual = 0 
            self.lvl +=1
            self.pontos+=5
        else:
            print("\nBUG no up\n")
    
    def _destribuirPontos(self):
        while self.pontos != 0:
            print("Você tem %d pontos de talento:"%(self.pontos))

class UpBarbaro(AlterPerson):
    def _attr(self):
        return (self.forca * 2  + self.consistencia*10), (self.forca *10 + int(self.consistencia/2) + int(self.destreza/2))
    
    def __str__(self) -> str:
        return 0

class UpLadino(AlterPerson):
    def _attr(self):
        return (self.forca * 2  + self.consistencia*10), (self.forca *10 + int(self.consistencia/2) + int(self.destreza/2))
    
    def __str__(self) -> str:
        return 0
class UpMago():
    def _attr(self):
        return (self.forca * 2  + self.consistencia*10), (self.inteligencia*10 + self.destreza*2)
    
    def __str__(self) -> str:
        return 0