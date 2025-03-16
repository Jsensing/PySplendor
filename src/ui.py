import pygame
import os

# ✅ Initialize Pygame before using display functions
pygame.init()

# ✅ Define Screen Size Constants After Initializing Pygame
SCREEN_WIDTH = pygame.display.Info().current_w  # Full screen width
SCREEN_HEIGHT = pygame.display.Info().current_h  # Full screen height

# ✅ Dynamic Card & Noble Sizing
CARD_WIDTH = int(SCREEN_WIDTH * 0.15)  # 15% of screen width
CARD_HEIGHT = int(SCREEN_HEIGHT * 0.2)  # 20% of screen height
NOBLE_CARD_SIZE = int(SCREEN_WIDTH * 0.12)  # 12% of screen width (square)

MARGIN_X = int(SCREEN_WIDTH * 0.02)  # 2% of screen width for spacing
MARGIN_Y = int(SCREEN_HEIGHT * 0.03)  # 3% of screen height for spacing

# ✅ Color mapping for cost text (for nobles and regular cards)
COST_COLOR_MAP = {
    "Diamond": (128, 128, 128),  # Gray for Diamond (White)
    "Sapphire": (0, 0, 255),  # Blue -> Sapphire
    "Emerald": (0, 255, 0),  # Green -> Emerald
    "Ruby": (255, 0, 0),  # Red -> Ruby
    "Onyx": (0, 0, 0),  # Black -> Onyx
}

# ✅ Mapping Old Colors to New Names for Cost Text
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

        # ✅ Get absolute paths for images
        card_assets_path = os.path.abspath("assets/cardImg")
        noble_img_path = os.path.abspath("assets/nobleImg/noble.jpg")  # ✅ One noble image for all

        # ✅ Load the **same noble image** for all nobles
        self.noble_image = None
        if os.path.exists(noble_img_path):
            try:
                original_img = pygame.image.load(noble_img_path)
                self.noble_image = pygame.transform.scale(original_img, (NOBLE_CARD_SIZE, NOBLE_CARD_SIZE))
                print(f"✅ Loaded noble image: {noble_img_path}")
            except pygame.error as e:
                print(f"❌ Failed to load noble image {noble_img_path}: {e}")
        else:
            print(f"⚠️ Warning: Noble image not found {noble_img_path}")

        # ✅ Load card images for each type
        self.card_images = {}
        card_types = ["Ruby", "Diamond", "Emerald", "Sapphire", "Onyx"]

        for card in card_types:
            img_path = os.path.join(card_assets_path, f"{card.lower()}.jpg")

            if os.path.exists(img_path):  # ✅ Check if file exists
                try:
                    original_img = pygame.image.load(img_path)
                    self.card_images[card] = pygame.transform.scale(original_img, (CARD_WIDTH, CARD_HEIGHT))
                    print(f"✅ Successfully loaded card image: {img_path}")  # ✅ Debugging message
                except pygame.error as e:
                    print(f"❌ Failed to load card image {img_path}: {e}")
                    self.card_images[card] = None  # Fallback to gray
            else:
                print(f"⚠️ Warning: Card image not found {img_path}")  # ✅ Debugging message
                self.card_images[card] = None  # Fallback to gray if missing

    def render_grid(self, grid):
        """Renders the 3 noble cards at the top and the 4x3 grid below with text drawn properly."""
        self.screen.fill((255, 255, 255))  # ✅ Clear the screen before drawing
        font = pygame.font.Font(None, int(SCREEN_HEIGHT * 0.03))  # ✅ Scale font size dynamically

        # ✅ Center noble cards horizontally and distribute evenly
        noble_start_x = (SCREEN_WIDTH - ((NOBLE_CARD_SIZE + MARGIN_X) * 3 - MARGIN_X)) // 2
        noble_y = int(SCREEN_HEIGHT * 0.05)  # Moves noble cards slightly lower

        for i, noble_card in enumerate(self.noble_cards):
            x = noble_start_x + i * (NOBLE_CARD_SIZE + MARGIN_X)

            # ✅ Draw noble card background using the **same image** for all nobles
            if self.noble_image:
                self.screen.blit(self.noble_image, (x, noble_y))
            else:
                pygame.draw.rect(self.screen, (180, 180, 180), (x, noble_y, NOBLE_CARD_SIZE, NOBLE_CARD_SIZE))

            pygame.draw.rect(self.screen, (0, 0, 0), (x, noble_y, NOBLE_CARD_SIZE, NOBLE_CARD_SIZE), 2)  # Border

            # ✅ Render noble points at the **top left**
            points_text = font.render(str(noble_card.points), True, (0, 0, 0))
            self.screen.blit(points_text, (x + 5, noble_y + 5))  # Top left position

            # ✅ Render noble cost in correct color (Bottom Left)
            cost_x, cost_y = x + 5, noble_y + NOBLE_CARD_SIZE - 30
            for color, cost in noble_card.cost.items():
                if cost > 0:
                    mapped_color = COLOR_NAME_MAP.get(color, color)  # Convert "White" -> "Diamond"
                    text_color = COST_COLOR_MAP.get(mapped_color, (0, 0, 0))  # Get mapped color
                    cost_text = font.render(f"{mapped_color[0]}: {cost}", True, text_color)
                    self.screen.blit(cost_text, (cost_x, cost_y))
                    cost_y -= 20  # ✅ Move text up for the next cost

        # ✅ Adjust grid Y position to space below noble cards
        grid_start_y = noble_y + NOBLE_CARD_SIZE + (MARGIN_Y * 4)

        for row in range(3, 0, -1):  # From Level 3 (top) to Level 1 (bottom)
            for col, card in enumerate(grid[row]):
                x = col * (CARD_WIDTH + MARGIN_X) + (SCREEN_WIDTH - (4 * (CARD_WIDTH + MARGIN_X))) // 2
                y = grid_start_y + (3 - row) * (CARD_HEIGHT + MARGIN_Y)

                # ✅ Display card image if available
                card_type = card.color
                if card_type in self.card_images and self.card_images[card_type]:
                    self.screen.blit(self.card_images[card_type], (x, y))
                else:
                    pygame.draw.rect(self.screen, (200, 200, 200), (x, y, CARD_WIDTH, CARD_HEIGHT))  # ✅ Default gray background
            
                pygame.draw.rect(self.screen, (0, 0, 0), (x, y, CARD_WIDTH, CARD_HEIGHT), 2)  # ✅ Border

                # ✅ Render card name in **black** at the **top center**
                name_text = font.render(card_type, True, (0, 0, 0))  # Black text for name
                name_rect = name_text.get_rect(center=(x + CARD_WIDTH // 2, y + 15))  # Centered name
                self.screen.blit(name_text, name_rect)

                # ✅ Render bonus points (Top Left)
                bonus_text = font.render(str(card.bonus), True, (0, 0, 0))
                self.screen.blit(bonus_text, (x + 5, y + 5))

                # ✅ Render cost in correct color (Bottom Left)
                cost_x, cost_y = x + 5, y + CARD_HEIGHT - 30
                for color, cost in card.cost.items():
                    if cost > 0:
                        mapped_color = COLOR_NAME_MAP.get(color, color)  # Convert "White" -> "Diamond"
                        text_color = COST_COLOR_MAP.get(mapped_color, (0, 0, 0))  # Get mapped color
                        cost_text = font.render(f"{mapped_color[0]}: {cost}", True, text_color)
                        self.screen.blit(cost_text, (cost_x, cost_y))
                        cost_y -= 20  # ✅ Move text up for the next cost
