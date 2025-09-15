# Define a class (object blueprint)
class Car:
    def __init__(self, brand, model, year, color):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color

    def display_info(self):
        return f"{self.year} {self.color} {self.brand} {self.model}"

# Create 5 unique objects (instances)
car1 = Car("Toyota", "Corolla", 2020, "White")
car2 = Car("Honda", "Civic", 2019, "Black")
car3 = Car("Ford", "Mustang", 2021, "Red")
car4 = Car("Tesla", "Model 3", 2022, "Blue")
car5 = Car("BMW", "X5", 2018, "Silver")

# Print their info
print(car1.display_info())
print(car2.display_info())
print(car3.display_info())
print(car4.display_info())
print(car5.display_info())
