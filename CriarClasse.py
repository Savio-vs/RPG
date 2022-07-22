from Classes import *

def Criar_classe(listaPersonagem):
    print("\n################################")
    nome = input("Nome do personagem:")
   
    print("\n################################")
    print("Escolha sua classe:")
    print('1-Barbaro:')
    print('2-Ladino:')
    print("3-Mago")
    print("################################")
    classe = int(input())
    if classe==1:
        id = Barbaro()
        add(listaPersonagem,id,nome,None)

    elif classe ==2:
        id = Ladino()
        add(listaPersonagem,id,nome,None)
    
    elif classe ==3:
        print("Mago ainda não implementado")
    
    else:
        print("Escolha de classe incorreta:\nTente novamente")