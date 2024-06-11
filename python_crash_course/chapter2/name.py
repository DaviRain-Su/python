# use functions to change the case of a string
name = "ada lovelace"
print(name.title())
print(name.upper())
print(name.lower())

# conact string
first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
print("conact string: {", full_name, " }")
print("Hello, " + full_name.title() + "!")
message = "Hello, " + full_name.title() + "!"
print(message)
langages = "Languages:\n\tPython\n\tC\n\tJavaScript"
print(langages)

favorite_language = " python "
print(":", favorite_language, ":")
# use rstrip() to remove the whitespace from the right side of the string
print(":", favorite_language.rstrip(), ":")

favorite_language = favorite_language.strip()
print(":", favorite_language, ":")
