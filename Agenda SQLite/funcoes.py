import os
from sqlite3 import Error
from colorama import Fore
from time import sleep

def Menu():
    os.system('cls')
    print(f"{'-'*30}\n{'- '*15}\n{'Agenda':^30}\n{'- '*15}\n{'-'*30}")
    option = input('''
1 - Cadastrar contato
2 - Editar contato
3 - Excluir contato
4 - Mostrar lista de contatos
0 - Fechar agenda
\n→ ''')
    return option

def contem_numbers(number):
    for letter in number:
        if letter in ['1','2','3','4','5','6','7','8','9','0']:
            return True
    return False

def contem_especial(valor):
    especial = ['!','@','.','#','%','*','&',';']
    for letter in valor:
        if letter in especial:
            return True
    return False

def contem_letras(valor):
    for caractere in valor:
        if "a" <= caractere <= "z" or "A" <= caractere <= "Z":
            return True
    return False

def CommitDB(connection,sql):
    c = connection.cursor()
    c.execute(sql)
    connection.commit()

def BuscarDB(connection,sql):
    try:
        c = connection.cursor()
        c.execute(sql)
        result = c.fetchall()
        return result
    except Error as er:
        print(Fore.RED+'Erro de conexão: '+Fore.RESET,er)

def Cadastro(connection):    
    while True:
        os.system('cls')
        print(f"{'-'*30}\n{'- '*15}\n{'Cadastro':^30}\n{'- '*15}\n{'-'*30}")
        option = input('''
 1 - Cadastrar contato
 0 - Voltar ao Menu
 \n→ ''')
        if option:
            if option=='1':
                os.system('cls')
                print(f"\n{'-'*30}")   
                while True:
                    nome = input('\nInsira o nome\n→ ').capitalize().strip()
                    if nome:
                        break
                    else:
                        print(Fore.RED+'\nInsira um nome válido!'+Fore.RESET)
                        sleep(2)
                while True:
                    telefone = input(f'\nInsira o telefone de {nome}\nex: (00)0000 0000\n→ ')
                    if contem_especial(telefone) or len(telefone)!=13 or telefone[0]!='(' or telefone[3]!=')' or telefone[8]!=" ":
                        print(Fore.RED+'\nInsira um telefone válido!'+Fore.RESET)
                        sleep(2)
                    else: break
                while True:
                    email = input(f'\nInsira o email de {nome}\nex: exemplo@agenda.com\n→ ')
                    if '@' in email and '.com' in email:
                        break
                    else:
                        print(Fore.RED+'\nInsira um email válido!')
                        sleep(2)                
                vSQL = f'''INSERT INTO Contatos (nome,telefone,email)
                            VALUES('{nome}','{telefone}','{email}')'''
                try:
                    CommitDB(connection,vSQL)
                    print(Fore.GREEN+f'\n{nome} cadastrado com sucesso!\n'+Fore.RESET)
                    print('-'*30)
                    print('Aperte "ENTER" para continuar...\n')
                    input()
                except:
                    print(Fore.RED+'\nErro de conexão... O contato não foi cadastrado!\n'+Fore.RESET)
                    print('-'*30)
                    print('Aperte "ENTER" para voltar...')
                    input()
                continue
            elif option=='0':
                break
            else: 
                print(Fore.RED+'\nInsira uma opção válida!\n'+Fore.RESET)
                print('Aperte "ENTER" para voltar...')
                print('-'*30)
                input()
        else:
            print(Fore.RED+'\nInsira uma opção válida!\n'+Fore.RESET)
            print('Aperte "ENTER" para voltar...')
            print('-'*30)
            input()
    print('-'*30)
    print('\nAperte "ENTER" para voltar...')
    input()

