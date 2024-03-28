class Gem:
    def __init__(self, name, points):
        self.name = name
        self.points = points

    def __str__(self):
        return f"{self.points} {self.name}"

class Card:
    def __init__(self, level, color, vp, black, blue, green, red, white):
        self.level = level
        self.color = color
        self.vp = vp
        self.black = black
        self.blue = blue
        self.green = green
        self.red = red
        self.white = white

    def __str__(self):
        return f"Level: {self.level} Color: {self.color} VP: {self.vp}, Black: {self.black}, Blue: {self.blue}, Green: {self.green}, Red: {self.red}, White: {self.white}"

""" def process_file(input_file):
    level1_deck = []
    level2_deck = []
    level3_deck = []

    with open(input_file, 'r') as f:
        for line in f:
            data = line.strip().split(',')
            level = int(data[0])
            color = data[1]
            vp = int(data[2])
            black = int(data[3])
            blue = int(data[4])
            green = int(data[5])
            red = int(data[6])
            white = int(data[7])

            card = Card(level, color, vp, black, blue, green, red, white)
            if level == 1:
                level1_deck.append(card)
            elif level == 2:
                level2_deck.append(card)
            elif level == 3:
                level3_deck.append(card)

    return level1_deck, level2_deck, level3_deck

# Example usage: process cards.txt and create decks
level1_deck, level2_deck, level3_deck = process_file(r'C:\Users\wrait\OneDrive\Desktop\PySplendor\cards.txt')

print("Level 1 Deck:")
for card in level1_deck:
    print(card)

print("\nLevel 2 Deck:")
for card in level2_deck:
    print(card)

print("\nLevel 3 Deck:")
for card in level3_deck:
    print(card)
"""


# Create Gem objects for each token type
"""ruby = Gem("Ruby", 1)
sapphire = Gem("Sapphire", 1)
diamond = Gem("Diamond", 1)
onyx = Gem("Onyx", 1)
emerald = Gem("Emerald", 1)
wild = Gem("Wild", 1)

# Create arrays of Gem objects
gems_array = [ruby, sapphire, diamond, onyx, emerald, wild]

# Print the array of Gem objects
for gem in gems_array:
    print(gem) """