class String:
    def __init__(self):
        self.str = ""
        
    def getString(self):
        self.str = input('str: ')
    
    def printString(self):
        print(self.str.upper())

inputStr = String()
inputStr.getString()
inputStr.printString()