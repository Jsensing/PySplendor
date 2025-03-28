import pygame
import os
import csv

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
    "gold": (218, 165, 32),
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

def load_cards_from_csv(csv_path):
    cards = []
    with open(csv_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if len(row) != 8:
                continue  # skip malformed rows
            tier, color, diamond, sapphire, emerald, ruby, onyx, points = row
            card = type("Card", (object,), {
                "tier": int(tier),
                "color": color.lower(),
                "points": int(points),
                "cost": {
                    "diamond": int(diamond),
                    "sapphire": int(sapphire),
                    "emerald": int(emerald),
                    "ruby": int(ruby),
                    "onyx": int(onyx),
                }
            })()
            cards.append(card)
    return cards

class UI:
    def __init__(self, screen, noble_cards, player1, player2):
        self.screen = screen
        self.noble_cards = noble_cards
        self.player1 = player1
        self.player2 = player2

        # Token stacks & selection state
        self.token_stacks = {
            "diamond": 4,
            "sapphire": 4,
            "emerald": 4,
            "ruby": 4,
            "onyx": 4,
            "gold": 5,
        }
        self.selected_tokens = {}
        self.selection_limit = 3
        self.token_areas = []

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

    def render_tokens(self):
        token_radius = int(SCREEN_HEIGHT * 0.035)
        spacing = token_radius * 3
        start_x = (SCREEN_WIDTH - spacing * 6) // 2
        y = SCREEN_HEIGHT - int(SCREEN_HEIGHT * 0.06)

        font = pygame.font.Font(None, token_radius)
        self.token_areas.clear()

        colors = ["diamond", "sapphire", "emerald", "ruby", "onyx"]
        for i, color in enumerate(colors):
            count = self.token_stacks[color]
            cx = start_x + i * spacing
            pygame.draw.circle(self.screen, COST_COLOR_MAP[color], (cx, y), token_radius, 3)
            rect = pygame.Rect(cx - token_radius, y - token_radius, token_radius * 2, token_radius * 2)
            self.token_areas.append((rect, color))
            count_text = font.render(str(count), True, (0, 0, 0))
            text_rect = count_text.get_rect(center=(cx, y))
            self.screen.blit(count_text, text_rect)

        gold_count = self.token_stacks["gold"]
        gold_x = start_x + len(colors) * spacing
        pygame.draw.circle(self.screen, COST_COLOR_MAP["gold"], (gold_x, y), token_radius, 3)
        rect = pygame.Rect(gold_x - token_radius, y - token_radius, token_radius * 2, token_radius * 2)
        self.token_areas.append((rect, "gold"))
        gold_text = font.render(str(gold_count), True, (0, 0, 0))
        gold_rect = gold_text.get_rect(center=(gold_x, y))
        self.screen.blit(gold_text, gold_rect)

    def handle_token_click(self, pos, player):
        for rect, color in self.token_areas:
            if rect.collidepoint(pos):
                available = self.token_stacks.get(color, 0)
                selected = self.selected_tokens.get(color, 0)

                if color == "gold":
                    return

                if selected == 1:
                    if available >= 4:
                        self.token_stacks[color] -= 2
                        player.tokens[color] = player.tokens.get(color, 0) + 2
                        self.selected_tokens.clear()
                    return

                if len(self.selected_tokens) < self.selection_limit and available > 0:
                    self.token_stacks[color] -= 1
                    player.tokens[color] = player.tokens.get(color, 0) + 1
                    self.selected_tokens[color] = 1
                return

                if len(self.selected_tokens) < self.selection_limit and available > 0:
                    self.token_stacks[color] -= 1
                    player.tokens[color] = player.tokens.get(color, 0) + 1
                    self.selected_tokens[color] = 1
                return

    def end_turn(self):
        self.selected_tokens.clear()

    def render_grid(self, grid):
        self.screen.fill((255, 255, 255))
        self.render_player_hand(self.player1, 10, 10)
        self.render_player_hand(self.player2, SCREEN_WIDTH - PLAYER_PANEL_WIDTH - 10, 10)

        font = pygame.font.Font(None, int(SCREEN_HEIGHT * 0.03 * SHRINK_FACTOR))

        noble_y = int(SCREEN_HEIGHT * 0.02)
        noble_start_x = (GAME_AREA_WIDTH - ((NOBLE_CARD_SIZE + MARGIN_X) * 3 - MARGIN_X)) // 2 + PLAYER_PANEL_WIDTH

        for i, noble_card in enumerate(self.noble_cards):
            x = noble_start_x + i * (NOBLE_CARD_SIZE + MARGIN_X)
            border_rect = pygame.Rect(x - 3, noble_y - 3, NOBLE_CARD_SIZE + 6, NOBLE_CARD_SIZE + 6)
            pygame.draw.rect(self.screen, (0, 0, 0), border_rect, 2)
            if self.noble_image:
                self.screen.blit(self.noble_image, (x, noble_y))
            points_text = font.render(str(getattr(noble_card, "points", 0)), True, (0, 0, 0))
            self.screen.blit(points_text, (x + 5, noble_y + 5))
            cost_font = pygame.font.Font(None, int(SCREEN_HEIGHT * 0.025 * SHRINK_FACTOR))
            noble_cost = getattr(noble_card, "cost", {})
            cost_y = noble_y + 30
            for color, amount in noble_cost.items():
                cost_color = COST_COLOR_MAP.get(color.lower(), (0, 0, 0))
                cost_text = cost_font.render(f"{color[0]}: {amount}", True, cost_color)
                self.screen.blit(cost_text, (x + 5, cost_y))
                cost_y += 20

        grid_start_y = noble_y + NOBLE_CARD_SIZE + int(SCREEN_HEIGHT * 0.04)

        for row in range(3, 0, -1):
            for col, card in enumerate(grid[row]):
                total_card_width = 4 * (CARD_WIDTH + MARGIN_X) - MARGIN_X
                x = PLAYER_PANEL_WIDTH + (GAME_AREA_WIDTH - total_card_width) // 2 + col * (CARD_WIDTH + MARGIN_X)
                y = grid_start_y + (3 - row) * (CARD_HEIGHT + MARGIN_Y)

                border_rect = pygame.Rect(x - 3, y - 3, CARD_WIDTH + 6, CARD_HEIGHT + 6)
                pygame.draw.rect(self.screen, (0, 0, 0), border_rect, 2)

                card_color = getattr(card, "color", "Unknown")
                card_points = getattr(card, "points", 0)
                card_cost = getattr(card, "cost", {})

                image_filename = f"{card_color.lower()}.jpg"
                image_path = os.path.join("assets", "cardImg", image_filename)
                card_img = load_scaled_image(image_path, (CARD_WIDTH, CARD_HEIGHT))
                if card_img:
                    self.screen.blit(card_img, (x, y))

                if card_points and int(card_points) > 0:
                    point_text = font.render(str(card_points), True, (0, 0, 0))
                    self.screen.blit(point_text, (x + CARD_WIDTH - 35, y + 10))

                card_text = font.render(card_color.capitalize(), True, (0, 0, 0))
                self.screen.blit(card_text, (x + 5, y + 5))

                cost_font = pygame.font.Font(None, int(SCREEN_HEIGHT * 0.03 * SHRINK_FACTOR))
                cost_y = y + 35
                for color, amount in card_cost.items():
                    text_color = COST_COLOR_MAP.get(color.lower(), (0, 0, 0))
                    cost_text = cost_font.render(f"{color[0].upper()}: {amount}", True, text_color)
                    self.screen.blit(cost_text, (x + 5, cost_y))
                    cost_y += 20

        self.render_tokens()

    def render_players(self):
        self.render_player_hand(self.player1, 10, 10)
        self.render_player_hand(self.player2, SCREEN_WIDTH - PLAYER_PANEL_WIDTH - 10, 10)
