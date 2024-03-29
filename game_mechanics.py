import pieces
import players
import random


def process_decks(input_file):
    level1_deck = []
    level2_deck = []
    level3_deck = []

    with open(input_file, 'r') as f:
        for line in f:
            data = line.strip().split(',')
            level = int(data[0])
            color = data[1]
            vp = int(data[2])
            onyx = int(data[3])
            sapphire = int(data[4])
            emerald = int(data[5])
            ruby = int(data[6])
            diamond = int(data[7])

            card = pieces.Card(level, color, vp, onyx, sapphire, emerald, ruby, diamond)
            if level == 1:
                level1_deck.append(card)
            elif level == 2:
                level2_deck.append(card)
            elif level == 3:
                level3_deck.append(card)

    return level1_deck, level2_deck, level3_deck

def create_token_deck(gemType, num_tokens):
    return [gemType] * num_tokens

def create_gem_decks():
    ruby_deck = create_token_deck("Ruby", 4)
    sapphire_deck = create_token_deck("Sapphire", 4)
    diamond_deck = create_token_deck("Diamond", 4)
    onyx_deck = create_token_deck("Onyx", 4)
    emerald_deck = create_token_deck("Emerald", 4)
    wild_deck = create_token_deck("Wild", 5)  # Wilds have 5 tokens
    return ruby_deck, sapphire_deck, diamond_deck, onyx_deck, emerald_deck, wild_deck

def add_gems(self, *gems):
    if len(gems) != 3:
        print("Error: You must select exactly 3 gems of different colors.")
        return

    colors = set()
    for gem in gems:
        if gem.color in colors:
            print("Error: Gems must be of different colors.")
            return
        colors.add(gem.color)

    self.gems_in_hand.extend(gems)
    print("Gems added successfully.")


def select3Gems(player):
    gems = ["diamond", "ruby", "emerald", "sapphire", "onyx"]
    selections = []

    for g in range(3):
        print("Select a gem:")
        for i, gem in enumerate(gems, start=1):
            print(f"{i}) {gem.capitalize()}")

        choice = int(input("Enter your choice (1-5): "))
        if choice < 1 or choice > 5:
            print("Invalid choice. Please select again.")
            continue

        selected_gem = gems.pop(choice - 1)
        selections.append(selected_gem)

    player.add_gems_to_hand(selections)
    print("Gems added to your inventory:", selections)

if __name__ == "__main__":
    field = []

    # create players
    player1 = players.Player()
    player2 = players.Player()

    # create card decks
    level1Deck, level2Deck, level3Deck = process_decks(r'C:\Users\wrait\OneDrive\Desktop\PySplendor\cards.txt')
    # create 3 random nobles
    noble = pieces.Nobles(r'C:\Users\wrait\OneDrive\Desktop\PySplendor\nobles.txt')
    noble1, noble2, noble3 = noble.get_random_nobles()
    nobles = [noble1, noble2, noble3]

    # create gem decks
    ruby_deck, sapphire_deck, diamond_deck, onyx_deck, emerald_deck, wild_deck = create_gem_decks()
# display nobles
    for a in nobles:
        print(a)
# break for readability
    print('\n')

    # Randomly select and display 4 objects from level1Deck
    selectedLevel1Cards = random.sample(level1Deck, 4)
    for card in selectedLevel1Cards:
        # Remove the selected card from level1Deck
        level1Deck.remove(card)
        # Add the selected card to the Field list
        field.append(card)

    # Randomly select and display 4 objects from level2Deck
    selectedLevel2Cards = random.sample(level2Deck, 4)
    for card in selectedLevel2Cards:
        # Remove the selected card from level2Deck
        level2Deck.remove(card)
        # Add the selected card to the Field list
        field.append(card)

    # Randomly select and display 4 objects from level3Deck
    selectedLevel3Cards = random.sample(level3Deck, 4)
    for card in selectedLevel3Cards:
        # Remove the selected card from level2Deck
        level3Deck.remove(card)
        # Add the selected card to the Field list
        field.append(card)

    for a in field:
        print(a)
    select3Gems(player1)