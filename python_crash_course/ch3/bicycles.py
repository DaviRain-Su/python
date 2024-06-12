bicycles = ["trek", "cannondale", "redline", "specialized"]
print(bicycles)
print(bicycles[1])
print(bicycles[0].title())

for bike in bicycles:
    print("->", bike)

# index last item
print(bicycles[-1].upper())

message = "My first bicycle was a " + bicycles[-1].title() + "."
print(message)
