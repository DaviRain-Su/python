#message = input("Tell me something, and I will repeat it back to you:")
#print(message)
prompt = "\nTell me something, and I will repeat it back to you."
prompt += "\n(Enter `quit` to end the program.)"
message = ""

active = True
while active:
    message = input(prompt)

    if message != "quit":
        print(message)
    else:
        active = False