<<<<<<< HEAD
def excluirReceitas() :
    while(True) :
        file = open("CRUD_projeto_python_1_unidade/receitas.txt","r",encoding="utf8")
        lista_de_receitas = file.readlines()
        receita_excluida = input("Qual a receita que deseja excluir?\n")
        file.close()
        file = open("CRUD_projeto_python_1_unidade/receitas.txt","w",encoding="utf8")
        file.write("")
        file.close()
        for i in range(len(lista_de_receitas)) :
            if receita_excluida in lista_de_receitas[i] :
                lista_de_receitas.pop(i)
                break
            elif i == len(lista_de_receitas)-1 :
                print("Não há como excluir a receita pois não há o seu registro no sistema")
                registroSem_a_excluida(lista_de_receitas)
        registroSem_a_excluida(lista_de_receitas)
        resposta = input("Deseja continuar excluindo receitas?\n").capitalize()
        if resposta == 'Não' or resposta == 'N' :
            break
        else : 
            pass

def registroSem_a_excluida(lista_de_receitas) :
    file = open("CRUD_projeto_python_1_unidade/receitas.txt","w",encoding="utf8")
    for receita in lista_de_receitas :
        file.write(f"{receita}\n")
        

=======
def excluirReceitas() :
    while(True) :
        file = open("CRUD_projeto_python_1_unidade/receitas.txt","r",encoding="utf8")
        lista_de_receitas = file.readlines()
        receita_excluida = input("Qual a receita que deseja excluir?\n")
        file.close()
        file = open("CRUD_projeto_python_1_unidade/receitas.txt","w",encoding="utf8")
        file.write("")
        file.close()
        for i in range(len(lista_de_receitas)) :
            if receita_excluida in lista_de_receitas[i] :
                lista_de_receitas.pop(i)
                break
            elif i == len(lista_de_receitas)-1 :
                print("Não há como excluir a receita pois não há o seu registro no sistema")
                registroSem_a_excluida(lista_de_receitas)
        registroSem_a_excluida(lista_de_receitas)
        resposta = input("Deseja continuar excluindo receitas?\n").capitalize()
        if resposta == 'Não' or resposta == 'N' :
            break
        else : 
            pass

def registroSem_a_excluida(lista_de_receitas) :
    file = open("CRUD_projeto_python_1_unidade/receitas.txt","w",encoding="utf8")
    for receita in lista_de_receitas :
        file.write(f"{receita}\n")
        

>>>>>>> 95d924e2a136dc816690e51f6801334d74651a35
