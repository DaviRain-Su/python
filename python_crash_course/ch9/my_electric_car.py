from car import Car, ElectricCar

my_tesla = ElectricCar("tesla", "model s", 2016)
print(my_tesla.get_descriptive_name())
# print(my_tesla.read_odometer())
# my_tesla.describe_battery()
# my_tesla.fill_gas_tank()
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
