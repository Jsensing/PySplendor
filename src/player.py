class Player:
    def __init__(self, name):
        self.name = name
        self.tokens = {"Diamond": 0, "Sapphire": 0, "Emerald": 0, "Ruby": 0, "Onyx": 0, "Gold": 0}
        self.points = 0
        self.cards = []  # List of acquired cards

    def add_token(self, color, amount=1):
        if color in self.tokens:
            self.tokens[color] += amount

    def remove_token(self, color, amount=1):
        if color in self.tokens and self.tokens[color] >= amount:
            self.tokens[color] -= amount

    def add_card(self, card):
        self.cards.append(card)
        self.points += card.bonus  # Assuming the card has a bonus (points)
