from Lista_Personagens import *

class AlterPerson :
    def __init__(self,classe,nv,xp,forc,con,des,int,pontos):
        self.classe = classe
        self.lvl = nv
        self.xp = xp
        self.intel = int
        self.des = des
        self.forc = forc
        self.con = con
        self.pontos = pontos
        self.vida , self.poder = self._attr()
    
    def busca (self):
        print ("%s nv.%s  %sxp\n\
HP:%s       Power:%s\n\
For:%s      Con:%s\n\
Des:%s      Int:%s\n\
Pontos:%s" %(self.classe,self.lvl,self.xp,self.vida,self.poder,self.forc,self.con,self.des,self.intel,self.pontos))

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
        return (self.forc * 2  + self.con*10), (self.forc *10 + int(self.con/2) + int(self.des/2))
    
    def __str__(self) -> str:
        return "Barbaro;%s;%s;%s;%s;%s;%s;%s;%s;%s;"\
            %(self.lvl,self.xp,self.vida,self.poder,self.forc,self.con,self.des,self.intel,self.pontos)
    
    
class UpLadino(AlterPerson):
    def _attr(self):
        return (self.forc * 2  + self.con*10), (self.forc *10 + int(self.con/2) + int(self.des/2))
    
    def __str__(self) -> str:
        return "Ladino;%s;%s;%s;%s;%s;%s;%s;%s;%s;"\
            %(self.lvl,self.xp,self.vida,self.poder,self.forc,self.con,self.des,self.intel,self.pontos)
    

class UpMago(AlterPerson):
    def _attr(self):
        return (self.forc * 2  + self.con*10), (self.intel*10 + self.des*2)
    
    def __str__(self) -> str:
        return "Mago;%s;%s;%s;%s;%s;%s;%s;%s;%s;"\
            %(self.lvl,self.xp,self.vida,self.poder,self.forc,self.con,self.des,self.intel,self.pontos)
