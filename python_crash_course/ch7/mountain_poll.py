reponses = {}

polling_active = True

while polling_active:
    name = input("\nWhat is your name?")
    repsonse = input("Which mountain would you like  to climb someday?")

    reponses[name] = repsonse

    repeat = input("Would you like to let another person repond? (yes/ no)")
    if repeat == "no":
        polling_active = False

print("\n --- Poll Results ---- ")
for name, reponse in reponses.items():
    print(name + " Would like to climb " + reponse + ".")
