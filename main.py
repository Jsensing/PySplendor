import pygame
from src.player import Player
from src.ui import UI, load_cards_from_csv  # ✅ Import the updated loader from UI
from src.load_cards import load_noble_cards
from src.grid import organize_cards

# ✅ Initialize Pygame and screen
pygame.init()
screen_info = pygame.display.Info()
WIDTH = screen_info.current_w
HEIGHT = screen_info.current_h

# ✅ Create fullscreen window
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN | pygame.NOFRAME)
clock = pygame.time.Clock()

# ✅ Load noble cards and game cards
noble_cards = load_noble_cards("nobles.txt")
cards = load_cards_from_csv("cards.txt")           # <-- Uses updated bonus-compatible loader
all_cards = cards                                   # Cards are now returned as a flat list
grid = organize_cards(all_cards)

# ✅ Initialize players and UI
player1 = Player("Player 1")
player2 = Player("Player 2")
ui = UI(screen, noble_cards, player1, player2)

# ✅ Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False

    ui.render_grid(grid)
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
