import random

class Card:
    def __init__(self, level, color, vp, onyx, sapphire, emerald, ruby, diamond):
        self.level = level
        self.color = color
        self.vp = vp
        self.onyx = onyx
        self.sapphire = sapphire
        self.emerald = emerald
        self.ruby = ruby
        self.diamond = diamond

    def __str__(self):
        return f"Level: {self.level} Color: {self.color} VP: {self.vp}, Black: {self.onyx}, Blue: {self.sapphire}, Green: {self.emerald}, Red: {self.ruby}, White: {self.diamond}"

class Noble:
    def __init__(self, ID, diamond, sapphire, emerald, ruby, onyx, wild, pointValue):
        self.ID = ID
        self.diamond = diamond
        self.sapphire = sapphire
        self.emerald = emerald
        self.ruby = ruby
        self.onyx = onyx
        self.wild = wild
        self.pointValue = pointValue

    def __str__(self):
        return f"ID: {self.ID}, Diamond: {self.diamond}, Sapphire: {self.sapphire}, Emerald: {self.emerald}, Ruby: {self.ruby}, Onyx: {self.onyx}, Wild: {self.wild}, Point Value: {self.pointValue}"
        self.pointValue = pointValue

class Nobles:
    def __init__(self, filename):
        self.nobles_list = []
        self.load_nobles(filename)

    def load_nobles(self, filename):
        with open(filename, 'r') as f:
            for line in f:
                ID, diamond, sapphire, emerald, ruby, onyx, pointValue = line.strip().split(',')
                noble = Noble(ID, int(diamond), int(sapphire), int(emerald), int(ruby), int(onyx), int(pointValue))
                self.nobles_list.append(noble)

    def get_random_nobles(self, num_nobles=3):
        return random.sample(self.nobles_list, num_nobles)