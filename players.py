class Player:
    def __init__(self, gems_in_hand=None, reserved_cards=None, vp=0, gems_in_play=None):
        if gems_in_hand is None:
            gems_in_hand = {}
        if reserved_cards is None:
            reserved_cards = []
        if gems_in_play is None:
            gems_in_play = {}

        self.gems_in_hand = gems_in_hand  # Dictionary to store gems and their quantities
        self.reserved_cards = reserved_cards  # List to store reserved cards
        self.vp = vp  # Victory points
        self.gems_in_play = gems_in_play  # Dictionary to store gems in play and their quantities

    def add_gems_to_hand(self, gem_type, quantity=1):
        if gem_type in self.gems_in_hand:
            self.gems_in_hand[gem_type] += quantity
        else:
            self.gems_in_hand[gem_type] = quantity

    def reserve_card(self, card):
        self.reserved_cards.append(card)

    def add_vp(self, points):
        self.vp += points

    def add_gems_to_play(self, gem_type, quantity):
        if gem_type in self.gems_in_play:
            self.gems_in_play[gem_type] += quantity
        else:
            self.gems_in_play[gem_type] = quantity

    def __str__(self):
        return f"Gems in Hand: {self.gems_in_hand}, Reserved Cards: {self.reserved_cards}, VP: {self.vp}, Gems in Play: {self.gems_in_play}"

# Example usage
#player1 = Player()
#player1.add_gems_to_hand('Ruby', 2)
#player1.reserve_card('Card A')
#player1.add_vp(5)
#player1.add_gems_to_play('Diamond', 1)

#print(player1)
