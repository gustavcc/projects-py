import pandas as pd
import pyautogui
import time

#   faça os tratamentos de erros adequados a cada circunstância

#   pyautogui.click() -> clica em um botão
#   pyautogui.write() -> escreve alguma informação em um input
#   pyautogui.press() -> aperta 1 tecla 
#   pyautogui.hotkey() -> combinação de teclas em clique (Ctrl + C)  
#   pyautogui.scroll() -> rolar o scroll  
#   pyautogui.position() -> peag a posição do mouse em x e y  

#   Defino o temporizador do pyautogui para cada comando deejado
pyautogui.PAUSE = 0.5

pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')

#   Entrar no link
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')

#   Esperar para executar algo
time.sleep(5)

#   Clique na posição especificada da screen    
pyautogui.click(x=917, y=515)

#   Preenche as informações
pyautogui.write("pythonimpressionador@gmail.com")
pyautogui.press('tab')
pyautogui.write('1234')
pyautogui.click(x=938, y=711)

#   Esperar para executar algo
time.sleep(3)

#   Importar a base de produtos pra cadastrar
import pandas as pd

tabela = pd.read_csv("produtos.csv")

# Inserir todas as informações uma por uma
for linha in tabela.index:
    # clicar no campo de código
    pyautogui.click(x=854, y=367)
    # pegar da tabela o valor do campo que a gente quer preencher por linha
    codigo = tabela.loc[linha, "codigo"]
    # preencher o campo
    pyautogui.write(str(codigo))
    # passar para o proximo campo
    pyautogui.press("tab")
    # preencher o campo
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))   
    pyautogui.press("tab")
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter") # cadastra o produto (botao enviar)
    # dar scroll de tudo pra cima
    pyautogui.scroll(5000)
    # Passo 5: Repetir o processo de cadastro até o fim