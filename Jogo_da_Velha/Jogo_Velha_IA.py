import os
import random
from colorama import Fore, Back, Style


jogarNovamente="s"
jogadas=0
quemJoga=2 #1=cpu - 2=jogador
maxJogadas=9
vit='n'
velha=[
    [" "," "," "],
    [" "," "," "],
    [" "," "," "]
]

def tela():
    global velha
    global jogadas
    os.system("cls")
    print("    0   1   2")
    print("    ¨   ¨   ¨")
    print("0:  "+velha[0][0]+" | "+velha[0][1]+" | "+velha[0][2])
    print("   -----------")
    print("1:  "+velha[1][0]+" | "+velha[1][1]+" | "+velha[1][2])
    print("   -----------")
    print("2:  "+velha[2][0]+" | "+velha[2][1]+" | "+velha[2][2])
    print("\n-----------------")
    print(Fore.BLUE+f"Jogadas -> {jogadas}"+Fore.RESET)
    print("-----------------")

def jogador_1Joga():
    global jogadas
    global quemJoga
    global maxJogadas 
    if quemJoga==2 and jogadas<maxJogadas:
        try: #try é para que o Python tente executar 
        # aquele código e caso não consiga executar por conta de 
        # um erro ele vai retornar o que temos dentro do except.
            linha=int(input("Linha\n:"))
            coluna=int(input("Coluna\n:"))
            while velha[linha][coluna]!=" ":
                linha=int(input("Linha\n:"))
                coluna=int(input("Coluna\n:"))
            velha[linha][coluna]=(f"{Fore.RESET}{Fore.RED}{'X'}{Fore.RESET}")
            quemJoga=1
            jogadas+=1
        except:
            print("\n-----------------")
            print(Fore.RED+"Error "+Fore.RESET+"-> linha e/ou coluna inválido")
            print("\n-----------------")

def cpuJoga():
    global jogadas
    global quemJoga
    global maxJogadas 
    if quemJoga==1 and jogadas<maxJogadas:
        linha=random.randrange(0,3)
        coluna=random.randrange(0,3)
        while velha[linha][coluna]!=" ":
            linha=random.randrange(0,3)
            coluna=random.randrange(0,3)
        velha[linha][coluna]=(f"{Fore.GREEN}{'O'}{Fore.RESET}")
        quemJoga=2
        jogadas+=1

def verificarVitoria():
    global velha
    global vitoria
    vitoria='n'
    # Verificar linhas
    linha=0
    while linha<3:
        if velha[linha][0]==velha[linha][1]==velha[linha][2]==(f"{Fore.RESET}{Fore.RED}{'X'}{Fore.RESET}"):
            vitoria='X'
            break
        elif velha[linha][0]==velha[linha][1]==velha[linha][2]==(f"{Fore.GREEN}{'O'}{Fore.RESET}"):
            vitoria='O'
            break
        linha+=1
    # Verificar colunas
    coluna=0
    while coluna<3:
        if velha[0][coluna]==velha[1][coluna]==velha[2][coluna]==(f"{Fore.RESET}{Fore.RED}{'X'}{Fore.RESET}"):
            vitoria='X'
            break
        elif velha[0][coluna]==velha[1][coluna]==velha[2][coluna]==(f"{Fore.GREEN}{'O'}{Fore.RESET}"):
            vitoria='O'
            break
        coluna+=1
    # Verificar 1° diagonal
    diagonal=0
    while diagonal<1:
        if velha[0][0]==velha[1][1]==velha[2][2]==(f"{Fore.RESET}{Fore.RED}{'X'}{Fore.RESET}"):
            vitoria='X'
            break
        elif velha[0][0]==velha[1][1]==velha[2][2]==(f"{Fore.GREEN}{'O'}{Fore.RESET}"):
            vitoria='O'
            break
        diagonal+=1
    # Verificar 2° diagonal
    simbolo=[f"{Fore.RESET}{Fore.RED}{'X'}{Fore.RESET}",f"{Fore.GREEN}{'O'}{Fore.RESET}"]
    diagonal_l=0
    diagonal_c=2
    qtd=0
    for i in simbolo:
        while diagonal_c>=0:
            if velha[diagonal_l][diagonal_c]==i:
                qtd+=1
            diagonal_l+=1
            diagonal_c-=1
        if qtd==3:
            vitoria=(Fore.RESET+i+Fore.RESET)
            break
    return vitoria


def redefinir():
    global velha
    global jogadas 
    global quemJoga
    global maxJogadas
    global vit
    jogadas=0
    quemJoga=2 #1=cpu - 2=jogador
    maxJogadas=9
    vit='n'
    velha=[
        [" "," "," "],
        [" "," "," "],
        [" "," "," "]
    ]

while jogarNovamente=='s':                
    while True:
        tela()
        jogador_1Joga()
        cpuJoga()
        tela()
        vit=verificarVitoria()
        if vit!='n' or jogadas==maxJogadas:
            print(Fore.YELLOW+'FIM DE JOGO!'+Fore.RESET)
            print("-----------------")
            break
    if vit=='X' or vit=='O':
        print('O jogador',vit,'venceu!')
        print("-----------------")
    else:
        print("Empate!")
        print("-----------------")
    jogarNovamente=input("\nJogar novamente? (s/n)\n:").lower()
    redefinir()
    if jogarNovamente[0]=='n':
        break

