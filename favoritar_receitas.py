def favoritar_receitas() :
    file = open("receitas.txt","r",encoding="utf8")
    lista_receitas = file.readlines()
    file.close()
    while(True) :
        #deseja visualizar as receitas registradas antes?
        receita_favorita = input("Qual receita deseja favoritar?\n").capitalize()
        for i in range(len(lista_receitas)) :
            if receita_favorita in lista_receitas[i] :
                file = open("receitas_favoritas.txt","w",encoding="utf8")
                file.write(lista_receitas[i])
                file.write("\n")
                file.close()
                break
            elif i == len(lista_receitas) - 1 :
                print("Essa receita não foi registrada ainda")
        resposta = input("Deseja continuar favoritando receitas?\n").capitalize()
        if resposta == "Sim" or resposta == 'S' :
            pass
        if resposta == 'Não' or resposta == 'N' :
            file = open("receitas_favoritas.txt","r",encoding="utf8")
            print(file.read())
            break
        else:
            pass


        
