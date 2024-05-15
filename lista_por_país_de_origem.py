def filtrar_por_pais(receitas,nome_da_receita,conteudo_de_cada_receita) :
    pais = receitas[nome_da_receita][conteudo_de_cada_receita[0]]
    receitas_por_pais = {}
    receitas_por_pais[pais] = {}
    receitas_por_pais[pais][nome_da_receita] = {}
    for i in range(3) :
        receitas_por_pais[pais][nome_da_receita][conteudo_de_cada_receita[i]] = receitas[nome_da_receita][conteudo_de_cada_receita[i]]  
    file = open("lista_por_país_de_origem.txt",'w',encoding='utf8')
    file.write(str(receitas_por_pais))
