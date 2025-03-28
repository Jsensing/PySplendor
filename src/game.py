import pygame
from src.player import Player
from src.ui import UI
from src.load_cards import load_noble_cards
from src.card import load_cards_from_csv  # now loads DevelopmentCard instances
from src.grid import organize_cards

class TokenManager:
    def __init__(self):
        self.stacks = {
            "diamond": 4,
            "sapphire": 4,
            "emerald": 4,
            "ruby": 4,
            "onyx": 4,
            "gold": 5
        }
        self.selected = {}

    def handle_click_from_ui(self, pos, token_areas, player):
        for rect, color in token_areas:
            if rect.collidepoint(pos):
                self.handle_click(color, player)

    def handle_click(self, color, player):
        if color == "gold":
            return

        available = self.stacks.get(color, 0)
        selected = self.selected.get(color, 0)
        total_colors = len(self.selected)

        # Invalid if already took 2 of same type
        if total_colors == 1 and list(self.selected.values())[0] == 2:
            return
        if total_colors == 3:
            return

        # Taking second of same token only if 4 would remain after
        if selected == 1:
            if total_colors == 1 and available - 1 >= 4:
                self.stacks[color] -= 1
                player.tokens[color] = player.tokens.get(color, 0) + 1
                self.selected[color] = 2
            return

        # Taking first of new color
        if selected == 0 and available > 0:
            self.stacks[color] -= 1
            player.tokens[color] = player.tokens.get(color, 0) + 1
            self.selected[color] = 1

    def reset_selection(self):
        self.selected.clear()

class Game:
    def __init__(self):
        pygame.init()
        screen_info = pygame.display.Info()
        self.screen = pygame.display.set_mode((screen_info.current_w, screen_info.current_h), pygame.FULLSCREEN | pygame.NOFRAME)
        self.running = True

        self.players = [Player("Player 1"), Player("Player 2")]
        self.current_player = 0

        self.cards = load_cards_from_csv("cards.txt")
        self.nobles = load_noble_cards("nobles.txt")
        self.grid = organize_cards(self.cards)

        self.token_manager = TokenManager()
        self.ui = UI(self.screen, self.nobles, self.players[0], self.players[1])
        self.ui.token_stacks = self.token_manager.stacks

    def run(self):
        while self.running:
            self.handle_events()
            self.ui.render_grid(self.grid)
            pygame.display.flip()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                self.running = False

            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                player = self.players[self.current_player]
                self.token_manager.handle_click_from_ui(pos, self.ui.token_areas, player)

            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                self.token_manager.reset_selection()
                self.current_player = (self.current_player + 1) % len(self.players)
