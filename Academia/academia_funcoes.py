import json
import os
from time import sleep
from colorama import Fore
import re

# Função menu que da inicio ao nosso programa, mostrando todas as opções disponíveis
def menu():
    print(f"\n{'- '*31}")
    print(f'{"-"*60}\n{" ACADEMIA ":^60}\n{"-"*60}') # deixar bunito
    print("""
1 - Cadastrar 
2 - Editar 
3 - Excluir
4 - Pesquisar 
5 - Listar 
6 - Relatório 
0 - Encerrar\n""")
    opcao = int(input("Insira a opção que dejesa\n:"))
    return opcao

def contem_letras(string):
                    for caractere in string:
                        if 'a' <= caractere <= 'z' or 'A' <= caractere <= 'Z':
                            return True
                    return False

# Função cadastrar com parametros que são dicionários, com o contador que será a chave de cada um
def cadastrar(clientes, avaliacoes, lista_exercicios, id_cliente, id_avaliacao, id_lista_exercicio, clientes_json, avaliacoes_json, exercicios_json): # parametros que são dicionários, com o contador que será a chave de cada
    os.system("cls")
    while True:
        print(f"\n{'- '*30}")
        print(f'{"-"*60}\n{" CADASTRAR ":^60}\n{"-"*60}') # deixar bunito
        print("""
1 - Cliente
2 - Avaliação
3 - Lista de exercicíos (por dia da semana)
0 - Sair\n""")
        opcao = input("Insira a opção que dejesar\n:").lower()
        if opcao == "1" or opcao == "c": # cadastrar cliente
            print(f'\n{"-"*60}\n{" CLIENTE ":^60}\n{"-"*60}\n')
            while True:
                especial = ['1','2','3','4','5','6','7','8','9','0','!','@','#','$','%','&',',','.',';']
                nome = input("Insira o nome\n:").capitalize()
                diferente = False
                for letra in nome:
                    if letra in especial:
                        diferente = True
                        break
                if diferente == True:
                    print("""\nO nome não pode conter esses caracteres
(1234567890!@#$%&*<>,.;)
Tente novamente!\n""")
                    sleep(3)
                else:
                    break
            while True:
                try:
                    idade = int(input("\nInsira a idade\n:"))
                    break
                except ValueError:
                    print("\nA idade deve ser inteiro\nTente novamente!")
                    sleep(3)
            while True:
                sexo = input("\nInsira o sexo\nF-feminino\nM-masculino\n:").upper()
                if sexo[0] == 'F' or sexo[0] == 'M':
                    break
                else:
                    print("\nSexo não permitido (F/M)\nTente novamente!")
                    sleep(3)
            while True:
                telefone = input("\nInsira o telefone\nex: (00)0000-0000\n:")
                if telefone[0]!='(' or telefone[3]!=')' or telefone[8]!='-' or len(telefone)!=13 or contem_letras(telefone):
                    print("\nFormato incorreto, deve conter 10 números no formato sugerido\nTente novamente!")
                    sleep(3)
                else:
                    break
            while True:
                status = input("\nInsira o status (Ativo/Inativo)\n:").lower()
                if status=="ativo" or status=="ativa" or status=="inativo" or status=="inativa":
                    break
                else:
                    print("\nStutus não permitido\nTente novamente!")
                    sleep(3)
            clientes[id_cliente] = {'nome':nome,'idade':idade,'sexo':sexo,'telefone':telefone,'status':status}
            with open(clientes_json,'w',encoding='utf-8') as dados_cliente:
                json.dump(clientes, dados_cliente, indent=4)
            print("\nCliente cadastrado com sucesso!")
            break
        elif opcao == '2':
            if not clientes:
                print(f'\n{"-"*60}')
                print(Fore.RED+"Não há clientes!"+Fore.RESET)
                print(f'{"-"*60}\n')
                break
            else:
                while True:
                    print(f'\n{"-"*60}\n{" AVALIAÇÃO ":^60}\n{"-"*60}\n')
                    for i, nome in clientes.items():
                        print(f"ID: {i} - NOME: {nome['nome']}")
                        print(f'{"-"*60}')
                    id_cli = input("\nInsira o ID do cliente que desejar ou '0' para sair\n:")
                    if id_cli in clientes.keys():
                        while True:
                            try:
                                altura = float(input(f"\nInsira a altura de {clientes[id_cli]['nome']} (metros)\n:"))
                                break
                            except ValueError:
                                print(Fore.RED+"\nEscreva um valor válido."+Fore.RESET+"Apenas números")
                                sleep(3)
                        while True:
                            try:
                                peso = float(input(f"\nInsira a peso de {clientes[id_cli]['nome']} (kg)\n:"))
                                break
                            except ValueError:
                                print(Fore.RED+"\nEscreva um valor válido."+Fore.RESET+"Apenas números")
                                sleep(3)
                        while True:
                            try:
                                gordura = float(input(f"\nInsira o percentual de gordura de {clientes[id_cli]['nome']} (em %)\n:"))
                                break
                            except ValueError:
                                print(Fore.RED+"\nEscreva um valor válido."+Fore.RESET+"Apenas números")
                                sleep(3)
                        while True:
                            try:
                                braco = float(input(f"\nInsira a medida do braço de {clientes[id_cli]['nome']} (em cm)\n:"))
                                break
                            except ValueError:
                                print(Fore.RED+"\nEscreva um valor válido."+Fore.RESET+"Apenas números")
                                sleep(3)
                        while True:
                            try:
                                perna = float(input(f"\nInsira a medida da perna de {clientes[id_cli]['nome']} (em cm)\n:"))
                                break
                            except ValueError:
                                print(Fore.RED+"\nEscreva um valor válido."+Fore.RESET+"Apenas números")
                                sleep(3)
                        while True:
                            try:
                                cintura = float(input(f"\nInsira a medida da cintura de {clientes[id_cli]['nome']} (em cm)\n:"))
                                break
                            except ValueError:
                                print(Fore.RED+"\nEscreva um valor válido."+Fore.RESET+"Apenas números")
                                sleep(3)
                        while True:
                            data = input("\nInsira a data da avaliação\nex: dd/mm/aaaa\n:")
                            if len(data)!=10 or data[2]!='/' or data[5]!='/' or contem_letras(data):
                                print("\nFormato incorreto, deve conter 8 números no formato sugerido\nTente novamente!")
                                sleep(3)
                            else:
                                break
                        avaliacoes[id_avaliacao] = {'altura':altura,'peso':peso,'gordura':gordura,
                                    'braço':braco,'perna':perna, 'cintura':cintura, 'data':data, "cliente":id_cli}
                        with open(avaliacoes_json,'w',encoding='utf-8') as dados_cliente:
                            json.dump(avaliacoes, dados_cliente, indent=4)
                        print("\nAvaliação cadastrada com sucesso!")
                        break
                    elif id_cli=='0':
                        break
                    else:
                        print("\nID não encontrado\nTente novamente!")
            break
        elif opcao == '3':
            if not clientes:
                print(f'\n{"-"*60}')
                print(Fore.RED+"Não há clientes!"+Fore.RESET)
                print(f'{"-"*60}\n')
                break
            else:
                while True:
                    print(f'\n{"-"*60}\n{" LISTA DE EXERCÍCIOS ":^60}\n{"-"*60}\n')
                    for i, valor in clientes.items():
                        print(f"ID: {i} - NOME: {valor['nome']} - STATUS: {valor['status']}")
                        print(f'{"-"*60}')
                    id_cli_exe = input("\nInsira o ID do cliente que desejar ou '0' para sair\n:")
                    if id_cli_exe in clientes.keys() and (clientes[id_cli_exe].get('status')=='ativo' or clientes[id_cli_exe].get('status')=='ativa' or clientes[id_cli_exe].get('status')[0]=='a'):
                        print(Fore.GREEN+f"\nCliente {clientes[id_cli_exe].get('status')}!\n"+Fore.RESET)
                        while True:
                            dia=['Segunda','Terça','Quarta',"Quinta","Sexta","Sábado"]
                            dia_semana=input(f"Dia da semana do exercício de {clientes[id_cli_exe]['nome']}\n:").capitalize().strip()
                            semana_separado=re.split("\s|-", dia_semana)
                            resp=False
                            if (semana_separado[0] in dia) or (semana_separado[0] in dia and semana_separado[1]=='feira'):
                                    resp=True
                            if resp==False:
                                print("\nEstão disponíveis apenas 'Segunda','Terça','Quarta','Quinta','Sexta' ou 'Sábado' (seguido de 'Feira' ou não)\nTente novamente!")
                                sleep(3)
                            else:
                                break
                        while True:
                            especial = ['1','2','3','4','5','6','7','8','9','0','!','@','#','$','%','&',',','.',';']
                            exercicio = input(f"\nInsira o nome do exercicio de {clientes[id_cli_exe]['nome']}\n:").capitalize()
                            diferente = False
                            for letra1 in exercicio:
                                if letra1 in especial:
                                    diferente = True
                                    break
                            if diferente == True:
                                print("""\nO exercício não pode conter esses caracteres
(1234567890!@#$%&*<>,.;)
Tente novamente!\n""")
                                sleep(3)
                            else:
                                break
                        while True:
                            especial = ['1','2','3','4','5','6','7','8','9','0','!','@','#','$','%','&',',','.',';']
                            grupo = input(f"\nInsira o grupo muscular\n:").capitalize()
                            diferente = False
                            for letra2 in grupo:
                                if letra2 in especial:
                                    diferente = True
                                    break
                            if diferente == True:
                                print("""\nO grupo muscular não pode conter esses caracteres
(1234567890!@#$%&*<>,.;)
Tente novamente!\n""")
                                sleep(3)
                            else:
                                break
                        while True:
                            try:
                                series = int(input(f"\nInsira a quantidade de séries do exercício {exercicio}\n:"))
                                break
                            except ValueError:
                                print(Fore.RED+"\nEscreva um valor válido."+Fore.RESET+"Apenas números")
                                sleep(3)
                        while True:
                            try:
                                repeticoes = int(input(f"\nInsira a quantidade de repetições do exercício {exercicio}\n:"))
                                break
                            except ValueError:
                                print(Fore.RED+"\nEscreva um valor válido."+Fore.RESET+"Apenas números")
                                sleep(3)
                        lista_exercicios[id_lista_exercicio]={"dia":dia_semana,"exercicio":exercicio,"grupo":grupo,"series":series,"repetições":repeticoes,"cliente":id_cli_exe}                        
                        with open(exercicios_json,'w',encoding='utf-8') as dados_cliente:
                            json.dump(lista_exercicios, dados_cliente, indent=4)
                        print("\nLista de exercícios cadastrada com sucesso!")
                        break
                    elif id_cli_exe=='0':
                        break
                    else:
                        print(Fore.RED+"\nID inválido e/ou cliente é INATIVO\nTente novamente!"+Fore.RESET)
            break
        elif opcao == '0':
            print()
            break
        else:
            print(Fore.RED+"\nOpção inválida\n"+Fore.RESET)
    print(f'{"-"*60}\n{"- "*30}') # deixar bunito
    return ""  

