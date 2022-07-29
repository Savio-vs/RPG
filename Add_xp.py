from Update_person import *
from criarBD import *

def Ganho_XP():
    cont = 0
    while cont !=1:
        nome=input("\nNome do personagem desejado:")
        cont = scan(nome)
        if cont != 1:
            print("\ninsira um nome valido:")
            

    lista = []
    lista = select(nome) # retorna uma lista com 9 valores, ver valores em criarDB.py
    #print(lista)
    if lista[0] == 'Barbaro':
        
        id = UpLadino(lista[0],lista[1],lista[2],lista[3],lista[4],lista[5],lista[6],lista[7]) #cria um objeto com apenas 8 valores da lista 
        add_xp(id,lista)
    
    elif lista[0] == 'Ladino':
        
        id = UpLadino(lista[0],lista[1],lista[2],lista[3],lista[4],lista[5],lista[6],lista[7])
        add_xp(id,lista)

    elif lista[0] == 'Mago':

        id = UpLadino(lista[0],lista[1],lista[2],lista[3],lista[4],lista[5],lista[6],lista[7]) # 
        add_xp(id,lista)

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
            id._destribuirPontos(lista[0])
        else:
            pass
    
    list_guard = []
    list_guard += id.busca()       # retorna os atributos atualizados do personagem
    list_guard.append(lista[8])  # o valor anteriormente omitido na criação do objeto retorna para a lista
    
    guardar(list_guard)            # atualiza o Banco com os novos atributos 