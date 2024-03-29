class Player:
    def __init__(self):
        self.gems_in_hand = {}  # Dictionary to store gems and their quantities
        self.reserved_cards = []  # List to store reserved cards
        self.vp = 0  # Victory points
        self.gems_in_play = {}  # Dictionary to store gems in play and their quantities

    def add_3gems_to_hand(self):
        gem_options = ["Diamond", "Ruby", "Emerald", "Sapphire", "Onyx"]
        selections = []
        for _ in range(3):
            print("Select a gem type:")
            for i, gem in enumerate(gem_options, 1):
                print(f"{i}) {gem.capitalize()}")
            while True:
                choice = int(input("Enter your choice (1-5): "))
                if choice in range(1, 6):
                    break
                else:
                    print("Invalid choice. Please enter a number between 1 and 5.")
            gem_type = gem_options.pop(choice - 1)  # Remove the selected gem type
            selections.append(gem_type)
        for gem_type in selections:
            self.add_gems_to_hand_single(gem_type)

    def add_gems_to_hand_single(self, gem_type):
        if gem_type in self.gems_in_hand:
            self.gems_in_hand[gem_type] += 1  # Increase the quantity by 1
        else:
            self.gems_in_hand[gem_type] = 1  # Add the gem with a quantity of 1

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
