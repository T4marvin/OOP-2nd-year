class TimeTraveler:
    def __init__(self, name, era_from, era_to, device, paradox_risk):
        self.name = name
        self.era_from = era_from
        self.era_to = era_to
        self.device = device
        self.paradox_risk = paradox_risk

    def journey(self):
        return f"{self.name}: From {self.era_from} → {self.era_to} using {self.device}, Paradox Risk: {self.paradox_risk}%"

# 5 unique travelers
t1 = TimeTraveler("Professor Chronos", "1890", "3025", "Pocket Watch Portal", 22)
t2 = TimeTraveler("Zara Flux", "2150", "500 BC", "Neural Chip", 65)
t3 = TimeTraveler("Captain Rift", "4000", "2020", "Wormhole Engine", 80)
t4 = TimeTraveler("Echo", "Unknown", "Everywhere", "Quantum Dust", 100)
t5 = TimeTraveler("Kael", "1300", "2300", "Time Blade", 40)

for t in [t1, t2, t3, t4, t5]:
    print(t.journey())
