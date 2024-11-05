import numpy as np

class Sudoku:
    def __init__(self, board=None):
        if board is None:
            self.board =np.zeros((9,9),dtype=int)
            [
                [0, 0, 6, 0, 0, 0, 5, 0, 8],
                [1, 0, 2, 3, 8, 0, 0, 0, 4],
                [0, 0, 0, 2, 0, 0, 1, 9, 0],
                [0, 0, 0, 0, 6, 3, 0, 4, 5],
                [0, 6, 3, 4, 0, 5, 8, 7, 0],
                [5, 4, 0, 9, 2, 0, 0, 0, 0],
                [0, 8, 7, 0, 0, 4, 0, 0, 0],
                [2, 0, 0, 0, 9, 8, 4, 0, 7],
                [4, 0, 9, 0, 0, 0, 3, 0, 0],
            ]
        else:
            self.board = np.array(board)

    def is_valid(self, row, col, num):
        if num in self.board[row]:
            return False

        if num in self.board[:, col]:
            return False
        
        box_row = row // 3
        box_col = col // 3
        if num in self.board[box_row*3:(box_row+1)*3, box_col*3:(box_col+1)*3]:
            return False

        return True

    def solve(self):
        for row in range(9):
            for col in range(9):
                if self.board[row, col] == 0:
                    for num in range(1, 10):
                        if self.is_valid(row, col, num):
                            self.board[row, col] = num
                            if self.solve():
                                return True
                            self.board[row, col] = 0
                    return False
        return True

    def print_board(self):
        for row in self.board:
            print(row)

def create_sudoku_game():
    game = Sudoku()
    game.print_board()
    if input("Solve the puzzle? (y/n): ").lower() == 'y':
        if game.solve():
            print("Solution:")
            game.print_board()
        else:
            print("No solution exists.")

if __name__ == "__main__":
    create_sudoku_game()