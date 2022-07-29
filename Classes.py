from Lista_Personagens import *

class Personagem :
    def __init__(self,classe) -> None:
        self.classe= classe
        self.intel = 5
        self.des = 5
        self.forc = 5
        self.con = 5 
        self.xp_atual = 0
        self.lvl = 1
        self.xp_up = self.lvl*100
        self.pontos =0
        self.vida,self.poder = self._attr()
    
    def _attr(self):
        return (self.forc   + self.con*2), (self.forc *2 + int(self.con/2) + int(self.des/2))
    
    def busca (self):
        print ("%s nv.%s  %sxp\n\
HP:%s       Power:%s\n\
For:%s      Con:%s\n\
Des:%s      Int:%s\n\
Pontos:%s" %(self.classe,self.lvl,self.xp_atual,self.vida,self.poder,self.forc,self.con,self.des,self.intel,self.pontos))

    def lista (self):
        return [self.classe,self.lvl,self.xp_atual,self.xp_up,self.vida,self.poder,self.forc,self.con,self.des,self.intel,self.pontos]
        
class Barbaro(Personagem):
    def _attr(self):
        return (self.forc * 2  + self.con*10), (self.forc *10 + int(self.con/2) + int(self.des/2))
    
    def __str__(self) -> str:
        return "Barbaro;%s;%s;%s;%s;%s;%s;%s;%s;%s;"\
            %(self.lvl,self.xp_atual,self.vida,self.poder,self.forc,self.con,self.des,self.intel,self.pontos)

class Ladino(Personagem):
    def _attr(self):
        return (self.forc * 2  + self.con*10), (self.forc *10 + int(self.con/2) + int(self.des/2))
    
    def __str__(self) -> str:
        return "Ladino;%s;%s;%s;%s;%s;%s;%s;%s;%s;"\
            %(self.lvl,self.xp_atual,self.vida,self.poder,self.forc,self.con,self.des,self.intel,self.pontos)

class Mago(Personagem):
    def _attr(self):
        return (self.forc * 2  + self.con*10), (self.intel*10 + self.des*2)
    
    def __str__(self) -> str:
        return "Mago;%s;%s;%s;%s;%s;%s;%s;%s;%s;"\
            %(self.lvl,self.xp_atual,self.vida,self.poder,self.forc,self.con,self.des,self.intel,self.pontos)