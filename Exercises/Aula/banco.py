import sqlite3

class DBConnection():
    
    def __init__(self):
        self.connection = None
        
    def conn(self):
        try:
            self.connection = sqlite3.connect('biblioteca.sqlite')
            self.cursor = self.connection.cursor()
        except sqlite3.Error as e:
            print('Erro: ',e)
            print('Aperte qualquer tecla pra continuar...')
            input()
    
    def disconnect(self):
        if self.connection:
            self.connection.close()
        else:
            print('Erro ao fechar banco')       
    
    def createTable(self):
        self.conn()
        try:
            sql = '''CREATE TABLE biblioteca (
                ISBN TEXT PRiMARY KEY,
                titulo TEXT,
                autor TEXT,
                ano INTEGER
                )'''
            self.cursor.execute(sql)
        except sqlite3.Error as e:
            print('Erro na criação de tabela: ',)
        finally:
            self.disconnect()
    
    def cadastrarLivroDB(self, titulo, autor, ano, ISBN):
        self.conn()
        try:
            sql = '''INSERT INTO biblioteca 
            (titulo, autor, ano, ISBN) 
            VALUES (?,?,?,?)'''
            self.cursor.execute(sql,(titulo, autor, ano, ISBN))
            self.connection.commit()
            print('Livro cadastrado com sucesso!')
        except sqlite3.Error as e:
            print('Erro no cadastro: ',e)
        finally:
            self.disconnect()        
    
    def deletarLivroDB(self, ISBN):
        self.conn()
        try:
            if self.selectLivroDB(ISBN):
                sql = '''DELETE FROM biblioteca 
                WHERE ISBN = ?;'''
                self.cursor.execute(sql,(ISBN,))
                self.connection.commit()
                print('Livro deletado com sucesso!')
            else:
                print('Esse livro não está no banco')
        except sqlite3.Error as e:
            print('Erro na exclusão: ',e)
        finally:
            self.disconnect()
            
    def vizualizarLivrosDB(self):
        self.conn()
        try:
            sql = '''SELECT * FROM biblioteca;'''
            self.cursor.execute(sql)
            livros = self.cursor.fetchall()
            for livro in livros:
                print('ISBN: ', livro[0], '\nAutor: ',livros[1])
        except sqlite3.Error as e:
            print('Erro na vizualização: ',e)
        finally:
            self.disconnect()
    def selectLivroDB(self, ISBN):
        try:
            sql = '''SELECT ISBN FROM biblioteca 
            WHERE ISBN = ?'''
            self.cursor.execute(sql,(ISBN,))
            livro = self.cursor.fetchone()
            exists = False
            if livro:
                exists = True
                print(livro)
            return exists
        except sqlite3.Error as e:
            print('Erro na busca do ISBN: ',e)
            
db = DBConnection()

# 12121344131-1
# print('tem') if db.selectLivroDB('12121344131-1') else print('n tem')
# db.cadastrarLivroDB('ALS', 'Paulo', 2024, '12121344131-1')
# db.deletarLivroDB('12121344131-1')
db.vizualizarLivrosDB()