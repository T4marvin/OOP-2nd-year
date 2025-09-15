class Instrument:
    def __init__(self, name, type, origin, rarity):
        self.name = name
        self.type = type
        self.origin = origin
        self.rarity = rarity

    def show(self):
        return f"{self.name} ({self.type}) from {self.origin}, rarity: {self.rarity}"

# 5 unique instruments
i1 = Instrument("Nyatiti", "String", "Kenya", "Rare")
i2 = Instrument("Theremin", "Electronic", "Russia", "Uncommon")
i3 = Instrument("Hang Drum", "Percussion", "Switzerland", "Rare")
i4 = Instrument("Didgeridoo", "Wind", "Australia", "Ancient")
i5 = Instrument("Crystal Flute", "Wind", "Fantasy Realm", "Legendary")

for i in [i1, i2, i3, i4, i5]:
    print(i.show())
