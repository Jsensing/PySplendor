import pygame
from src.player import Player
from src.ui import UI  # ✅ Only import UI (WIDTH & HEIGHT set dynamically here)
from src.load_cards import load_cards_from_csv, load_noble_cards
from src.grid import organize_cards

# ✅ Initialize Pygame before setting screen size
pygame.init()
screen_info = pygame.display.Info()
WIDTH = screen_info.current_w  # Get full screen width
HEIGHT = screen_info.current_h  # Get full screen height

# ✅ Create Fullscreen Window Without Overlapping Taskbar
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN | pygame.NOFRAME)
clock = pygame.time.Clock()

# ✅ Load noble cards from CSV
noble_cards = load_noble_cards("nobles.txt")  # Update with actual CSV path

# ✅ Load game cards and create UI
cards = load_cards_from_csv("cards.txt")
grid = organize_cards(cards)
player1 = Player("Player 1")
player2 = Player("Player 2")
ui = UI(screen, noble_cards, player1, player2)

# ✅ Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  # Close when clicking the close button

        # ✅ Close game when pressing the ESC key
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False  # Exit the loop

    ui.render_grid(grid)  # Render updated grid
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
