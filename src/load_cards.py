import pandas as pd
import random 
from src.card import DevelopmentCard

file_path = "../cards.txt"
def load_cards_from_csv(file_path):
    df = pd.read_csv(file_path, names=["level", "color", "costWhite", "costBlue", "costGreen", "costRed", "costBlack", "bonus"])

    cards = []
    for _, row in df.iterrows():
        cost = {
            "White": int(row["costWhite"]),
            "Blue": int(row["costBlue"]),
            "Green": int(row["costGreen"]),
            "Red": int(row["costRed"]),
            "Black": int(row["costBlack"]),
        }
        card = DevelopmentCard(level=row["level"], color=row["color"], cost=cost, bonus=row["bonus"])
        cards.append(card)

    return cards

class NobleCard:
    def __init__(self, cost, points):
        self.cost = cost  # Dictionary {color: amount}
        self.points = points  # Prestige points

def load_noble_cards(file_path):
    df = pd.read_csv(file_path, names=["costWhite", "costBlue", "costGreen", "costRed", "costBlack", "points"])

    noble_cards = []
    for _, row in df.iterrows():
        cost = {
            "White": int(row["costWhite"]),
            "Blue": int(row["costBlue"]),
            "Green": int(row["costGreen"]),
            "Red": int(row["costRed"]),
            "Black": int(row["costBlack"])
        }
        card = NobleCard(cost=cost, points=int(row["points"]))
        noble_cards.append(card)

    # Select 3 random noble cards
    return random.sample(noble_cards, 3)
