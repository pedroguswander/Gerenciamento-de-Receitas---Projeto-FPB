<<<<<<< HEAD
def favoritar_receitas() :
    file = open("CRUD_projeto_python_1_unidade/receitas.txt","r",encoding="utf8")
    lista_receitas = file.readlines()
    file.close()
    while(True) :
        #deseja visualizar as receitas registradas antes?
        receita_favorita = input("Qual receita deseja favoritar?\n").capitalize()
        for i in range(len(lista_receitas)) :
            if receita_favorita in lista_receitas[i] :
                file = open("CRUD_projeto_python_1_unidade/receitas_favoritas.txt","w",encoding="utf8")
                file.write(lista_receitas[i])
                file.write("\n")
                file.close()
                break
            elif i == len(lista_receitas) - 1 :
                print("Essa receita não foi registrada ainda")
        resposta = input("Deseja continuar favoritando receitas?").capitalize()
        if resposta == 'Não' or resposta == 'N' :          
            break
        else:
            pass


        
=======
def favoritar_receitas() :
    file = open("CRUD_projeto_python_1_unidade/receitas.txt","r",encoding="utf8")
    lista_receitas = file.readlines()
    file.close()
    while(True) :
        #deseja visualizar as receitas registradas antes?
        receita_favorita = input("Qual receita deseja favoritar?\n").capitalize()
        for i in range(len(lista_receitas)) :
            if receita_favorita in lista_receitas[i] :
                file = open("CRUD_projeto_python_1_unidade/receitas_favoritas.txt","w",encoding="utf8")
                file.write(lista_receitas[i])
                file.write("\n")
                file.close()
                break
            elif i == len(lista_receitas) - 1 :
                print("Essa receita não foi registrada ainda")
        resposta = input("Deseja continuar favoritando receitas?").capitalize()
        if resposta == 'Não' or resposta == 'N' :          
            break
        else:
            pass


        
>>>>>>> 95d924e2a136dc816690e51f6801334d74651a35
