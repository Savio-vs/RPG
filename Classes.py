from Personagens import *
class Personagem :
    def __init__(self,int,dex,forc,con) -> None:
        self.inteligencia = int
        self.destreza = dex
        self.forca = forc
        self.consistencia = con 
        self.xp_atual = 0
        self.lvl = 1
        self.vida,self.poder = self._attr()

    def _attr(self):
        return (self.forca * 2 + self.destreza), (self.forca *2)
    
    def __str__(self) -> str:
        return "Classe: Iniciante \nVida = %s \nPoder = %s\nForça = %s\nDestreza = %s\nInteligencia = %s"\
                %(self.vida,self.poder,self.forca,self.destreza,self.inteligencia)
    
    # incremento de XP :
    def _up (self,valor):
        xp_up = self.lvl * 100
        self.xp_atual += valor 
        if self.xp_atual > xp_up:
            while self.xp_atual > xp_up:
                sobra = self.xp_atual - xp_up
                self.lvl +=1
                self.xp_atual=sobra
                xp_up = self.lvl*100
            
        elif self.xp_atual == xp_up:
            self.xp_atual = 0 
            self.lvl +=1
        else:
            print("\nBUG no up\n")

class Barbaro(Personagem):
    def _attr(self):
        return (self.forca * 2  + self.consistencia*10), (self.forca *10 + self.consistencia/2 + self.destreza/2)
    def __str__(self) -> str:
        return "Classe: Barbaro lvl %s \nVida = %s \nPoder = %s\nForça = %s\nDestreza = %s\nInteligencia = %s"\
                %(self.lvl,self.vida,self.poder,self.forca,self.destreza,self.inteligencia)

class Ladino(Personagem):
    def _attr(self):
        return (self.forca * 2  + self.consistencia*10), (self.forca *10 + self.consistencia/2 + self.destreza/2)
    def __str__(self) -> str:
        return "Classe: Ladino lvl %s \nVida = %s \nPoder = %s\nForça = %s\nDestreza = %s\nInteligencia = %s"\
                %(self.lvl,self.vida,self.poder,self.forca,self.destreza,self.inteligencia)

class Mago(Personagem):
    def _attr(self):
        return (self.forca * 2  + self.consistencia*10), (self.inteligencia*10 + self.destreza*2)
    def __str__(self) -> str:
        return "Classe: Ladino lvl %s \nVida = %s \nPoder = %s\nForça = %s\nDestreza = %s\nInteligencia = %s"\
                %(self.lvl,self.vida,self.poder,self.forca,self.destreza,self.inteligencia)
        