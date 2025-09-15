class Potion:
    def __init__(self, name, effect, rarity, power_level):
        self.name = name
        self.effect = effect
        self.rarity = rarity
        self.power_level = power_level

    def describe(self):
        return f"{self.name} ({self.rarity}) → Effect: {self.effect}, Power: {self.power_level}"

# 5 unique potions
p1 = Potion("Elixir of Shadows", "Invisibility for 10 minutes", "Legendary", 95)
p2 = Potion("Dragon’s Breath", "Fire attack boost", "Epic", 88)
p3 = Potion("Moonlight Dew", "Heal 70 HP instantly", "Rare", 73)
p4 = Potion("Goblin Brew", "Random stat change", "Common", 40)
p5 = Potion("Celestial Nectar", "Revive once after death", "Mythic", 100)

for p in [p1, p2, p3, p4, p5]:
    print(p.describe())
