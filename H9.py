#1,2,4,6,9, 10,13-15

#9.1

print("\n9.1\n")

class Restaurant():

    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print("Welcome at " + self.name + "! Here we serve " + self.cuisine + " food")

    def open_restaurant(self):
        print(self.name + ' is now open!')

    def set_number_served(self, amount):
        self.number_served = self.number_served + amount

    def increment_number_served(self):
        self.number_served = self.number_served + 1

name = "Chili's"
cuisine = 'Mexcican'

print(name)
print(cuisine)

restaurant = Restaurant(name,cuisine)

restaurant.describe_restaurant()
restaurant.open_restaurant()

#9.2

print("\n9.2\n")

dominos = Restaurant("Dominos", "Italian")
tacobell = Restaurant('Taco Bell', "Mexican")
verhage = Restaurant('Verhage', 'Dutch')

dominos.describe_restaurant()
tacobell.describe_restaurant()
verhage.describe_restaurant()

#9.4

print("\n9.4\n")

print(restaurant.number_served)
restaurant.set_number_served(25)

#9.6

print("\n9.6\n")

class IceCreamStand(Restaurant):
    def __init__(self, name, cuisine_type):
        super().__init__(name, cuisine_type)
        self.flavors = []

    def display_flavors(self):
        print("Available ice cream flavors:")
        for flavor in self.flavors:
            print("- " + flavor)

ice_cream_stand = IceCreamStand("Ijs &Zo", "Ice Cream")
ice_cream_stand.flavors = ["Vanilla", "Chocolate", "Strawberry", "Smurf"]
ice_cream_stand.describe_restaurant()
ice_cream_stand.open_restaurant()
ice_cream_stand.display_flavors()

#9.9

print("\n9.9\n")
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

class Battery:
    def __init__(self, battery_size=75):
        self.battery_size = battery_size

    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def get_range(self):
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 85:
            range = 300
        print("This car can go approximately " + str(range) + " miles on a full charge.")

    def upgrade_battery(self):
        if self.battery_size != 85:
            self.battery_size = 85

my_electric_car = ElectricCar("Tesla", "Model S", 2024)
print("Range before upgrading the battery:")
my_electric_car.battery.get_range()
my_electric_car.battery.upgrade_battery()
print("\nRange after upgrading the battery:")
my_electric_car.battery.get_range()


#9.10

print("\n9.10\n")

# Veel werk, skip

