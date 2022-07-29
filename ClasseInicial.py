from Classes import *
from criarBD import *
import sqlite3 
def Classe_inicial():
    
    valor = 1
    while valor ==1:
        nome = input("Digite o nome:")
        valor = scan(nome)
        if valor == 1 :
            print("Nome já criado:\nTente novamente.")

    
    print("\n################################")
    print("Escolha sua classe:")
    print('1-Barbaro:')
    print('2-Ladino:')
    print("3-Mago")
    print("################################")
    classe = int(input())
   
   #################### corrigir o armazenamento dos objetos ######################
    if classe==1:
        id = Barbaro('Barbaro')  
        lista = [nome]
        lista += id.lista()
        insert(lista)    
        

    elif classe ==2:
        id = Ladino('Ladino')
        lista = [nome]
        lista += id.lista()
        insert(lista)
        
    
    elif classe ==3:
        id = Mago('Mago')
        lista = [nome]
        lista += id.lista()
        insert(lista)
        
    
    else:
        print("Escolha de classe incorreta:\nTente novamente")