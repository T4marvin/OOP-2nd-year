class Spaceship:
    def __init__(self, name, fuel_type, crew_capacity, warp_speed):
        self.name = name
        self.fuel_type = fuel_type
        self.crew_capacity = crew_capacity
        self.warp_speed = warp_speed

    def status(self):
        return f"{self.name}: Fuel={self.fuel_type}, Crew={self.crew_capacity}, Warp Speed={self.warp_speed}x"

# 5 unique spaceships
s1 = Spaceship("Nebula Runner", "Quantum Plasma", 5, 3.2)
s2 = Spaceship("Orion Falcon", "Dark Matter", 12, 4.8)
s3 = Spaceship("Cosmos Whale", "Solar Sails", 50, 1.5)
s4 = Spaceship("Eclipse Phantom", "Antimatter", 2, 6.9)
s5 = Spaceship("Starlight Ark", "Fusion Core", 200, 2.0)

for s in [s1, s2, s3, s4, s5]:
    print(s.status())