# Função editar com parametros que são dicionários, aqui você pode editar qualquer informação de cliente, avaliaçaõ ou lista de exercicios
def editar(clientes,avaliacoes,lista_exercicios, clientes_json, avaliacoes_json, exercicios_json):
    os.system("cls")
    print(f"\n{'- '*30}")
    while True:
        print(f'{"-"*60}\n{" EDITAR ":^60}\n{"-"*60}') # deixar bunito
        print("""
1 - Cliente
2 - Avaliação
3 - Lista de exercicíos (por dia da semana)
0 - Sair\n""")
        opcao = input("Insira a opção que dejesar\n:").lower()  
        if opcao=='1':
            os.system('cls')
            if not clientes:
                print(f'\n{"-"*60}')
                print(Fore.RED+"Não há clientes!"+Fore.RESET)
                print(f'{"-"*60}\n')
                break
            else:
                print(f'{"-"*60}\n{" EDITAR CLIENTE":^60}\n{"-"*60}') 
                print(f'\n{" CLIENTES ":^60}\n') # clientes disponíveis
                for key, value in clientes.items():
                    print(f"ID: {key} - NOME: {value['nome']}\n")
                while True:
                    cliente = input("\nInsira o ID do cliente que desejar ou '0' para sair\n: ")
                    if cliente in clientes.keys(): # se o cliente sugerido existe do banco de dados
                        print("""\n
1. Nome
2. Idade
3. Sexo
4. Telefone
5. Status)""")
                        opcao_editar = input(f'\nInsira o que deseja editar de {clientes[cliente]["nome"]}\n:').lower()
                        if opcao_editar == '1' or opcao_editar[0]=='n': # editar nome do cliente
                            while True:
                                especial = ['1','2','3','4','5','6','7','8','9','0','!','@','#','$','%','&',',','.',';']
                                novo_nome = input("Insira o nome\n:").capitalize()
                                diferente = False
                                for letra in novo_nome:
                                    if letra in especial:
                                        diferente = True
                                        break
                                if diferente == True:
                                    print("""\nO nome não pode conter esses caracteres
(1234567890!@#$%&*<>,.;)
Tente novamente!\n""")
                                    sleep(3)
                                else:
                                    break 
                            clientes[cliente]["nome"] = novo_nome # substitui no arquivo
                            with open(clientes_json,'w',encoding='utf-8') as dados_nome:
                                json.dump(clientes, dados_nome,indent=4)
                            print(f"\nO nome foi alterado com sucesso!\n")

                        elif opcao_editar == '2' or opcao_editar[0]=='i': # editar idade do cliente
                            while True:
                                try:
                                    novo_idade = int(input("\nInsira a idade\n:"))
                                    break
                                except ValueError:
                                    print("\nA idade deve ser inteiro\nTente novamente!")
                                    sleep(3)
                            clientes[cliente]['idade'] = novo_idade #substitui no arquivo
                            with open(clientes_json,'w',encoding='utf-8') as dados_idade:
                                json.dump(clientes, dados_idade,indent=4)
                            print(f"\nA idade de {clientes[cliente]['nome']} foi alterada com sucesso!\n")

                        elif opcao_editar == '3' or opcao_editar[0]=='s':
                            while True:
                                novo_sexo = input("\nInsira o sexo\nF-feminino\nM-masculino\n:").upper()
                                if novo_sexo[0] == 'F' or novo_sexo[0] == 'M':
                                    break
                                else:
                                    print("\nSexo não permitido (F/M)\nTente novamente!")
                                    sleep(3)
                            clientes[cliente]['sexo'] = novo_sexo
                            with open(clientes_json,'w',encoding='utf-8') as dados_idade:
                                json.dump(clientes, dados_idade,indent=4)
                            print(f"\nA sexo de {clientes[cliente]['nome']} foi alterado com sucesso!\n")

                        elif opcao_editar == '4' or opcao_editar[0]=='t':
                            while True:
                                novo_tel = input("\nInsira o telefone\nex: (00)0000-0000\n:")
                                if novo_tel[0]!='(' or novo_tel[3]!=')' or novo_tel[8]!='-' or len(novo_tel)!=13 or contem_letras(novo_tel):
                                    print("\nFormato incorreto, deve conter 10 números no formato sugerido\nTente novamente!")
                                    sleep(3)
                                else:
                                    break
                            clientes[cliente]['telefone'] = novo_tel
                            with open(clientes_json,'w',encoding='utf-8') as dados_idade:
                                json.dump(clientes, dados_idade,indent=4)
                            print(f"\nA telefone de {clientes[cliente]['nome']} foi alterado com sucesso!\n")

                        elif opcao_editar == '5' or opcao_editar[0]=='s':
                            while True:
                                novo_status = input("\nInsira o status (Ativo/Inativo)\n:").lower()
                                if novo_status=="ativo" or novo_status=="ativa" or novo_status=="inativo" or novo_status=="inativa":
                                    break
                                else:
                                    print("\nStutus não permitido\nTente novamente!")
                                    sleep(3)
                            clientes[cliente]['status'] = novo_status
                            with open(clientes_json,'w',encoding='utf-8') as dados_idade:
                                json.dump(clientes, dados_idade,indent=4)
                            print(f"\nO status de {clientes[cliente]['nome']} foi alterado com sucesso!\n")
                        break
                    elif cliente=='0':
                        break
                    else:
                        print(Fore.RED+"\nID inválido!\nTente novamente!"+Fore.RESET)
                        sleep(3)
            break
        elif opcao=='2':
            os.system('cls')
            if not avaliacoes:
                print(f'\n{"-"*60}')
                print(Fore.RED+"Não há avaliações!"+Fore.RESET)
                print(f'{"-"*60}\n')
                break
            else:
                print(f'{"-"*60}\n{" EDITAR AVALIAÇÃO":^60}\n{"-"*60}') 
                print(f'\n{" AVALIAÇÕES ":^60}\n') # AVALIAÇÕES CADASTRADAS 
                for key, value in avaliacoes.items():
                    cliente = value['cliente']
                    print(f"ID: {key} - CLIENTE: {cliente} - NOME_CLIENTE: {clientes[cliente]['nome']}\n")
                while True:
                    avaliacao = input("\nInsira o ID da avaliação que deseja editar ou '0' para sair\n: ")
                    if avaliacao in avaliacoes.keys(): # se a avaliação sugerido existe do banco de dados
                        print('''\n
1. Altura 
2. Peso
3. Percentual de gordura
4. Braço
5. Perna
6. Cintura
7. Data''')
                        opcao_editar= input(f'\nInsira o que deseja editar da avaliação\n:').lower()
                        if opcao_editar == '1' or opcao_editar[0]=='a':
                            while True:
                                try:
                                    nova_altura = float(input(f"\nInsira a nova altura (metros)\n:"))
                                    break
                                except ValueError:
                                    print(Fore.RED+"\nEscreva um valor válido."+Fore.RESET+"Apenas números")
                                    sleep(3)
                            avaliacoes[avaliacao]['altura'] = nova_altura
                            with open(avaliacoes_json,'w',encoding='utf-8') as dados_altura:
                                json.dump(avaliacoes, dados_altura,indent=4)
                            print(f"\nA altura foi alterada com sucesso!\n")
                        elif opcao_editar == '2' or opcao_editar[0]=='p':
                            while True:
                                try:
                                    novo_peso = float(input(f"\nInsira o novo peso (kg)\n:"))
                                    break
                                except ValueError:
                                    print(Fore.RED+"\nEscreva um valor válido."+Fore.RESET+"Apenas números")
                                    sleep(3)
                            avaliacoes[avaliacao]['peso'] = novo_peso
                            with open(avaliacoes_json,'w',encoding='utf-8') as dados_peso:
                                json.dump(avaliacoes, dados_peso,indent=4)
                            print(f"\nO peso foi alterado com sucesso!\n")
                            break
                        elif opcao_editar == '3':
                            while True:
                                try:
                                    novo_percentual = float(input(f"\nInsira o novo percentual de gordura (em %)\n:"))
                                    break
                                except ValueError:
                                    print(Fore.RED+"\nEscreva um valor válido."+Fore.RESET+"Apenas números")
                                    sleep(3)
                            avaliacoes[avaliacao]['gordura'] = novo_percentual
                            with open('avaliacoes.json','w',encoding='utf-8') as dados_gordura:
                                json.dump(avaliacoes, dados_gordura,indent=4)
                            print(f"\nO percuntual de gordura foi alterado com sucesso!\n")
                        elif opcao_editar == '4' or opcao_editar[0]=='b':
                            while True:
                                try:
                                    novo_braco = float(input(f"\nInsira a nova medida do braço (em cm)\n:"))
                                    break
                                except ValueError:
                                    print(Fore.RED+"\nEscreva um valor válido."+Fore.RESET+"Apenas números")
                                    sleep(3)
                            avaliacoes[avaliacao]['braço'] = novo_braco
                            with open(avaliacoes_json,'w',encoding='utf-8') as dados_braco:
                                json.dump(avaliacoes, dados_braco,indent=4)
                            print(f"\nO tamanho do braço foi alterado com sucesso!\n")
                        elif opcao_editar == '5':
                            while True:
                                try:
                                    nova_perna = float(input(f"\nInsira a nova medida da perna de (em cm)\n:"))
                                    break
                                except ValueError:
                                    print(Fore.RED+"\nEscreva um valor válido."+Fore.RESET+"Apenas números")
                                    sleep(3)
                            avaliacoes[avaliacao]['perna'] = nova_perna
                            with open(avaliacoes_json,'w',encoding='utf-8') as dados_perna:
                                json.dump(avaliacoes, dados_perna,indent=4)
                            print(f"\nO tamanho da perna foi alterado com sucesso!\n")
                        elif opcao_editar=='6':
                            while True:
                                try:
                                    nova_cintura = float(input(f"\nInsira a nova medida da cintura de (em cm)\n:"))
                                    break
                                except ValueError:
                                    print(Fore.RED+"\nEscreva um valor válido."+Fore.RESET+"Apenas números")
                                    sleep(3)
                            avaliacoes[avaliacao]['cintura'] = nova_cintura
                            with open(avaliacoes_json,'w',encoding='utf-8') as dados_cintura:
                                json.dump(avaliacoes, dados_cintura,indent=4)
                            print(f"\nO tamanho da cintura foi alterado com sucesso!\n")
                        elif opcao_editar == '7' or opcao_editar[0]=='d':
                            while True:
                                nova_data = input("\nInsira a data da avaliação\nex: dd/mm/aaaa\n:")
                                if len(nova_data)!=10 or nova_data[2]!='/' or nova_data[5]!='/' or contem_letras(nova_data):
                                    print("\nFormato incorreto, deve conter 8 números no formato sugerido\nTente novamente!")
                                    sleep(3)
                                else:
                                    break
                            avaliacoes[avaliacao]['data'] = nova_data
                            with open(avaliacoes_json,'w',encoding='utf-8') as dados_data:
                                json.dump(avaliacoes, dados_data,indent=4)
                            print(f"\nA data de avaliação foi alterado com sucesso!\n")
                        break
                    elif avaliacao=='0':
                        break
                    else:
                        print("\nID não encontrado\nTente novamente!")
                        sleep(3)
            break
        elif opcao=='3':
            os.system('cls')
            if not lista_exercicios:
                print(f'\n{"-"*60}')
                print(Fore.RED+"Não há lista de exercícios!"+Fore.RESET)
                print(f'{"-"*60}\n')
                break
            else:
                print(f'{"-"*60}\n{" EDITAR LISTA DE EXERCICIOS":^60}\n{"-"*60}') 
                print(f'{" LISTA DE EXERCÍCIOS ":^60}\n{"-"*60}') # clientes disponíveis
                for key, value in lista_exercicios.items():
                    cliente = value['cliente']
                    print(f"ID: {key} - CLIENTE: {cliente} - NOME_CLIENTE: {clientes[cliente]['nome']} - DIA: {value['dia']}")
                    print(f'{"-"*60}')
                while True:                    
                    id_lista = input("\nInsira o ID da lista de exercícios que deseja editar ou '0' para sair\n: ")
                    dia = input('\nInsira o dia da semana que deseja editar a lista de exercício\n: ').capitalize()
                    if id_lista in lista_exercicios.keys() and dia in lista_exercicios[id_lista]['dia']:
                        print("""\n
1. Nome do exercício
2. Grupo muscular
3. Quantidade de séries
4. Quantidade de repetições)""")
                        opcao_editar = input('\nInsira o que deseja editar da lista de exercicios\n:').lower()
                        if opcao_editar == '1' or opcao_editar[0]=='n':
                                while True:
                                    especial = ['1','2','3','4','5','6','7','8','9','0','!','@','#','$','%','&',',','.',';']
                                    novo_nome_exe = input(f"\nInsira o nome do novo exercicio \n:").capitalize()
                                    diferente = False
                                    for letra1 in novo_nome_exe:
                                        if letra1 in especial:
                                            diferente = True
                                            break
                                    if diferente == True:
                                        print("""\nO exercício não pode conter esses caracteres
(1234567890!@#$%&*<>,.;)
Tente novamente!\n""")
                                        sleep(3)
                                    else:
                                        break
                                lista_exercicios[id_lista]['exercicio'] = novo_nome_exe
                                with open(exercicios_json,'w',encoding='utf-8') as dados_nome_exercicio:
                                    json.dump(lista_exercicios, dados_nome_exercicio,indent=4)
                                print(f"O nome do exercício foi alterado com sucesso!\n")
                        elif opcao_editar == '2' or opcao_editar[0]=='g':
                                while True:
                                    especial = ['1','2','3','4','5','6','7','8','9','0','!','@','#','$','%','&',',','.',';']
                                    novo_grupo = input(f"\nInsira o novo grupo muscular\n:").capitalize()
                                    diferente = False
                                    for letra2 in novo_grupo:
                                        if letra2 in especial:
                                            diferente = True
                                            break
                                    if diferente == True:
                                        print("""\nO grupo muscular não pode conter esses caracteres
        (1234567890!@#$%&*<>,.;)
        Tente novamente!\n""")
                                        sleep(3)
                                    else:
                                        break
                                lista_exercicios[id_lista]['grupo'] = novo_grupo
                                with open(exercicios_json,'w',encoding='utf-8') as dados_grupo:
                                    json.dump(lista_exercicios, dados_grupo,indent=4)
                                print(f"O grupo muscular foi alterado com sucesso!\n")
                        elif opcao_editar == '3' or opcao_editar[0]=='q':
                                while True:
                                    try:
                                        nova_serie = int(input(f"\nInsira a quantidade de séries do exercício\n:"))
                                        break
                                    except ValueError:
                                        print(Fore.RED+"\nEscreva um valor válido."+Fore.RESET+"Apenas números")
                                        sleep(3)
                                lista_exercicios[id_lista]['series'] = nova_serie
                                with open(exercicios_json,'w',encoding='utf-8') as dados_serie:
                                    json.dump(lista_exercicios, dados_serie,indent=4)
                                print(f"A quantidade de séries do exercíos foi alterada com sucesso!\n")
                        elif opcao_editar == '4' or opcao_editar[0]=='q':
                                while True:
                                    try:
                                        nova_repeticao = int(input(f"\nInsira a quantidade de repetições do exercício\n:"))
                                        break
                                    except ValueError:
                                        print(Fore.RED+"\nEscreva um valor válido."+Fore.RESET+"Apenas números")
                                        sleep(3)
                                lista_exercicios[id_lista]['repetições'] = nova_repeticao
                                with open(exercicios_json,'w',encoding='utf-8') as dados_repeticao:
                                    json.dump(lista_exercicios, dados_repeticao,indent=4)
                                print(f"\nA quantidade de repetições foi alterada com sucesso!\n")
                        break
                    elif id_lista=='0':
                            break
                    else:
                        print("\nID não encontrado e/ou dia da semana inexistente\nTente novamente!")
                        sleep(3)
            break
        elif opcao=='0':
            break
        else:
            print(Fore.RED+"\nOpção inválida\n"+Fore.RESET)
    print(f'{"-"*60}\n{"- "*30}') # deixar bunito
    return ""

