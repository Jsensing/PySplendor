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
        return f"Level {self.level} {self.color} - VP: {self.vp}, Black: {self.black}, Blue: {self.blue}, Green: {self.green}, Red: {self.red}, White: {self.white}"

""""# Create decks for each level
level1_deck = []
level2_deck = []
level3_deck = []

# Define the cards based on the provided data
cards_data = [
    (1, "Black", 0, 0, 1, 1, 1, 1),
    # Add more card data here...
]

# Create Card objects and add them to their respective decks
for data in cards_data:
    level, color, vp, black, blue, green, red, white = data
    card = Card(level, color, vp, black, blue, green, red, white)
    if level == 1:
        level1_deck.append(card)
    elif level == 2:
        level2_deck.append(card)
    elif level == 3:
        level3_deck.append(card) """


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