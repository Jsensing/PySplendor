class DevelopmentCard:
    COLOR_NAME_MAP = {
        "White": "Diamond",
        "Blue": "Sapphire",
        "Green": "Emerald",
        "Red": "Ruby",
        "Black": "Onyx"
    }

    def __init__(self, level, color, cost, bonus, prestige=0):
        self.level = int(level)  # 1, 2, or 3
        self.color = self.COLOR_NAME_MAP.get(color, color)  # Convert old color names to new names
        self.cost = {self.COLOR_NAME_MAP.get(k, k): v for k, v in cost.items()}  # Convert cost color names
        self.bonus = self.COLOR_NAME_MAP.get(bonus, bonus)  # Convert bonus color name
        self.prestige = int(prestige)  # Prestige points (if included in the CSV)
