
def receitas_por_paisdeOrigem() :
    file = open("receitas.txt","r",encoding="utf8")
    lista_de_receitas = file.readlines()
    file.close()
    pais_e_receitas = {}
    while(True) :
        pais_receitas = input("Deseja ver receitas de que país?\n")
        pais_e_receitas[pais_receitas] = []
        for receita in lista_de_receitas :
            if pais_receitas in receita :
                nova_lista_de_receitas = receita.split()   
                index_pais = nova_lista_de_receitas.index("País")
                lista_nome_receita = []
                for x in range(index_pais) :
                    lista_nome_receita.append(nova_lista_de_receitas[x])
                pais_e_receitas[pais_receitas].append(" ".join(lista_nome_receita))
        print(pais_receitas,":")
        for i in range(len(pais_e_receitas[pais_receitas])) :
            print(pais_e_receitas[pais_receitas][i],end=",")
        resposta = input("\ndeseja continuar vendo receitas por país de origem?\n").capitalize()
        if resposta == "Sim" or resposta == 'S' :
            pass
        if resposta == "Não" or resposta == 'N' :
            break
            
