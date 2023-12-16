import chess
import chess.svg
from IPython.display import display, SVG

def print_board(board):
    return SVG(chess.svg.board(board=board))

def main():
    board = chess.Board()
    display(print_board(board))

    while not board.is_game_over():
        move_uci = input("Enter your move (in UCI format, e.g., 'e2e4'): ")
        if chess.Move.from_uci(move_uci) in board.legal_moves:
            board.push(chess.Move.from_uci(move_uci))
        else:
            print("Invalid move! Try again.")

        display(print_board(board))

    print("Game Over!")

if __name__ == "__main__":
    main()
