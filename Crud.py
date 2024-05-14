import os
os.system('cls')
import visualizar_receitas
import excluir_receitas
import favoritar_receitas

print("Bem vindo ao CRUD de receitas!!")
print('\033[34m=\033[m' * 50)
print('                  \033[1;34;40mFATIADOS\033[m')
print('\033[34m=\033[m' * 50)
print('1 -\033[32m Registrar Receitas\033[m')
print('2 -\033[32m Visualizar Receitas\033[m')
print('3 -\033[32m Excluir Receitas\033[m')
print('4 -\033[32m Favoritar Receitas\033[m')
print('\033[34m=\033[m' * 50)


# print("""As opções de menu são : registrar receitas , visualizar receitas , atualizar receitas ,
# excluir receitas , favoritar receitas , visualizar as receitas de acordo com o país de origem e (opção extra)  """)

while (True) :
    print("Escolha uma opção do menu :",end=" ")
    menu = int(input())
    if menu == 1 :
        registrar_receitas.registrarRecitas(registrar_receitas.receitas)
    elif menu == 2 :
        visualizar_receitas.visualizarReceitas()
    elif menu == 3 :
        excluir_receitas.excluirReceitas()
    elif menu == 4 :
        favoritar_receitas.favoritar_receitas()        
        
