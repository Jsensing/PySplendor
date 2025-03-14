import pygame
from src.load_cards import load_cards_from_csv
from src.grid import organize_cards
from src.ui import UI

# Pygame setup
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

# Load and organize cards
cards = load_cards_from_csv("cards.txt")
grid = organize_cards(cards)

# UI manager
ui = UI(screen)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    ui.render_grid(grid)  # Draw the card grid
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
