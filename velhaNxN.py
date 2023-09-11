'''
Jogo da velha NxN, com lógica similar ao 4x4, mas o tamanho do tabuleiro é definido pelo usuário
'''

'''
Primeiro, definimos uma função para imprimir o tabuleiro, usando um loop for para imprimir cada linha do tabuleiro
'''
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * (len(board) * 3 - 1))


'''
Para verificar o vencedor, usamos um for para iterar por todas linhas, colunas e diagonais, 
verificando se estão preenchidas com o mesmo símbolo (jogador).
'''
def check_winner(board, player):
    size = len(board)

    # Verificando linhas e colunas
    for i in range(size):
        if all(board[i][j] == player for j in range(size)) or \
           all(board[j][i] == player for j in range(size)):
            return True

    # Verificando diagonais
    if all(board[i][i] == player for i in range(size)) or \
       all(board[i][size - 1 - i] == player for i in range(size)):
        return True

    return False

'''
A função principal é onde inicializamos o tabuleiro, o jogador e o número de jogadas.
'''
def main():
    
    # Recebendo o tamanho do tabuleiro do usuário
    size = int(input("Digite o tamanho do tabuleiro (NxN): "))
    board = [[" " for _ in range(size)] for _ in range(size)]
    player = "X"
    
    # Jogo permanece em loop ate que haja um vencedor ou empate
    for _ in range(size * size):
        print_board(board)
        row = int(input(f"Jogador {player}, escolha a linha (1-{size}): ")) - 1
        col = int(input(f"Jogador {player}, escolha a coluna (1-{size}): ")) - 1

        # Verificando se posição está vazia
        if 0 <= row < size and 0 <= col < size and board[row][col] == " ":
            board[row][col] = player
        else:
            print("Essa posição já foi escolhida.")
            continue

        if check_winner(board, player):
            print_board(board)
            print(f"Jogador {player} venceu.")
            break

        # Definindo próximo jogador
        if player == "X":
            player = "O"
        else:
            player = "X"

    else:
        print_board(board)
        print("Empate.")

if __name__ == "__main__":
    main()
