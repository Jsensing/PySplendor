class DevelopmentCard:
    def __init__(self, level, cost, bonus, prestige):
        self.level = level
        self.cost = cost  # Dictionary {color: amount}
        self.bonus = bonus
        self.prestige = prestige
