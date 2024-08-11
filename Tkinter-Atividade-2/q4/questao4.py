import datetime
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
        
        
        def calcularIdade():
            diaAtual = datetime.datetime.now().strftime('%d')
            mesAtual = datetime.datetime.now().strftime('%m')
            anoAtual = datetime.datetime.now().strftime('%Y')
            idade = entradaAge.get()
            if idade[2] == '/' and idade[5] == '/' and len(idade) == 10:
                listIdade = idade.split('/')
                idadeNumber = ''.join(listIdade)
                if idadeNumber.isdigit():
                    self.saida.set(diaAtual+'/'+mesAtual+'/'+anoAtual)
                else:
                    self.saida.set('A data de nascimento deve ter somente números inteiros!')
            
            else:
                 self.saida.set('Formato da data incorreto!')  
                     
        
         # widgets
        labelTexto = tk.Label(self, text="Age calc", bg=self.cor, fg="#FFF", font="Arial 18")
        labelTexto.pack(fill="x", ipady="30")
        
        label1 = tk.Label(self, text="Insira sua idade (dd/mm/aaaa):", bg=self.cor, fg="#000", font="Arial 18")
        label1.pack(fill="x", ipady="30")
        
        
        entradaAge = tk.Entry(self, font="Arial 14")
        entradaAge.pack(pady=10)
        
        self.saida = tk.StringVar()
        self.saida.set(' ')
        
        labelSaida = tk.Label(self, textvariable=self.saida, bg=self.cor, fg="black", font="Arial 16")
        labelSaida.pack(fill="x", pady="2")
        
        calc = tk.Button(self, text="Calcular idade", bg='red', font="16", command=lambda: calcularIdade())
        calc.pack(pady=37, ipadx=10)


# Principal
if __name__ == '__main__':
    app = Aplicativo()
    app.mainloop()

print(datetime.datetime.now().strftime('%Y'))