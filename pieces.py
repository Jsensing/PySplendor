import random

class Gem:
    def __init__(self, name, points):
        self.name = name
        self.points = points

    def __str__(self):
        return f"{self.points} {self.name}"


class Card:
    def __init__(self, level, color, vp, onyx, sapphire, emerald, ruby, diamond):
        self.level = level
        self.color = color
        self.vp = vp
        self.onyx = onyx
        self.sapphire = sapphire
        self.emerald = emerald
        self.ruby = ruby
        self.diamond = diamond

    def __str__(self):
        return f"Level: {self.level} Color: {self.color} VP: {self.vp}, Black: {self.onyx}, Blue: {self.sapphire}, Green: {self.emerald}, Red: {self.ruby}, White: {self.diamond}"

class Noble:
    def __init__(self, ID, diamond, sapphire, emerald, ruby, onyx, pointValue):
        self.ID = ID
        self.diamond = diamond
        self.sapphire = sapphire
        self.emerald = emerald
        self.ruby = ruby
        self.onyx = onyx
        self.pointValue = pointValue

    def __str__(self):
        return f"ID: {self.ID}, Diamond: {self.diamond}, Sapphire: {self.sapphire}, Emerald: {self.emerald}, Ruby: {self.ruby}, Onyx: {self.onyx}, Point Value: {self.pointValue}"

class Nobles:
    def __init__(self, filename):
        self.nobles_list = []
        self.load_nobles(filename)

    def load_nobles(self, filename):
        with open(filename, 'r') as f:
            for line in f:
                ID, diamond, sapphire, emerald, ruby, onyx, pointValue = line.strip().split(',')
                noble = Noble(ID, int(diamond), int(sapphire), int(emerald), int(ruby), int(onyx), int(pointValue))
                self.nobles_list.append(noble)

    def get_random_nobles(self, num_nobles=3):
        return random.sample(self.nobles_list, num_nobles)

# Example usage
nobles_obj = Nobles(r'C:\Users\wrait\OneDrive\Desktop\PySplendor\nobles.txt')
random_nobles = nobles_obj.get_random_nobles()

print("Random Nobles:")
for noble in random_nobles:
    print(noble)


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

            card = Card(level, color, vp, onyx, sapphire, emerald, ruby, diamond)
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



# Create Gem objects for each token type
ruby = Gem("Ruby", 1)
sapphire = Gem("Sapphire", 1)
diamond = Gem("Diamond", 1)
onyx = Gem("Onyx", 1)
emerald = Gem("Emerald", 1)
wild = Gem("Wild", 1)

# Create arrays of Gem objects
gems_array = [ruby, sapphire, diamond, onyx, emerald, wild]

# Print the array of Gem objects
for gem in gems_array:
    print(gem)