import pygame

# ✅ Initialize Pygame to get the usable screen size (excluding taskbar)
pygame.init()
screen_info = pygame.display.Info()
SCREEN_WIDTH = screen_info.current_w  # Full screen width
SCREEN_HEIGHT = screen_info.current_h  # Full screen height, including taskbar

# ✅ Grid Layout
GRID_COLUMNS = 4  # 4 main cards per row
GRID_ROWS = 3  # 3 rows for levels
TOP_CARDS = 3  # Number of noble cards

# ✅ Dynamic Sizing Based on Screen Resolution
MARGIN_X_RATIO = 0.02  # 2% of screen width for spacing
MARGIN_Y_RATIO = 0.03  # 3% of screen height for spacing

CARD_WIDTH = int(SCREEN_WIDTH * 0.15)  # 15% of screen width
CARD_HEIGHT = int(SCREEN_HEIGHT * 0.2)  # 20% of screen height
NOBLE_CARD_SIZE = int(SCREEN_WIDTH * 0.12)  # 12% of screen width (square)

MARGIN_X = int(SCREEN_WIDTH * MARGIN_X_RATIO)
MARGIN_Y = int(SCREEN_HEIGHT * MARGIN_Y_RATIO)

# ✅ Create a TRUE FULLSCREEN Window That Covers Taskbar
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN | pygame.NOFRAME)

# ✅ Debugging: Print Screen and Card Sizes
print(f"Usable screen size: {SCREEN_WIDTH}x{SCREEN_HEIGHT}")
print(f"Card size: {CARD_WIDTH}x{CARD_HEIGHT}, Noble size: {NOBLE_CARD_SIZE}x{NOBLE_CARD_SIZE}")

class UI:
    def __init__(self, screen, noble_cards):
        self.screen = screen
        self.noble_cards = noble_cards

        # Load images for each card type and resize them dynamically
        self.card_images = {
            "Ruby": pygame.transform.scale(pygame.image.load("assets/cardImg/ruby.jpg"), (CARD_WIDTH, CARD_HEIGHT)),
            "Diamond": pygame.transform.scale(pygame.image.load("assets/cardImg/diamond.jpg"), (CARD_WIDTH, CARD_HEIGHT)),
            "Emerald": pygame.transform.scale(pygame.image.load("assets/cardImg/emerald.jpg"), (CARD_WIDTH, CARD_HEIGHT)),
            "Sapphire": pygame.transform.scale(pygame.image.load("assets/cardImg/sapphire.jpg"), (CARD_WIDTH, CARD_HEIGHT)),
            "Onyx": pygame.transform.scale(pygame.image.load("assets/cardImg/onyx.jpg"), (CARD_WIDTH, CARD_HEIGHT))
        }

    def render_grid(self, grid):
        """Renders the 3 noble cards at the top and the 4x3 grid below with equal spacing."""
        self.screen.fill((255, 255, 255))  # Clear the screen
        font = pygame.font.Font(None, int(SCREEN_HEIGHT * 0.03))  # Scale font size dynamically

        # ✅ Center noble cards horizontally and distribute evenly
        noble_start_x = (SCREEN_WIDTH - ((NOBLE_CARD_SIZE + MARGIN_X) * TOP_CARDS - MARGIN_X)) // 2
        noble_y = int(SCREEN_HEIGHT * 0.05)  # Moves noble cards slightly lower

        for i, noble_card in enumerate(self.noble_cards):
            x = noble_start_x + i * (NOBLE_CARD_SIZE + MARGIN_X)

            # Draw noble card background
            pygame.draw.rect(self.screen, (180, 180, 180), (x, noble_y, NOBLE_CARD_SIZE, NOBLE_CARD_SIZE))
            pygame.draw.rect(self.screen, (0, 0, 0), (x, noble_y, NOBLE_CARD_SIZE, NOBLE_CARD_SIZE), 2)  # Border

            # Render noble points at the top of the noble card
            points_text = font.render(f"{noble_card.points}", True, (0, 0, 0))
            self.screen.blit(points_text, (x + NOBLE_CARD_SIZE // 3, noble_y + 10))

        # ✅ Adjust grid Y position to space evenly below noble cards
        grid_start_y = noble_y + NOBLE_CARD_SIZE + (MARGIN_Y * 4)  # ✅ More spacing to prevent overlap

        for row in range(3, 0, -1):  # From Level 3 (top) to Level 1 (bottom)
            for col, card in enumerate(grid[row]):
                x = col * (CARD_WIDTH + MARGIN_X) + (SCREEN_WIDTH - (GRID_COLUMNS * (CARD_WIDTH + MARGIN_X))) // 2
                y = grid_start_y + (3 - row) * (CARD_HEIGHT + MARGIN_Y)

                # Draw main card background
                pygame.draw.rect(self.screen, (200, 200, 200), (x, y, CARD_WIDTH, CARD_HEIGHT))
                pygame.draw.rect(self.screen, (0, 0, 0), (x, y, CARD_WIDTH, CARD_HEIGHT), 2)  # Border
