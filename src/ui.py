import pygame
import os

# Initialize Pygame before using display functions
pygame.init()

# Define Screen Size Constants After Initializing Pygame
SCREEN_WIDTH = pygame.display.Info().current_w
SCREEN_HEIGHT = pygame.display.Info().current_h

# Dynamic Card & Noble Sizing
CARD_WIDTH = int(SCREEN_WIDTH * 0.15)
CARD_HEIGHT = int(SCREEN_HEIGHT * 0.17)  # Reduced height to prevent cutoff
NOBLE_CARD_SIZE = int(SCREEN_WIDTH * 0.12)

MARGIN_X = int(SCREEN_WIDTH * 0.02)
MARGIN_Y = int(SCREEN_HEIGHT * 0.02)  # Reduced vertical margin for tighter layout

# Player UI Panels
PLAYER_PANEL_WIDTH = int(SCREEN_WIDTH * 0.18)
PLAYER_PANEL_HEIGHT = int(SCREEN_HEIGHT * 0.2)
GAME_AREA_WIDTH = SCREEN_WIDTH - (PLAYER_PANEL_WIDTH * 2)

# Color mapping
COST_COLOR_MAP = {
    "Diamond": (128, 128, 128),
    "Sapphire": (0, 0, 255),
    "Emerald": (0, 255, 0),
    "Ruby": (255, 0, 0),
    "Onyx": (0, 0, 0),
}

def load_scaled_image(path, size):
    if os.path.exists(path):
        try:
            img = pygame.image.load(path)
            return pygame.transform.scale(img, size)
        except pygame.error as e:
            print(f"Error loading image {path}: {e}")
    else:
        print(f"Image not found: {path}")
    return None

class UI:
    def __init__(self, screen, noble_cards, player1, player2):
        self.screen = screen
        self.noble_cards = noble_cards
        self.player1 = player1
        self.player2 = player2

        # Load shared noble image once
        self.noble_image = load_scaled_image("assets/nobleImg/noble.jpg", (NOBLE_CARD_SIZE, NOBLE_CARD_SIZE))

    def render_player_hand(self, player, x, y):
        font = pygame.font.Font(None, int(SCREEN_HEIGHT * 0.025))
        name_text = font.render(player.name, True, (0, 0, 0))
        self.screen.blit(name_text, (x + 10, y + 10))
        points_text = font.render(f"Points: {player.points}", True, (0, 0, 0))
        self.screen.blit(points_text, (x + 10, y + 40))

        token_y = y + 80
        for color, amount in player.tokens.items():
            text_color = COST_COLOR_MAP.get(color, (0, 0, 0))
            token_text = font.render(f"{color[0]}: {amount}", True, text_color)
            self.screen.blit(token_text, (x + 10, token_y))
            token_y += 25

    def render_grid(self, grid):
        self.screen.fill((255, 255, 255))

        self.render_player_hand(self.player1, 10, 10)
        self.render_player_hand(self.player2, SCREEN_WIDTH - PLAYER_PANEL_WIDTH - 10, 10)

        font = pygame.font.Font(None, int(SCREEN_HEIGHT * 0.03))

        # 🔧 Raise noble cards slightly to make space
        noble_y = int(SCREEN_HEIGHT * 0.14)
        noble_start_x = (GAME_AREA_WIDTH - ((NOBLE_CARD_SIZE + MARGIN_X) * 3 - MARGIN_X)) // 2 + PLAYER_PANEL_WIDTH

        for i, noble_card in enumerate(self.noble_cards):
            x = noble_start_x + i * (NOBLE_CARD_SIZE + MARGIN_X)
            if self.noble_image:
                self.screen.blit(self.noble_image, (x, noble_y))

            points_text = font.render(str(getattr(noble_card, "points", 0)), True, (0, 0, 0))
            self.screen.blit(points_text, (x + 5, noble_y + 5))

            # Render noble cost ON TOP of image (color coded)
            cost_font = pygame.font.Font(None, int(SCREEN_HEIGHT * 0.02))
            noble_cost = getattr(noble_card, "cost", {})
            cost_y = noble_y + 30
            for color, amount in noble_cost.items():
                text_color = COST_COLOR_MAP.get(color, (0, 0, 0))
                cost_text = cost_font.render(f"{color[0]}: {amount}", True, text_color)
                self.screen.blit(cost_text, (x + 5, cost_y))
                cost_y += 20

        # 🔧 Adjust layout to fit all card rows
        grid_start_y = noble_y + NOBLE_CARD_SIZE + int(SCREEN_HEIGHT * 0.02)

        for row in range(3, 0, -1):
            for col, card in enumerate(grid[row]):
                x = col * (CARD_WIDTH + MARGIN_X) + (GAME_AREA_WIDTH - (4 * (CARD_WIDTH + MARGIN_X))) // 2 + PLAYER_PANEL_WIDTH
                y = grid_start_y + (3 - row) * (CARD_HEIGHT + MARGIN_Y)

                card_color = getattr(card, "color", "Unknown")
                card_points = getattr(card, "points", 0)
                card_cost = getattr(card, "cost", {})

                # Image by color name (lowercase)
                image_filename = f"{card_color.lower()}.jpg"
                image_path = os.path.join("assets", "cardImg", image_filename)
                card_img = load_scaled_image(image_path, (CARD_WIDTH, CARD_HEIGHT))
                if card_img:
                    self.screen.blit(card_img, (x, y))

                card_text = font.render(f"{card_color} ({card_points})", True, (0, 0, 0))
                self.screen.blit(card_text, (x + 5, y + 5))

                cost_font = pygame.font.Font(None, int(SCREEN_HEIGHT * 0.02))
                cost_y = y + CARD_HEIGHT - 60
                for color, amount in card_cost.items():
                    text_color = COST_COLOR_MAP.get(color, (0, 0, 0))
                    cost_text = cost_font.render(f"{color[0]}: {amount}", True, text_color)
                    self.screen.blit(cost_text, (x + 5, cost_y))
                    cost_y += 20

    def render_players(self):
        self.render_player_hand(self.player1, 10, 10)
        self.render_player_hand(self.player2, SCREEN_WIDTH - PLAYER_PANEL_WIDTH - 10, 10)
