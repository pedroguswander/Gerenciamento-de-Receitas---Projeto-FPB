import os
os.system("cls")
import random
def receitas_aleatorias():
    file = open("receitas.txt","r",encoding="utf8")
    linhas = file.readlines()
    receita_aleatoria = random.choice(linhas)
    print("Que tal essa receita: ",receita_aleatoria) 