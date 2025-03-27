import pygame
import os

# Initialize Pygame before using display functions
pygame.init()

# Define Screen Size Constants After Initializing Pygame
SCREEN_WIDTH = pygame.display.Info().current_w
SCREEN_HEIGHT = pygame.display.Info().current_h

# Shrink Factor for All UI Elements
SHRINK_FACTOR = 0.85

# Dynamic Card & Noble Sizing (scaled down)
CARD_WIDTH = int(SCREEN_WIDTH * 0.15 * SHRINK_FACTOR)
CARD_HEIGHT = int(SCREEN_HEIGHT * 0.22 * SHRINK_FACTOR)
NOBLE_CARD_SIZE = int(SCREEN_WIDTH * 0.12 * SHRINK_FACTOR)

MARGIN_X = int(SCREEN_WIDTH * 0.02 * SHRINK_FACTOR)
MARGIN_Y = int(SCREEN_HEIGHT * 0.04 * SHRINK_FACTOR)

# Player UI Panels
PLAYER_PANEL_WIDTH = int(SCREEN_WIDTH * 0.18 * SHRINK_FACTOR)
PLAYER_PANEL_HEIGHT = int(SCREEN_HEIGHT * 0.2 * SHRINK_FACTOR)
GAME_AREA_WIDTH = SCREEN_WIDTH - (PLAYER_PANEL_WIDTH * 2)

# Color mapping
COST_COLOR_MAP = {
    "diamond": (128, 128, 128),
    "sapphire": (0, 0, 255),
    "emerald": (0, 255, 0),
    "ruby": (255, 0, 0),
    "onyx": (0, 0, 0),
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
        font = pygame.font.Font(None, int(SCREEN_HEIGHT * 0.025 * SHRINK_FACTOR))
        name_text = font.render(player.name, True, (0, 0, 0))
        self.screen.blit(name_text, (x + 10, y + 10))
        points_text = font.render(f"Points: {player.points}", True, (0, 0, 0))
        self.screen.blit(points_text, (x + 10, y + 40))

        token_y = y + 80
        for color, amount in player.tokens.items():
            text_color = COST_COLOR_MAP.get(color.lower(), (0, 0, 0))
            token_text = font.render(f"{color[0]}: {amount}", True, text_color)
            self.screen.blit(token_text, (x + 10, token_y))
            token_y += 25

    def render_grid(self, grid):
        self.screen.fill((255, 255, 255))

        self.render_player_hand(self.player1, 10, 10)
        self.render_player_hand(self.player2, SCREEN_WIDTH - PLAYER_PANEL_WIDTH - 10, 10)

        font = pygame.font.Font(None, int(SCREEN_HEIGHT * 0.03 * SHRINK_FACTOR))

        # 👑 Move nobles to top of screen
        noble_y = int(SCREEN_HEIGHT * 0.02)
        noble_start_x = (GAME_AREA_WIDTH - ((NOBLE_CARD_SIZE + MARGIN_X) * 3 - MARGIN_X)) // 2 + PLAYER_PANEL_WIDTH

        for i, noble_card in enumerate(self.noble_cards):
            x = noble_start_x + i * (NOBLE_CARD_SIZE + MARGIN_X)
            if self.noble_image:
                self.screen.blit(self.noble_image, (x, noble_y))

            points_text = font.render(str(getattr(noble_card, "points", 0)), True, (0, 0, 0))
            self.screen.blit(points_text, (x + 5, noble_y + 5))

            cost_font = pygame.font.Font(None, int(SCREEN_HEIGHT * 0.02 * SHRINK_FACTOR))
            noble_cost = getattr(noble_card, "cost", {})
            cost_y = noble_y + 30
            for color, amount in noble_cost.items():
                cost_color = COST_COLOR_MAP.get(color.lower(), (0, 0, 0))
                cost_text = cost_font.render(f"{color[0]}: {amount}", True, cost_color)
                self.screen.blit(cost_text, (x + 5, cost_y))
                cost_y += 20

        # 📐 Center grid and give enough vertical space
        grid_start_y = noble_y + NOBLE_CARD_SIZE + int(SCREEN_HEIGHT * 0.04)

        for row in range(3, 0, -1):
            for col, card in enumerate(grid[row]):
                total_card_width = 4 * (CARD_WIDTH + MARGIN_X) - MARGIN_X
                x = PLAYER_PANEL_WIDTH + (GAME_AREA_WIDTH - total_card_width) // 2 + col * (CARD_WIDTH + MARGIN_X)
                y = grid_start_y + (3 - row) * (CARD_HEIGHT + MARGIN_Y)

                card_color = getattr(card, "color", "Unknown")
                card_points = getattr(card, "points", 0)
                card_cost = getattr(card, "cost", {})

                image_filename = f"{card_color.lower()}.jpg"
                image_path = os.path.join("assets", "cardImg", image_filename)
                card_img = load_scaled_image(image_path, (CARD_WIDTH, CARD_HEIGHT))
                if card_img:
                    self.screen.blit(card_img, (x, y))

                card_text = font.render(f"{card_color} ({card_points})", True, (0, 0, 0))
                self.screen.blit(card_text, (x + 5, y + 5))

                cost_font = pygame.font.Font(None, int(SCREEN_HEIGHT * 0.02 * SHRINK_FACTOR))
                cost_y = y + CARD_HEIGHT - 60
                for color, amount in card_cost.items():
                    text_color = COST_COLOR_MAP.get(color.lower(), (0, 0, 0))
                    cost_text = cost_font.render(f"{color[0]}: {amount}", True, text_color)
                    self.screen.blit(cost_text, (x + 5, cost_y))
                    cost_y += 20

    def render_players(self):
        self.render_player_hand(self.player1, 10, 10)
        self.render_player_hand(self.player2, SCREEN_WIDTH - PLAYER_PANEL_WIDTH - 10, 10)
