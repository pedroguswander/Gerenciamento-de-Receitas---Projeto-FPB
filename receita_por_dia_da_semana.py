def receita_por_dia_da_semana() :
    while(True) :
        dias_da_semana_e_suas_receitas = {}
        dias_da_semana = ['Segunda-feira','Terça-feira','Quarta-feira','Quinta-feira','Sexta-feira','Sábado','Domingo']
        file = open("receitas.txt",'r',encoding="utf8")
        lista_receitas = file.readlines()
        file.close()
        if len(lista_receitas) >= 7 :
            for i in range(7) :
                receita = input(f"Qual receita deseja colocar {'no' if i == 5 or i == 6 else 'na'} {dias_da_semana[i]}?\n")
                for x in range(len(lista_receitas)) :
                    if receita in lista_receitas[x] :
                        dias_da_semana_e_suas_receitas[dias_da_semana[i]] = receita
                        break
                    elif x == len(lista_receitas) - 1 :
                        print("receita não encontrada")
            file = open("receitas_por_dia_da_semana.txt",'w',encoding="utf8")
            for chaves in dias_da_semana_e_suas_receitas :
                file.write(f"{chaves} : {dias_da_semana_e_suas_receitas[chaves]}\n")
            file.close()            
            resposta = input("deseja refazer o cronograma de receitas por dia da semana?\n").capitalize()
            if resposta == "Não" or resposta == 'N' :
                break
        else :
            print("Não há 7 receitas")
            break

            
                
                


    