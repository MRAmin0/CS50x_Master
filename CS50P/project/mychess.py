import pygame
import sys
import chess
import chess.svg

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Function to draw the chessboard
def draw_board(screen, board):
    chessboard = chess.svg.board(board=board).encode("UTF-8")
    chessboard_surface = pygame.image.load_extended(pygame.compat.BytesIO(chessboard))
    screen.blit(chessboard_surface, (0, 0))

# Main function
def main():
    # Create Pygame screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Chess Game")

    # Create a chessboard
    board = chess.Board()

    # Main game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Draw the chessboard
        draw_board(screen, board)

        # Update the display
        pygame.display.flip()

if __name__ == "__main__":
    main()
