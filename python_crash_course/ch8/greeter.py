from typing import LiteralString

# def greet_user():
#    """显示简单的问候语"""
#    print("Hello!")

# greet_user()


def greet_user(username):
    """显示简单的问候语"""
    print("Hello, " + username.title() + "!")


greet_user("jesse")


def get_formated_name(first_name: str, last_name: str):
    full_name = first_name + " " + last_name
    return full_name.title()


while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")
    f_name = input("First name: ")
    if f_name == "q":
        break
    l_name = input("Last name: ")
    if l_name == "q":
        break

    formatted_name = get_formated_name(f_name, l_name)
    print("\nHello, " + formatted_name + "!")
