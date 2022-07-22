
from Personagens import *
def Ganho_XP(listaPersonagens):
    nome = input("Nome do personagem:")
    xp = int(input("xp ganha:"))
    listaPersonagens.Upper(nome,xp)
    listaPersonagens.buscar_personagem(nome)