from Lista_Personagens import *

class Personagem :
    def __init__(self) -> None:
        self.inteligencia = 5
        self.destreza = 5
        self.forca = 5
        self.consistencia = 5 
        self.xp_atual = 0
        self.lvl = 1
        self.pontos =0
        self.vida,self.poder = self._attr()
        
    def _attr(self):
        return (self.forca   + self.consistencia*2), (self.forca *2 + int(self.consistencia/2) + int(self.destreza/2))
          

class Barbaro(Personagem):
    def _attr(self):
        return (self.forca * 2  + self.consistencia*10), (self.forca *10 + int(self.consistencia/2) + int(self.destreza/2))
    
    def __str__(self) -> str:
        return "Barbaro;%s;%s;%s;%s;%s;%s;%s;%s;%s;"\
            %(self.lvl,self.xp_atual,self.vida,self.poder,self.forca,self.consistencia,self.destreza,self.inteligencia,self.pontos)

class Ladino(Personagem):
    def _attr(self):
        return (self.forca * 2  + self.consistencia*10), (self.forca *10 + int(self.consistencia/2) + int(self.destreza/2))
    
    def __str__(self) -> str:
        return "Ladino;%s;%s;%s;%s;%s;%s;%s;%s;%s;"\
            %(self.lvl,self.xp_atual,self.vida,self.poder,self.forca,self.consistencia,self.destreza,self.inteligencia,self.pontos)

class Mago(Personagem):
    def _attr(self):
        return (self.forca * 2  + self.consistencia*10), (self.inteligencia*10 + self.destreza*2)
    
    def __str__(self) -> str:
        return "Mago;%s;%s;%s;%s;%s;%s;%s;%s;%s;"\
            %(self.lvl,self.xp_atual,self.vida,self.poder,self.forca,self.consistencia,self.destreza,self.inteligencia,self.pontos)