from Update_person import *
from criarBD import *

def Ganho_XP(decision):
    cont = 0
    while cont !=1:
        nome=input("\nNome do personagem desejado:")
        cont = scan(nome)
        if cont != 1:
            print("\ninsira um nome valido:")
            

    lista = []
    lista = select(nome) # retorna uma lista com 10 valores, ver valores em criarDB.py
    #print(lista)
    if lista[0] == 'Barbaro':
        
        id = UpBarbaro(lista[0],lista[1],lista[2],lista[3],lista[4],lista[5],lista[6],lista[7],lista[8]) #cria um objeto com apenas 9 valores da lista 
        if decision == 4:
            add_xp(id,lista)
        elif decision == 5:
            distribute(id)
            list_guard = []
            list_guard += id.busca()       # retorna os atributos atualizados do personagem
            list_guard.append(lista[9])  # o valor anteriormente omitido na criação do objeto retorna para a lista

            guardar(list_guard)            # atualiza o Banco com os novos atributos 

    elif lista[0] == 'Ladino':
        
        id = UpLadino(lista[0],lista[1],lista[2],lista[3],lista[4],lista[5],lista[6],lista[7],lista[8])
        if decision == 4:
            add_xp(id,lista)
        elif decision == 5:
            distribute(id)
            list_guard = []
            list_guard += id.busca()       # retorna os atributos atualizados do personagem
            list_guard.append(lista[9])  # o valor anteriormente omitido na criação do objeto retorna para a lista

            guardar(list_guard)            # atualiza o Banco com os novos atributos 

    elif lista[0] == 'Mago':

        id = UpMago(lista[0],lista[1],lista[2],lista[3],lista[4],lista[5],lista[6],lista[7],lista[8]) # 
        if decision == 4:
            add_xp(id,lista)
        elif decision == 5:
            print(id)
            distribute(id)
            print(id)
            list_guard = []
            list_guard += id.busca()       # retorna os atributos atualizados do personagem
            print(list_guard)
            list_guard.append(lista[9])  # o valor anteriormente omitido na criação do objeto retorna para a lista

            guardar(list_guard)            # atualiza o Banco com os novos atributos 


    else:
        print("Ocorreu um erro !!!\n")

def add_xp(id,lista):
    valor=int(input("Valor de xp ganho na campanha:"))
        
    retorno = id._up(valor) #Incrementa a XP no personagem
    if retorno > 0:
        print("*******************")
        print("\nSeu personagem tem pontos de talentos livre.\nDeseja usalos agora?\nY / N: ")
        resposta = input().upper()
        if resposta == "Y":
            id._destribuirPontos(id)
        else:
            pass
    
    list_guard = []
    list_guard += id.busca()       # retorna os atributos atualizados do personagem
    list_guard.append(lista[9])  # o valor anteriormente omitido na criação do objeto retorna para a lista
    

    guardar(list_guard)            # atualiza o Banco com os novos atributos 

def distribute(id):
    pontos = 0
    pontos = id._up(0)
    if pontos != 0:
        id._destribuirPontos(id)
    else:
        print("\nNão existe pontos para serem destribuidos.\n")
     