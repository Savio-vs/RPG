from Personagens import *
from Classes import*

########inicio das chamadas#########

listaPersonagens = Raiz()
x=-1
# Menu de açôes.
while x!=0:
    print("################################")
    print("1-Criar novo Personagem:")
    print("2-Deletar personagem")
    print("0-Sair:")
    x= int(input())
    print("################################")
    if x==0:
        break
    print("\n################################")
    nome = input("Nome do personagem:")
    print("################################")
    print("\n################################")
    print("\nEscolha sua classe:")
    print('1-Barbaro:')
    print('2-Ladino:')
    print("3-Mago")
    classe = int(input())
    print("################################")
    print("\n################################")
    i = int(input("\nPontos de Inteligencia:"))
    d = int(input("Pontos de destresa:"))
    f = int(input("Pontos de Força:"))
    c = int(input("Pontos de Consistencia:"))
    print("################################")
    
    if classe==1:
        id = Barbaro(i,d,f,c)
        add(listaPersonagens,id,nome,None)

    elif classe ==2:
        id = Ladino(i,d,f,c)
        add(listaPersonagens,id,nome,None)
    elif classe ==3:
        print("Mago ainda não implementado")
    else:
        print("Escolha de classe incorreta:\nTente novamente")
    

#listaPersonagens.imprimir() # lista os personagens criados 
#listaPersonagens.buscar_personagem(input("Buscar um personagem:"))
nome = input("Nome do personagem:")
xp = int(input("xp ganha:"))
listaPersonagens.Upper(nome,xp)
listaPersonagens.buscar_personagem(nome)