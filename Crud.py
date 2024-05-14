import os
os.system("cls")
import registrar_receitas
import visualizar_receitas
import excluir_receitas
import favoritar_receitas
print("Bem vindo ao CRUD de receitas!!")

print("""As opções de menu são : registrar receitas , visualizar receitas , atualizar receitas ,
excluir receitas , favoritar receitas , visualizar as receitas de acordo com o país de origem e (opção extra)  """)

while (True) :
    print("Escolha uma opção do menu :",end=" ")
    menu = input()
    if menu == 'registrar receitas' :
        registrar_receitas.registrarRecitas(registrar_receitas.receitas)
    elif menu == 'visualizar receitas' :
        visualizar_receitas.visualizarReceitas()
    elif menu == 'excluir receitas' :
        excluir_receitas.excluirReceitas()
    elif menu == 'favoritar receitas' :
        favoritar_receitas.favoritar_receitas()        