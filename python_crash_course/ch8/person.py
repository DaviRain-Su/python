from typing import LiteralString


# TODO: we can change age type to Integer
def build_person(
    first_name: LiteralString, last_name: LiteralString, age: LiteralString = ""
):
    """Return a dictionary of information about a person."""
    person = {"first": first_name, "last": last_name}
    if age:
        person["age"] = age
    return person


musician = build_person("jimi", "hendrix", age="27")
print(musician)
