motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)

# change the first item in the list
motorcycles[0] = "ducati"
print(motorcycles)

motorcycles.append("ducati")
print(motorcycles)

# append item to an empty list
motorcycles = []
print(motorcycles)

motorcycles.append("honda")
motorcycles.append("yamaha")
motorcycles.append("suzuki")
print(motorcycles)

# insert item to a list
motorcycles.insert(0, "ducati")
print(motorcycles)

# delete item from a list
del motorcycles[0]
print(motorcycles)
del motorcycles[1]
print(motorcycles)

# pop item from a list on last index
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

motorcycles = ["honda", "yamaha", "suzuki"]
last_owned = motorcycles.pop()
print("The last motorcycle I owned was a " + last_owned.title() + ".")

# pop item from a list on any index
first_owned = motorcycles.pop(0)
print("The first motorcycle I owned was a " + first_owned.title() + ".")
print(motorcycles)

# remove item by value
motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)

motorcycles.remove("honda")
print(motorcycles)

motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)

too_expensive = "yamaha"
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me.")
