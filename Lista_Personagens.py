
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
        personagem = self.root
        if personagem.next != None:
            id = personagem.id
            print("\t",personagem.nome,"--", id.classe,"Nv.", id.lvl)
            personagem =  personagem.next
            personagem.imprimir()
    
        else:
            id = personagem.id
            print("\t",personagem.nome,"--", id.classe,"Nv.", id.lvl ,"\n")
            
   
    def buscar_personagem(self,nome):
        id = self.root
        if id.nome == nome:
            print("##############################")
            print("Personagem: ",id.nome) 
            objeto=id.id                    # .id  é um objeto da classe personagem 
            objeto.busca()
            print("##############################")
        elif id.nome != nome and id.next != None:
            id = id.next
            id.buscar_personagem(nome)
        else:
            print("\nPersonogem não existe:\n\n")
           
    #adicionar um valor de xp ao personagem
    def Upper(self,nome,xp):
        personagem = self.root 
        if personagem.nome == nome: # verifica é o personagem escolhido
            ganha_xp =personagem.id # ganha_xp se torna uma referencia para o objeto instanciado de personagem
            ganha_xp._up(xp)        # _up() é um metodo da classe personagem
        
        else:
            personagem.next.Upper(nome,xp)    # busca o proximo personagem na lista encadeada

# Adicionando um persogem a lista encadeado de execução
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
        
        