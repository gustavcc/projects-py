from db import ConnEmpresa

class Funcionario():
    
    __slots__ = ['__mat','__nome','__salario']
    
    def __init__ (self,mat, nome, salario):
        self.setMat(mat)
        self.setNome(nome)
        self.setSalario(salario)
        self.bd = ConnEmpresa()
    
    def getMat(self):
        return self.__mat
    def getNome(self):
        return self.__nome
    def getSalario(self):
        return self.__salario
    
    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    def setMat(self, novaMat):
        print(novaMat)
        while True:
            try:
                novaMat
                if novaMat == int(novaMat): 
                    if self.bd.existeFuncBD(novaMat):
                        novaMat = int(input('\nMatricula existente.\nInsira uma inexistente\n: '))
                    else: break
            except: 
                print('Insira uma matricula válida')
        print('usuario cadastrado')

func = Funcionario(1,'Deri',3000)