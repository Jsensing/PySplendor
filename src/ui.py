import pygame

# Constants - Increased screen size to fit all cards properly
CARD_WIDTH, CARD_HEIGHT = 150, 200  # Bigger cards
MARGIN_X = 30  # Horizontal space between cards
MARGIN_Y = 30  # Vertical space between rows
NOBLE_CARD_SIZE = 120  # Square noble cards

GRID_COLUMNS = 4  # 4 cards per row
GRID_ROWS = 3  # 3 rows for levels
TOP_CARDS = 3  # Number of noble cards

# ✅ Dynamically set screen size based on card dimensions and margins
WIDTH = (CARD_WIDTH + MARGIN_X) * GRID_COLUMNS + 50  # Adjusted width
HEIGHT = (CARD_HEIGHT + MARGIN_Y) * GRID_ROWS + 200  # Adjusted height

# Color Mapping for Display Text
COLOR_MAP = {
    "Diamond": (128, 128, 128),  # Gray for Diamond (White)
    "Sapphire": (0, 0, 255),  # Blue -> Sapphire
    "Emerald": (0, 255, 0),  # Green -> Emerald
    "Ruby": (255, 0, 0),  # Red -> Ruby
    "Onyx": (0, 0, 0),  # Black -> Onyx
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
    def __init__(self, screen, noble_cards):
        self.screen = screen
        self.noble_cards = noble_cards

        # Load images for each card type and resize them
        self.card_images = {
            "Ruby": pygame.transform.scale(pygame.image.load("assets/cardImg/ruby.jpg"), (CARD_WIDTH, CARD_HEIGHT)),
            "Diamond": pygame.transform.scale(pygame.image.load("assets/cardImg/diamond.jpg"), (CARD_WIDTH, CARD_HEIGHT)),
            "Emerald": pygame.transform.scale(pygame.image.load("assets/cardImg/emerald.jpg"), (CARD_WIDTH, CARD_HEIGHT)),
            "Sapphire": pygame.transform.scale(pygame.image.load("assets/cardImg/sapphire.jpg"), (CARD_WIDTH, CARD_HEIGHT)),
            "Onyx": pygame.transform.scale(pygame.image.load("assets/cardImg/onyx.jpg"), (CARD_WIDTH, CARD_HEIGHT))
        }

    def render_grid(self, grid):
        """Renders the 4x3 grid of cards with increased spacing."""
        self.screen.fill((255, 255, 255))  # Clear the screen
        font = pygame.font.Font(None, 30)  # Increased font size
        
        # Render the 3 noble cards at the top
        for i, noble_card in enumerate(self.noble_cards):
            x = i * (NOBLE_CARD_SIZE + MARGIN_X) + 150
            y = 20  # Position noble cards at the top

            # Draw square noble card background
            pygame.draw.rect(self.screen, (180, 180, 180), (x, y, NOBLE_CARD_SIZE, NOBLE_CARD_SIZE))
            pygame.draw.rect(self.screen, (0, 0, 0), (x, y, NOBLE_CARD_SIZE, NOBLE_CARD_SIZE), 2)  # Border

            # Render noble points at the top of the noble card
            points_text = font.render(f"{noble_card.points}", True, (0, 0, 0))
            self.screen.blit(points_text, (x + 50, y + 10))

            # Render cost in the bottom-left of the noble card
            cost_x, cost_y = x + 5, y + NOBLE_CARD_SIZE - 30
            for color, cost in noble_card.cost.items():
                if cost > 0:
                    text_color = COLOR_MAP.get(color, (0, 0, 0))
                    cost_text = font.render(f"{color[0]}: {cost}", True, text_color)
                    self.screen.blit(cost_text, (cost_x, cost_y))
                    cost_y -= 20  # Move text up for the next cost

        for row in range(3, 0, -1):  # From Level 3 (top) to Level 1 (bottom)
            for col, card in enumerate(grid[row]):
                x = col * (CARD_WIDTH + MARGIN_X) + 50  # Adjusted position
                y = (3 - row) * (CARD_HEIGHT + MARGIN_Y) + 50  # Adjusted position

                # Convert old color names to new names
                new_color_name = COLOR_NAME_MAP.get(card.color, card.color)  # Default to original if not mapped

                # Draw card background using images
                if new_color_name in self.card_images:
                    self.screen.blit(self.card_images[new_color_name], (x, y))  # Display corresponding image
                else:
                    pygame.draw.rect(self.screen, (200, 200, 200), (x, y, CARD_WIDTH, CARD_HEIGHT))  # Default background
                
                pygame.draw.rect(self.screen, (0, 0, 0), (x, y, CARD_WIDTH, CARD_HEIGHT), 2)  # Border

                # Move bonus points closer to the top-left corner
                bonus_text = font.render(f"{card.bonus}", True, (0, 0, 0))  # Always black
                self.screen.blit(bonus_text, (x + 5, y + 5))  # Moved slightly up

                # Move the card name lower to avoid overlap
                color_text = font.render(new_color_name, True, (0, 0, 0))  # Force black text
                color_rect = color_text.get_rect(center=(x + CARD_WIDTH // 2, y + 15))  # Moved down slightly
                self.screen.blit(color_text, color_rect)

                # Keep the bottom-left cost values in their respective colors (Diamond in gray)
                cost_x, cost_y = x + 5, y + CARD_HEIGHT - 30  # Bottom-left positioning, moved slightly up
                for color, cost in card.cost.items():
                    if cost > 0:
                        new_cost_color = COLOR_NAME_MAP.get(color, color)
                        text_color = (128, 128, 128) if new_cost_color == "Diamond" else COLOR_MAP.get(new_cost_color, (0, 0, 0))
                        cost_text = font.render(f"{new_cost_color[0]}: {cost}", True, text_color)  # Apply color
                        self.screen.blit(cost_text, (cost_x, cost_y))
                        cost_y -= 25  # Increased spacing to prevent overlap
