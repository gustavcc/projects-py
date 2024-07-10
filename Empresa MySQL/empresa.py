from bdMySql import EmpresaBD
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
                        matEdit = input('\nInsira a matricula para editar\n: ').strip().capitalize()
                        matEdit = self.validarMat(matEdit)
                        funcionario = self.banco.dadosFuncEspecifico(matEdit)
                        if self.banco.existeFuncBD(matEdit):
                            system('cls')
                            novaMat = input('\nInsira a nova matricula ou vazio para manter\n: ').capitalize().strip()
                            novoNome = input('\nInsira o novo nome ou vazio para manter\n: ').capitalize().strip()
                            novoSalario = input('\nInsira o novo salário ou vazio para manter\n: ').capitalize().strip()
                            if novaMat=='':
                                novaMat=funcionario[0]
                                funcionario[0]
                            if novoNome=='':
                                novoNome=funcionario[1]
                            if novoSalario=='':
                                novoSalario=funcionario[2]
                            self.fun = Funcionario(novaMat,novoNome,novoSalario,matEdit)
                            self.linha
                            self.banco.editarFuncBD(self.fun.getMat(), self.fun.getNome(), self.fun.getSalario(),matEdit)
                        else:
                            print('\nEsse funcionário não existe!\n')
                            print(self.linha)
                            print('\nAperte qualquer tecla pra continuar...')
                            input()
                            continue
                    case '0':
                        print(self.linha)
                        break
                    case _:
                        print('\nInsria uma opção válida!\n')
                        print(self.linha)
                        print('\nAperte qualquer tecla pra continuar...')
                        input()
    
    def excluirFun(self):
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
{'Excluir':^40}
{self.linha}''')
                
                op = input('''
[1] - Excluir
[0] - Sair
: ''').strip()    
                match op:
                    case '1':
                        system('cls')
                        self.banco.listarFuncBD()
                        matDel = input('\nInsira a matricula para excluir\n: ').strip().capitalize()
                        matDel = self.validarMat(matDel)
                        if self.banco.existeFuncBD(matDel):
                            while True:
                                system('cls')
                                resp = input('\nDeseja realmente excluir esse funcionario?\n:').strip()
                                if resp in ['s','S','sim','Sim']:
                                    self.linha
                                    self.banco.excluirFuncBD(matDel)
                                    break
                                elif resp in ['n','N','nao','Nao','não','Não']:
                                    break
                                else:
                                    continue
                        else:
                            print('\nEsse funcionário não existe!\n')
                            print(self.linha)
                            print('\nAperte qualquer tecla pra continuar...')
                            input()
                            continue
                    case '0':
                        break
                    case _:
                        print('\nInsria uma opção válida!\n')
                        print(self.linha)
                        print('\nAperte qualquer tecla pra continuar...')
                        input()
    
    def ordenarFun(self):
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
{'Ordenar':^40}
{self.linha}''')
                
                op = input('''
[1] - Ordenar por matricula
[2] - Ordenar por nome
[0] - Sair
: ''').strip()    
                match op:
                    case '1':
                        system('cls')
                        self.banco.ordenarFuncBD(int(op))
                    case '2':
                        system('cls')
                        self.banco.ordenarFuncBD(int(op))
                    case '0':
                        break
                    case _:
                        print('\nInsria uma opção válida!\n')
                        print(self.linha)
                        print('\nAperte qualquer tecla pra continuar...')
                        input()
    
    def pesquisarFun(self):
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
{'Pesquisar':^40}
{self.linha}''')
                
                op = input('''
[1] - Pesquisar por matricula
[2] - Pesquisar por nome
[0] - Sair
: ''').strip()    
                match op:
                    case '1':
                        system('cls')
                        # self.banco.listarFuncBD()
                        matPesc = input('\nInsira a matricula para pesquisar\n: ').strip().capitalize()
                        matPesc = self.validarMat(matPesc)
                        if self.banco.existeFuncBD(matPesc):
                            system('cls')
                            self.banco.pesquisarFuncBD(int(op),matPesc)
                        else:
                            print('\nEsse funcionário não existe!\n')
                            print(self.linha)
                            print('\nAperte qualquer tecla pra continuar...')
                            input()
                            continue
                    case '2':
                        system('cls')
                        # self.banco.listarFuncBD()
                        nome = input('\nInsira o nome para pesquisar\n: ').strip().capitalize()
                        if self.banco.existeFuncNomeBD(nome):
                            system('cls')
                            self.banco.pesquisarFuncBD(int(op),nome)
                        else:
                            print('\nEsse funcionário não existe!\n')
                            print(self.linha)
                            print('\nAperte qualquer tecla pra continuar...')
                            input()
                            continue
                    case '0':
                        break
                    case _:
                        print('\nInsria uma opção válida!\n')
                        print(self.linha)
                        print('\nAperte qualquer tecla pra continuar...')
                        input()
    
    def filtrarFun(self):
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
{'Filtrar Salarios':^40}
{self.linha}''')
                
                op = input('''
[1] - Filtrar acima de 1000
[2] - Filtrar abaixo de 1000
[3] - Filtrar iguais a 1000
[0] - Sair
: ''').strip()    
                match op:
                    case '1':
                        system('cls')
                        self.banco.filtrarFuncBD(int(op))
                    case '2':
                        system('cls')
                        self.banco.filtrarFuncBD(int(op))
                    case '3':
                        system('cls')
                        self.banco.filtrarFuncBD(int(op))
                    case '0':
                        break
                    case _:
                        print('\nInsria uma opção válida!\n')
                        print(self.linha)
                        print('\nAperte qualquer tecla pra continuar...')
                        input()
    
    def validarMat(self, mat):
        while True:
            try:
                mat = int(mat)
                break
            except ValueError: 
                print(self.linha)
                mat = input('\nMatricula inválida.\nInsira uma nova\n: ').strip()
                continue
        return int(mat)

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