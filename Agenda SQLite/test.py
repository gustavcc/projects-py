from funcoes import BuscarDB, CommitDB
import sqlite3
from sqlite3 import Error
from colorama import Fore
from time import sleep

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

def ConnectionDB():
    path = "Agenda.db"
    c = None
    try:
        c=sqlite3.connect(path)
    except Error as er:
        print(Fore.RED+'Erro: ',er+Fore.RESET)
    return c

vConnection=ConnectionDB()

nome = 'Stefanny'
email = "stefanny@gmail.com"
id = 7
vSQL = f"UPDATE Contatos SET nome='{nome}', email='{email}' WHERE id_contato='{id}'"

CommitDB(vConnection,vSQL)