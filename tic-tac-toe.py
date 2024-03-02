import random

class BattleshipGame:
    def __init__(self, size=5):
        self.size = size
        self.board = [[' ' for _ in range(size)] for _ in range(size)]
        self.ships = size // 2
        self.remaining_ships = self.ships

    def place_ships(self):
        for _ in range(self.ships):
            x = random.randint(0, self.size - 1)
            y = random.randint(0, self.size - 1)
            self.board[x][y] = 'S'

    def print_board(self, show_ships=False):
        print("  " + " ".join(str(i) for i in range(self.size)))
        for i in range(self.size):
            row = " ".join(self.board[i][j] if self.board[i][j] != 'S' or show_ships else ' ' for j in range(self.size))
            print(str(i) + " " + row)

    def make_guess(self, x, y):
        if self.board[x][y] == 'S':
            print("Hit!")
            self.board[x][y] = 'H'
            self.remaining_ships -= 1
            if self.remaining_ships == 0:
                print("Congratulations! You sunk all the battleships.")
                return True
        elif self.board[x][y] == 'H' or self.board[x][y] == 'M':
            print("You've already guessed this position.")
        else:
            print("Miss!")
            self.board[x][y] = 'M'
        return False

def get_valid_input(prompt, size):
    while True:
        try:
            value = int(input(prompt))
            if 0 <= value < size:
                return value
            else:
                print("Invalid input. Value must be between 0 and {}.".format(size - 1))
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    print("Welcome to Battleship Game!")
    size = get_valid_input("Enter the size of the board (minimum size is 5): ", 100)
    game = BattleshipGame(size)
    game.place_ships()
    game_over = False

    while not game_over:
        print("\nYour current board:")
        game.print_board()
        print("\nMake a guess:")
        x = get_valid_input("Enter X coordinate: ", size)
        y = get_valid_input("Enter Y coordinate: ", size)
        game_over = game.make_guess(x, y)

if __name__ == "__main__":
    main()
