score = "B"

# Match score:
match score:
    case "A":
        print("You got an A!")
    case "B":
        print("You got a B!")
    case "C":
        print("You got a C.")
    case _:
        print("You need to study more.")

args = ["gcc", "hello.c", "world.c"]

match args:
    case ["gcc"]:
        print("Compiling all files.")
    case ["gcc", file1, *files]:
        print(f"Compiling {file1} and {len(files)} other files.")
    case ["clean"]:
        print("Cleaning up.")
    case _:
        print("Unknown command.")
