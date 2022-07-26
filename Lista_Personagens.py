
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
            
    def buscar_nome(self,nome):
        id = self.root
        if id.nome == nome:
            buscar  = id.id
            buscar._destribuirPontos()

        elif id.nome != nome and id.next != None:
            id = id.next
            id.buscar_nome(nome)
        else:
             print("\nPersonogem não existe:\n\n")

    def buscar_personagem(self,nome):
        id = self.root
        if id.nome == nome:
            print("\n##############################")
            print("Personagem:",id.nome) 
            objeto=id.id                    # .id  é um objeto da classe personagem 
            objeto.busca()
            print("##############################\n")
        elif id.nome != nome and id.next != None:
            id = id.next
            id.buscar_personagem(nome)
        else:
            print("\nPersonogem não existe:\n\n")
           
    #adicionar um valor de xp ao personagem
    def Upper(self,nome,xp):
        personagem = self.root 
           
        if personagem.nome == nome: # verifica se é o personagem escolhido
            ganha_xp =personagem.id # ganha_xp se torna uma referencia para o objeto instanciado de personagem
            ptl = ganha_xp._up(xp)        # _up() é um metodo da classe personagem
            
            print(ptl,"pontos livres")
            if ptl > 0 :
                descisao  = input("Você tem pontos de Talentos para serem distribuidos, deseja fazer isso agora ?\nY/N :").upper()
                if descisao == 'Y':
                    ganha_xp._destribuirPontos()
                
                elif descisao == 'N':
                    exit
                
                else:
                    print("Entrada invalida:")
        
        elif personagem.nome != nome and personagem.next != None:
            personagem.next.Upper(nome,xp)    # busca o proximo personagem na lista encadeada

        else:
            print("\n\tPersonagem não encontrado:\n\tVerifique se escreveu no nome corretamente:\n")
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
        
        