from tkinter import *

root = Tk()
root.title('Calculadora')
root.iconbitmap('img/icon_calc.jpg')
root.geometry(f"{1100}x{580}")
root.configure(bg='purple')
root.configure()

class Calc:
    
    def __init__(self, root):
        
        self.l1 = Label(root, text='Primeiro app', bg='purple', font=('JetBrains Mono', 12))
        self.l1.pack(pady=10)
        
        self.text_primeiro = Label(root, text='Primeiro Number', fg='#000', bg='purple', font=('JetBrains Mono', 12))
        self.text_primeiro.pack(pady=10)

        self.primeiro = Entry(root, width=20)
        self.primeiro.pack(pady=10)
        
        self.soma = Label(root, text='+', fg='#000', bg='purple', font=('JetBrains Mono', 12))
        self.soma.pack(pady=10)

        self.text_segundo = Label(root, text='Segundo Número', fg='#000', bg='purple', font=('JetBrains Mono', 12))
        self.text_segundo.pack(pady=10)

        self.segundo = Entry(root, width=20)
        self.segundo.pack(pady=10)
        
        self.text_result = Label(root, text='=', fg='#000', bg='purple', font=('JetBrains Mono', 12))
        self.text_result.pack(pady=10)
        
        self.result = StringVar()
        self.label_result = Label(root, textvariable=self.result, fg='#000', bg='purple', font=('JetBrains Mono', 12))
        self.label_result.pack(pady=10)
        self.result.set(' ')
        
        self.calc = Button(root, text='Calcular soma', command = self.calcularSoma)
        self.calc.pack(pady=20)
    
    def calcularSoma(self):
        first = int(self.primeiro.get())
        second = int(self.segundo.get())
        sun = str(first+second)
        self.result.set(sun)

app = Calc(root)

root.mainloop()