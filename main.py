import pygame
from src.ui import UI, WIDTH, HEIGHT
from src.load_cards import load_cards_from_csv, load_noble_cards
from src.grid import organize_cards

# ✅ Load noble cards from CSV
noble_cards = load_noble_cards("nobles.txt")  # Update with your actual CSV path

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))  # Updated screen size
clock = pygame.time.Clock()

# Load game cards and create UI
cards = load_cards_from_csv("cards.txt")
grid = organize_cards(cards)
ui = UI(screen, noble_cards)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    ui.render_grid(grid)  # Render updated grid
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
