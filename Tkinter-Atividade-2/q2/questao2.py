import tkinter as tk

class Aplicativo(tk.Tk):
    def __init__(self):
        super().__init__()
        self.cor = "#aaa"
        self.clicks = 0
        self.janelaPrincipal()
    
    def janelaPrincipal(self):
        self.geometry("500x600")
        self.title("Aplicativo")
        self.configure(bg=self.cor)
        self.resizable(False,False)
        
        
        def contarCliques():
            self.clicks += 1
            self.saida.set(self.clicks)
        
        def resetar():
            self.clicks = 0
            self.saida.set(self.clicks)
        
         # widgets
        labelTexto = tk.Label(self, text="Clicks", bg=self.cor, fg="#FFF", font="Arial 18")
        labelTexto.pack(fill="x", ipady="30")
        
        
        label3 = tk.Label(self, text="Quantidade de cliques:", bg=self.cor, fg="black", font="Arial 16")
        label3.pack(fill="x", pady="2")
        
        self.saida = tk.StringVar()
        self.saida.set(self.clicks)
        
        labelSaida = tk.Label(self, textvariable=self.saida, bg=self.cor, fg="black", font="Arial 16")
        labelSaida.pack(fill="x", pady="2")
        
        addClique = tk.Button(self, text="Click me", bg='red', font="16", command=lambda: contarCliques())
        addClique.pack(pady=37, ipadx=10)
        
        resetClique = tk.Button(self, text="Reset", bg='red', font="16", command=lambda: resetar())
        resetClique.pack(pady=37, ipadx=10)


# Principal
if __name__ == '__main__':
    app = Aplicativo()
    app.mainloop()