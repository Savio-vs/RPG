
from Lista_Personagens import *
def Ganho_XP(listaPersonagens):
    nome = input("Nome do personagem:")
    xp = int(input("xp ganha na campanha:"))
    listaPersonagens.Upper(nome,xp)
    listaPersonagens.buscar_personagem(nome)
