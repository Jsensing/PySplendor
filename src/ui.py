import pygame

# Constants
WIDTH, HEIGHT = 800, 600
CARD_WIDTH, CARD_HEIGHT = 100, 150
MARGIN_X = 20
MARGIN_Y = 20

# Updated Color Names
COLOR_MAP = {
    "Diamond": (255, 255, 255),
    "Sapphire": (0, 0, 255),
    "Emerald": (0, 255, 0),
    "Ruby": (255, 0, 0),  
    "Onyx": (0, 0, 0),  
    "Gold": (255, 215, 0)  # Gold (Joker)
}

# Mapping Old Colors to New Names
COLOR_NAME_MAP = {
    "White": "Diamond",
    "Blue": "Sapphire",
    "Green": "Emerald",
    "Red": "Ruby",
    "Black": "Onyx"
}

class UI:
    def __init__(self, screen):
        self.screen = screen
        self.ruby_card_image = pygame.image.load("assets/cardImg/ruby.jpg")  # Load Ruby (Red) card image
        self.ruby_card_image = pygame.transform.scale(self.ruby_card_image, (CARD_WIDTH, CARD_HEIGHT))  # Resize

    def render_grid(self, grid):
        """Renders the 4x3 grid of cards."""
        self.screen.fill((255, 255, 255))  # Clear the screen
        font = pygame.font.Font(None, 24)  # Font for text

        for row in range(3, 0, -1):  # From Level 3 (top) to Level 1 (bottom)
            for col, card in enumerate(grid[row]):
                x = col * (CARD_WIDTH + MARGIN_X) + 100
                y = (3 - row) * (CARD_HEIGHT + MARGIN_Y) + 50

                # Convert old color names to new names
                new_color_name = COLOR_NAME_MAP.get(card.color, card.color)  # Default to original if not mapped

                # Draw card background
                if new_color_name == "Ruby":  # Red -> Ruby
                    self.screen.blit(self.ruby_card_image, (x, y))  # Use Ruby card image
                else:
                    pygame.draw.rect(self.screen, (200, 200, 200), (x, y, CARD_WIDTH, CARD_HEIGHT))  # Default background

                pygame.draw.rect(self.screen, (0, 0, 0), (x, y, CARD_WIDTH, CARD_HEIGHT), 2)  # Border

                # Draw the bonus points at the TOP LEFT corner
                bonus_text = font.render(f" {card.bonus}", True, (0, 0, 0))
                self.screen.blit(bonus_text, (x + 5, y + 5))

                # Draw the new color name at the TOP CENTER of the card
                color_text = font.render(new_color_name, True, COLOR_MAP.get(new_color_name, (0, 0, 0)))
                color_rect = color_text.get_rect(center=(x + CARD_WIDTH // 2, y + 10))
                self.screen.blit(color_text, color_rect)

                # Draw costs in the bottom-left corner
                cost_x, cost_y = x + 5, y + CARD_HEIGHT - 20
                for color, cost in card.cost.items():
                    if cost > 0:
                        # Convert old cost color name to new color name
                        new_cost_color = COLOR_NAME_MAP.get(color, color)
                        cost_text = font.render(f"{new_cost_color[0]}: {cost}", True, COLOR_MAP.get(new_cost_color, (0, 0, 0)))
                        self.screen.blit(cost_text, (cost_x, cost_y))
                        cost_y -= 20  # Move text up for the next cost
