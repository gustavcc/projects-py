import tkinter as tk

class Aplicativo(tk.Tk):
    def __init__(self):
        super().__init__()
        self.cor = "#aaa"
        self.janelaPrincipal()
    
    def janelaPrincipal(self):
        self.geometry("500x600")
        self.title("Aplicativo")
        self.configure(bg=self.cor)
        self.resizable(False,False)
        
        
        def verificar():
            if entradaNumber.get().isdigit():
                if (int(entradaNumber.get())%2==0):
                    self.saida.set('O número digitado é par!')
                else:
                     self.saida.set('O número digitado é ímpar!')
            else:
                self.saida.set('Valor inválido! Apenas números inteiros!')
        
         # widgets
        labelTexto = tk.Label(self, text="Odd or Even", bg=self.cor, fg="#FFF", font="Arial 18")
        labelTexto.pack(fill="x", ipady="30")
        
        
        entradaNumber = tk.Entry(self, font="Arial 14")
        entradaNumber.pack(pady=10)
        
        self.saida = tk.StringVar()
        self.saida.set(' ')
        
        labelSaida = tk.Label(self, textvariable=self.saida, bg=self.cor, fg="black", font="Arial 16")
        labelSaida.pack(fill="x", pady="2")
        
        verify = tk.Button(self, text="Verificar número", bg='red', font="16", command=lambda: verificar())
        verify.pack(pady=37, ipadx=10)


# Principal
if __name__ == '__main__':
    app = Aplicativo()
    app.mainloop()