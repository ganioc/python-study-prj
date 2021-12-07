from car import Car

class ElectricCar(Car):
    """Electric Car Model"""
    def __init__(self,make, model, year):
        super().__init__(make, model, year)
        self.battery_size = 70  
    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

my_tesla = ElectricCar('tesla', 'model S', 2017)
print("\nTest electric_car.py")
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()

