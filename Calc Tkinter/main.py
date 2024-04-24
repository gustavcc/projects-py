import tkinter as tk

def calcular_soma():
    fisrt = int(primeiro.get())
    second = int(segundo.get())
    soma = str(fisrt + second)
    result.set(soma)

calc = tk.Tk()
calc.title('Calculadora')
calc.configure(background='#000', padx=50, pady=50)

text1 = tk.Label(calc, text='Primeiro Número',bg='#000', fg='#fff')
text1.grid(row=0, column=0, padx=10, pady=10)

primeiro = tk.Entry(calc, width=20)
primeiro.grid(row=0, column=1, padx=10, pady=10)


text2 = tk.Label(calc, text='Segundo Número',bg='#000', fg='#fff')
text2.grid(row=2, column=0, padx=10, pady=10)

segundo = tk.Entry(calc, width=20)
segundo.grid(row=2, column=1, padx=10, pady=10)

soma = tk.Label(text='+',bg='#000', fg='#fff')
soma.grid(row=1, column=0, columnspan=2, ipadx=80)

calcular = tk.Button(calc, text='Calcular soma', command = calcular_soma)
calcular.grid(row=4, column=0, padx=10, pady=10, columnspan=2, ipadx=80)

text3 = tk.Label(calc, text='Resultado aqui:',bg='#000', fg='#fff')
text3.grid(row=3, column=0, padx=10, pady=10)

result = tk.StringVar()
text4 = tk.Label(calc, textvariable= result ,bg='#000', fg='#ff0000')
text4.grid(row=3, column=1, padx=10, pady=10)
result.set(' ')

calc.mainloop()