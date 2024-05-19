import os
os.system("cls")
def registrarRecitas(receitas) :
    conteudo_de_cada_receita = ['País de origem','Ingredientes','Modo de preparo']
    while True :
        nome_da_receita = input("Nome da receita: ").capitalize()
        receitas[nome_da_receita] = {}
        for i in range(1) :    
            receitas[nome_da_receita][conteudo_de_cada_receita[0]] = input("País de origem : ")
            receitas[nome_da_receita][conteudo_de_cada_receita[1]] = input("Ingredientes : ")
            receitas[nome_da_receita][conteudo_de_cada_receita[2]] = input("Modo de preparo : ")
        registro(receitas,nome_da_receita)
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
    file.write(f"Nome: {nome_da_receita} | ")
    for chaves in receita[nome_da_receita] :
        file.write(f" {chaves} | {receita[nome_da_receita][chaves]} | ")
    file.write("\n")
    file.close()
receitas = {}
