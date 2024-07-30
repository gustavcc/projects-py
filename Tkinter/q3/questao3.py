import tkinter as tk
from tkinter import messagebox
from conexao import ConexaoBD

conn = ConexaoBD()

class Aplicativo(tk.Tk, ConexaoBD):
    
    global conn
    
    def __init__(self):
        super().__init__()
        self.janelaPrincipal()
        self.telaLogin()
    
    def janelaPrincipal(self):
        self.geometry("500x600")
        self.title("Aplicativo")
        self.resizable(False,False)
    
    # Login
    def telaLogin(self):
        
        def varificarCredenciais():
            if conn.existe_usuarioDB(self.entradaUsuario.get()) == True:
                messagebox.showerror("Login","Usuário não existe!")
                self.entradaUsuario.delete(0,'end')
                self.entradaSenha.delete(0,'end')
            else: 
                usuario = conn.existe_usuarioDB(self.entradaUsuario.get())
                if usuario[0] == self.entradaUsuario.get() and usuario[1] == self.entradaSenha.get():
                    self.telaDashboard()
                else:
                    messagebox.showerror("Login","Senha incorreta!") 
                    self.entradaUsuario.delete(0,'end')
                    self.entradaSenha.delete(0,'end')
        
        cor = "#10AAB0"
        
        # Frame a parte para ser puzaxo dentro da uma janela só.
        self.frameLogin = tk.Frame(self, width=400, height=400)
        self.frameLogin.configure(bg=cor)
        self.frameLogin.pack(fill='both', expand=True)
            
        # widgets
        labelLogin = tk.Label(self.frameLogin, text="Login", bg="black", fg="#FFF", font="Arial 16")
        labelLogin.pack(fill="x", ipady="30")
        
        usuarioLogin = tk.Label(self.frameLogin, text="Usuario", bg=cor, fg="black", font="Arial 16")
        usuarioLogin.pack(fill="x", pady="2")
    
        self.entradaUsuario = tk.Entry(self.frameLogin, font="Arial 14")
        self.entradaUsuario.pack(pady=10)
        
        senha=tk.Label(self.frameLogin, text="Senha", bg=cor,fg="black", font="Arial 16")
        senha.pack(fill="x")
        
        self.entradaSenha = tk.Entry(self.frameLogin, font="Arial 14", show="*")
        self.entradaSenha.pack(pady=10)
        
        botaoLogin = tk.Button(self.frameLogin, text="Entrar", bg="#0F7", font="16", command=varificarCredenciais)
        botaoLogin.pack(pady=37, ipadx=10)
    
    #   Dashboard   
    def telaDashboard(self):
        
        self.frameLogin.pack_forget()
        
        cor = "#801090"
        
        # Frame a parte para ser puzaxo dentro da uma janela só.
        self.frameDash = tk.Frame(self, width=400, height=400)
        self.frameDash.configure(bg=cor)
        self.frameDash.pack(fill='both', expand=True)
            
        #widget
        labelDash = tk.Label(self.frameDash, text="Dashboard", bg="black", fg="#FFF", font="Arial 16")
        labelDash.pack(fill="x", ipady="30")
        
        #------------------------------------------------
        
        usuarioDash = tk.Label(self.frameDash, text="Seja bem vindo(a)", bg=cor, fg="black", font="Arial 14")
        usuarioDash.pack(fill="x", pady="2")
        
        usuarioInfo = tk.Label(self.frameDash, text = self.entradaUsuario.get(), bg=cor, fg="black", font="Arial 14")
        usuarioInfo.pack(fill="x", pady="2")


# Principal
if __name__ == '__main__':
    app = Aplicativo()
    app.mainloop()
