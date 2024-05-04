from bd import EmpresaBD
from funcionario import Funcionario
from os import system

class Empresa():
    banco = EmpresaBD()
    
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

    def cadastrarFun(self):
        while True:
            system('cls')
            print(f'''
{self.linha}
{'Cadastro':^40}
{self.linha}''')
            
            op = input('''
[1] - Cadastrar
[0] - Sair
: ''').strip()    
            match op:
                case '1':
                    system('cls')
                    mat = input('\nInsira a matricula\n: ').capitalize().strip()
                    nome = input('\nInsira o nome\n: ').capitalize().strip()
                    salario = input('\nInsira o salario\n: ').capitalize().strip()
                    self.fun = Funcionario(mat, nome, salario)
                    self.banco.cadastrarFuncBD(self.fun.getMat(), self.fun.getNome(), self.fun.getSalario())
                case '0':
                    print(self.linha)
                    break
                case _:
                    print('\nInsria uma opção válida!\n')
                    print(self.linha)
                    print('\nAperte qualquer tecla pra continuar...')
                    input()
    
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
    
    def validarMat(self, mat):
        try:
            mat = int(mat)
            return True
        except ValueError: 
            return False
    
    def iniciar(self):
        while True:
            system('cls')
            print(self.menu)
            op = input('\nSelecione uma opção\n: ')
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