'''
Jogo da velha 4x4, com lógica similar ao 3x3, mas mudando o tamanho do tabuleiro
'''

'''
Primeiro, definimos uma função para imprimir o tabuleiro, usando um loop for para imprimir cada linha do tabuleiro
'''
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 13)


'''
Para verificar o vencedor, usamos um for para iterar por todas linhas, colunas e diagonais, 
verificando se estão preenchidas com o mesmo símbolo (jogador).
'''
def check_winner(board, player):
    # Verificando linhas e colunas
    for i in range(4):
        if all(board[i][j] == player for j in range(4)) or \
           all(board[j][i] == player for j in range(4)):
            return True

    # Verificando diagonais
    if all(board[i][i] == player for i in range(4)) or \
       all(board[i][3 - i] == player for i in range(4)):
        return True

    return False

'''
A função principal é onde inicializamos o tabuleiro, o jogador e o número de jogadas.
'''
def main():
    board = [[" " for _ in range(4)] for _ in range(4)]
    player = "X"
    moves = 0

    # Jogo permanece em loop ate que haja um vencedor ou empate
    while True:
        print_board(board)
        row = int(input(f"Jogador {player}, escolha a linha (1-4): ")) - 1
        col = int(input(f"Jogador {player}, escolha a coluna (1-4): ")) - 1

        # Verificando se posição está vazia
        if board[row][col] == " ":
            board[row][col] = player
            moves += 1
        else:
            print("Essa posição já foi escolhida.")
            continue

        if check_winner(board, player):
            print_board(board)
            print(f"Jogador {player} venceu.")
            break

        # Verificando empate se numero de jogadas for 16 (maximo possivel)
        if moves == 16:
            print_board(board)
            print("Empate.")
            break

        # Definindo próximo jogador
        if player == "X":
            player = "O"
        else:
            player = "X"



if __name__ == "__main__":
    main()
