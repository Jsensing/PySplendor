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

    def render_grid(self, grid):
        """Renders the 4x3 grid of cards."""
        self.screen.fill((255, 255, 255))  # Clear the screen
        font = pygame.font.Font(None, 24)  # Font for text

        for row in range(3, 0, -1):  # From Level 3 (top) to Level 1 (bottom)
            for col, card in enumerate(grid[row]):
                x = col * (CARD_WIDTH + MARGIN_X) + 100
                y = (3 - row) * (CARD_HEIGHT + MARGIN_Y) + 50

                # Draw card background
                pygame.draw.rect(self.screen, (200, 200, 200), (x, y, CARD_WIDTH, CARD_HEIGHT))
                pygame.draw.rect(self.screen, (0, 0, 0), (x, y, CARD_WIDTH, CARD_HEIGHT), 2)  # Border

                # Draw the color name at the TOP CENTER of the card
                color_text = font.render(card.color, True, COLOR_MAP.get(card.color, (0, 0, 0)))
                color_rect = color_text.get_rect(center=(x + CARD_WIDTH // 2, y + 10))  # Positioned at top center
                self.screen.blit(color_text, color_rect)

                # Draw costs in the bottom-left corner
                cost_x, cost_y = x + 5, y + CARD_HEIGHT - 20  # Bottom-left positioning
                for color, cost in card.cost.items():
                    if cost > 0:  # Only display costs greater than zero
                        cost_text = font.render(f"{color[0]}: {cost}", True, COLOR_MAP.get(color, (0, 0, 0)))
                        self.screen.blit(cost_text, (cost_x, cost_y))
                        cost_y -= 20  # Move text up for the next cost
