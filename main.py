import pygame
from src.ui import UI
from src.load_cards import load_cards_from_csv
from src.grid import organize_cards
from src.ui import WIDTH, HEIGHT  # Import updated screen size

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))  # Updated screen size
clock = pygame.time.Clock()

# Load cards and create UI
cards = load_cards_from_csv("cards.txt")
grid = organize_cards(cards)
ui = UI(screen)

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
