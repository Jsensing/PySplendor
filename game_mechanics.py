import pieces
import players
import random


def process_file(input_file):
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

def reveal_cards(cards_list):
    random.shuffle(cards_list)
    revealed_cards = []
    for level in range(1, 4):
        level_cards = [card for card in cards_list if card.level == level]
        revealed_cards.extend(random.sample(level_cards, 4))
    return revealed_cards

def reveal_nobles(nobles_list):
    random.shuffle(nobles_list)
    return random.sample(nobles_list, 3)

def create_token_deck(gem_type, num_tokens):
    return [gem_type] * num_tokens

def create_gem_decks():
    ruby_deck = create_token_deck("Ruby", 4)
    sapphire_deck = create_token_deck("Sapphire", 4)
    diamond_deck = create_token_deck("Diamond", 4)
    onyx_deck = create_token_deck("Onyx", 4)
    emerald_deck = create_token_deck("Emerald", 4)
    wild_deck = create_token_deck("Wild", 5)  # Wilds have 5 tokens
    return ruby_deck, sapphire_deck, diamond_deck, onyx_deck, emerald_deck, wild_deck

def game_setup(cards_list, nobles_list):
    revealed_cards = reveal_cards(cards_list)
    revealed_nobles = reveal_nobles(nobles_list)
    remaining_nobles = [noble for noble in nobles_list if noble not in revealed_nobles]
    ruby_deck, sapphire_deck, diamond_deck, onyx_deck, emerald_deck, wild_deck = create_gem_decks()
    return revealed_cards, revealed_nobles, remaining_nobles, ruby_deck, sapphire_deck, diamond_deck, onyx_deck, emerald_deck, wild_deck

if __name__ == "__main__":
    player1 = players.Player()
    player2 = players.Player()

    level1Deck, level2Deck, level3Deck = process_file(r'C:\Users\wrait\OneDrive\Desktop\PySplendor\cards.txt')
    noble = pieces.Nobles(r'C:\Users\wrait\OneDrive\Desktop\PySplendor\nobles.txt')
    noble1, noble2, noble3 = noble.get_random_nobles()
    print(noble1)
    print(len(level1Deck))

