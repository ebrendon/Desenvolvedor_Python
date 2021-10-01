import os

# -------- variáveis Globais ------------
jogo_em_andamento = True   # Variável para analisar se o jogo chegou ao fim

vencedor = None  # Variável para armazenar o vencedor ao fim, None = Empate

jogador_atual = "X"  # Jogador a jogar a seguir, por default deixarei com X iniciando

tabuleiro = ["-", "-", "-",     # Tabuleiro inicialmente vazio
             "-", "-", "-",
             "-", "-", "-"]

# -------- variáveis Globais ------------


# Função para imprimir tabuleiro formatado como jogo da velha

def exibir_tabuleiro():
    print(tabuleiro[0]+" | "+tabuleiro[1]+" | "+tabuleiro[2])
    print(tabuleiro[3]+" | "+tabuleiro[4]+" | "+tabuleiro[5])
    print(tabuleiro[6]+" | "+tabuleiro[7]+" | "+tabuleiro[8])

# Função para verificar se usuário jogará novamente
# As variáveis globais são retornadas aos valores defaul


def jogar_novamente():
    global tabuleiro, jogo_em_andamento, vencedor, jogador_atual
    novamente = int(
        input("Se deseja jogar novamente digite 1, se não, digite 0: "))
    if novamente == 1:
        jogo_em_andamento = True
        vencedor = None
        jogador_atual = "X"
        tabuleiro = ["-", "-", "-",
                     "-", "-", "-",
                     "-", "-", "-"]
        os.system('cls') or None
        iniciar_jogo()
    else:
        print("Até mais!")


# Início do Jogo
def iniciar_jogo():

    exibir_tabuleiro()

    while jogo_em_andamento:
        jogada(jogador_atual)
        verifica_fim_de_jogo()
        alterar_jogador()
    if vencedor == "X" or vencedor == "O":
        print(vencedor + " venceu")
    elif vencedor == None:
        print("Empate")
    jogar_novamente()


# Troca de mão
def jogada(player):
    print("Vez de " + player)
    position = input("Escolha a posição (1-9): ")

    valid = False
    while not valid:

        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Escolha a posição (1-9): ")

        position = int(position)-1

        if tabuleiro[position] == "-":
            valid = True
        else:
            print("Não é possível escolher essa posição")

    tabuleiro[position] = player
    exibir_tabuleiro()

# Analisando se o jogo chegou ao fim


def verifica_fim_de_jogo():
    checar_vitoria()
    checar_empate()

# Verifica o resultado do jogo


def checar_vitoria():
    global vencedor
    vitoria_linha = checar_linhas()
    vitoria_coluna = checar_colunas()
    vitoria_diagonal = checar_diagonais()

    if vitoria_linha:
        vencedor = vitoria_linha
    elif vitoria_coluna:
        vencedor = vitoria_coluna
    elif vitoria_diagonal:
        vencedor = vitoria_diagonal
    else:
        vencedor = None
    return

# Analisando se teve vencedor na linha


def checar_linhas():
    global jogo_em_andamento

    linha_1 = tabuleiro[0] == tabuleiro[1] == tabuleiro[2] != "-"
    linha_2 = tabuleiro[3] == tabuleiro[4] == tabuleiro[5] != "-"
    linha_3 = tabuleiro[6] == tabuleiro[7] == tabuleiro[8] != "-"

    if linha_1 or linha_2 or linha_3:
        jogo_em_andamento = False
    if linha_1:
        return tabuleiro[0]
    elif linha_2:
        return tabuleiro[3]
    elif linha_3:
        return tabuleiro[6]
    return

# Analisando se houve vencedor nas colunas


def checar_colunas():
    global jogo_em_andamento

    coluna_1 = tabuleiro[0] == tabuleiro[3] == tabuleiro[6] != "-"
    coluna_2 = tabuleiro[1] == tabuleiro[4] == tabuleiro[7] != "-"
    coluna_3 = tabuleiro[2] == tabuleiro[5] == tabuleiro[8] != "-"

    if coluna_1 or coluna_2 or coluna_3:
        jogo_em_andamento = False
    if coluna_1:
        return tabuleiro[0]
    elif coluna_2:
        return tabuleiro[1]
    elif coluna_3:
        return tabuleiro[2]
    return

# Analisando se houve vencedor nas diagonais


def checar_diagonais():
    global jogo_em_andamento

    diagonal_1 = tabuleiro[0] == tabuleiro[4] == tabuleiro[8] != "-"
    diagonal_2 = tabuleiro[2] == tabuleiro[4] == tabuleiro[6] != "-"

    if diagonal_1 or diagonal_2:
        jogo_em_andamento = False
    if diagonal_1:
        return tabuleiro[0]
    elif diagonal_2:
        return tabuleiro[2]
    return

# Analisando se houve um empate


def checar_empate():
    global jogo_em_andamento
    if "-" not in tabuleiro:
        jogo_em_andamento = False
    return

# Altera quem joga a seguir


def alterar_jogador():
    global jogador_atual
    if jogador_atual == "X":
        jogador_atual = "O"
    elif jogador_atual == "O":
        jogador_atual = "X"
    return


iniciar_jogo()
