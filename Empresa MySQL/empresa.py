from bd import EmpresaBD
from funcionario import Funcionario
from os import system

class Empresa():
    
    linha = '-'*40
    
    menu = f'''
{linha}
{'Empresa Cardoso':^40}
{linha}
[1] - Cadastrar funcionário.
[2] - Editar funcionário.
[3] - Excluir funcionário.
[4] - Ordenar funcionários.
[5] - Pesquisar funcionário.
[6] - Filtrar funcionários.
[0] - Sair
{linha}'''

    # def __init__(self):
    #     self.bd = EmpresaBD()
    #     self.funcionario = Funcionario()

    def cadastrarFun(self):
        pass
    
    def editarFun(self):
        pass
    
    def excluirFun(self):
        pass
    
    def ordenarFun(self):
        pass
    
    def pesquisarFun(self):
        pass
    
    def filtrarFun(self):
        pass
    
    def iniciar(self):
        while True:
            system('cls')
            print(self.menu)
            op = input('\nSelecione uma opção\n:')
            match op:
                case '1':
                    self.cadastrarFun()
                case '2':
                    self.editarFun()
                case '3':
                    self.excluirFun()
                case '4':
                    self.ordenarFun()
                case '5':
                    self.pesquisarFun()
                case '6':
                    self.filtrarFun()
                case '0':
                    system('cls')
                    print(self.linha)
                    print("\nFim do programa!\n")
                    print(self.linha)
                    break
                case _:
                    print(self.linha)
                    print('\nInsira uma opção válida')
                    print('Aparte qualquer tecla para continuar...\n')
                    print(self.linha)
                    input()