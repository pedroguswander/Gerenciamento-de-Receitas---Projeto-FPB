import os
os.system('cls')
import registrar_receitas
import visualizar_receitas
import excluir_receitas
import favoritar_receitas
import receitas_aleatorias
import atualizar_receitas
import receitas_por_país_de_origem
import receita_por_dia_da_semana

print("Bem vindo ao CRUD de receitas!!")

while (True) :
    print('\033[34m=\033[m' * 50)
    print('                  \033[1;34;40mFATIADOS\033[m')
    print('\033[34m=\033[m' * 50)
    print('1 -\033[32m Registrar Receitas\033[m')
    print('2 -\033[32m Visualizar Receitas\033[m')
    print('3 -\033[32m Excluir Receitas\033[m')
    print('4 -\033[32m Favoritar Receitas\033[m')
    print('5 -\033[32m Sugestão de Receita Aleatória\033[m')
    print('6 -\033[32m Atualizar Receitas\033[m')
    print('7 -\033[32m Ver Receitas por País de Origem\033[m')
    print('8 -\033[32m Receita por Dia da Semana\033[m')
    print('\033[34m=\033[m' * 50)
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
    elif menu == 5 :
        receitas_aleatorias.receitas_aleatorias()
    elif menu == 6 :
        atualizar_receitas.atualizar_receitas()
    elif menu == 7 :
        receitas_por_país_de_origem.receitas_por_paisdeOrigem()
    elif menu == 8 :
        receita_por_dia_da_semana.receita_por_dia_da_semana()