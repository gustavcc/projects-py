import os
from colorama import Fore, Back, Style

vit_X = 0
vit_O = 0
jogarNovamente="s"
jogadas=0
quemJoga=1 #1=jogador 1 - 2=jogador 2
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
    print("   ---|---|---")
    print("1:  "+velha[1][0]+" | "+velha[1][1]+" | "+velha[1][2])
    print("   ---|---|---")
    print("2:  "+velha[2][0]+" | "+velha[2][1]+" | "+velha[2][2])
    print("\n-----------------")
    print(Fore.BLUE+f"Jogadas → {jogadas}"+Fore.RESET)
    print(f"Jogador 1 → {Fore.RESET}{Fore.RED}{vit_X}{Fore.RESET}")
    print(f"Jogador 2 → {Fore.RESET}{Fore.GREEN}{vit_O}{Fore.RESET}")
    print("-"*60)

def jogador_1Joga():
    global jogadas
    global quemJoga
    global maxJogadas 
    if quemJoga==1 and jogadas<maxJogadas:
        print("1° JOGADOR\n")
        while True:
            try:
                linha=int(input("Linha\n:"))
                break
            except ValueError:
                continue
        while True:
            try:
                coluna=int(input("Coluna\n:"))
                break
            except ValueError:
                continue
        if velha[linha][coluna]==" ":
            while velha[linha][coluna]!=" ":
                linha=int(input("Linha\n:"))
                coluna=int(input("Coluna\n:"))
            velha[linha][coluna]=(f"{Fore.RESET}{Fore.RED}{'X'}{Fore.RESET}")
            quemJoga=2
            jogadas+=1
            print("-"*60)
        else:
            print("-"*60)
            print(Fore.RED+"Error "+Fore.RESET+"-> posição inválida ou preenchida")
            print("-"*60)
            print("Aperte uma tecla para continuar...")
            input()

def jogador_2Joga():
    global jogadas
    global quemJoga
    global maxJogadas 
    if quemJoga==2 and jogadas<maxJogadas:
        print('2° JOGADOR\n')
        while True:
            try:
                linha=int(input("Linha\n:"))
                break
            except ValueError:
                continue
        while True:
            try:
                coluna=int(input("Coluna\n:"))
                break
            except ValueError:
                continue
        if velha[linha][coluna]==" ":
            while velha[linha][coluna]!=" ":
                linha=int(input("Linha\n:"))
                coluna=int(input("Coluna\n:"))
            velha[linha][coluna]=(f"{Fore.RESET}{Fore.GREEN}{'O'}{Fore.RESET}")
            quemJoga=1
            jogadas+=1
            print("-"*60)
        else:
            print("-"*60)
            print(Fore.RED+"Error "+Fore.RESET+"-> posição inválida ou preenchida")
            print("-"*60)
            print("Aperte uma tecla para continuar...")
            input()

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
        elif velha[linha][0]==velha[linha][1]==velha[linha][2]==(f"{Fore.RESET}{Fore.GREEN}{'O'}{Fore.RESET}"):
            vitoria='O'
            break
        linha+=1

    # Verificar colunas
    coluna=0
    while coluna<3:
        if velha[0][coluna]==velha[1][coluna]==velha[2][coluna]==(f"{Fore.RESET}{Fore.RED}{'X'}{Fore.RESET}"):
            vitoria='X'
            break
        elif velha[0][coluna]==velha[1][coluna]==velha[2][coluna]==(f"{Fore.RESET}{Fore.GREEN}{'O'}{Fore.RESET}"):
            vitoria='O'
            break
        coluna+=1

    # Verificar 1° diagonal
    diagonal_1=0
    while diagonal_1<1:
        if velha[0][0]==velha[1][1]==velha[2][2]==(f"{Fore.RESET}{Fore.RED}{'X'}{Fore.RESET}"):
            vitoria='X'
            break
        elif velha[0][0]==velha[1][1]==velha[2][2]==(f"{Fore.RESET}{Fore.GREEN}{'O'}{Fore.RESET}"):
            vitoria='O'
            break
        diagonal_1+=1

    # Verificar 2° diagonal
    diagonal_2 = 0
    while diagonal_2<1:
        if velha[2][0]==velha[1][1]==velha[0][2]==(f"{Fore.RESET}{Fore.RED}{'X'}{Fore.RESET}"):
            vitoria='X'
            break
        elif velha[2][0]==velha[1][1]==velha[0][2]==(f"{Fore.RESET}{Fore.GREEN}{'O'}{Fore.RESET}"):
            vitoria='O'
            break
        diagonal_2+=1
    return vitoria

def redefinir():
    global velha
    global jogadas 
    global quemJoga
    global maxJogadas
    global vit
    jogadas=0
    quemJoga=1 #1=jogador 1 - 2=jogador 2
    maxJogadas=9
    vit='n'
    velha=[
        [" "," "," "],
        [" "," "," "],
        [" "," "," "]
    ]

while jogarNovamente[0]=='s':                
    while True:
        tela()
        jogador_1Joga()
        vit=verificarVitoria()
        tela()
        if vit!='n' or jogadas==maxJogadas:
            print(Fore.YELLOW+'FIM DE JOGO!'+Fore.RESET)
            print("-"*60)
            break
        jogador_2Joga()
        tela()
        vit=verificarVitoria()
        if vit!='n' or jogadas==maxJogadas:
            print(Fore.YELLOW+'FIM DE JOGO!'+Fore.RESET)
            print("-"*60)
            break
    if vit=='X':
        vit_X += 1
        print(f'O jogador 1 ({Fore.RESET}{Fore.RED}{vit}{Fore.RESET}) venceu!')
        print("-"*60)
    elif vit=='O':
        vit_O += 1
        print(f'O jogador 2 ({Fore.RESET}{Fore.GREEN}{vit}{Fore.RESET}) venceu!')
        print("-"*60)
    else:
        print("Empate!")
        print("-"*60)
    jogarNovamente=input("\nJogar novamente? (s/n)\n:").lower().strip()
    redefinir()
    if jogarNovamente[0]=='n':
        os.system('cls')
        print('\n\nFim do Jogo!\n\n')
        break