# Função excluir com parametros que são dicionários, aqui você exlui clientes, avaliações ou lista de exercicios
def excluir(clientes,avaliacoes,lista_exercicios, clientes_json, avaliacoes_json, exercicios_json):
    os.system("cls")
    print(f"\n{'- '*30}")
    while True:
        print(f'{"-"*60}\n{" EXCLUIR ":^60}\n{"-"*60}') 
        print("""   
1 - Cliente
2 - Avaliação do cliente
3 - Lista de exercicíos (por dia da semana)
0 - Sair\n""")
        opcao = input("Insira a opção que desejar\n:")
        if opcao == '1' or opcao =='c'.lower():
            os.system('cls')
            if not clientes:
                print(f'\n{"-"*60}')
                print(Fore.RED+"Não há clientes!"+Fore.RESET)
                print(f'{"-"*60}\n')
                break
            else:
                print(f'\n{" CLIENTES ":^60}\n') # clientes disponíveis
                for key, value in clientes.items():
                    print(f"ID: {key} - NOME: {value['nome']}\n")
                while True:
                    cliente = input("Deseja excluir qual cliente? (insira o id): ")
                    if cliente in clientes.keys(): # se o cliente existir, ele exclui
                            while True:
                                resp = input("\nRealmente deseja excluir? (sim/nao)\nIsso apagará o cliente, avaliação e lista de exercícios!\n")
                                if resp=="sim" or resp=='s':
                                    clientes.pop(cliente) # exclui o cliente
                                    with open(clientes_json,'w',encoding='utf-8') as dados_cliente: # salva no arquivo .json novamente
                                                json.dump(clientes, dados_cliente,indent=4)
                                    for key_avaliacao, value_avaliacao in avaliacoes.items(): # pega a chave e os valores dessa chave do dicionário avaliações
                                            if value_avaliacao['cliente'] == cliente:
                                                avaliacoes.pop(key_avaliacao) # exclui a avaliação
                                                with open(avaliacoes_json,'w',encoding='utf-8') as dados_ava: # salva no arquivo .json novamente
                                                    json.dump(avaliacoes, dados_ava,indent=4)
                                                break
                                    for key_lista, value_lista in lista_exercicios.items(): # pega a chave e os valores dessa chave do dicionário lista_exercicios
                                            if value_lista['cliente'] == cliente:
                                                lista_exercicios.pop(key_lista)
                                                with open(exercicios_json,'w',encoding='utf-8') as dados_nome: # salva no arquivo .json novamente
                                                    json.dump(lista_exercicios, dados_nome,indent=4)
                                                break
                                    print("\nCliente excluido com sucesso!")
                                    break
                                elif resp=='nao' or resp=="não" or resp=='n':
                                    break
                                else:
                                    print(Fore.RED+"\nInsira novamente!\n"+Fore.RESET)
                            break
                    else:
                            print("\nID inválida. Tente novamente.\n")
            break
        elif opcao == '2' or opcao =='a'.lower():
            os.system('cls')
            if not avaliacoes:
                print(f'\n{"-"*60}')
                print(Fore.RED+"Não há avaliações!"+Fore.RESET)
                print(f'{"-"*60}\n')
                break
            else:
                print(f'{" CLIENTES ":^60}\n') # clientes disponíveis
                for key, value in clientes.items():
                    print(f"ID: {key} - NOME: {value['nome']}\n")
                while True:
                    cliente_ava = input("Deseja excluir a avaliação de qual cliente? (insira o id): ")
                    if cliente_ava in clientes.keys(): # se o cliente existir, ele exclui
                        for key_avaliacao, value_avaliacao in avaliacoes.items(): # pega a chave e os valores dessa chave do dicionário avaliações
                            if value_avaliacao['cliente'] == cliente_ava:
                                avaliacoes.pop(key_avaliacao) # exclui a avaliação
                                with open(avaliacoes_json,'w',encoding='utf-8') as dados_ava: # salva no arquivo .json novamente
                                    json.dump(avaliacoes, dados_ava,indent=4)
                                print("\nAvaliação excluido com sucesso!")
                                break
                            else:
                                print("\nEsse cliente não possui avaliacoes")
                        break
                    else:
                        print("\nID inválido. Tente novamente.\n")
            break
        elif opcao == '3' or opcao =='l'.lower():
            os.system('cls')
            if not lista_exercicios:
                print(f'\n{"-"*60}')
                print(Fore.RED+"Não há lista de exercicíos!"+Fore.RESET)
                print(f'{"-"*60}\n')
                break
            else:
                print(f'{" CLIENTES ":^60}\n') # clientes disponíveis
                for key, value in clientes.items():
                    print(f"ID: {key} - NOME: {value['nome']}\n")
                while True:
                    cliente_lista = input("Deseja excluir a lista de exercicios de qual cliente? (insira a chave): ")
                    if cliente_lista in clientes.keys(): # se o cliente existir, ele exclui
                        for key_lista, value_lista in lista_exercicios.items(): # pega a chave e os valores dessa chave do dicionário lista de exercicios
                            if value_lista['cliente'] == cliente_lista:
                                lista_exercicios.pop(key_lista) # exclui a lista de exercicios
                                with open(exercicios_json,'w',encoding='utf-8') as dados_lista: # salva no arquivo .json novamente
                                    json.dump(lista_exercicios, dados_lista,indent=4)
                                print("\nLista de exercicios excluido com sucesso!")
                                break
                            else:
                                print("\nEsse cliente não possui lista de exercicios")
                        break
                    else:
                        print("\nID inválido. Tente novamente.\n")
            break
        elif opcao=="0":
            break
        else:
            print("\nOpção inválida")

    print(f'{"-"*60}\n{"- "*30}') # deixar bunito
    return ""

