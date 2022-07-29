from Lista_Personagens import *

class AlterPerson :
    def __init__(self,classe,nv,xp,xp_up,forc,con,des,int,pontos):
        self.classe = classe
        self.lvl = nv
        self.xp = xp
        self.xp_up =  xp_up
        self.intel = int
        self.des = des
        self.forc = forc
        self.con = con
        self.pontos = pontos
        self.vida , self.poder = self._attr()
    
    def busca (self):
        return [self.lvl,self.xp,self.xp_up,self.vida,self.poder,self.forc,self.con,self.des,self.intel,self.pontos]

    # incremento de XP 
    def _up (self,valor):
        self.xp += valor 
        if self.xp > self.xp_up:
            while self.xp > self.xp_up:
                sobra = self.xp - self.xp_up
                self.lvl +=1
                self.pontos +=5
                self.xp=sobra
                self.xp_up += self.lvl*100
            
        if self.xp == self.xp_up:
            self.xp = 0 
            self.lvl +=1
            self.pontos+=5
            self.xp_up += self.lvl * 100
            return self.pontos
        
        if self.pontos > 0 :
            return self.pontos
        else:
            print("\nVocê não tem pontos de talento para distribuir:\n")
        
    
    def _destribuirPontos(self,id):
        while self.pontos != 0:
            print("\n################################")
            print("\nVocê tem %d pontos de talento:\nOnde deseja colocalos?\n"%(self.pontos))
            x=int(input("1-Força:\n2-Consistencia:\n3-Destreza:\n4-Inteligencia:\n"))
            if x == 1:
                valor= int(input("Quantos pontos em Força?"))
                self.forc += valor 
                self.pontos -=valor
            elif x==2:
                valor =  int(input("Quantos pontos em Consistencia?"))
                self.con += valor 
                self.pontos -=valor
            elif x==3:
                valor = int(input("Quantos pontos em Destreza?"))
                self.des += valor
                self.pontos -=valor
            elif x==4:
                valor = int(input("Quantos pontos em Inteligenca?"))
                self.intel += valor 
                self.pontos -=valor
            else:
                print("insira um valor valido:")
        self.vida , self.poder = id._attr()
        '''if classe == 'Barbaro':
            self.vida , self.poder = id._attr()
        elif classe == 'Ladino':
            self.vida , self.poder = UpLadino._attr()
        elif classe == 'Mago':
            self.vida , self.poder = UpMago._attr()
        else:
            print("não recebi a classe certa!!!")'''
        print("\nNão Existe mais pontos a serem destribuidos:\n")

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
