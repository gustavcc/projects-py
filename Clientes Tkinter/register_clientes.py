import tkinter as tk
import sqlite3
from sqlite3 import Error
import pandas as pd

def Connection():
    path = "clientes.db"
    c = None
    try:
        c = sqlite3.connect(path)
    except Error as er:
        print("\nErro: ",er)
    finally:
        return c

#* função que define a criação do DB e da tabela
# def CriarTabela():
#     connection = Connection()
#     try:
#         vsql = '''CREATE TABLE Clientes(
#                         id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
#                         nome TEXT,
#                         sobrenome TEXT,
#                         telefone TEXT,
#                         email TEXT
# );'''
#         c = connection.cursor()
#         c.execute(vsql)
#         connection.commit()
#         print('\nTabela Criada\n')
#     except Error as er:
#         print("\nErro: ",er)
# CriarTabela()

def contem_letra(str):
    if 'a'<= str <= 'z' or 'A'<= str <= 'Z':
        return True
    return False

#* Funções
def cadastrar_cliente():
    connection = Connection()
    try:
        if not Entry_nome.get() or not Entry_sobrenome.get() or not Entry_email.get() or not Entry_telefone.get():
            erro = tk.Tk()
            erro.title('Erro')
            aviso1 = tk.Label(erro, text='Algum campo está errado!', foreground='red')
            aviso1.grid(row=0, column=0, padx=20, pady=20)

            aviso3 = tk.Label(erro, text='Não deixe campos vazios!', foreground='red')
            aviso3.grid(row=1, column=0, padx=20, pady=20)

            print('\nAlgum campo está errado!\n')
        elif len(Entry_telefone.get())!=10 or contem_letra(Entry_telefone.get()) or '@' not in Entry_email.get() or '.com' not in Entry_email.get():
            erro = tk.Tk()
            erro.title('Erro')
            aviso1 = tk.Label(erro, text='Algum campo está errado!', foreground='red')
            aviso1.grid(row=0, column=0, padx=20, pady=20)

            aviso2 = tk.Label(erro, text='Exemplo de telefone: 7711112222 (sem letras, 10 dígitose sem espaços) ', foreground='red')
            aviso2.grid(row=1, column=0, padx=20, pady=20)

            aviso3 = tk.Label(erro, text='Exemplo de email: exmplo@email.com (com @ e .com)', foreground='red')
            aviso3.grid(row=2, column=0, padx=20, pady=20)
        else:
            c = connection.cursor()
            c.execute(f"INSERT INTO Clientes (nome,sobrenome,telefone,email) VALUES('{Entry_nome.get()}','{Entry_sobrenome.get()}','{Entry_telefone.get()}','{Entry_email.get()}');")
            connection.commit()
            cadastrado = tk.Tk()
            cadastrado.title('Erro')
            aviso1 = tk.Label(cadastrado, text='Cliente cadastrado!', foreground='green')
            aviso1.grid(row=0, column=0, padx=20, pady=20)
            print("\nCliente castrado")
            
            #* resetar inputs 
            # Entry_nome.delete(0, "end")
            # Entry_sobrenome.delete(0, "end")
            # Entry_email.delete(0, "end")
            # Entry_telefone.delete(0, "end")
    except Error as er:
        print("\nErro: ",er)

def exportar_cliente():
    connection = Connection()
    try:
        c = connection.cursor()
        c.execute(f"SELECT * FROM clientes")
        clientes = c.fetchall()

        clientes = pd.DataFrame(clientes, columns=['id','nome','sobrenome','telefone','email'])
        clientes.to_excel('clientes.xlsx')
        connection.commit()

        #* resetar inputs 
        # Entry_nome.delete(0, "end")
        # Entry_sobrenome.delete(0, "end")
        # Entry_email.delete(0, "end")
        # Entry_telefone.delete(0, "end")
    except Error as er:
        print("\nErro: ",er)

#* Interface Gráfica
window = tk.Tk()

# titulo
window.title('Cadastro de Clientes')

# labels
Label_nome = tk.Label(window, text='Nome')
Label_nome.grid(row=0, column=0, padx=10, pady=10)

Label_sobrenome = tk.Label(window, text='Sebrenome')
Label_sobrenome.grid(row=1, column=0, padx=10, pady=10)

Label_email = tk.Label(window, text='Email')
Label_email.grid(row=2, column=0, padx=10, pady=10)

Label_telefone = tk.Label(window, text='Telefone')
Label_telefone.grid(row=3, column=0, padx=10, pady=10)

# entrys
Entry_nome = tk.Entry(window, text='Nome', width=30)
Entry_nome.get().capitalize().strip()
Entry_nome.grid(row=0, column=1, padx=10, pady=10)

Entry_sobrenome = tk.Entry(window, text='Sebrenome', width=30)
Entry_sobrenome.get().capitalize().strip()
Entry_sobrenome.grid(row=1, column=1, padx=10, pady=10)

Entry_email = tk.Entry(window, text='Email', width=30)
Entry_email.grid(row=2, column=1, padx=10, pady=10)

Entry_telefone = tk.Entry(window, text='Telefone', width=30)
Entry_telefone.grid(row=3, column=1, padx=10, pady=10)

# buttons
Entry_cadastrar = tk.Button(window, text='Cadastrar Cliente', command = cadastrar_cliente)
Entry_cadastrar.grid(row=4, column=0, padx=10, pady=10, columnspan=2, ipadx=80)

Entry_exportar = tk.Button(window, text='Exportar Cliente Excel', command = exportar_cliente)
Entry_exportar.grid(row=5, column=0, padx=10, pady=10, columnspan=2, ipadx=80)

window.mainloop()