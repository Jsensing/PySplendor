class DevelopmentCard:
    def __init__(self, tier, color, cost, points):
        self.tier = tier
        self.color = color
        self.cost = cost
        self.points = points

def load_cards_from_csv(csv_path):
    import csv
    cards = []
    with open(csv_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if len(row) != 8:
                continue
            tier, color, diamond, sapphire, emerald, ruby, onyx, points = row
            cost = {
                "diamond": int(diamond),
                "sapphire": int(sapphire),
                "emerald": int(emerald),
                "ruby": int(ruby),
                "onyx": int(onyx),
            }
            card = DevelopmentCard(int(tier), color.lower(), cost, int(points))
            cards.append(card)
    return cards
