import pygame

# Constants
WIDTH, HEIGHT = 800, 600
CARD_WIDTH, CARD_HEIGHT = 100, 150
MARGIN_X = 20
MARGIN_Y = 20

# Color Mapping for Visualization
COLOR_MAP = {
    "White": (255, 255, 255),
    "Blue": (0, 0, 255),
    "Green": (0, 255, 0),
    "Red": (255, 0, 0),
    "Black": (0, 0, 0),
    "Gold": (255, 215, 0)  # Gold (Joker)
}

class UI:
    def __init__(self, screen):
        self.screen = screen

    def render_grid(screen, grid):
        """Renders the 4x3 grid of cards."""
        screen.fill((255, 255, 255))  # Clear the screen
        font = pygame.font.Font(None, 24)  # Font for rendering text

        for row in range(3, 0, -1):  # From top (level 3) to bottom (level 1)
            for col, card in enumerate(grid[row]):
                x = col * (CARD_WIDTH + MARGIN_X) + 100
                y = (3 - row) * (CARD_HEIGHT + MARGIN_Y) + 50

                # Draw card background
                pygame.draw.rect(screen, (200, 200, 200), (x, y, CARD_WIDTH, CARD_HEIGHT))

                # Render and center the color text
                text = font.render(card.color, True, (0, 0, 0))
                text_width, text_height = text.get_size()
                text_x = x + (CARD_WIDTH // 2) - (text_width // 2)
                text_y = y + 5
                screen.blit(text, (text_x, text_y))

