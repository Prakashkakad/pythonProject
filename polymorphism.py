class Car:
    total_cars=0
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        Car.total_cars += 1

    def fuel_type(self):
        return "Petrol or Desiel"
    def full_name(self):
        return f"{self.brand} {self.model}"
    @staticmethod
    def general_desc():
        return"Cars are means of transport"

class Electric_Car(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric Charge"

my_tesla = Electric_Car("Tesla", "Model S", "85kWh")
print(my_tesla.fuel_type())

# Create an instance of Car
my_car = Car("Toyota", "Corolla")

new_car = Car("Toyota1", "Corolla1")

# Call the fuel_type method on my_car
print(my_car.fuel_type())

print(Car.total_cars)
print(Car.general_desc())

