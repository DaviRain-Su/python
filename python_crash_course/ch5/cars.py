cars = ["audi", "bmw", "subaru", "toyota"]

for car in cars:
    if car == "bmw":
        print(car.upper())
    else:
        print(car.title())

car = "bmw"
print("car = ", car)
print("car == 'bmw': ", car == "bmw")
car = "audi"
print("car = ", car)
print("car == 'bmw': ", car == "bmw")
car = "Audi"
print("car = ", car)
print("car == 'audi': ", car == "audi")
car = "Audi"
print("car = ", car)
print("car.lower() == 'audi'", car.lower() == "audi")
car = "Audi"
print("car = ", car)
print("car.lower() == 'audi': ", car.lower() == "audi")
print("car = ", car)