# Função pesquisar com parametros que são dicionários e da para pesquisar pelos clientes, avaliações e lista de exercicios
def pesquisar(clientes,avaliacoes,lista_exercicios, clientes_json, avaliacoes_json, exercicios_json):
    os.system("cls")
    print(f"\n{'- '*30}")
    while True:
        print(f'{"-"*60}\n{" PESQUISAR ":^60}\n{"-"*60}')
        print("""
1 - Cliente
2 - Avaliação do cliente
3 - Lista de exercicíos (por dia da semana)
0 - Sair\n""")
        opcao = input("\nInsira a opção que desejar\n:")
        if opcao == '1' or opcao == 'c'.lower():
            print(f'\n{"-"*60}\n{" PESQUISA DE CLIENTES ":^60}\n{"-"*60}\n')
            if not clientes:
                print(f'\n{"-"*60}')
                print(Fore.RED+"Não há clientes!"+Fore.RESET)
                print(f'{"-"*60}\n')
                break
            else:
                while True:
                    resp = input('\nDeseja pesquisar por?\n1. Nome\n2. Id\n:').lower()
                    if resp == '1' or resp == 'n':
                        print(f'{" CLIENTES ":^60}\n') # clientes disponíveis
                        for key, value in clientes.items():
                            print(f"ID: {key} - NOME: {value['nome']}\n")
                        while True:
                            cont = 0
                            nome = input("\nInsira o nome do cliente\n:").capitalize().strip()
                            nome_clientes = []
                            for key, value in clientes.items():
                                nome_clientes.append(value['nome'])
                            if nome in nome_clientes: # verifica se o cliente existe
                                print(f'{" CLIENTES ":^60}\n') # clientes disponíveis
                                os.system("cls")
                                for key_cliente, value_cliente in clientes.items(): # pega a chave (id) e o valor (nome,idade...) de cada cliente
                                    if value_cliente['nome'] == nome:
                                        print("-"*60) # deixar bunito 
                                        print(f'\nID -> {key_cliente}\nNOME -> {value_cliente["nome"]}\nIDADE -> {value_cliente["idade"]}', # mostra clientes disponíveis
                                        f'\nSEXO -> {value_cliente["sexo"]}\nTELEFONE -> {value_cliente["telefone"]}\nSTATUS -> {value_cliente["status"]}\n')
                                        cont+=1
                                print(f"\nExistem {cont} com esse nome")
                                break
                            else:
                                print(f"\n{nome} não foi encontado(a)\n")
                                print("-"*60) # deixar bunito 
                        break
                    elif resp == '2' or resp[0] == 'i':
                        print(f'{" CLIENTES ":^60}\n') # clientes disponíveis
                        for key, value in clientes.items():
                            print(f"ID: {key} - NOME: {value['nome']}\n")
                        while True:
                            id_ = input("\nInsira o id do cliente\n:")
                            if id_ in clientes.keys(): # verifica se o cliente existe
                                print(f'{" CLIENTES ":^60}\n') # clientes disponíveis
                                os.system("cls")
                                for key_cliente, value_cliente in clientes.items(): # pega a chave (id) e o valor (nome,idade...) de cada cliente
                                    if id_ == key_cliente:
                                        print("-"*60) # deixar bunito 
                                        print(f'\nID -> {key_cliente}\nNOME -> {value_cliente["nome"]}\nIDADE -> {value_cliente["idade"]}', # mostra clientes disponíveis
                                        f'\nSEXO -> {value_cliente["sexo"]}\nTELEFONE -> {value_cliente["telefone"]}\nSTATUS -> {value_cliente["status"]}\n')
                                break
                            else:
                                print(f"\n{id_} não foi encontado(a)\n")
                                print("-"*60) # deixar bunito 
                        break
            break
        elif opcao == '2' or opcao == 'a'.lower():
            print(f'\n{"-"*60}\n{" PESQUISA DE AVALIAÇÕES ":^60}\n{"-"*60}\n')
            if not avaliacoes:
                print(f'\n{"-"*60}')
                print(Fore.RED+"Não há avaliações!"+Fore.RESET)
                print(f'{"-"*60}\n')
                break
            else:
                while True:
                    resp = input("\nDeseja pesquisar por:\n1. ID avaliação\n2. ID cliente\n3. Nome cliente\n4. Data avaliação\n:")
                    if resp == '1':
                        while True:
                            avaliacao_id = input("\nInsira o id da avaliação\n: ")
                            if avaliacao_id in avaliacoes.keys(): # verifica se a avaliação existe
                                print(f'{" AVALIAÇÕES ":^60}\n') # clientes disponíveis
                                os.system("cls")
                                for key_ava, value_ava in avaliacoes.items(): # pega a chave (id) e o valor  de cada avalição
                                    if avaliacao_id == key_ava: # se essa chave da avaliação existe
                                        print("-"*60) # deixar bunito 
                                        print(f'\nID -> {key_ava}\nALTURA -> {value_ava["altura"]}\nPESO -> {value_ava["peso"]}', # mostra clientes disponíveis
                                        f'\nGORDURA (%) -> {value_ava["gordura"]}\nBRAÇOS (cm) -> {value_ava["braço"]}\nCINTURA (cm) -> {value_ava["cintura"]}',
                                        f'\nPERNAS (cm) -> {value_ava["perna"]}\nDATA -> {value_ava["data"]}\nCHAVE CLIENTE ->{value_ava["cliente"]}\n')
                                break
                            else:
                                print(f"\nA avaliação {avaliacao_id} não foi encontada\n")
                                print("-"*60) # deixar bunito 
                        break
                    elif resp == '2':
                        while True:
                            cliente_id = input("\nInsira o id do cliente\n:")
                            cliente_id_ava = []
                            for key, value in avaliacoes.items():
                                cliente_id_ava.append(value['cliente'])
                            if cliente_id in cliente_id_ava: # se essa chave do cliente existe
                                print(f'{" AVALIAÇÕES ":^60}\n') # clientes disponíveis
                                os.system("cls")
                                for key_ava, value_ava in avaliacoes.items(): # pega a chave (id) e o valor  de cada avaliação
                                    if cliente_id == value_ava['cliente']: # se essa chave do cliente existe
                                        print("-"*60) # deixar bunito 
                                        print(f'\nID -> {key_ava}\nALTURA -> {value_ava["altura"]}\nPESO -> {value_ava["peso"]}', # mostra clientes disponíveis
                                        f'\nGORDURA (%) -> {value_ava["gordura"]}\nBRAÇOS (cm) -> {value_ava["braço"]}\nCINTURA (cm) -> {value_ava["cintura"]}',
                                        f'\nPERNAS (cm) -> {value_ava["perna"]}\nDATA -> {value_ava["data"]}\nCHAVE CLIENTE ->{value_ava["cliente"]}\n')
                                break
                            else:
                                print(f"\nO cliente {cliente_id} não foi encontado(a)\n")
                                print("-"*60) # deixar bunito 
                        break
                    elif resp == '3':
                        while True:
                            nome = input("\nInsira o nome do cliente\n:").capitalize().strip()
                            cliente_id = None
                            for id_cliente, info_cliente in clientes.items(): # echa o ID do cliente com base no nome
                                if info_cliente['nome'] == nome:
                                    cliente_id = id_cliente
                                    break
                            cliente_possui_avaliacao = False # verifica se o cliente possui uma avaliação
                            for avaliacao in avaliacoes.values(): 
                                if avaliacao['cliente'] == cliente_id:
                                    cliente_possui_avaliacao = True
                                    break
                            if cliente_possui_avaliacao: # se possui avaliação, ele mostra a avaliação do cliente
                                print(f'{" AVALIAÇÕES ":^60}\n') # clientes disponíveis
                                os.system("cls")
                                for key_ava, value_ava in avaliacoes.items():
                                    if cliente_possui_avaliacao:
                                        print("-"*60) # deixar bunito 
                                        print(f'\nID -> {key_ava}\nALTURA -> {value_ava["altura"]}\nPESO -> {value_ava["peso"]}', # mostra clientes disponíveis
                                        f'\nGORDURA (%) -> {value_ava["gordura"]}\nBRAÇOS (cm) -> {value_ava["braço"]}\nCINTURA (cm) -> {value_ava["cintura"]}',
                                        f'\nPERNAS (cm) -> {value_ava["perna"]}\nDATA -> {value_ava["data"]}\nCHAVE CLIENTE ->{value_ava["cliente"]}\n')
                                break
                            else:
                                    print(f"\nO cliente {nome} não possui uma avaliação.\n")
                                    print("-"*60) # deixar bunito
                        break 
                    elif resp == '4':
                        while True:
                            data = input("\nInsira a data da avaliação\nex: dd/mm/aaaa\n:")
                            data_ava = []
                            for key, value in avaliacoes.items():
                                    data_ava.append(value['data'])
                            if data in data_ava: # se essa chave do cliente existe
                                print(f'{" AVALIAÇÕES ":^60}\n') # clientes disponíveis
                                os.system("cls")
                                for key_ava, value_ava in avaliacoes.items(): # pega a chave (id) e o valor  de cada avaliação
                                    if data == value_ava['data']: # se essa chave do cliente existe
                                        print("-"*60) # deixar bunito 
                                        print(f'\nID -> {key_ava}\nALTURA -> {value_ava["altura"]}\nPESO -> {value_ava["peso"]}', # mostra clientes disponíveis
                                        f'\nGORDURA (%) -> {value_ava["gordura"]}\nBRAÇOS (cm) -> {value_ava["braço"]}\nCINTURA (cm) -> {value_ava["cintura"]}',
                                        f'\nPERNAS (cm) -> {value_ava["perna"]}\nDATA -> {value_ava["data"]}\nCHAVE CLIENTE ->{value_ava["cliente"]}\n')
                                break
                            else:
                                print(f"\nA data {data} não foi encontada.\n")
                                print("-"*60) # deixar bunito 
                        break
                    else:
                        print("\nOpção inválida!\n")               
            break
        elif opcao == '3' or opcao == 'l'.lower():
            if not lista_exercicios:
                print(f'\n{"-"*60}')
                print(Fore.RED+"Não há lista de exercicíos!"+Fore.RESET)
                print(f'{"-"*60}\n')
                break
            else:
                while True:
                    os.system('cls')
                    print(f'\n{"-"*60}\n{" PESQUISA DE LISTA DE EXERCICIOS ":^60}\n{"-"*60}\n')
                    for key,value in clientes.items(): # cliente disponíveis
                        print(f"ID: {key} - NOME: {value['nome']}\n")
                    nome = input("\nInsira o nome do cliente\n:").capitalize().strip()
                    cliente_id = None
                    for id_cliente, info_cliente in clientes.items(): # echa o ID do cliente com base no nome
                        if info_cliente['nome'] == nome:
                            cliente_id = id_cliente
                            break
                    cliente_possui_exercicio = False # verifica se o cliente possui uma lista de exercicios
                    for lista in lista_exercicios.values(): 
                        if lista['cliente'] == cliente_id:
                            cliente_possui_exercicio = True
                            break
                    while True:
                        dia = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado']
                        dia_semana = input(f"\nDia da semana (Segunda - Sábado)\nEx: Terça\n:").capitalize().strip()
                        semana_separado=re.split("[ -]", dia_semana)
                        correct_dia = False
                        if (semana_separado[0] in dia) or ((semana_separado[0] in dia) and (semana_separado[1] == 'feira')):
                            correct_dia = True
                        if correct_dia:
                            break
                        else:
                            print("\nInsira um dia válido\n")
                    if cliente_possui_exercicio and correct_dia: # se possui lista de exercicios, ele mostra a lista de exercicio do cliente
                        os.system("cls")
                        for key_lista, value_lista in lista_exercicios.items():
                            if value_lista['dia'] == dia_semana:
                                for key_cliente, value_cliente in clientes.items():
                                    if nome == value_cliente['nome']:
                                        print("-"*60) # deixar bunito 
                                        print(f'\n{f"{nome} - {dia_semana}":^60}\n')
                                        print(f'\nID -> {key_lista}\nEXERCICIO -> {value_lista["exercicio"]}\nMUSCULO -> {value_lista["grupo"]}\nSÉRIES -> {value_lista["series"]}',
                                        f'\nREPETIÇÕES -> {value_lista["repetições"]}\nCLIENTE -> {value_lista["cliente"]}')
                        break
                    else:
                        print(f"\nO cliente {nome} não existe ou não possui uma lista de exercicios nessa data!!")
                        print("-"*60) # deixar bunito    
                        sleep(3)           
            break
        elif opcao=="0":
            break
        else:
            print("\nOpção inválida! Tente novamente\n")
    print(f'{"-"*60}\n{"- "*30}') # deixar bunito
    return ""