def Editar(connection):
    while True:
        os.system('cls')
        print(f"{'-'*30}\n{'- '*15}\n{'Editar':^30}\n{'- '*15}\n{'-'*30}")
        option = input('''
 1 - Editar contato
 0 - Voltar ao Menu
 \n→ ''')
        if option:
            if option=='1':
                vSQL = '''SELECT * FROM Contatos'''
                contatos = BuscarDB(connection,vSQL)
                if contatos:
                    while True:
                        nome_edit = input(Fore.BLUE+'\nInsira o nome do contato que deseja editar\n→ '+Fore.RESET).capitalize().strip()
                        if nome_edit:
                            vSQL = f'''SELECT * FROM Contatos WHERE nome="{nome_edit}"'''
                            contatos = BuscarDB(connection,vSQL)
                            have = False
                            for cont in contatos:
                                if cont[1]==nome_edit:   
                                    have = True
                                    os.system('cls')
                                    print(f"\n{'-'*30}")
                                    print(f"{'Contatos':^30}")
                                    print('-'*30)
                                    for contato in contatos:
                                        print(f"\nID______ → {contato[0]}\nNome____ → {contato[1]}\nTelefone → {contato[2]}\nEmail___ → {contato[3]}")
                                    break
                            if have:
                                while True:
                                    try:
                                        id_edit = int(input(Fore.BLUE+f"\nInsira o ID do contato que deseja excluir\n→ "+Fore.RESET))
                                        vSQL = f'''SELECT * FROM Contatos'''
                                        contatos = BuscarDB(connection,vSQL)
                                        for id_e in contatos:
                                            if id_e[0]==id_edit:
                                                break
                                        if id_e[0]==id_edit:
                                            break
                                        else:
                                            print(Fore.RED+'\nEsse ID não existe!'+Fore.RESET)
                                            print('-'*30)
                                            print('Aperte "ENTER" para continuar...')
                                            input()
                                    except ValueError:
                                        print(Fore.RED+'\nInsira uma opção válida!\n'+Fore.RESET)
                                        print('-'*30)
                                        print('Aperte "ENTER" para continuar...')
                                        input()
                                os.system('cls')
                                while True:
                                    new_nome = input(Fore.BLUE+'\nNovo nome\n→ '+Fore.RESET).capitalize().strip()
                                    if new_nome:
                                        break
                                    else:
                                        print(Fore.RED+'\nInsira um nome válido!\n'+Fore.RESET)
                                        sleep(2)
                                while True:
                                    new_telefone = input(Fore.BLUE+'\nNovo telefone\n→ '+Fore.RESET).capitalize().strip()
                                    if not new_telefone or contem_especial(new_telefone) or len(new_telefone)!=13 or new_telefone[0]!='(' or new_telefone[3]!=')' or new_telefone[8]!=" ":
                                        print(Fore.RED+'\nInsira um telefone válido!\n'+Fore.RESET)
                                        sleep(2) 
                                    else: break
                                while True:
                                    new_email = input(Fore.BLUE+f'\nNovo email\nex: exemplo@agenda.com\n→ '+Fore.RESET)
                                    if '@' in new_email and '.com' in new_email:
                                        break
                                    else:
                                        print(Fore.RED+'\nInsira um email válido!\n')
                                        sleep(2)
                                vSQL = f"UPDATE Contatos SET nome='{new_nome}', telefone='{new_telefone}', email='{new_email}' WHERE id_contato='{id_edit}'"
                                try:
                                    CommitDB(connection,vSQL)
                                    print(Fore.GREEN+f'\nContato editado com sucesso!\n'+Fore.RESET)
                                    print('-'*30)
                                    print('Aperte "ENTER" para continuar...')
                                    input()
                                except Error as er:
                                    print(Fore.RED+f'\nErro de conexão... O contato não foi editado!\nErro:{er}'+Fore.RESET)
                                    sleep(2)
                                finally:
                                    break
                            else:
                                print(Fore.RED+f"\n{nome_edit} não existe na base de dados!\n"+Fore.RESET)
                                print('-'*30)
                                print('Aperte "ENTER" para continuar...')
                                input()
                        else:
                            print(Fore.RED+'\nEsse contato não existe!\n'+Fore.RESET)
                            print('-'*30)
                            print('Aperte "ENTER" para continuar...')
                            input()
                    continue
                else:
                    print(Fore.RED+'\nNão existe nenhum contato cadastrado\n'+Fore.RESET)
                    break
            if option=='0':
                break
            else:
                print(Fore.RED+'\nInsira uma opção válida!\n'+Fore.RESET)
                print('-'*30)
                print('Aperte "ENTER" para continuar...')
                input()
        else:
            print(Fore.RED+'\nInsira uma opção válida!'+Fore.RESET)
            print('-'*30)
            print('Aperte "ENTER" para continuar...')
            input()
    print('-'*30)
    print('Aperte "ENTER" para voltar...')
    input()

