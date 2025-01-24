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
        
        def mostrarTexto():
            if entradaTexto.get():
                self.resultado.set(entradaTexto.get())
            else:
                self.resultado.set('Não definido!')
        
         # widgets
        labelTexto = tk.Label(self, text="Texto:", bg=self.cor, fg="#FFF", font="Arial 16")
        labelTexto.pack(fill="x", ipady="30")
        
    
        entradaTexto = tk.Entry(self, font="Arial 14")
        entradaTexto.pack(pady=10)
        
        
        label3 = tk.Label(self, text="Resultado:", bg=self.cor, fg="black", font="Arial 16")
        label3.pack(fill="x", pady="2")
        
        self.resultado = tk.StringVar()
        self.resultado.set(' ')
        labelResultado = tk.Label(self, textvariable=self.resultado, bg=self.cor, fg="black", font="Arial 16")
        labelResultado.pack(fill="x", pady="2")
        
        mostrar = tk.Button(self, text="Mostrar", bg='red', font="16", command=lambda:mostrarTexto())
        mostrar.pack(pady=37, ipadx=10)


# Principal
if __name__ == '__main__':
    app = Aplicativo()
    app.mainloop()