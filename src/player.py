class Player:
    def __init__(self, name):
        self.name = name
        self.tokens = {"Emerald": 0, "Diamond": 0, "Sapphire": 0, "Onyx": 0, "Ruby": 0, "Gold": 0}
        self.cards = []  # List of DevelopmentCard objects
        self.nobles = []
        self.prestige = 0

    def take_tokens(self, color, amount):
        if self.tokens[color] + amount <= 10:
            self.tokens[color] += amount

    def buy_card(self, card):
        # Logic for checking token cost and purchasing
        pass
