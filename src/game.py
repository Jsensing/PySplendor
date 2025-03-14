import pygame
from src.player import Player
from src.token import Token
from src.card import DevelopmentCard
from src.ui import UI

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.running = True
        self.players = [Player("Player 1"), Player("Player 2")]
        self.ui = UI(self.screen)

    def run(self):
        while self.running:
            self.handle_events()
            self.ui.render()
            pygame.display.flip()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
