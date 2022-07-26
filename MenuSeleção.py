from Lista_Personagens import *
from Classes import*
from ClasseInicial import*
from Add_xp import*
from Update_person import *

######## Menu Inicial #########

listaPersonagens = Raiz()
x=-1

for linha in open("lista.csv","r"):
    linha = linha.split(';')
    if linha[1] == 'Barbaro':
        id =UpBarbaro(linha[1],int(linha[2]),int(linha[3]),int(linha[6]),int(linha[7]),int(linha[8]),int(linha[9]),int(linha[10]))
        add(listaPersonagens,id,linha[0],None)
    
    elif linha[1] =='Ladino':
        id =UpLadino(linha[1],int(linha[2]),int(linha[3]),int(linha[6]),int(linha[7]),int(linha[8]),int(linha[9]),int(linha[10]))
        add(listaPersonagens,id,linha[0],None)
    
    elif linha[1] == 'Mago':
        id =UpMago(linha[1],int(linha[2]),int(linha[3]),int(linha[6]),int(linha[7]),int(linha[8]),int(linha[9]),int(linha[10]))
        add(listaPersonagens,id,linha[0],None)
    
# Menu de açôes.
while x!=0:
    print("################################")
    print("1-Criar novo Personagem:")
    print("2-Procurar Personagem:")
    print("3-Adicionar XP:")
    print("4-Listar Todos Personagens:")
    print("0-Sair:")
    print("################################")
    x= int(input())
    
    #criar personagem
    if x == 1:
        Classe_inicial(listaPersonagens)
    
    #procurar personagem
    elif x==2:
        listaPersonagens.buscar_personagem(input("Nome do personagem desejado:"))
    
    # Adicionar XP a um personagem    
    elif x==3:
        Ganho_XP(listaPersonagens)
    
    #Listar todos os personagenm
    elif x==4:
        print("################################")
        listaPersonagens.imprimir()

    elif x==0:
        break
    else:
        print("Digite um valor valido:\n")
