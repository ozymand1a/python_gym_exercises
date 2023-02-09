ROWS = COLS = QUEENS = 8
chess_board = [[False for _ in range(COLS)] for _ in range(ROWS)]


def eight_queens(chess_board, queens, next_row=0):
    if not check_placement(chess_board):
        return

    if queens == QUEENS:
        show_board(chess_board)
        return

    for row in range(ROWS)[next_row:]:
        for col in range(COLS):
            if not chess_board[row][col]:
                chess_board[row][col] = True
                eight_queens(chess_board, queens + 1, row + 1)
                chess_board[row][col] = False


def check_placement(chess_board):
    for row in range(ROWS):
        for col in range(COLS):
            if chess_board[row][col]:
                # check string
                for c in chess_board[row][col + 1:]:
                    if c:
                        return False

                # check row
                for r in chess_board[row + 1:]:
                    if r[col]:
                        return False

                # check diagonals
                # left and to up
                r, c = row, col
                while r < ROWS - 1 and c > 0:
                    r, c = r + 1, c - 1
                    if chess_board[r][c]:
                        return False

                # right and to bottom
                r, c = row, col
                while r < ROWS - 1 and c < COLS - 1:
                    r, c = r + 1, c + 1
                    if chess_board[r][c]:
                        return False

    return True


def show_board(chess_board):
    for row in chess_board:
        for col in row:
            print({False: ".", True: "Q"}[col], end=" ")
        print()
    print()


if __name__ == '__main__':
    eight_queens(chess_board, 0)
