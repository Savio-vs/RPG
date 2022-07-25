
class No:
    def __init__(self,id,nome,back,next) -> None:
        self.id = id        #ponteiro para um Obejeto de Personagem 
        self.nome = nome
        self.back = back
        self.next = next
        

class Raiz:
    def __init__(self) -> None:
        self.root = None
        self.next = None
        self.back = None
    def imprimir (self): # lista os personagens criados 
        if self.root != None:
            item = self.root
            if item.next != None:
                next = item.next
                next.imprimir()
                print(item.nome)
            else:
                print(item.nome)
        else:
            print("ocorreu um erro!!")
   
    def buscar_personagem(self,nome):
        id = self.root
        if id.nome == nome:
            print("##############################")
            print("Personagem: ",id.nome,"\n",id.id) # .id  é um objeto da classe personagem 
        else:
            id = id.next
            id.buscar_personagem(nome)
           
    #adicionar um valor de xp ao personagem
    def Upper(self,nome,xp):
        personagem = self.root
        if personagem.nome == nome:
            ganha_xp =personagem.id
            ganha_xp._up(xp)
        
        else:
            personagem.next.Upper(nome,xp)    


def add(end, id ,nome,back):
    if end.root != None:
        item = end.root
        if item.next != None:
            add(item.next,id,nome,item)
        else:
            item.next = Raiz()
            add(item.next,id,nome,item)
    else:
        end.root = No(id,nome,back,None)
        
        