import excluir_receitas
def atualizar_receitas() :
    while(True) :
        file = open("receitas.txt",'r',encoding='utf8')
        lista_receitas = file.readlines()
        file.close()
        receita = input("Qual receita deseja alterar?\n")
        categoria = input("Em que categoria deve ocorrer a alteração?\n")
        conteudo = input("Digite o conteúdo da modificação\n")
        for i in range(len(lista_receitas)) :
            if receita in lista_receitas[i] :
                if categoria == "País de origem" :
                    nova_lista_receitas = lista_receitas[i].split()
                    index_origem = nova_lista_receitas.index("origem")
                    index_ingredientes = nova_lista_receitas.index("Ingredientes")
                    #atualizar(nova_lista_receitas,lista_receitas,i,conteudo,index_origem,index_ingredientes)
                    for x in range(index_origem+1,index_ingredientes) :
                        nova_lista_receitas.pop(x)
                    nova_lista_receitas.insert(index_origem+1,conteudo)
                    print(nova_lista_receitas)
                    lista_receitas.pop(i)
                    lista_receitas.insert(i," ".join(nova_lista_receitas))
                    excluir_receitas.registroSem_a_excluida(lista_receitas)
                    break
                elif categoria == "Ingredientes" :
                    nova_lista_receitas = lista_receitas[i].split()
                    index_ingredientes = nova_lista_receitas.index("Ingredientes")
                    index_modo = nova_lista_receitas.index("Modo")
                    for x in range(index_ingredientes+1,index_modo) :
                        nova_lista_receitas.pop(x)
                    nova_lista_receitas.insert(index_ingredientes+1,conteudo)
                    print(nova_lista_receitas)
                    lista_receitas.pop(i)
                    lista_receitas.insert(i," ".join(nova_lista_receitas))
                    excluir_receitas.registroSem_a_excluida(lista_receitas)               
                    break
                elif categoria == "Modo de preparo" :
                    nova_lista_receitas = lista_receitas[i].split()
                    index_preparo = nova_lista_receitas.index("preparo")
                    for x in range(index_preparo+1,len(nova_lista_receitas)) :
                        nova_lista_receitas.pop(x)
                    nova_lista_receitas.insert(index_preparo+1,conteudo)
                    print(nova_lista_receitas)
                    lista_receitas.pop(i)
                    lista_receitas.insert(i," ".join(nova_lista_receitas))
                    excluir_receitas.registroSem_a_excluida(lista_receitas)
                    break
            elif i == len(lista_receitas)-1:
                print("Não há como alterar a receita pois não há o seu registro no sistema")
        resposta = input("Deseja continuar atualizando receitas?\n").capitalize()
        if resposta == "Não" or resposta == "N" :
            return



                        

                