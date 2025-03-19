import pygame
import os

# Initialize Pygame before using display functions
pygame.init()

# Define Screen Size Constants After Initializing Pygame
SCREEN_WIDTH = pygame.display.Info().current_w  # Full screen width
SCREEN_HEIGHT = pygame.display.Info().current_h  # Full screen height

# Dynamic Card & Noble Sizing
CARD_WIDTH = int(SCREEN_WIDTH * 0.15)  # 15% of screen width
CARD_HEIGHT = int(SCREEN_HEIGHT * 0.2)  # 20% of screen height
NOBLE_CARD_SIZE = int(SCREEN_WIDTH * 0.12)  # 12% of screen width (square)

MARGIN_X = int(SCREEN_WIDTH * 0.02)  # 2% of screen width for spacing
MARGIN_Y = int(SCREEN_HEIGHT * 0.03)  # 3% of screen height for spacing

# Space for player hands on left & right
PLAYER_PANEL_WIDTH = int(SCREEN_WIDTH * 0.18)  # 18% of screen width for player hands
GAME_AREA_WIDTH = SCREEN_WIDTH - (PLAYER_PANEL_WIDTH * 2)  # Remaining area for game board

# Color mapping for cost text (for nobles and regular cards)
COST_COLOR_MAP = {
    "Diamond": (128, 128, 128),  # Gray for Diamond (White)
    "Sapphire": (0, 0, 255),  # Blue -> Sapphire
    "Emerald": (0, 255, 0),  # Green -> Emerald
    "Ruby": (255, 0, 0),  # Red -> Ruby
    "Onyx": (0, 0, 0),  # Black -> Onyx
}

class UI:
    def __init__(self, screen, noble_cards, player1, player2):
        self.screen = screen
        self.noble_cards = noble_cards
        self.player1 = player1
        self.player2 = player2

        # Get absolute paths for images
        card_assets_path = os.path.abspath("assets/cardImg")
        noble_img_path = os.path.abspath("assets/nobleImg/noble.jpg")  # One noble image for all

        # Load the **same noble image** for all nobles
        self.noble_image = None
        if os.path.exists(noble_img_path):
            try:
                original_img = pygame.image.load(noble_img_path)
                self.noble_image = pygame.transform.scale(original_img, (NOBLE_CARD_SIZE, NOBLE_CARD_SIZE))
            except pygame.error as e:
                print(f"❌ Failed to load noble image {noble_img_path}: {e}")
        else:
            print(f"⚠️ Warning: Noble image not found {noble_img_path}")

    def render_player_hand(self, player, x, y):
        # Renders the player's tokens, points, and owned cards at a given x position.
        font = pygame.font.Font(None, int(SCREEN_HEIGHT * 0.025))  # Adjust font size

        # Draw the player panel
        pygame.draw.rect(self.screen, (220, 220, 220), (x, y, PLAYER_PANEL_WIDTH, SCREEN_HEIGHT - 40))  # Background
        pygame.draw.rect(self.screen, (0, 0, 0), (x, y, PLAYER_PANEL_WIDTH, SCREEN_HEIGHT - 40), 2)  # Border

        # Display Player Points
        points_text = font.render(f"Points: {player.points}", True, (0, 0, 0))
        self.screen.blit(points_text, (x + 10, y + 10))

        # Display Player Tokens (Color-Coded)
        token_y = y + 50
        for color, amount in player.tokens.items():
            text_color = COST_COLOR_MAP.get(color, (0, 0, 0))  # Get mapped color
            token_text = font.render(f"{color[0]}: {amount}", True, text_color)
            self.screen.blit(token_text, (x + 10, token_y))
            token_y += 30

        # Display Player's Owned Cards (Small Previews)
        card_y = token_y + 20
        for card in player.cards:  # FIX: Use player.cards instead of player.owned_cards
            card_text = font.render(card.color, True, (0, 0, 0))
            self.screen.blit(card_text, (x + 10, card_y))
            card_y += 25  # Space out card previews

    def render_grid(self, grid):
        # Renders the game grid and player hands.
        self.screen.fill((255, 255, 255))  # Clear screen

        # Render Player Hands on Left & Right
        self.render_player_hand(self.player1, 10, 10)  # Left side
        self.render_player_hand(self.player2, SCREEN_WIDTH - PLAYER_PANEL_WIDTH - 10, 10)  # Right side

        font = pygame.font.Font(None, int(SCREEN_HEIGHT * 0.03))  # Scale font size dynamically

        # Render nobles (Centered)
        noble_start_x = (GAME_AREA_WIDTH - ((NOBLE_CARD_SIZE + MARGIN_X) * 3 - MARGIN_X)) // 2 + PLAYER_PANEL_WIDTH
        noble_y = int(SCREEN_HEIGHT * 0.05)

        for i, noble_card in enumerate(self.noble_cards):
            x = noble_start_x + i * (NOBLE_CARD_SIZE + MARGIN_X)

            # Draw noble card image
            if self.noble_image:
                self.screen.blit(self.noble_image, (x, noble_y))

            # Render noble points at the **top left**
            points_text = font.render(str(noble_card.points), True, (0, 0, 0))
            self.screen.blit(points_text, (x + 5, noble_y + 5))  # Top left position

        # Adjust grid Y position
        grid_start_y = noble_y + NOBLE_CARD_SIZE + (MARGIN_Y * 4)

        for row in range(3, 0, -1):
            for col, card in enumerate(grid[row]):
                x = col * (CARD_WIDTH + MARGIN_X) + (GAME_AREA_WIDTH - (4 * (CARD_WIDTH + MARGIN_X))) // 2 + PLAYER_PANEL_WIDTH
                y = grid_start_y + (3 - row) * (CARD_HEIGHT + MARGIN_Y)

                # Draw card image
                card_text = font.render(card.color, True, (0, 0, 0))
                self.screen.blit(card_text, (x + CARD_WIDTH // 2 - 20, y + 10))

    def render_players(self):
        # Renders player tokens, points, and cards on both sides of the screen.
        self.render_player_hand(self.player1, 10, 10)  # Left side
        self.render_player_hand(self.player2, SCREEN_WIDTH - PLAYER_PANEL_WIDTH - 10, 10)  # Right side
