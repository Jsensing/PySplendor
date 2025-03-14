class DevelopmentCard:
    def __init__(self, level, color, cost, bonus, prestige=0):
        self.level = int(level)  # 1, 2, or 3
        self.color = color  # Card color (Blue, Red, etc.)
        self.cost = cost  # Dictionary {color: amount}
        self.bonus = bonus  # Bonus color (e.g., "Blue")
        self.prestige = int(prestige)  # Prestige points (if included in the CSV)
