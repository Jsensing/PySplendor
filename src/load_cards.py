import pandas as pd
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
