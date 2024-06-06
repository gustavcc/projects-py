import tkinter as tk

class Calculadora():
    
    def __init__(self):
        self.calc = tk.Tk()
        self.calc.title('Calculadora')
        self.calc.configure(background='#000', padx=50, pady=50)

        self.text1 = tk.Label(self.calc, text='Primeiro Número',bg='#000', fg='#fff')
        self.text1.grid(row=0, column=0, padx=10, pady=10)

        self.primeiro = tk.Entry(self.calc, width=20)
        self.primeiro.grid(row=0, column=1, padx=10, pady=10)


        self.text2 = tk.Label(self.calc, text='Segundo Número',bg='#000', fg='#fff')
        self.text2.grid(row=2, column=0, padx=10, pady=10)

        self.segundo = tk.Entry(self.calc, width=20)
        self.segundo.grid(row=2, column=1, padx=10, pady=10)

        self.soma = tk.Label(text='+',bg='#000', fg='#fff')
        self.soma.grid(row=1, column=0, columnspan=2, ipadx=80)

        self.calcular = tk.Button(self.calc, text='Calcular soma', command = self.calcular_soma(self.primeiro, self.segundo))
        self.calcular.grid(row=4, column=0, padx=10, pady=10, columnspan=2, ipadx=80)

        self.text3 = tk.Label(self.calc, text='Resultado aqui:',bg='#000', fg='#fff')
        self.text3.grid(row=3, column=0, padx=10, pady=10)

        self.result = tk.StringVar()
        self.text4 = tk.Label(self.calc, textvariable = self.result ,bg='#000', fg='#ff0000')
        self.text4.grid(row=3, column=1, padx=10, pady=10)
        self.result.set(' ')

    def calcular_soma(self, primeiro,segundo):
        print(primeiro.get(), segundo.get())
        # self.fisrt = int(primeiro.get())
        # self.second = int(segundo.get())
        # self.soma = str(self.fisrt + self.second)
        # self.result.set(self.soma)

calculadora = Calculadora()

calculadora.mainloop()