def Excluir(connection):
    while True:
        os.system('cls')
        print(f"{'-'*30}\n{'- '*15}\n{'Excluir':^30}\n{'- '*15}\n{'-'*30}")
        option = input('''
 1 - Excluir contato
 0 - Voltar ao Menu
 \n→ ''')
        if option:
            if option=='1':
                os.system('cls')
                print('-'*30)
                nome = input(Fore.BLUE+'\nInsira o nome do contato que deseja excluir\n→ '+Fore.RESET).capitalize().strip()
                if nome:
                    vSQL = f'''SELECT * FROM Contatos WHERE nome="{nome}"'''
                    contatos = BuscarDB(connection,vSQL)
                    have = False
                    for cont in contatos:
                        if cont[1]==nome:   
                            have = True
                            print(f"\n{'-'*30}")
                            print(f"{'Contatos':^30}")
                            print('-'*30)
                            for contato in contatos:
                                print(f"\nID______ → {contato[0]}\nNome____ → {contato[1]}\nTelefone → {contato[2]}\nEmail___ → {contato[3]}")
                            break
                        else:
                            print(Fore.RED+f"\n{nome} não existe na base de dados!\n"+Fore.RESET)
                            sleep(2)
                    if have:
                        while True:
                            try:
                                id_contato = int(input(Fore.BLUE+f"\nInsira o ID do contato que deseja excluir\n→ "+Fore.RESET))
                                for id_c in contatos:
                                    if id_c[1]==nome:
                                        if id_c[0]==id_contato:
                                            break
                                if id_c[0]==id_contato:
                                    break
                                else:
                                    print(Fore.RED+'\nEsse ID não existe!'+Fore.RESET)
                                sleep(2)
                            except ValueError:
                                print(Fore.RED+'\nInsira uma opção válida!\n'+Fore.RESET)
                                sleep(2)
                        resp='s'
                        while resp=='s':
                            resp = input(Fore.RED+f"\nRealmente deseja exlcluir esse contato? (s/n)\n→ "+Fore.RESET)
                            if resp:
                                if resp=='s' or resp[0]=='s':
                                    vSQL = f'''DELETE FROM Contatos WHERE id_contato="{id_contato}";
'''
                                    CommitDB(connection,vSQL)
                                    print(f"\n{'-'*30}")
                                    print(Fore.GREEN+f"Contato excluido com sucesso!"+Fore.RESET)
                                    print(f"{'-'*30}\n")
                                    break
                                else:
                                    resp='n'
                            else:
                                print(Fore.RED+'\nInsira uma opção válida!\n'+Fore.RESET)
                                sleep(2)
                        print('-'*30)
                        print('Aperte "ENTER" para continuar...\n')
                        input()
                    else:
                        print(Fore.RED+'\nEsse nome não existe!\n'+Fore.RESET)
                        print('-'*30)
                        print('Aperte "ENTER" para continuar...\n')
                        input()
                else:
                    print(Fore.RED+'\nNome inválido!\n'+Fore.RESET)
                    sleep(2)
            elif option=='0':
                break
            else:
                print(Fore.RED+'\nInsira uma opção válida!\n'+Fore.RESET)
                sleep(2)
        else:
            print(Fore.RED+'\nInsira uma opção válida!\n'+Fore.RESET)
            sleep(2)
    print('-'*30)
    print('Aperte "ENTER" para voltar...\n')
    input()

def Mostrar(connection):
    while True:
        os.system('cls')
        os.system('cls')
        print(f"{'-'*30}\n{'- '*15}\n{'Pesquisar':^30}\n{'- '*15}\n{'-'*30}")
        option = input('''
 1 - Todos os contatos
 2 - Por nome
 0 - Voltar ao Menu
 \n→ ''')
        if option:
            vSQl = "SELECT * FROM Contatos"
            contatos = BuscarDB(connection, vSQl)
            if contatos:
                if option=='1':
                    os.system('cls')
                    print('-'*52)
                    print('|'+f'{"Contatos":^50}'+'|')
                    print('-'*52)
                    vSQl = "SELECT * FROM Contatos"
                    contatos = BuscarDB(connection, vSQl)
                    for contato in contatos:
                        print('|'+f'{f"ID → {contato[0]}":^50}'+'|')
                        print('|'+f'{f"Nome → {contato[1]}":^50}'+'|')
                        print('|'+f'{f"Telefone → {contato[2]}":^50}'+'|')
                        print('|'+f'{f"Email → {contato[3]}":^50}'+'|')
                        print('-'*52)
                    print('\nAperte "ENTER" para voltar...')
                    input()
                elif option=='2':
                    while True:
                        nome = input('\nInsira o nome da pessoa\n→ ').capitalize().strip()
                        if nome:
                            break
                        else:
                            print(Fore.RED+'\nInsira um nome válido!\n'+Fore.RESET)
                            print('-'*30)
                            print('Aperte "ENTER" para continuar...')
                            input()
                            vSQl = "SELECT * FROM Contatos"
                    contatos = BuscarDB(connection, vSQl)
                    have = False
                    for contato in contatos:
                        if contato[1]==nome:
                            have=True
                    if have:
                        os.system('cls')
                        print('-'*52)
                        print('|'+f'{"Contatos":^50}'+'|')
                        print('-'*52)
                        for contato in contatos:
                            if contato[1]==nome:
                                print('|'+f'{f"ID → {contato[0]}":^50}'+'|')
                                print('|'+f'{f"Nome → {contato[1]}":^50}'+'|')
                                print('|'+f'{f"Telefone → {contato[2]}":^50}'+'|')
                                print('|'+f'{f"Email → {contato[3]}":^50}'+'|')
                                print('-'*52)
                        print('\nAperte "ENTER" para voltar...')
                        input()
                    else:
                        print(Fore.RED+'\nEsse nome não está cadastrado!\n'+Fore.RESET)
                        print('-'*30)
                        print('Aperte "ENTER" para continuar...')
                        input()
                else:
                    break
            else:
                print(Fore.RED+'\nNão existe nenhum contato cadastrado\n'+Fore.RESET)
                break
        else:
            print(Fore.RED+'\nInsira uma opção válida!'+Fore.RESET)
            print('-'*30)
            print('Aperte "ENTER" para continuar...')
            input()
    print('-'*30)
    print('Aperte qualquer tecla para voltar...')
    input()
