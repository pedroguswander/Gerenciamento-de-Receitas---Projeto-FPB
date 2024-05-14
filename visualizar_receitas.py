import os
os.system("cls")
def visualizarReceitas() :
    while(True) :
        file = open("CRUD_projeto_python_1_unidade/receitas.txt","r",encoding="utf8")
        lista_receitas = file.readlines()
        receita_visualizada = input("Qual receita deseja visualizar?\n")
        for i in range(len(lista_receitas)) :
            if receita_visualizada in lista_receitas[i] :
                print(lista_receitas[i])
                break
            if  i == len(lista_receitas)-1 :
                print("Essa receita não foi registrada ainda")
                # deseja registrar essa receita?
        resposta = input("deseja continuar vendo receitas?\n").capitalize()
        if resposta == 'Não' or resposta == 'N' :
            break
        else : 
            pass
    