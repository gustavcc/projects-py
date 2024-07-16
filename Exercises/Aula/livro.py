import sqlite3

class Livro:
    
    __slots__ = ['__titulo', '__ano', '__autor', '__ISBN']
    
    def __init__(self, titulo, autor, ano, ISBN):
        self.set_titulo(titulo)
        self.set_ano(ano)
        self.set_autor(autor)
        self.set_ISBN(ISBN)
        
    def get_titulo(self):
        return self.__titulo
    def get_ano(self):
        return self.__ano
    def get_autor(self):
        return self.__autor
    def get_ISBN(self):
        return self.__ISBN
        
    def set_titulo(self, titulo):
        try:
            if titulo == '' or not titulo:
                print('Titulo indefinido!')
        except sqlite3.Error as er:
            print('Erro: ',er)
        self.__titulo = titulo
        
    def set_autor(self, autor):
        try:
            if autor == '' or not autor:
                print('Autor indefinido!')
        except sqlite3.Error as er:
            print('Erro: ',er)
        self.__autor = autor
        
    def set_ano(self, ano):
        try:
            ano = int(ano)
            if ano == '' or not ano:
                print('Ano indefinido!')
        except sqlite3.Error as er:
            print('Erro: ',er)
        self.__ano = ano
        
    def set_ISBN(self, ISBN):
        try:
            if ISBN == '' or not ISBN:
                print('ISBN indefinido!')
        except sqlite3.Error as er:
            print('Erro: ',er)
        self.__ISBN = ISBN