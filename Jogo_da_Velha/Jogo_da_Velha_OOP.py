import os
class Tabuleiro:
    def __init__(self):
        self.tabuleiro = [" "] * 9

    def mostrar_tabuleiro(self):
        print(f" {self.tabuleiro[0]} | {self.tabuleiro[1]} | {self.tabuleiro[2]} " )
        print("---+---+---")
        print(f" {self.tabuleiro[3]} | {self.tabuleiro[4]} | {self.tabuleiro[5]} ")
        print("---+---+---")
        print(f" {self.tabuleiro[6]} | {self.tabuleiro[7]} | {self.tabuleiro[8]} ")

    def fazer_jogada(self, posicao, jogador):
        if 1 <= posicao <= 9 and self.tabuleiro[posicao - 1] == " ":
            self.tabuleiro[posicao - 1] = jogador
            return True
        else:
            return False

    def verificar_vitoria(self, jogador):
        linhas = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
        colunas = [[0, 3, 6], [1, 4, 7], [2, 5, 8]]
        diagonais = [[0, 4, 8], [2, 4, 6]]

        for linha in linhas + colunas + diagonais:
            if all(self.tabuleiro[i] == jogador for i in linha):
                return True

        return False

    def tabuleiro_cheio(self):
        return " " not in self.tabuleiro


class JogoDaVelha:
    def __init__(self):
        self.tabuleiro = Tabuleiro()
        self.jogador_atual = "X"

    def trocar_jogador(self):
        if self.jogador_atual == "X":
            self.jogador_atual = "O"
        else:
            self.jogador_atual = "X"

    def jogar(self):
        print("Jogo da Velha - Python")
        while True:
            os.system("cls")
            self.tabuleiro.mostrar_tabuleiro()
            jogada = int(input(f"Jogador {self.jogador_atual}, escolha uma posição (1-9): "))

            if self.tabuleiro.fazer_jogada(jogada, self.jogador_atual):
                if self.tabuleiro.verificar_vitoria(self.jogador_atual):
                    print(f"Jogador {self.jogador_atual} venceu!")
                    break
                elif self.tabuleiro.tabuleiro_cheio():
                    print("O jogo terminou em empate!")
                    break
                else:
                    self.trocar_jogador()
            else:
                print("Posição inválida ou ocupada. Tente novamente.")

if __name__ == "__main__":
    jogo = JogoDaVelha()
    jogo.jogar()