# Função listar com parametros que são dicionários, onde você pode listar algumas informações
def listar(clientes,avaliacoes,lista_exercicios, clientes_json, avaliacoes_json, exercicios_json):
    os.system("cls")
    print(f"\n{'- '*30}")
    print(f'{"-"*60}\n{" LISTAR ":^60}\n{"-"*60}') 
    print("""
1 - todos os cliente;
2 - todos os clientes ativos;
3 - todos os clientes inativos;
4 - todas as listas de exercícios, por cliente;
5 - todas as avaliações, por cliente;
0 - Sair.\n""")
    while True:
        opcao = input("Escolha a opção (pelo número) que deseja listar: \n") # recebe o que a pessoa quer listar
        if opcao == '1': # lista clientes
            print(f'{"-"*60}\n{" CLIENTES ":^60}\n{"-"*60}')
            with open("clientes.json","r",encoding="utf8") as dados_cli: # verifica se exite mclientes cadastrados
                cliente = json.load(dados_cli)
            if not cliente:
                    print("Não há clientes!\n")
                    break
            else:
                for key, value in clientes.items(): # pega todas as chaves e valores do diconário clientes
                    print(f'ID -> {key}\nNOME -> {value[0]}\nIDADE -> {value[1]}\nSEXO -> {value[2]}',
                        f'\nTELEFONE -> {value[3]}\nSTATUS -> {value[4]}')    
                    print("-"*60) # deixar bunito 
                print("\nLista de clientes!")              
            break
        elif opcao == '2': # lista clientes ativos
            print(f'{"-"*60}\n{" CLIENTES ATIVOS ":^60}\n{"-"*60}')
            with open("clientes.json","r",encoding="utf8") as dados_cli: # verifica se exite mclientes cadastrados
                cliente = json.load(dados_cli)
            if not cliente:
                    print("Não há clientes!\n")
                    break
            else:
                for key, value in clientes.items(): # pega todas as chaves e valores do dicionário clientes
                    if value[-1] == 'ativo' or value[-1] == 'ativa' or value[-1] == 'a': 
                        print(f'ID -> {key}\nNOME -> {value[0]}\nIDADE -> {value[1]}\nSEXO -> {value[2]}',
                        f'\nTELEFONE -> {value[3]}\nSTATUS -> {value[4]}')        
                        print("-"*60) # deixar bunito
                print("\nLista de clientes ativos!")
            break
        elif opcao == '3': # lista de clientes inativos
            print(f'{"-"*60}\n{" CLIENTES INATIVOS ":^60}\n{"-"*60}')
            with open("clientes.json","r",encoding="utf8") as dados_cli: # verifica se exite mclientes cadastrados
                cliente = json.load(dados_cli)
            if not cliente:
                    print("Não há clientes!\n")
                    break
            else:
                for key, value in clientes.items(): # pega todas as chaves e valores do dicionário clientes
                    if value[-1] == 'inativo' or value[-1] == 'inativa' or value[-1] == 'i': 
                        print(f'ID -> {key}\nNOME -> {value[0]}\nIDADE -> {value[1]}\nSEXO -> {value[2]}',
                        f'\nTELEFONE -> {value[3]}\nSTATUS -> {value[4]}')
                        print("-"*60) # deixar bunito
                print("\nLista de clientes inativos!")
            break  
        elif opcao == '4': # lista de listas de exercícios por cliente
            print(f'{"-"*60}\n{" LISTA DE EXERCICIOS POR CLIENTE ":^60}\n{"-"*60}')
            with open("lista_exercicios.json","r",encoding="utf8") as dados_lista: # verifica se exitem lista de exercicios cadastrados
                lista = json.load(dados_lista)
            if not lista:
                    print("Não há lista de exercicios!\n")
                    break
            else:
                for key, value in lista_exercicios.items(): # pega todas as chaves e valores do dicionário lista_exercicios
                    if str(value[-1]) in clientes.keys():
                        print(f'{f" {clientes[str(value[-1])][0]} - {value[-1]}":^60}\n')
                        print(f'ID -> {key}\nDIA DA SEMANA -> {value[0]}\nEXERCICIO -> {value[1]}\nMUSCULO -> {value[2]}\nSERIES -> {value[3]}',
                        f'\nREPETIÇÕES -> {value[4]}\nCLIENTE -> {value[5]}\n')
                        print("-"*60) # deixar bunito
                    else:
                        print(f"Não há lista de exercicios para {clientes[str(value[-1])][0]}")
                print("\nLista de lista de exercicios por cliente!")
            break
        elif opcao == '5': # lista de avalições por cliente
            print(f'{"-"*60}\n{" AVALIAÇÕES POR CLIENTE ":^60}\n{"-"*60}')
            with open("avaliacoes.json","r",encoding="utf8") as dados_ava: # verifica se exite mclientes cadastrados
                avaliacao = json.load(dados_ava)
            if not avaliacao:
                    print("Não há avaliações!\n")
                    break
            else:
                for key, value in avaliacoes.items(): # pega todas as chaves e valores do dicionário avaliacoes
                    if str(value[-1]) in clientes.keys():
                        print(f'{f" {clientes[str(value[-1])][0]} - {value[-1]}":^60}\n')
                        print(f'\nID -> {key}\nALTURA -> {value[0]}\nPESO -> {value[1]}', # mostra clientes disponíveis
                                    f'\nGORDURA (%) -> {value[2]}\nBRAÇOS (cm) -> {value[3]}\nCINTURA (cm) -> {value[4]}',
                                    f'\nPERNAS (cm) -> {value[5]}\nDATA -> {value[6]}\nCLIENTE -> {value[7]}\n')
                        print("-"*60) # deixar bunito
                    else:
                        print(f"Não há avalições para {clientes[str(value[-1])][0]}")
                print("\nAvaliações por cliente!")
            break
        elif opcao == '0':
            break
        else:
            print("\nOpção inválida! Tente novamente\n")
    print(f"\n{'- '*30}")

