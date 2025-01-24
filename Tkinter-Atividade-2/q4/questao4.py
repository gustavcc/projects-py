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
            #   Não considerei anos bissextos, portanto, fevereiro possui 28 dias
            mesesDoAno = {
                1: {"nome": "Janeiro", "dias": 31},
                2: {"nome": "Fevereiro", "dias": 28},
                3: {"nome": "Março", "dias": 31},
                4: {"nome": "Abril", "dias": 30},
                5: {"nome": "Maio", "dias": 31},
                6: {"nome": "Junho", "dias": 30},
                7: {"nome": "Julho", "dias": 31},
                8: {"nome": "Agosto", "dias": 31},
                9: {"nome": "Setembro", "dias": 30},
                10: {"nome": "Outubro",  "dias": 31},
                11: {"nome": "Novembro",  "dias": 30},
                12: {"nome": "Dezembro",  "dias": 31}
            }
            
            diaAtual = datetime.datetime.now().strftime('%d')
            mesAtual = datetime.datetime.now().strftime('%m')
            anoAtual = datetime.datetime.now().strftime('%Y')
            idade = entradaAge.get()
            if idade[2] == '/' and idade[5] == '/' and len(idade) == 10:
                listIdade = idade.split('/')
                idadeNumber = ''.join(listIdade)
                if idadeNumber.isdigit():
                    try:
                        if  1 <= int(listIdade[1]) <= 12:
                            qtdDiasMes = int(mesesDoAno[int(listIdade[1])]['dias'])
                            nomeMes = mesesDoAno[int(listIdade[1])]['nome']
                            if int(listIdade[0]) <= qtdDiasMes:
                                
                                if int(listIdade[2]) <= int(anoAtual):
                                    if int(listIdade[1]) <= int(mesAtual) or int(listIdade[2]) < int(anoAtual):
                                        if (int(listIdade[0]) <= int(diaAtual) or int(listIdade[1]) < int(mesAtual)) or int(listIdade[2]) < int(anoAtual):
                                            
                                            ano = int(anoAtual) - int(listIdade[2])
                                            mes = int(mesAtual) - int(listIdade[1])
                                            if mes < 0:
                                                ano -= 1
                                                mes = 12 + mes
                                            self.saida.set('Você tem '+str(ano)+' anos e '+str(mes)+' meses de idade')
                                        else:
                                            self.saida.set('Você não pode nascer depois de: '+diaAtual+'/'+mesAtual+'/'+anoAtual)
                                    else:
                                        self.saida.set('Você não pode nascer depois de: '+diaAtual+'/'+mesAtual+'/'+anoAtual)
                                else:
                                    self.saida.set('Você não pode nascer depois de: '+diaAtual+'/'+mesAtual+'/'+anoAtual)
                            else: 
                                 self.saida.set(nomeMes+' só possui '+str(qtdDiasMes)+' dias!')
                        else:
                            self.saida.set('Esse mês não existe!')
                    except Exception as e:
                        print('Erro: ', e)
                else:
                    self.saida.set('A data deve ter somente números inteiros!')
            
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