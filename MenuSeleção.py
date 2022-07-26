from Lista_Personagens import *
from Classes import*
from ClasseInicial import*
from Add_xp import*
from Update_person import UpBarbaro, UpLadino, UpMago

######## Menu Inicial #########

listaPersonagens = Raiz()
x=-1

# Menu de açôes.
while x!=0:
    print("################################")
    print("1-Criar novo Personagem:")
    print("2-Listar Personagens:")
    print("3-Adicionar XP:")
    print("4-teste:")
    print("0-Sair:")
    print("################################")
    x= int(input())
    
    if x == 1:
        Classe_inicial(listaPersonagens)
    
    elif x==2:
        for linha in open("lista.csv","r"):
            linha = linha.split(';')
            print(linha[0],linha[1],linha[2])
        #listaPersonagens.imprimir()
    
    elif x==3:
        Ganho_XP(listaPersonagens)
    elif x==4:
        nome = input ("buscar no banco:")
        leitura = open("lista.csv","r")
        for linha in leitura:
            linha = linha.split(';')
            if linha[0] == nome:
                if linha[1] == 'Barbaro':  
                    id = UpBarbaro(linha[2],linha[3],linha[6],linha[7],linha[8],linha[9],linha[10])
                
                elif linha[1] =='Ladino':
                    id=UpLadino(linha[2],linha[3],linha[6],linha[7],linha[8],linha[9],linha[10])
                
                elif linha[1] == 'Mago':
                    id=UpMago(linha[2],linha[3],linha[6],linha[7],linha[8],linha[9],linha[10])
                
                #add(listaPersonagens,id,nome,None)
                
        leitura.close()
        listaPersonagens.imprimir()
    elif x==0:
        break
    else:
        print("Digite um valor valido:\n")
