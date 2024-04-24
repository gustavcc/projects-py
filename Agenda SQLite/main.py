import os
import sqlite3
from sqlite3 import Error
from colorama import Fore
from funcoes import *

# ----- conexão DB -----
def ConnectionDB():
    path = "Agenda.db"
    c = None
    try:
        c=sqlite3.connect(path)
    except Error as er:
        print(Fore.RED+'Erro: ',er+Fore.RESET)
    return c

vConnection=ConnectionDB()

# ---- main -----
while True:
    
    option = Menu()
    
    if option=='1':
        Cadastro(vConnection)
    elif option=='2':
        Editar(vConnection)
    elif option=='3':
        Excluir(vConnection)
    elif option=='4':
        Mostrar(vConnection)
    elif option=='0':
        os.system('cls')
        print(f"{'-'*30}\n")
        print('Fechando agenda...')
        sleep(1)
        print(Fore.RED+'Fim do programa.'+Fore.RESET)
        print(f"\n{'-'*30}")
        break
    else:
        print(Fore.RED,f'\nInsira uma opção válida!\n',Fore.RESET)
        sleep(2)