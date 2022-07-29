from telnetlib import GA
from Classes import*
from ClasseInicial import*
from Add_xp import*
from Update_person import *
from criarBD import *
######## Menu Inicial #########

listaPersonagens = Raiz()
x=-1

    
# Menu de açôes.
while x!=0:
    print("################################")
    print("1-Criar novo Personagem:")
    print("2-Procurar Personagem:")
    print("3-Listar Todos Personagens:")
    print("4-Adicionar XP:")
    print("5-Destribuir Pontos de talento:")
    print("0-Sair:")
    print("################################")
    x= int(input())
    
    #criar personagem  OK!!!
    if x == 1:
        Classe_inicial()
    
    #procurar personagem OK!!!
    elif x==2:
        nome = (input("Nome do personagem desejado:"))
        valor = scan(nome)
        if valor != 1:
            print("\nPersonagem não existe:\n")
        else:    
            buscar(nome)

    #Listar todos os personagenm OK!!!
    elif x==3:
        print("\n###Lista de Personagens:###")
        buscar_tds()
        print("\n")

    #adicionar XP ao personagem4 OK!!!!
    elif x==4:
        Ganho_XP()
    
    # distribuir pontos de talentos
    elif x==5:
        nome = input("Qual personagem?\n")
        
        
    elif x==0:
        break
    else:
        print("Digite um valor valido:\n")
