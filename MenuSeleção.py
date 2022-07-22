from Personagens import *
from Classes import*
from CriarClasse import*
from Add_xp import*
######## Menu Inicial #########

listaPersonagens = Raiz()
x=-1
# Menu de açôes.
while x!=0:
    print("################################")
    print("1-Criar novo Personagem:")
    print("2-Deletar personagem")
    print("3-Adicionar XP:")
    print("0-Sair:")
    print("################################")
    x= int(input())
    if x == 1:
        Criar_classe(listaPersonagens)
    
    elif x==2:
        pass
    
    elif x==3:
        Ganho_XP(listaPersonagens)

    elif x==0:
        break
    else:
        print("Digite um valor valido:\n")
