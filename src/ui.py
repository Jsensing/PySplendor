import pygame

# Constants
WIDTH, HEIGHT = 800, 600
CARD_WIDTH, CARD_HEIGHT = 100, 150
MARGIN_X, MARGIN_Y = 20

class UI:
    def __init__(self, screen):
        self.screen = screen

    def render_grid(self, grid):
        """Renders the 4x3 grid of cards."""
        self.screen.fill((255, 255, 255))  # Clear the screen

        for row in range(3, 0, -1):  # From Level 3 (top) to Level 1 (bottom)
            for col, card in enumerate(grid[row]):
                x = col * (CARD_WIDTH + MARGIN_X) + 100
                y = (3 - row) * (CARD_HEIGHT + MARGIN_Y) + 50

                # Draw card background
                pygame.draw.rect(self.screen, (200, 200, 200), (x, y, CARD_WIDTH, CARD_HEIGHT))

                # Render text (color & level)
                font = pygame.font.Font(None, 24)
                text = font.render(f"{card.color} L{card.level}", True, (0, 0, 0))
                self.screen.blit(text, (x + 10, y + 10))
