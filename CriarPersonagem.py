from Personagens import *
class Personagem :
    def __init__(self,int,dex,forc) -> None:
        self.inteligencia = int
        self.destreza = dex
        self.forca = forc
        self.vida,self.poder = self._attr()

    def _attr(self):
        return (self.forca * 2 + self.destreza), (self.forca *2)
    def __str__(self) -> str:
        return 'Iniciante \nVida = %s \nPoder = %s\n'%(self.vida,self.poder)

class Barbaro(Personagem):
    def _attr(self):
        return (self.forca * 10 + self.destreza), (self.forca *20)
    def __str__(self) -> str:
        return "Barbaro \nVida = %s \nPoder = %s\n"\
                %(self.vida,self.poder)
listaPersonagens = Raiz()
x=-1
# Menu de açôes.
while x!=0:
    print("1-Criar novo Personagem:")
    print("2-Deletar personagem")
    print("0-Sair:")
    x= int(input())
    if x==0:
        break
    nome = input("Nome do personagem:")
    print("Escolha sua classe:")
    print('1-Barbaro:')
    print('2-Ladino:')
    classe = int(input())
    i = int (input("Pontos de Inteligencia:"))
    d = int (input("Pontos de destresa:"))
    f = int (input("Pontos de Força:"))
    if classe==1:
        id = Barbaro(i,d,f)
        add(listaPersonagens,id,nome,None)

    elif classe ==2:
        pass
    else:
        print("Escolha de classe incorreta:\nTente novamente")
    

listaPersonagens.imprimir() # lista os personagens criados 

