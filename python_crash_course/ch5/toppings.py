# compare the value of the variable requested_topping to the string 'anchovies'
requested_topping = "mushrooms"

if requested_topping != "anchovies":
    print("Hold the anchovies!")

requested_toppings = ["mushrooms", "extra cheese", "green peppers"]

if "mushrooms" in requested_toppings:
    print("Adding mushrooms.")
elif "pepperoni" in requested_toppings:
    print("Adding pepperoni.")
elif "extra cheese" in requested_toppings:
    print("Adding extra cheese.")

print("\nFinished making your pizza!")

for requested_topping in requested_toppings:
    if requested_topping == "green peppers":
        print("Sorry, we are out of green peppers right now.")
    else:
        print("Adding " + requested_topping + ".")

print("\nFinished making your pizza!")

requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        print("Adding " + requested_topping + ".")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")

avilable_toppings = [
    "mushrooms",
    "olives",
    "green peppers",
    "pepperoni",
    "pineapple",
    "extra cheese",
]
requested_toppings = ["mushrooms", "french fries", "extra cheese"]

for requested_topping in requested_toppings:
    if requested_topping in avilable_toppings:
        print("Adding " + requested_topping + ".")
    else:
        print("Sorry, we don't have " + requested_topping + ".")
