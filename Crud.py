<<<<<<< HEAD
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
=======
import os
os.system("cls")
import registrar_receitas
import visualizar_receitas
import excluir_receitas
import favoritar_receitas
print("Bem vindo ao CRUD de receitas!!")

print("""As opções de menu são : 1 - registrar receitas , 2 - visualizar receitas , 3 - atualizar receitas ,
4 - excluir receitas , 5 - favoritar receitas , 6 - visualizar as receitas de acordo com o país de origem e 7 - (opção extra)  """)

while (True) :
    print("Escolha uma opção do menu :",end=" ")
    menu = int(input())
    if menu == 1 :
        registrar_receitas.registrarRecitas(registrar_receitas.receitas)
    elif menu == 2 :
        visualizar_receitas.visualizarReceitas()
    elif menu == 4 :
        excluir_receitas.excluirReceitas()
    elif menu == 5 :
>>>>>>> 95d924e2a136dc816690e51f6801334d74651a35
        favoritar_receitas.favoritar_receitas()        