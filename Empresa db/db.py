import mysql.connector as mysql
from colorama import Fore
opa = 1

class ConnEmpresa():
    def __init__(self):
        self.connection = None
    
    def connect(self):
        try:
            self.connection = mysql.connect(
                host='localhost',
                username='root',
                password='admin',
                database='empresa')
            self.cursor = self.connection.cursor()
        except mysql.Error as e:
            print(Fore.RED,'Erro na conexão do banco: ',e,Fore.RESET)
    
    def disconnect(self):
        if self.connection:
            self.connection.close()
        else:
            print(Fore.RED+'Não há conexão estabelecida!'+Fore.RESET)
    
    def criarTabelaBD(self):
        self.connect()
        try: 
            querry = f'''CREATE TABLE IF NOT EXISTS Funcionarios (
                matricula INT PRIMARY KEY UNIQUE,
                nome VARCHAR(45) NOT NULL,
                salario REAL NOT NULL
            );'''
            self.cursor.execute(querry)
        except mysql.Error as e:
            print(Fore.RED,'Erro ao criar tabela: ',e,Fore.RESET)
        finally:
            self.disconnect()
    
    def inserirFuncBD(self,mat,nome,salario):
        self.connect()
        try:
            querry = '''INSERT INTO Funcionarios (matricula, nome, salario)
                            VALUES (%s,%s,%s);'''
            self.cursor.execute(querry,(mat,nome,salario))
            self.connection.commit()
            print(Fore.GREEN+'\nFuncionario inserido!\n'+Fore.RESET)
        except mysql.Error as e:
            print(Fore.RED,'Erro ao inserir registro: ',e,Fore.RESET)
        finally:
            self.disconnect()
    
    def editarFuncBD(self,mat,nome,salario):
        self.connect()
        try:
            querry = '''UPDATE Funcionarios SET nome=%s,salario=%s WHERE matricula=%s;'''
            self.cursor.execute(querry,(nome,salario, mat))
            self.connection.commit()
            print(Fore.GREEN+'\nFuncionario editado!\n'+Fore.RESET)
        except mysql.Error as e:
            print(Fore.RED,'Erro ao editar registro: ',e,Fore.RESET)
        finally:
            self.disconnect()
    
    def excluirFuncBD(self,mat):
        self.connect()
        try:
            querry = '''DELETE FROM Funcionarios WHERE matricula=%s;'''
            self.cursor.execute(querry,(mat,))
            self.connection.commit()
            print(Fore.GREEN+'\nFuncionario excluido!\n'+Fore.RESET)
        except mysql.Error as e:
            print(Fore.RED,'Erro ao excluir registro: ',e,Fore.RESET)
        finally:
            self.disconnect()
    
    def mostrarFuncBD(self):
        self.connect()
        try:
            querry = '''SELECT * FROM Funcionarios;'''
            self.cursor.execute(querry)
            funcionarios = self.cursor.fetchall()
            for func in funcionarios:
                print(func)
        except mysql.Error as e:
            print(Fore.RED,'Erro ao mostrar registros: ',e,Fore.RESET)
        finally:
            self.disconnect()
    
    def ordenarFuncBD(self,option):
        self.connect()
        try:
            if option==1:
                querry = '''SELECT * FROM Funcionarios ORDER BY matricula;'''
                self.cursor.execute(querry)
            elif option==2:
                querry = '''SELECT * FROM Funcionarios ORDER BY nome;'''
                self.cursor.execute(querry)
            funcOrdenado = self.cursor.fetchall()
            for func in funcOrdenado:
                print(func)
        except mysql.Error as e:
            print(Fore.RED,'Erro ao ordenar registros: ',e,Fore.RESET)
        finally:
            self.disconnect()
    
    def pesquisarFuncBD(self,option,mat=None,nome=None):
        # se for nome, passsar mat como None la em funcionarios
        self.connect()
        try:
            if option==1:
                querry = '''SELECT * FROM Funcionarios WHERE matricula=%s;'''
                self.cursor.execute(querry,(mat,))
            elif option==2:
                querry = '''SELECT * FROM Funcionarios WHERE nome=%s;'''
                self.cursor.execute(querry,(nome,))
            else:
                querry = '''SELECT * FROM Funcionarios;'''
                self.cursor.execute(querry)
            funcOrdenado = self.cursor.fetchall()
            for func in funcOrdenado:
                print(func)
        except mysql.Error as e:
            print(Fore.RED,'Erro ao ordenar registros: ',e,Fore.RESET)
        finally:
            self.disconnect()
    
    def filtrarFuncBD(self,option=None):
        self.connect()
        try:
            if option==1:
                querry = '''SELECT * FROM Funcionarios WHERE salario>1000;'''
                self.cursor.execute(querry)
            elif option==2:
                querry = '''SELECT * FROM Funcionarios WHERE salario<1000;'''
                self.cursor.execute(querry)
            elif option==3:
                querry = '''SELECT * FROM Funcionarios WHERE salario=1000;'''
                self.cursor.execute(querry)
            else:
                querry = '''SELECT * FROM Funcionarios;'''
                self.cursor.execute(querry)
            funcFiltrado = self.cursor.fetchall()
            for func in funcFiltrado:
                print(func)
        except mysql.Error as e:
            print(Fore.RED,'Erro ao ordenar registros: ',e,Fore.RESET)
        finally:
            self.disconnect()
    
    def listarFuncBD(self,mat=None):
        self.connect()
        try:
            if mat:
                querry = '''SELECT * FROM Funcionarios WHERE matricula=%s;'''
                self.cursor.execute(querry,(mat,))
            else:
                querry = '''SELECT * FROM Funcionarios;'''
                self.cursor.execute(querry)
            funcLista = self.cursor.fetchall()
            for func in funcLista:
                print(func)
        except mysql.Error as e:
            print(Fore.RED,'Erro ao listar funcionarios: ',e,Fore.RESET)
        finally:
            self.disconnect()
    
    def existeFuncBD(self,mat):
        self.connect()
        try:
            querry = '''SELECT * FROM Funcionarios;'''
            self.cursor.execute(querry)
            funcionarios = self.cursor.fetchall()
            existe = False
            for func in funcionarios:
                # return mat==func[0] or False
                if mat == func[0]:
                    existe = True
                    break
            return existe or False 
        except mysql.Error as e:
            print(Fore.RED,'Não existe funcionários: ',e,Fore.RESET)
        finally:
            self.disconnect()

bd = ConnEmpresa()
if bd.existeFuncBD(0):
    print('existe')