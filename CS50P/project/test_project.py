from project import check_valid_moves

# Test function for check_valid_moves


def test_check_valid_moves():
    # Test case 1: Test with a valid move
    board1 = [['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'],
              ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
              [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
              [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
              [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
              [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
              ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
              ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r']]
    move1 = ((6, 4), (4, 4))  # Moving a pawn from (6, 4) to (4, 4)
    assert is_valid_move(board1, move1) == True

    # Test case 2: Test with an invalid move
    board2 = [['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'],
              ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
              [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
              [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
              [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
              [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
              ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
              ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r']]
    move2 = ((6, 4), (3, 4))  # Moving a pawn to an invalid position
    assert is_valid_move(board2, move2) == False
