import os
os.system("cls")
import lista_por_país_de_origem
def registrarRecitas(receitas) :
    conteudo_de_cada_receita = ['País de origem','Ingredientes','Modo de preparo']
    while True :
        nome_da_receita = input("Qual é a receita?\n").capitalize()
        receitas[nome_da_receita] = {}
        for i in range(3) :    
            receitas[nome_da_receita][conteudo_de_cada_receita[i]] = input()
        registro(receitas,nome_da_receita)
        lista_por_país_de_origem.filtrar_por_pais(receitas,nome_da_receita,conteudo_de_cada_receita)
        resposta = input("Deseja continuar regitrando receitas?\n").capitalize()
        if resposta == "Não" or resposta == 'N' :
            arquivo = open("receitas.txt",'r',encoding="utf8")
            print(arquivo.read())
            arquivo.close()
            break
def registro(receita,nome_da_receita) :
    file = open("receitas.txt",'a',encoding="utf8")      
    #for chave in receita :
    #   file.write(chave+" ")
    file.write(nome_da_receita+" ")
    for chaves in receita[nome_da_receita] :
        file.write(f"{chaves} {receita[nome_da_receita][chaves]} ")
    file.write("\n")
    file.close()
receitas = {}
