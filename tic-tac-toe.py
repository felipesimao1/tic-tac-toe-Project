def print_board(board):
    """
    Imprime o tabuleiro do jogo.
    """
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    """
    Verifica se há um vencedor no jogo.
    Retorna 'X' se o jogador X venceu, 'O' se o jogador O venceu,
    ou None se não houver vencedor.
    """
    # Verifica linhas
    for row in board:
        if len(set(row)) == 1 and row[0] != ' ':
            return row[0]

    # Verifica colunas
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != ' ':
            return board[0][col]

    # Verifica diagonais
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        return board[0][2]

    return None

def is_full(board):
    """
    Verifica se o tabuleiro está cheio (empate).
    """
    for row in board:
        if ' ' in row:
            return False
    return True

def main():
    """
    Função principal do jogo.
    """
    print("Pressione Enter para iniciar o Jogo da Velha...")
    input()  # Aguarda o usuário pressionar Enter

    board = [[' ' for _ in range(3)] for _ in range(3)]
    player = 'X'

    while True:
        print_board(board)
        try:
            row = int(input(f"Player {player}, choose a row (1, 2, 3): ")) - 1
            col = int(input(f"Player {player}, choose a column (1, 2, 3): ")) - 1

            if row < 0 or row > 2 or col < 0 or col > 2:
                print("Invalid row or column. Please choose again.")
                continue

            if board[row][col] == ' ':
                board[row][col] = player
            else:
                print("This position is already taken. Try again.")
                continue

            winner = check_winner(board)
            if winner:
                print_board(board)
                print(f"Congratulations! Player {winner} wins!")
                break

            if is_full(board):
                print_board(board)
                print("Draw!")
                break

            player = 'O' if player == 'X' else 'X'
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
