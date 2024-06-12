# filename = "../data/alice.txt"


def count_words(filename):
    try:
        with open(filename) as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        msg = "Sorry, the file " + filename + " does not exist."
        print(msg)
    else:
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words) + " Words.")


filenames = ["alice.txt", "siddhartha.txt", "moby_dick.txt", "little_women.txt"]
for filename in filenames:
    filename = f"../data/{filename}"
    count_words(filename)