# Função relatorio com parametros que são dicionários, mostrar o relatório de algumas informações
def relatorio(clientes,avaliacoes,lista_exercicios, clientes_json, avaliacoes_json, exercicios_json):
    os.system("cls")
    print(f"\n{'- '*30}")
    print(f'{"-"*60}\n{" RELATÓRIO ":^60}\n{"-"*60}')
    print("""
1 - total de cliente;
2 - total de clientes ativos e inativos;
3 - total de avaliações, por cliente;
4 - total de listas de exercícios, por cliente;
5 - total de exercícios diários, por cliente;
0 - Sair.\n""")
    while True:
        opcao = input("Digite a opção desejada (o número)\n:")
        if opcao == '1':
            print(f'\n{"-"*60}\n{" TOTAL DE CLIENTES ":^60}\n{"-"*60}\n')
            with open("clientes.json","r",encoding="utf8") as dados_cli: # verifica se exite mclientes cadastrados
                cliente = json.load(dados_cli)
            if not cliente:
                print("\nNão há clientes!\n")
                break
            else:
                contador_cliente = 0
                for key in clientes.keys(): # pega todas as chaves do diconário clientes
                    contador_cliente += 1 # conta quantas chaves tem no dicionário clientes
                print("-"*60) # deixar bunito  
                print(f"\nO total de clientes é {contador_cliente}!\n")             
                print("-"*60) # deixar bunito  
            break
        elif opcao == '2':
            print(f'\n{"-"*60}\n{" TOTAL DE CLIENTES ATIVOS E INATIVOS ":^60}\n{"-"*60}')
            with open("clientes.json","r",encoding="utf8") as dados_cli: # verifica se exite mclientes cadastrados
                cliente = json.load(dados_cli)
            if not cliente:
                    print("\nNão há clientes!\n")
                    break
            else:
                contador_ativos = 0
                contador_inativos = 0
                for value_a in clientes.values(): # pega todas as chaves e valores do dicionário clientes
                    if value_a[-1] == 'ativo' or value_a[-1] == 'ativa' or value_a[-1] == 'a': 
                        contador_ativos += 1 # conta quantos clientes ativos tem
                for value_i in clientes.values(): # pega todas as chaves e valores do dicionário clientes
                    if value_i[-1] == 'inativo' or value_i[-1] == 'inativa' or value_i[-1] == 'i':
                        contador_inativos += 1 # conta quantos clientes inativos tem
                print("-"*60) # deixar bunito
                print(f"\nO total de clientes ativos é {contador_ativos}!\n")
                print(f"\nO total de clientes inativos é {contador_inativos}!\n")
                print("-"*60) # deixar bunito
            break
        elif opcao == '3':
            print(f'\n{"-"*60}\n{" TOTAL DE AVALIAÇÕES ":^60}\n{"-"*60}')
            with open("avaliacoes.json","r",encoding="utf8") as dados_ava: # verifica se exite mclientes cadastrados
                avaliacao = json.load(dados_ava)
            if not avaliacao:
                    print("\nNão há avaliações!\n")
                    break
            else:
                total_avaliacoes_por_cliente = {} # novo dicionario para armazenar o total de avaliações por clientes
                for cliente_id in clientes: # começa o total de avaliações por cliente como zero para todos os clientes
                    total_avaliacoes_por_cliente[cliente_id] = 0

                for avaliacao_id, avaliacao_valor in avaliacoes.items(): # conta as avaliações por cliente
                    cliente_id = str(avaliacao_valor[-1])
                    total_avaliacoes_por_cliente[cliente_id] += 1

                for cliente_id, total_avaliacoes in total_avaliacoes_por_cliente.items(): # mostra o total de avaliações por cliente
                    cliente_nome = clientes[cliente_id][0]
                    print(f"Cliente: {cliente_nome}, Total de Avaliações: {total_avaliacoes}")
                    print("-"*60) # deixar bunito
            break
        elif opcao == '4':
            print(f'\n{"-"*60}\n{" TOTAL DE LISTA DE EXERCICIOS ":^60}\n{"-"*60}')
            with open("lista_exercicios.json","r",encoding="utf8") as dados_exer: # verifica se exite mclientes cadastrados
                lista = json.load(dados_exer)
            if not lista:
                print("\nNão há lista de exercicios!\n")
                break
            else:
                total_lista_exercicios_por_cliente = {} # novo dicionario para armazenar o total de lista de exercicios por clientes
                for cliente_id in clientes: # começa o total de lista de exercicios por cliente como zero para todos os clientes
                    total_lista_exercicios_por_cliente[cliente_id] = 0

                for lista_id, exercicio in avaliacoes.items(): # conta as listas de exercicios por cliente
                    cliente_id = str(exercicio[-1])
                    total_lista_exercicios_por_cliente[cliente_id] += 1

                for cliente_id, total_lista_exercicios in total_lista_exercicios_por_cliente.items(): # mostra o total de lista de exercicios por cliente
                    cliente_nome = clientes[cliente_id][0]
                    print(f"Cliente: {cliente_nome}, Total de lista de exercicios: {total_lista_exercicios}")
                    print("-"*60) # deixar bunito
            break
        elif opcao == '5':
            print(f'\n{"-"*60}\n{" TOTAL DE EXERCICIOS DIÁRIOS ":^60}\n{"-"*60}')
            with open("lista_exercicios.json","r",encoding="utf8") as dados_exer: # verifica se exite mclientes cadastrados
                lista = json.load(dados_exer)
            if not lista:
                print("\nNão há lista de exercicios!\n")
                break
            else:
                total_exercicios_por_cliente = {}
                for cliente_id in clientes: # começa o total de exercícios diários por cliente como zero para todos os clientes
                    total_exercicios_por_cliente[cliente_id] = {}

                for exercicio_id, exercicio in lista_exercicios.items(): # conta os exercícios diários por cliente
                    dia_semana = exercicio[0] # define dia_semana como o valor do dia que está armazenado em lista_exercicios
                    cliente_id = str(exercicio[-1]) # define cliente_id como o  ultimo valor que está armazenado em lista_exercicios 
                    # (que é o id de cada cliente em clientes)
                    if dia_semana in total_exercicios_por_cliente[cliente_id]:
                        total_exercicios_por_cliente[cliente_id][dia_semana] += 1
                    else:
                        total_exercicios_por_cliente[cliente_id][dia_semana] = 1

                for cliente_id, total_exercicios in total_exercicios_por_cliente.items(): # mostra o total de exercícios diários por cliente
                    cliente_nome = clientes[cliente_id][0] # pega o nome do cliente através do id
                    print("-"*60) # deixar bunito
                    print(f"Cliente: {cliente_nome}")
                    for dia_semana, total in total_exercicios.items(): # mostra cada dia da semana e total de exercicios de cada cliente
                        print(f"Dia: {dia_semana}, Total de exercícios diários: {total}")
                break
        elif opcao == '0':
            break
        else:
            print("\nOpção inválida! Tente novamente\n")
    print(f"\n{'- '*30}")