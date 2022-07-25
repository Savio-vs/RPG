from Classes import *
from Personagens import *
def Criar_classe(listaPersonagem):
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
        with open ("RPG/lista.txt","a") as arq:
            arq.write("======================================\n")
            arq.write("Nome: " + nome +"    ")
            arq.write(str(id) +"\n")
            
        add(listaPersonagem,id,nome,None)

    elif classe ==2:
        id = Ladino()
        with open ("RPG/lista.txt","a") as arq:
            arq.write("======================================\n")
            arq.write("ID" + id +"\n")
            arq.write("Nome: " + nome + "   ")
            arq.write("Ladino ")

        add(listaPersonagem,id,nome,None)
    
    elif classe ==3:
        id = Mago()
        with open ("RPG/lista.txt","a") as arq:
            arq.write("======================================\n")
            arq.write("ID" + str(id)+"\n")
            arq.write("Nome: " + nome + "   ")
            arq.write("Mago ")
        
        add(listaPersonagem,id,nome,None)
    
    else:
        print("Escolha de classe incorreta:\nTente novamente")