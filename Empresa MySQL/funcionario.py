from bd import EmpresaBD
from os import system 

class Funcionario():
    
    banco = EmpresaBD()
    
    linha = '-'*40
    
    __slots__ = ['__mat','__nome','__salario']
    
    def __init__ (self,mat, nome, salario):
        self.setMat(mat)
        self.setNome(nome)
        self.setSalario(salario)
    
    def getMat(self):
        return self.__mat
    def getNome(self):
        return self.__nome
    def getSalario(self):
        return self.__salario
    
    def setMat(self, novaMat):
        while True:
            try:
                novaMat = int(novaMat)
                if self.banco.existeFuncBD(int(novaMat)):
                    system('cls')
                    self.banco.listarFuncBD()
                    print(self.linha)
                    novaMat = int(input('\nMatricula existente.\nInsira uma nova\n: ').strip())
                else:
                    break
            except ValueError: 
                print(self.linha)
                novaMat = input('\nMatricula inválida.\nInsira uma nova\n: ').strip()
                continue
        self.__mat = int(novaMat)
        
    def setNome(self, novoNome):
            while True:
                if novoNome=='' or novoNome==' ':
                    print(self.linha)
                    novoNome = input('\nNome inválido.\nInsira um novo\n: ').strip()
                else:
                    break
            self.__nome = novoNome
    
    def setSalario(self, novoSalario):
            while True:
                try:
                    novoSalario==float(novoSalario)
                    if novoSalario=='' or novoSalario==' ' or float(novoSalario)<0 or float(novoSalario)==0:
                        print(self.linha)
                        novoSalario = float(input('\nSalario inválido.\nInsira um novo\n: ').strip())
                    else:
                        break
                except ValueError: 
                    print(self.linha)
                    novoSalario = input('\nSalario inválido.\nInsira um novo\n: ').strip()
                    continue
            self.__salario = novoSalario
        
    def setMatSemVerificar(self, novaMat):
        
        self.__mat = int(novaMat)