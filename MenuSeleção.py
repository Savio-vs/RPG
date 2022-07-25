from Personagens import *
from Classes import*
from CriarClasse import*
from Add_xp import*

######## Menu Inicial #########

listaPersonagens = Raiz()
x=-1


'''lista_personagens = open ("RPG/lista.txt","r")
if lista_personagens != None:
    for line in lista_personagens:
        print(line)'''
leitura = open("RPG/lista.txt","r")
for linha in leitura:
    if linha == "======================================\n":
        linha = leitura.readline()
        lista = linha.split()
            
leitura.close()

# Menu de açôes.
while x!=0:
    print("################################")
    print("1-Criar novo Personagem:")
    print("2-Listar Personagens:")
    print("3-Adicionar XP:")
    print("0-Sair:")
    print("################################")
    x= int(input())
    
    if x == 1:
        Criar_classe(listaPersonagens)
    
    elif x==2:
        
        '''for i in leitura:
            if i == "======================================\n":
                linha = leitura.readline()          # 'linha' contém a proxima linha dentro do arquivo quando a sequencia de caracteres acima for encontrada .
                lista= linha.split()                # 'lista' é um array onde cada posição contém uma palavra de 'linha'. 
                print(lista[1])
                break''' 
        listaPersonagens.imprimir()
    
    elif x==3:
        Ganho_XP(listaPersonagens)

    elif x==0:
        break
    else:
        print("Digite um valor valido:\n")
