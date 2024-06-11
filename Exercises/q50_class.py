class American(object):
    @staticmethod # pode instanciar diretamente pela class
    def printNationality():
        print('America')

american = American()
american.printNationality()
American().printNationality()