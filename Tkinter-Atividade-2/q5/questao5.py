import datetime
import tkinter as tk

class Aplicativo(tk.Tk):
    def __init__(self):
        super().__init__()
        self.cor = "#aaa"
        self.janelaPrincipal()
    
    def janelaPrincipal(self):
        self.geometry("600x600")
        self.title("Aplicativo")
        self.configure(bg=self.cor)
        self.resizable(True,False)
        
        def vencedor():
            if entradaTime1.get() and entradaTime2.get() and entradaPlacar1.get() and entradaPlacar2.get():
                if entradaPlacar1.get().isdigit() and entradaPlacar2.get().isdigit():
                    if int(entradaPlacar1.get()) >= 0 and int(entradaPlacar2.get()) >= 0:
                        time = {
                            1: {'nome': entradaTime1.get(), 'placar': entradaPlacar1.get()}, 
                            2: {'nome': entradaTime2.get(), 'placar': entradaPlacar2.get()}, 
                        }
                        if int(entradaPlacar1.get()) > int(entradaPlacar2.get()):
                            self.saida.set('Vencedor: '+time[1]['nome'])
                        elif int(entradaPlacar1.get()) < int(entradaPlacar2.get()):
                            self.saida.set('Vencedor: '+time[2]['nome'])
                        else:
                             self.saida.set('Empate!!')
                            
                    else:
                        self.saida.set('O placar deve ser >= 0!')
                else:
                    self.saida.set('O placar deve ser número inteiro!')
            else:
                self.saida.set('Defina todos os campos!')
        
         # widgets
        labelTexto = tk.Label(self, text="Futebol ⚽", bg=self.cor, fg="#FFF", font="Arial 18")
        labelTexto.grid(row=0, column=1, pady=30)
        
        label1 = tk.Label(self, text="Time 1:", bg=self.cor, fg="#000", font="Arial 18")
        label1.grid(row=1, column=0, pady=5, padx=7)
        
        entradaTime1 = tk.Entry(self, font="Arial 14")
        entradaTime1.grid(row=2, column=0, pady=5, padx=7)
        # --------------------------------- #
        labelX1 = tk.Label(self, text="X", bg=self.cor, fg="#000", font="Arial 18")
        labelX1.grid(row=2, column=1, pady=5)
        
        labelX2 = tk.Label(self, text="X", bg=self.cor, fg="#000", font="Arial 18")
        labelX2.grid(row=4, column=1, pady=2)
        # --------------------------------- #
        label2 = tk.Label(self, text="Time 2:", bg=self.cor, fg="#000", font="Arial 18")
        label2.grid(row=1, column=2, pady=5)
        
        entradaTime2 = tk.Entry(self, font="Arial 14")
        entradaTime2.grid(row=2, column=2, pady=5)
        
        #---------------------------------- #
        labelP1 = tk.Label(self, text="Placar 1:", bg=self.cor, fg="#000", font="Arial 18")
        labelP1.grid(row=3, column=0, pady=5)
        
        labelP2 = tk.Label(self, text="Placar 2:", bg=self.cor, fg="#000", font="Arial 18")
        labelP2.grid(row=3, column=2, pady=5)
        
        
        entradaPlacar1 = tk.Entry(self, font="Arial 14")
        entradaPlacar1.grid(row=4, column=0, pady=5, padx=7)
        
        entradaPlacar2 = tk.Entry(self, font="Arial 14")
        entradaPlacar2.grid(row=4, column=2, pady=5)
        
        self.saida = tk.StringVar()
        self.saida.set(' ')
        
        labelSaida = tk.Label(self, textvariable=self.saida, bg=self.cor, fg="black", font="Arial 16")
        labelSaida.grid(row=5, column=0, pady=5)
        
        calc = tk.Button(self, text="Ver vencedor", bg='red', font="16", command=lambda: vencedor())
        calc.grid(row=6,pady=20, column=1)


# Principal
if __name__ == '__main__':
    app = Aplicativo()
    app.mainloop()