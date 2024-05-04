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
                    system('cls')
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
        if self.banco.bancoVazio():
            system('cls')
            print('\nO não existe funcionarios para editar!\n')
            print(self.linha)
            print('\nAperte qualquer tecla pra continuar...')
            input()
            self.iniciar()
        else:
            while True:
                system('cls')
                print(f'''
{self.linha}
{'Editar':^40}
{self.linha}''')
                
                op = input('''
[1] - Editar
[0] - Sair
: ''').strip()    
                match op:
                    case '1':
                        system('cls')
                        self.banco.listarFuncBD()
                        mat_op = input('\nInsira a mat do funcionario que deseja editar\n: ').strip()
                        mat_op = self.validarMat(mat_op)
                        if self.banco.existeFuncBD(mat_op):
                            while True:
                                system('cls')
                                op_edit = input(f'''Editar...
[1] - Matricula
[2] - Nome
[3] - Salario
:''')
                                match op_edit:
                                    case '1':
                                        mat = input('\nInsira a nova matricula\n: ').capitalize().strip()
                                        mat = self.validarMatEdit(mat,mat_op)
                                        print('ok')
                                        input()
                                        funcionario = self.banco.buscaFuncAtributo(mat_op)
                                        system('cls')
                                        self.banco.editarFuncBD(mat, funcionario[1], funcionario[2], mat_op)
                                        break
                                    case '2':
                                        nome = input('\nInsira o novo nome\n: ').capitalize().strip()
                                        self.fun = 
                                        self.fun.setNome(nome)
                                        print('ok')
                                        input()
                                        funcionario = self.banco.buscaFuncAtributo(mat_op)
                                        system('cls')
                                        self.banco.editarFuncBD(mat_op, funcionario[1], funcionario[2], mat_op)
                                    case '3':
                                        pass
                                    case _:
                                        print('\nInsira um valor valido!\n')
                                        print(self.linha)
                                        print('\nAperte qualquer tecla pra continuar...')
                                        input()
                            #     nome = input('\nInsira o novo nome\n: ').capitalize().strip()
                            #     salario = input('\nInsira o novo salario\n: ').capitalize().strip()
                            #     funcionario = self.banco.buscaFuncAtributo(mat_op)
                                
                                
                            # system('cls')
                            
                            # self.banco.editarFuncBD(self.fun.getMat(), self.fun.getNome(), self.fun.getSalario())
                        else:
                            print('\nEsse funcionário não existe!\n')
                            print(self.linha)
                            print('\nAperte qualquer tecla pra continuar...')
                            input()
                    case '0':
                        print(self.linha)
                        break
                    case _:
                        print('\nInsria uma opção válida!\n')
                        print(self.linha)
                        print('\nAperte qualquer tecla pra continuar...')
                        input()
    
    def excluirFun(self):
        pass
    
    def ordenarFun(self):
        pass
    
    def pesquisarFun(self):
        pass
    
    def filtrarFun(self):
        pass
    
    def validarMat(self, mat):
        while True:
            try:
                mat = int(mat)
                break
            except ValueError: 
                print(self.linha)
                mat = input('\nMatricula inválida.\nInsira uma nova\n: ').strip()
                continue
        return mat
    
    def validarMatEdit(self, mat,mat_edit):
        while True:
            try:
                mat = int(mat)
                if self.banco.existeFuncBD(int(mat)) and mat!=mat_edit:
                    system('cls')
                    self.banco.listarFuncBD()
                    print(self.linha)
                    mat = int(input('\nMatricula existente.\nInsira uma nova\n: ').strip())
                else:
                    break
            except ValueError: 
                print(self.linha)
                mat = input('\nMatricula inválida.\nInsira uma nova\n: ').strip()
                continue
        return mat

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