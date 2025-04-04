import random

def organize_cards(cards):
    # Separate by tiers (was 'level', now 'tier' to match CSV and card object)
    level_1 = [card for card in cards if card.tier == 1]
    level_2 = [card for card in cards if card.tier == 2]
    level_3 = [card for card in cards if card.tier == 3]

    # Shuffle for randomness
    random.shuffle(level_1)
    random.shuffle(level_2)
    random.shuffle(level_3)

    # Select 4x3 grid (4 columns per level)
    grid = {
        3: level_3[:4],  # Top row (Level 3)
        2: level_2[:4],  # Middle row (Level 2)
        1: level_1[:4],  # Bottom row (Level 1)
    }

    return grid
