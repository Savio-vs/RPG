from Classes import *
from Lista_Personagens import *
def Classe_inicial(listaPersonagem):
    print("\n################################")
    nome = input("Nome do personagem:")
   
    print("\n################################")
    print("Escolha sua classe:")
    print('1-Barbaro:')
    print('2-Ladino:')
    print("3-Mago")
    print("################################")
    classe = int(input())
   
   #################### corrigir o armazenamento dos objetos ######################
    if classe==1:
        id = Barbaro()  
        with open ("lista.csv","a") as arq:
            arq.write('\n'+nome +";")
            arq.write(str(id))
            
        add(listaPersonagem,id,nome,None)

    elif classe ==2:
        id = Ladino()
        with open ("lista.csv","a") as arq:
            arq.write('\n'+nome +";")
            arq.write(str(id))

        add(listaPersonagem,id,nome,None)
    
    elif classe ==3:
        id = Mago()
        with open ("lista.csv","a") as arq:
            arq.write('\n'+nome +";")
            arq.write(str(id))
        
        add(listaPersonagem,id,nome,None)
    
    else:
        print("Escolha de classe incorreta:\nTente novamente")