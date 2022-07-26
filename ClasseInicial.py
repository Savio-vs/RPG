from Classes import *
from Lista_Personagens import *
def Classe_inicial(listaPersonagem):
    x = True
    while x :
        x = False
        busca = open("lista.csv","r")
        print("\n################################")
        nome = input("Nome do personagem:")
        print("################################")
        for linha in busca:
            linha = linha.split(';')
            if linha[0] == nome:
                print ("\nNome já cadastrado.\nTente tente novamente.")
                x = True
                break
        
    
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
        with open ("lista.csv","a") as arq:
            arq.write('\n'+nome +";")
            arq.write(str(id))
            
        add(listaPersonagem,id,nome,None)

    elif classe ==2:
        id = Ladino('Ladino')
        with open ("lista.csv","a") as arq:
            arq.write('\n'+nome +";")
            arq.write(str(id))

        add(listaPersonagem,id,nome,None)
    
    elif classe ==3:
        id = Mago('Mago')
        with open ("lista.csv","a") as arq:
            arq.write('\n'+nome +";")
            arq.write(str(id))
        
        add(listaPersonagem,id,nome,None)
    
    else:
        print("Escolha de classe incorreta:\nTente novamente")