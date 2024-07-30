import tkinter as tk

class Aplicativo(tk.Tk):
    def __init__(self):
        super().__init__()
        self.cor = "#10AAB0"
        self.janelaPrincipal()
    
    def janelaPrincipal(self):
        self.geometry("500x600")
        self.title("Aplicativo")
        self.configure(bg=self.cor)
        self.resizable(False,False)
        
        def somar():
            if entrada1.get().isdigit() and entrada2.get().isdigit():
                self.resultado.set(str(int(entrada1.get()) + int(entrada2.get())))
            else:
                self.resultado.set('Valor inválido!')
        
         # widgets
        labelSoma = tk.Label(self, text="Soma", bg="black", fg="#FFF", font="Arial 16")
        labelSoma.pack(fill="x", ipady="30")
        
        label1 = tk.Label(self, text="Número 1", bg=self.cor, fg="black", font="Arial 16")
        label1.pack(fill="x", pady="2")
    
        entrada1 = tk.Entry(self, font="Arial 14")
        entrada1.pack(pady=10)
        
        label2 = tk.Label(self, text="Número 2", bg=self.cor, fg="black", font="Arial 16")
        label2.pack(fill="x", pady="2")
    
        entrada2 = tk.Entry(self, font="Arial 14")
        entrada2.pack(pady=10)
        
        label3 = tk.Label(self, text="Resultado:", bg=self.cor, fg="black", font="Arial 16")
        label3.pack(fill="x", pady="2")
        
        self.resultado = tk.StringVar()
        self.resultado.set(' ')
        label4 = tk.Label(self, textvariable=self.resultado, bg=self.cor, fg="black", font="Arial 16")
        label4.pack(fill="x", pady="2")
        
        calc = tk.Button(self, text="Calcular", bg='red', font="16", command=somar)
        calc.pack(pady=37, ipadx=10)


# Principal
if __name__ == '__main__':
    app = Aplicativo()
    app.mainloop()
