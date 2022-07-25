from Personagens import *

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
        with open ("RPG/lista.txt","a") as arq:
            arq.write("LVL: " + str (self.lvl) +"       ")
            arq.write("XP: " + str (self.xp_atual) +"\n")
            arq.write("Vida: " +  str (self.vida) +"        ")
            arq.write("Poder: " + str (self.poder) +"\n")
            arq.write("For: " + str (self.forca)+"      ")
            arq.write("Con: " + str (self.consistencia)+"\n")
            arq.write("Des: " + str (self.destreza) +"      ")
            arq.write("Int: " + str (self.inteligencia) +"\n")
            arq.write("Pontos de talento: " + str (self.pontos) +"\n")
            arq.write("================================\n")

    def _attr(self):
        return (self.forca   + self.consistencia*2), (self.forca *2 + int(self.consistencia/2) + int(self.destreza/2))

    # incremento de XP :
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
          

class Barbaro(Personagem):
    def _attr(self):
        return (self.forca * 2  + self.consistencia*10), (self.forca *10 + int(self.consistencia/2) + int(self.destreza/2))
    
    def __str__(self) -> str:
        return "Classe: Barbaro lvl %s\nPontos de atributos livre = %s\
            \nHP = %s           Power = %s\
            \nFor = %s          Con = %s \
            \nDes = %s          Int = %s"\
            %(self.lvl,self.pontos,self.vida,self.poder,self.forca,self.consistencia,self.destreza,self.inteligencia)

class Ladino(Personagem):
    def _attr(self):
        return (self.forca * 2  + self.consistencia*10), (self.forca *10 + int(self.consistencia/2) + int(self.destreza/2))
    
    def __str__(self) -> str:
        return "Classe: Ladino lvl %s \nPontos de atributos livre = %s\
            \nHP = %s           Power = %s\
            \nFor = %s          Con = %s \
            \nDes = %s          Int = %s"\
            %(self.lvl,self.pontos,self.vida,self.poder,self.forca,self.consistencia,self.destreza,self.inteligencia)

class Mago(Personagem):
    def _attr(self):
        return (self.forca * 2  + self.consistencia*10), (self.inteligencia*10 + self.destreza*2)
    
    def __str__(self) -> str:
        return "Classe: Mago lvl %s \nPontos de atributos livre = %s\
            \nHP = %s           Power = %s\
            \nFor = %s          Con = %s \
            \nDes = %s          Int = %s"\
            %(self.lvl,self.pontos,self.vida,self.poder,self.forca,self.consistencia,self.destreza,self.inteligencia)
        