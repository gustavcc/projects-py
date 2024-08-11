from sqlite3 import connect
from os import path


class ConexaoBD:

    def conecta(self):
        try:
            pasta = path.dirname(
                path.realpath(__file__))  # pasta do arquivo
            self.conexao = connect(f'{pasta}/database.sqlite3')
            self.cursor = self.conexao.cursor()
        except:
            print("Erro na criação do Banco de Dados.")

    def fecha_conexao(self):
        try:
            self.conexao.close()
        except:
            print("Conexão Inexistente!")

    def gera_tabela_usuarios(self):
        self.conecta()
        query = '''CREATE TABLE IF NOT EXISTS usuarios (
            username VARCHAR(30) PRIMARY KEY,
            password VARCHAR(100) NOT NULL)'''
        try:
            self.cursor.execute(query)
        except:
            print("Erro na criação da Tabela Usuários.")
        finally:
            self.fecha_conexao()

    def add_usuario(self, login, senha):
        self.conecta()
        query = "INSERT INTO usuarios VALUES (?, ?)"
        try:
            self.cursor.execute(query, (login, senha))
            self.conexao.commit()
        except:
            print("Erro na criação da Tabela Usuários.")
        finally:
            self.fecha_conexao()
    
    def existe_usuarioDB(self, username):
        self.conecta()
        query = "SELECT * FROM usuarios WHERE username = ?"
        try:
            self.cursor.execute(query, (username,))
            self.usuario = self.cursor.fetchone()
            if (self.usuario):
                return self.usuario
            return True
        except:
            print("Usuário não encontrado!")
            return True
        finally:
            self.fecha_conexao()

# Principal
# if __name__ == '__main__':
#     conn = ConexaoBD()
    # conn.gera_tabela_usuarios()
    # conn.add_usuario("admin", "Senha@123")
