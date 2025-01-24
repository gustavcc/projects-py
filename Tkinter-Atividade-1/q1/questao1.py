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
        
        def mudarCor(cor):
            self.cor = cor
            self.configure(bg=self.cor)
        
        vermelho = 'red'
        verde = 'green'
        azul = 'blue'
            
        labelLogin = tk.Label(self, text="Questão 1", bg="black", fg="#FFF", font="Arial 16")
        labelLogin.pack(fill="x", ipady="30")
        
        botaoVermelho = tk.Button(self, text="Vermelho", bg=vermelho, font="16", command=lambda:mudarCor(vermelho))
        botaoVermelho.pack(pady=37, ipadx=10)
        
        botaoVerde = tk.Button(self, text="Verde", bg=verde, font="16", command=lambda:mudarCor(verde))
        botaoVerde.pack(pady=37, ipadx=10)
        
        botaoAzul = tk.Button(self, text="Azul", bg=azul, font="16", command=lambda:mudarCor(azul))
        botaoAzul.pack(pady=37, ipadx=10)


# Principal
if __name__ == '__main__':
    app = Aplicativo()
    app.mainloop()
