class Gem:
    def __init__(self, name, points):
        self.name = name
        self.points = points

    def __str__(self):
        return f"{self.points} {self.name}"

# Create Gem objects for each token type
"""ruby = Gem("Ruby", 1)
sapphire = Gem("Sapphire", 1)
diamond = Gem("Diamond", 1)
onyx = Gem("Onyx", 1)
emerald = Gem("Emerald", 1)
wild = Gem("Wild", 1)

# Create arrays of Gem objects
gems_array = [ruby, sapphire, diamond, onyx, emerald, wild]

# Print the array of Gem objects
for gem in gems_array:
    print(gem) """