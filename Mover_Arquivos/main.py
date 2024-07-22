import os
import shutil as sh

#   get current word directory: pega a pasta atual do projeto 
path = os.getcwd()
#   Pode passar vazio (mostra os arquivos do diretório padrão) ou passar um caminho inteiro ou um caminho dentro do diretório padrão
arquivos = os.listdir(path)

for arquivo in arquivos:
    if '.xlsx' in arquivo:
        if ('compras' in arquivo):
            #   Copia um arquivo e permite colar em uma pasta
            sh.copy2(arquivo, f'Compras/{arquivo}') 
        elif ('vendas' in arquivo):
            #   Renomeia o arquivo, porém posso renomar e passar simutaneamente para um folder específico
            os.rename(arquivo, f'Vendas/{arquivo}')